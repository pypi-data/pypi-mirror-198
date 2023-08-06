#!/usr/bin/python3

import yt.yson as yson
from yt.wrapper import YtClient, TablePath, config, ypath_join
from yt.common import YtError

from yt.environment.init_cluster import get_default_resource_limits

import argparse
import copy
import logging
import subprocess
import time


DEFAULT_SHARD_COUNT = 100
DEFAULT_ARCHIVE_PATH = "//sys/operations_archive"
OPERATIONS_ARCHIVE_ACCOUNT_NAME = "operations_archive"
SYS_ACCOUNT_NAME = "sys"
DEFAULT_BUNDLE_NAME = "default"
SYS_BUNDLE_NAME = "sys"
SYS_BLOBS_BUNDLE_NAME = "sys_blobs"
RESOURCE_LIMITS_ATTRIBUTE = "resource_limits"
NODES_LIMIT_ATTRIBUTE = "node_count"
JOB_TABLE_PARTITION_COUNT = 10


def wait_for_predicate(predicate, message, timeout=60, pause=1):
    start = time.time()
    while not predicate():
        if time.time() - start > timeout:
            error = "Timeout while waiting for \"%s\"" % message
            logging.info(error)
            raise YtError(error)
        logging.info("Waiting for \"%s\"" % message)
        time.sleep(pause)


def get_job_table_pivots(shard_count):
    pivot_keys = [[]]
    shards_per_partition = shard_count // JOB_TABLE_PARTITION_COUNT + 1
    for job_id_partition in range(JOB_TABLE_PARTITION_COUNT):
        for i in range(shards_per_partition):
            pivot_keys.append([yson.YsonUint64(job_id_partition), yson.YsonUint64(i * 2**64 / shards_per_partition)])
    return pivot_keys


def unmount_table(client, path):
    logging.info("Unmounting table %s", path)
    client.unmount_table(path, sync=True)


def mount_table(client, path):
    logging.info("Mounting table %s", path)
    client.mount_table(path, sync=True)


def make_dynamic_table_attributes(schema, key_columns, optimize_for):
    attributes = {
        "dynamic": True,
        "optimize_for": optimize_for,
        "schema": schema,
    }
    for column in schema:
        assert (column.get("sort_order") == "ascending") == (column["name"] in key_columns)
    return attributes


class TableInfo(object):
    def __init__(self, key_columns, value_columns, in_memory=False, get_pivot_keys=None, attributes={}):
        def make_column(name, type_name, key=False):
            result = {
                "name": name,
                "type": type_name,
            }
            if name in ["progress", "brief_progress"]:
                result["lock"] = "controller_agent"
            elif not key:
                result["lock"] = "operations_cleaner"
            return result

        def make_key_column(name, type_name, expression=None):
            result = make_column(name, type_name, key=True)
            result["sort_order"] = "ascending"
            if expression:
                result["expression"] = expression
            return result

        self.schema = [make_key_column(*columns) for columns in key_columns]
        self.key_columns = [column["name"] for column in self.schema]
        self.schema += [make_column(*column) for column in value_columns]
        self.user_columns = [column["name"] for column in self.schema if "expression" not in column]
        self.get_pivot_keys = get_pivot_keys
        self.in_memory = in_memory
        self.attributes = attributes

    def create_table(self, client, path, sorted=True):
        if sorted:
            key_columns = self.key_columns
        else:
            key_columns = []

        schema = copy.deepcopy(self.schema)
        if not sorted:
            for column in schema:
                if "sort_order" in column:
                    del column["sort_order"]

        attributes = make_dynamic_table_attributes(schema, key_columns, "scan")
        attributes.update(self.attributes)
        attributes["dynamic"] = False

        logging.info("Creating table %s with attributes %s", path, attributes)
        client.create("table", path, recursive=True, attributes=attributes)

    def create_dynamic_table(self, client, path):
        attributes = make_dynamic_table_attributes(self.schema, self.key_columns, "scan")
        attributes.update(self.attributes)

        logging.info("Creating dynamic table %s with attributes %s", path, attributes)
        client.create("table", path, recursive=True, attributes=attributes)

    def to_dynamic_table(self, client, path):
        attributes = make_dynamic_table_attributes(self.schema, self.key_columns, "scan")

        # add unique_keys to schema
        attributes["schema"] = yson.to_yson_type(attributes["schema"], attributes={"unique_keys": True})

        logging.info("Sorting table %s with attributes %s", path, attributes)
        primary_medium = client.get(path + "/@primary_medium")
        account = client.get(path + "/@account")
        client.run_sort(path, TablePath(path, attributes=attributes), sort_by=self.key_columns, spec={
            "merge_job_io": {"table_writer": {"block_size": 256 * 2**10, "desired_chunk_size": 100 * 2**20}},
            "force_transform": True,
            "intermediate_data_medium": primary_medium,
            "intermediate_data_account": account,
            "use_new_partitions_heuristic": True,
            "max_speculative_job_count_per_task": 20,
        })
        logging.info("Converting table to dynamic %s", path)
        client.alter_table(path, dynamic=True)
        for attr, value in self.attributes.items():
            client.set("{0}/@{1}".format(path, attr), value)

    def alter_table(self, client, path, shard_count, mount=True):
        logging.info("Altering table %s", path)
        unmount_table(client, path)
        attributes = make_dynamic_table_attributes(self.schema, self.key_columns, "scan")

        logging.info("Alter table %s with attributes %s", path, attributes)
        client.alter_table(path, schema=attributes["schema"])
        for attr, value in self.attributes.items():
            client.set("{0}/@{1}".format(path, attr), value)

        if self.get_pivot_keys:
            client.reshard_table(path, self.get_pivot_keys(shard_count), sync=True)

        if mount:
            mount_table(client, path)

    def get_default_mapper(self):
        column_names = self.user_columns

        def default_mapper(row):
            yield dict([(key, row.get(key)) for key in column_names])

        return default_mapper


