import terrascript.core as core


@core.data(type="aws_db_snapshot", namespace="aws_rds")
class DsDbSnapshot(core.Data):

    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    db_instance_identifier: str | core.StringOut | None = core.attr(str, default=None)

    db_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    db_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    include_public: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_shared: bool | core.BoolOut | None = core.attr(bool, default=None)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    license_model: str | core.StringOut = core.attr(str, computed=True)

    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    option_group_name: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    snapshot_create_time: str | core.StringOut = core.attr(str, computed=True)

    snapshot_type: str | core.StringOut | None = core.attr(str, default=None)

    source_db_snapshot_identifier: str | core.StringOut = core.attr(str, computed=True)

    source_region: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    storage_type: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        db_instance_identifier: str | core.StringOut | None = None,
        db_snapshot_identifier: str | core.StringOut | None = None,
        include_public: bool | core.BoolOut | None = None,
        include_shared: bool | core.BoolOut | None = None,
        most_recent: bool | core.BoolOut | None = None,
        snapshot_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbSnapshot.Args(
                db_instance_identifier=db_instance_identifier,
                db_snapshot_identifier=db_snapshot_identifier,
                include_public=include_public,
                include_shared=include_shared,
                most_recent=most_recent,
                snapshot_type=snapshot_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_instance_identifier: str | core.StringOut | None = core.arg(default=None)

        db_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        include_public: bool | core.BoolOut | None = core.arg(default=None)

        include_shared: bool | core.BoolOut | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_type: str | core.StringOut | None = core.arg(default=None)