class Conversion(object):
    def __init__(self, table, table_info=None, mapper=None, source=None, use_default_mapper=False):
        self.table = table
        self.table_info = table_info
        self.mapper = mapper
        self.source = source
        self.use_default_mapper = use_default_mapper

    def __call__(self, client, table_info, target_table, source_table, archive_path, shard_count=DEFAULT_SHARD_COUNT, **kwargs):
        if self.table_info:
            table_info = self.table_info

        source_table = self.source or source_table
        if source_table:
            source_table = ypath_join(archive_path, source_table)
            old_key_columns = client.get(source_table + "/@key_columns")
            need_sort = old_key_columns != table_info.key_columns
        else:
            need_sort = False

        if not self.use_default_mapper and not self.mapper and not self.source and source_table and not need_sort:
            table_info.alter_table(client, source_table, shard_count, mount=False)
            return True  # in place transformation

        if source_table:
            if client.exists(source_table):
                primary_medium = client.get(source_table + "/@primary_medium")
                # If need_sort == True, we create target table non-sorted to avoid
                # sort order violation error during map.
                table_info.create_table(client, target_table, sorted=not need_sort)
                client.set(target_table + "/@tablet_cell_bundle", client.get(source_table + "/@tablet_cell_bundle"))
                client.set(target_table + "/@primary_medium", primary_medium)
                for key, value in client.get(source_table + "/@user_attributes").items():
                    client.set(target_table + "/@" + key, value)
                mapper = self.mapper if self.mapper else table_info.get_default_mapper()
                unmount_table(client, source_table)

                logging.info("Run mapper '%s': %s -> %s", mapper.__name__, source_table, target_table)
                client.run_map(mapper, source_table, target_table, spec={"data_size_per_job": 2 * 2**30})
                table_info.to_dynamic_table(client, target_table)
                client.set(target_table + "/@forced_compaction_revision", 1)
        else:
            logging.info("Creating dynamic table %s", target_table)
            table_info.create_dynamic_table(client, target_table)

        if table_info.in_memory:
            client.set(target_table + "/@in_memory_mode", "compressed")
        table_info.alter_table(client, target_table, shard_count, mount=False)
        return False  # need additional swap


class ExecAction(object):
    def __init__(self, *args):
        self.args = args

    def __call__(self, client):
        logging.info("Executing: %s", self.args)
        subprocess.check_call(self.args)


def get_default_pivots(shard_count):
    return [[]] + [[yson.YsonUint64((i * 2 ** 64) / shard_count)] for i in range(1, shard_count)]


def set_table_ttl(client, table, ttl=None, auto_compaction_period=None, forbid_obsolete_rows=False):
    if ttl is not None:
        client.set(table + "/@max_data_ttl", ttl)
    if auto_compaction_period is not None:
        client.set(table + "/@auto_compaction_period", auto_compaction_period)
    if forbid_obsolete_rows:
        client.set(table + "/@max_data_versions", 1)
        client.set(table + "/@min_data_ttl", 0)
    client.set(table + "/@min_data_versions", 0)
    client.set(table + "/@forced_compaction_revision", 1)
    if client.get(table + "/@tablet_state") == "mounted":
        client.remount_table(table)


def create_operations_archive_account(client):
    if not client.exists("//sys/accounts/{0}".format(OPERATIONS_ARCHIVE_ACCOUNT_NAME)):
        logging.info("Creating account: %s", OPERATIONS_ARCHIVE_ACCOUNT_NAME)
        client.create("account", attributes={
            "name": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
            "resource_limits" : get_default_resource_limits(client)
        })
        while client.get("//sys/accounts/{0}/@life_stage".format(OPERATIONS_ARCHIVE_ACCOUNT_NAME)) != "creation_committed":
            time.sleep(0.1)

    limits = client.get("//sys/accounts/{0}/@{1}".format(SYS_ACCOUNT_NAME, RESOURCE_LIMITS_ATTRIBUTE))
    limits[NODES_LIMIT_ATTRIBUTE] = 100
    logging.info("Setting account limits %s", limits)
    client.set("//sys/accounts/{0}/@{1}".format(OPERATIONS_ARCHIVE_ACCOUNT_NAME, RESOURCE_LIMITS_ATTRIBUTE), limits)


def _create_table(client, table_info, table_path, shard_count=None):
    logging.info("Creating dynamic table %s", table_path)
    table_info = copy.deepcopy(table_info)

    if (
        table_info.attributes.get("tablet_cell_bundle") == SYS_BLOBS_BUNDLE_NAME
        and not client.exists("//sys/tablet_cell_bundles/{}".format(SYS_BLOBS_BUNDLE_NAME))
    ):
        table_info.attributes["tablet_cell_bundle"] = SYS_BUNDLE_NAME
    if (
        table_info.attributes.get("tablet_cell_bundle") == SYS_BUNDLE_NAME
        and not client.exists("//sys/tablet_cell_bundles/{}".format(SYS_BUNDLE_NAME))
    ):
        table_info.attributes["tablet_cell_bundle"] = DEFAULT_BUNDLE_NAME

    if shard_count is None:
        bundle = table_info.attributes.get("tablet_cell_bundle", DEFAULT_BUNDLE_NAME)
        shard_count = 5 * client.get("//sys/tablet_cell_bundles/{}/@tablet_cell_count".format(bundle))
    if table_info.get_pivot_keys is not None:
        table_info.attributes["pivot_keys"] = table_info.get_pivot_keys(shard_count)
    if table_info.in_memory:
        table_info.attributes["in_memory_mode"] = "compressed"
    table_info.create_dynamic_table(client, table_path)


INITIAL_TABLE_INFOS = {
    "jobs": TableInfo(
        [
            ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
            ("operation_id_hi", "uint64"),
            ("operation_id_lo", "uint64"),
            ("job_id_hi", "uint64"),
            ("job_id_lo", "uint64")
        ], [
            ("type", "string"),
            ("state", "string"),
            ("start_time", "int64"),
            ("finish_time", "int64"),
            ("address", "string"),
            ("error", "any"),
            ("statistics", "any"),
            ("stderr_size", "uint64"),
            ("spec", "string"),
            ("spec_version", "int64"),
            ("has_spec", "boolean"),
            ("has_fail_context", "boolean"),
            ("fail_context_size", "uint64"),
            ("events", "any"),
            ("transient_state", "string"),
            ("update_time", "int64"),
        ],
        get_pivot_keys=get_default_pivots,
        attributes={
            "atomicity": "none",
            "tablet_cell_bundle": SYS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
    "operation_ids": TableInfo(
        [
            ("job_id_hash", "uint64", "farm_hash(job_id_hi, job_id_lo)"),
            ("job_id_hi", "uint64"),
            ("job_id_lo", "uint64")
        ], [
            ("operation_id_hi", "uint64"),
            ("operation_id_lo", "uint64"),
        ],
        attributes={
            "atomicity": "none",
            "tablet_cell_bundle": SYS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
    "job_specs": TableInfo(
        [
            ("job_id_hash", "uint64", "farm_hash(job_id_hi, job_id_lo)"),
            ("job_id_hi", "uint64"),
            ("job_id_lo", "uint64"),
        ], [
            ("spec", "string"),
            ("spec_version", "int64"),
            ("type", "string"),
        ],
        get_pivot_keys=get_default_pivots,
        attributes={
            "atomicity": "none",
            "tablet_cell_bundle": SYS_BLOBS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
    "stderrs": TableInfo(
        [
            ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
            ("operation_id_hi", "uint64"),
            ("operation_id_lo", "uint64"),
            ("job_id_hi", "uint64"),
            ("job_id_lo", "uint64")
        ], [
            ("stderr", "string"),
        ],
        get_pivot_keys=get_default_pivots,
        attributes={
            "atomicity": "none",
            "tablet_cell_bundle": SYS_BLOBS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
    "fail_contexts": TableInfo(
        [
            ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
            ("operation_id_hi", "uint64"),
            ("operation_id_lo", "uint64"),
            ("job_id_hi", "uint64"),
            ("job_id_lo", "uint64")
        ], [
            ("fail_context", "string"),
        ],
        get_pivot_keys=get_default_pivots,
        attributes={
            "atomicity": "none",
            "tablet_cell_bundle": SYS_BLOBS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
    "ordered_by_id": TableInfo(
        [
            ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
            ("id_hi", "uint64"),
            ("id_lo", "uint64"),
        ], [
            ("state", "string"),
            ("authenticated_user", "string"),
            ("operation_type", "string"),
            ("progress", "any"),
            ("spec", "any"),
            ("brief_progress", "any"),
            ("brief_spec", "any"),
            ("start_time", "int64"),
            ("finish_time", "int64"),
            ("filter_factors", "string"),
            ("result", "any"),
            ("events", "any"),
            ("alerts", "any"),
            ("slot_index", "int64"),
            ("unrecognized_spec", "any"),
            ("full_spec", "any"),
            ("runtime_parameters", "any")
        ],
        in_memory=True,
        get_pivot_keys=get_default_pivots,
        attributes={
            "tablet_cell_bundle": SYS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
    "ordered_by_start_time": TableInfo(
        [
            ("start_time", "int64"),
            ("id_hi", "uint64"),
            ("id_lo", "uint64"),
        ], [
            ("operation_type", "string"),
            ("state", "string"),
            ("authenticated_user", "string"),
            ("filter_factors", "string"),
            ("pool", "string"),
            ("pools", "any"),
            ("has_failed_jobs", "boolean"),
        ],
        in_memory=True,
        attributes={
            "tablet_cell_bundle": SYS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
    "operation_aliases": TableInfo(
        [
            ("alias_hash", "uint64", "farm_hash(alias)"),
            ("alias", "string"),
        ], [
            ("operation_id_hi", "uint64"),
            ("operation_id_lo", "uint64"),
        ],
        in_memory=True,
        get_pivot_keys=get_default_pivots,
        attributes={
            "tablet_cell_bundle": SYS_BUNDLE_NAME,
            "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
        }),
}

INITIAL_VERSION = 26


def _initialize_archive(client, archive_path, version=INITIAL_VERSION, tablet_cell_bundle=None, shard_count=1, mount=False):
    create_operations_archive_account(client)

    table_infos = copy.deepcopy(INITIAL_TABLE_INFOS)
    for version in range(INITIAL_VERSION + 1, version + 1):
        for conversion in TRANSFORMS.get(version, []):
            if conversion.table_info:
                table_infos[conversion.table] = conversion.table_info

    for table_name, table_info in table_infos.items():
        if tablet_cell_bundle is not None:
            table_info.attributes["tablet_cell_bundle"] = tablet_cell_bundle
        _create_table(client, table_info, ypath_join(archive_path, table_name), shard_count=shard_count)

    one_day = 1000 * 3600 * 24
    one_week = one_day * 7
    one_month = one_day * 30
    two_years = one_month * 12 * 2

    for name in ["jobs", "stderrs", "job_specs", "fail_contexts", "operation_ids"]:
        table = ypath_join(archive_path, name)
        set_table_ttl(client, table, ttl=one_week, auto_compaction_period=one_day, forbid_obsolete_rows=True)
    for name in ["ordered_by_id", "ordered_by_start_time"]:
        table = ypath_join(archive_path, name)
        set_table_ttl(client, table, ttl=two_years, auto_compaction_period=one_month, forbid_obsolete_rows=True)

    if mount:
        for table_name in table_infos.keys():
            client.mount_table(ypath_join(archive_path, table_name), sync=False)
        for table_name in table_infos.keys():
            wait_for_predicate(
                lambda: client.get(ypath_join(archive_path, table_name) + "/@tablet_state") == "mounted",
                "table {} becomes mounted".format(table_name))

    client.set(archive_path + "/@version", version)


TRANSFORMS = {}
ACTIONS = {}


TRANSFORMS[27] = [
    Conversion(
        "ordered_by_id",
        table_info=TableInfo(
            [
                ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("state", "string"),
                ("authenticated_user", "string"),
                ("operation_type", "string"),
                ("progress", "any"),
                ("spec", "any"),
                ("brief_progress", "any"),
                ("brief_spec", "any"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("filter_factors", "string"),
                ("result", "any"),
                ("events", "any"),
                ("alerts", "any"),
                ("slot_index", "int64"),
                ("unrecognized_spec", "any"),
                ("full_spec", "any"),
                ("runtime_parameters", "any"),
                ("slot_index_per_pool_tree", "any"),
            ],
            in_memory=True))
]

TRANSFORMS[28] = [
    Conversion(
        "job_profiles",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64"),
                ("part_index", "int64"),
            ], [
                ("profile_type", "string"),
                ("profile_blob", "string")
            ],
            get_pivot_keys=get_default_pivots,
            attributes={
                "atomicity": "none",
                "tablet_cell_bundle": SYS_BUNDLE_NAME,
            }),
        use_default_mapper=True)
]

TRANSFORMS[29] = [
    Conversion(
        "ordered_by_id",
        table_info=TableInfo(
            [
                ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("state", "string"),
                ("authenticated_user", "string"),
                ("operation_type", "string"),
                ("progress", "any"),
                ("spec", "any"),
                ("brief_progress", "any"),
                ("brief_spec", "any"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("filter_factors", "string"),
                ("result", "any"),
                ("events", "any"),
                ("alerts", "any"),
                ("slot_index", "int64"),
                ("unrecognized_spec", "any"),
                ("full_spec", "any"),
                ("runtime_parameters", "any"),
                ("slot_index_per_pool_tree", "any"),
                ("annotations", "any")
            ],
            in_memory=True))
]

TRANSFORMS[30] = [
    Conversion(
        "ordered_by_start_time",
        table_info=TableInfo(
            [
                ("start_time", "int64"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("operation_type", "string"),
                ("state", "string"),
                ("authenticated_user", "string"),
                ("filter_factors", "string"),
                ("pool", "string"),
                ("pools", "any"),
                ("has_failed_jobs", "boolean"),
                ("acl", "any"),
            ],
            in_memory=True)),
]

TRANSFORMS[31] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
            ],
            attributes={"atomicity": "none"})),
]

TRANSFORMS[32] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string")
            ],
            attributes={"atomicity": "none"})),
]

TRANSFORMS[33] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean")
            ],
            attributes={"atomicity": "none"})),
]

TRANSFORMS[34] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
            ],
            attributes={"atomicity": "none"})),
]

TRANSFORMS[35] = [
    Conversion(
        "ordered_by_id",
        table_info=TableInfo(
            [
                ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("state", "string"),
                ("authenticated_user", "string"),
                ("operation_type", "string"),
                ("progress", "any"),
                ("spec", "any"),
                ("brief_progress", "any"),
                ("brief_spec", "any"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("filter_factors", "string"),
                ("result", "any"),
                ("events", "any"),
                ("alerts", "any"),
                ("slot_index", "int64"),
                ("unrecognized_spec", "any"),
                ("full_spec", "any"),
                ("runtime_parameters", "any"),
                ("slot_index_per_pool_tree", "any"),
                ("annotations", "any"),
                ("task_names", "any")
            ],
            in_memory=True)),
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
                ("task_name", "string"),
            ],
            attributes={"atomicity": "none"}))
]

TRANSFORMS[36] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
                ("task_name", "string"),
                ("statistics_lz4", "string"),
                ("brief_statistics", "any"),
            ],
            attributes={"atomicity": "none"}))
]

TRANSFORMS[37] = [
    Conversion(
        "operation_ids",
        table_info=TableInfo(
            [
                ("job_id_hash", "uint64", "farm_hash(job_id_hi, job_id_lo)"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
            ],
            attributes={"atomicity": "none"})),
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
                ("task_name", "string"),
                ("statistics_lz4", "string"),
                ("brief_statistics", "any"),
                ("pool_tree", "string"),
            ],
            attributes={"atomicity": "none"}))
]


TRANSFORMS[38] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("job_id_partition_hash", "uint64", "farm_hash(job_id_hi, job_id_lo) % {}".format(JOB_TABLE_PARTITION_COUNT)),
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
                ("task_name", "string"),
                ("statistics_lz4", "string"),
                ("brief_statistics", "any"),
                ("pool_tree", "string"),
            ],
            get_pivot_keys=get_job_table_pivots,
            attributes={"atomicity": "none"})),
    Conversion(
        "operation_ids",
        table_info=TableInfo(
            [
                ("job_id_hash", "uint64", "farm_hash(job_id_hi, job_id_lo)"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
            ],
            get_pivot_keys=get_default_pivots,
            attributes={
                "atomicity": "none",
                "tablet_cell_bundle": SYS_BUNDLE_NAME,
                "account": OPERATIONS_ARCHIVE_ACCOUNT_NAME,
            })),
]

TRANSFORMS[39] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("job_id_partition_hash", "uint64", "farm_hash(job_id_hi, job_id_lo) % {}".format(JOB_TABLE_PARTITION_COUNT)),
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
                ("task_name", "string"),
                ("statistics_lz4", "string"),
                ("brief_statistics", "any"),
                ("pool_tree", "string"),
                ("monitoring_descriptor", "string"),
            ],
            get_pivot_keys=get_job_table_pivots,
            attributes={"atomicity": "none"})),
]

TRANSFORMS[40] = [
    Conversion(
        "ordered_by_id",
        table_info=TableInfo(
            [
                ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("state", "string"),
                ("authenticated_user", "string"),
                ("operation_type", "string"),
                ("progress", "any"),
                ("spec", "any"),
                ("experiment_assignments", "any"),
                ("experiment_assignment_names", "any"),
                ("brief_progress", "any"),
                ("brief_spec", "any"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("filter_factors", "string"),
                ("result", "any"),
                ("events", "any"),
                ("alerts", "any"),
                ("slot_index", "int64"),
                ("unrecognized_spec", "any"),
                ("full_spec", "any"),
                ("runtime_parameters", "any"),
                ("slot_index_per_pool_tree", "any"),
                ("annotations", "any"),
                ("task_names", "any")
            ],
            in_memory=True)),
]

TRANSFORMS[41] = [
    Conversion(
        "job_profiles",
        table_info=TableInfo(
            [
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64"),
                ("part_index", "int64"),
            ], [
                ("profile_type", "string"),
                ("profile_blob", "string"),
                ("profiling_probability", "double"),
            ],
            get_pivot_keys=get_default_pivots,
            attributes={
                "atomicity": "none",
                "tablet_cell_bundle": SYS_BUNDLE_NAME,
            }),
        use_default_mapper=True)
]

TRANSFORMS[42] = [
    Conversion(
        "ordered_by_id",
        table_info=TableInfo(
            [
                ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("state", "string"),
                ("authenticated_user", "string"),
                ("operation_type", "string"),
                ("progress", "any"),
                ("spec", "any"),
                ("experiment_assignments", "any"),
                ("experiment_assignment_names", "any"),
                ("brief_progress", "any"),
                ("brief_spec", "any"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("filter_factors", "string"),
                ("result", "any"),
                ("events", "any"),
                ("alerts", "any"),
                ("slot_index", "int64"),
                ("unrecognized_spec", "any"),
                ("full_spec", "any"),
                ("runtime_parameters", "any"),
                ("slot_index_per_pool_tree", "any"),
                ("annotations", "any"),
                ("task_names", "any"),
                ("controller_features", "any"),
            ],
            in_memory=True)),
]

TRANSFORMS[43] = [
    Conversion(
        "ordered_by_id",
        table_info=TableInfo(
            [
                ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("state", "string"),
                ("authenticated_user", "string"),
                ("operation_type", "string"),
                ("progress", "any"),
                ("spec", "any"),
                ("experiment_assignments", "any"),
                ("experiment_assignment_names", "any"),
                ("brief_progress", "any"),
                ("brief_spec", "any"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("filter_factors", "string"),
                ("result", "any"),
                ("events", "any"),
                ("alerts", "any"),
                ("slot_index", "int64"),
                ("unrecognized_spec", "any"),
                ("full_spec", "any"),
                ("runtime_parameters", "any"),
                ("slot_index_per_pool_tree", "any"),
                ("annotations", "any"),
                ("task_names", "any"),
                ("controller_features", "any"),
                ("alert_events", "any"),  # TODO(egor-gutrov): strict type
            ],
            in_memory=True)),
]

TRANSFORMS[44] = [
    Conversion(
        "ordered_by_start_time",
        table_info=TableInfo(
            [
                ("start_time", "int64"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("operation_type", "string"),
                ("state", "string"),
                ("authenticated_user", "string"),
                ("filter_factors", "string"),
                ("pool", "string"),
                ("pools", "any"),
                ("has_failed_jobs", "boolean"),
                ("acl", "any"),
                ("pool_tree_to_pool", "any"),
            ],
            in_memory=True)),
]

TRANSFORMS[45] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("job_id_partition_hash", "uint64", "farm_hash(job_id_hi, job_id_lo) % {}".format(JOB_TABLE_PARTITION_COUNT)),
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
                ("task_name", "string"),
                ("statistics_lz4", "string"),
                ("brief_statistics", "any"),
                ("pool_tree", "string"),
                ("monitoring_descriptor", "string"),
                ("probing_job_competition_id", "string"),
                ("has_probing_competitors", "boolean"),
            ],
            get_pivot_keys=get_job_table_pivots,
            attributes={"atomicity": "none"})),
]

TRANSFORMS[46] = [
    Conversion(
        "ordered_by_id",
        table_info=TableInfo(
            [
                ("id_hash", "uint64", "farm_hash(id_hi, id_lo)"),
                ("id_hi", "uint64"),
                ("id_lo", "uint64"),
            ], [
                ("state", "string"),
                ("authenticated_user", "string"),
                ("operation_type", "string"),
                ("progress", "any"),
                ("provided_spec", "any"),
                ("spec", "any"),
                ("full_spec", "any"),
                ("experiment_assignments", "any"),
                ("experiment_assignment_names", "any"),
                ("brief_progress", "any"),
                ("brief_spec", "any"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("filter_factors", "string"),
                ("result", "any"),
                ("events", "any"),
                ("alerts", "any"),
                ("slot_index", "int64"),
                ("unrecognized_spec", "any"),
                ("runtime_parameters", "any"),
                ("slot_index_per_pool_tree", "any"),
                ("annotations", "any"),
                ("task_names", "any"),
                ("controller_features", "any"),
                ("alert_events", "any"),
            ],
            in_memory=True)),
]

TRANSFORMS[47] = [
    Conversion(
        "jobs",
        table_info=TableInfo(
            [
                ("job_id_partition_hash", "uint64", "farm_hash(job_id_hi, job_id_lo) % {}".format(JOB_TABLE_PARTITION_COUNT)),
                ("operation_id_hash", "uint64", "farm_hash(operation_id_hi, operation_id_lo)"),
                ("operation_id_hi", "uint64"),
                ("operation_id_lo", "uint64"),
                ("job_id_hi", "uint64"),
                ("job_id_lo", "uint64")
            ], [
                ("type", "string"),
                ("state", "string"),
                ("start_time", "int64"),
                ("finish_time", "int64"),
                ("address", "string"),
                ("error", "any"),
                ("statistics", "any"),
                ("stderr_size", "uint64"),
                ("spec", "string"),
                ("spec_version", "int64"),
                ("has_spec", "boolean"),
                ("has_fail_context", "boolean"),
                ("fail_context_size", "uint64"),
                ("events", "any"),
                ("transient_state", "string"),
                ("update_time", "int64"),
                ("core_infos", "any"),
                ("job_competition_id", "string"),
                ("has_competitors", "boolean"),
                ("exec_attributes", "any"),
                ("task_name", "string"),
                ("statistics_lz4", "string"),
                ("brief_statistics", "any"),
                ("pool_tree", "string"),
                ("monitoring_descriptor", "string"),
                ("probing_job_competition_id", "string"),
                ("has_probing_competitors", "boolean"),
                ("job_cookie", "int64"),
            ],
            get_pivot_keys=get_job_table_pivots,
            attributes={"atomicity": "none"})),
]

# NB(renadeen): don't forget to update min_required_archive_version at yt/yt/server/lib/scheduler/config.cpp


def swap_table(client, target, source, version):
    backup_path = target + ".bak.{0}".format(version)
    has_target = False
    if client.exists(target):
        has_target = True
        unmount_table(client, target)

    unmount_table(client, source)

    logging.info("Swapping tables %s <-> %s", source, target)
    if has_target:
        client.move(target, backup_path)
    client.move(source, target)

    mount_table(client, target)


def transform_archive(client, transform_begin, transform_end, force, archive_path, **kwargs):
    logging.info("Transforming archive from %s to %s version", transform_begin - 1, transform_end)
    table_infos = copy.deepcopy(INITIAL_TABLE_INFOS)
    for version in range(INITIAL_VERSION, transform_begin):
        for conversion in TRANSFORMS.get(version, []):
            if conversion.table_info:
                table_infos[conversion.table] = conversion.table_info

    for version in range(transform_begin, transform_end + 1):
        logging.info("Transforming to version %d", version)
        swap_tasks = []
        if version in TRANSFORMS:
            for conversion in TRANSFORMS[version]:
                table = conversion.table
                table_exists = client.exists(ypath_join(archive_path, table))
                tmp_path = "{0}/{1}.tmp.{2}".format(archive_path, table, version)
                if force and client.exists(tmp_path):
                    client.remove(tmp_path)
                in_place = conversion(
                    client=client,
                    table_info=table_infos.get(table),
                    target_table=tmp_path,
                    source_table=table if (table in table_infos and table_exists) else None,
                    archive_path=archive_path,
                    **kwargs)
                if not in_place:
                    swap_tasks.append((ypath_join(archive_path, table), tmp_path))
                if conversion.table_info:
                    table_infos[table] = conversion.table_info

            for target_path, tmp_path in swap_tasks:
                swap_table(client, target_path, tmp_path, version)

        if version in ACTIONS:
            for action in ACTIONS[version]:
                action(client)

        client.set_attribute(archive_path, "version", version)

    for table in table_infos.keys():
        path = ypath_join(archive_path, table)
        if client.get(path + "/@tablet_state") != "mounted":
            mount_table(client, path)


def get_latest_version():
    latest_version = max(TRANSFORMS.keys())
    if ACTIONS:
        latest_version = max(latest_version, max(ACTIONS.keys()))
    return latest_version


def create_tables(client, target_version, override_tablet_cell_bundle="default", shard_count=1, archive_path=DEFAULT_ARCHIVE_PATH):
    """ Creates operation archive tables of given version """
    assert target_version in TRANSFORMS
    assert target_version >= INITIAL_VERSION

    if not client.exists(archive_path):
        _initialize_archive(
            client,
            archive_path=archive_path,
            version=target_version,
            tablet_cell_bundle=override_tablet_cell_bundle,
            shard_count=shard_count,
            mount=True,
        )
        return

    current_version = client.get("{0}/@".format(archive_path)).get("version", INITIAL_VERSION)
    assert current_version >= INITIAL_VERSION, \
        "Expected archive version to be >= {}, got {}".format(INITIAL_VERSION, current_version)

    table_infos = {}
    for version in range(current_version + 1, target_version + 1):
        for conversion in TRANSFORMS.get(version, []):
            if conversion.table_info:
                table_infos[conversion.table] = conversion.table_info

    for table, table_info in table_infos.items():
        table_path = ypath_join(archive_path, table)
        if override_tablet_cell_bundle is not None:
            table_info.attributes["tablet_cell_bundle"] = override_tablet_cell_bundle
        if not client.exists(table_path):
            table_info.create_dynamic_table(client, table_path)
        table_info.alter_table(client, table_path, shard_count)

    client.set(archive_path + "/@version", target_version)


# Warning! This function does NOT perform actual transformations, it only creates tables with latest schemas.
def create_tables_latest_version(client, override_tablet_cell_bundle="default", shard_count=1, archive_path=DEFAULT_ARCHIVE_PATH):
    """ Creates operation archive tables of latest version """
    create_tables(
        client,
        get_latest_version(),
        override_tablet_cell_bundle,
        shard_count=shard_count,
        archive_path=archive_path)


def build_arguments_parser():
    parser = argparse.ArgumentParser(description="Transform operations archive")
    parser.add_argument("--force", action="store_true", default=False)
    parser.add_argument("--archive-path", type=str, default=DEFAULT_ARCHIVE_PATH)
    parser.add_argument("--shard-count", type=int, default=DEFAULT_SHARD_COUNT)
    parser.add_argument("--proxy", type=str, default=config["proxy"]["url"])

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--target-version", type=int)
    group.add_argument("--latest", action="store_true")
    return parser


def run(client, args):
    archive_path = args.archive_path

    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

    client.config['pickling']['module_filter'] = lambda module: 'hashlib' not in getattr(module, '__name__', '')

    if client.exists(archive_path):
        current_version = client.get("{0}/@".format(archive_path)).get("version", INITIAL_VERSION)
    else:
        _initialize_archive(client, archive_path=archive_path)
        current_version = INITIAL_VERSION
    assert current_version >= INITIAL_VERSION, \
        "Expected archive version to be >= {}, got {}".format(INITIAL_VERSION, current_version)

    next_version = current_version + 1

    if args.latest:
        target_version = max(TRANSFORMS.keys())
        if ACTIONS:
            target_version = max(target_version, max(ACTIONS.keys()))
    else:
        target_version = args.target_version
    transform_archive(client, next_version, target_version, args.force, archive_path, shard_count=args.shard_count)


def main():
    args = build_arguments_parser().parse_args()
    client = YtClient(proxy=args.proxy, token=config["token"])

    run(client, args)


if __name__ == "__main__":
    main()
