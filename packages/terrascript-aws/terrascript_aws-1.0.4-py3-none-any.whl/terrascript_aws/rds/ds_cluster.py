import terrascript.core as core


@core.data(type="aws_rds_cluster", namespace="rds")
class DsCluster(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    backtrack_window: int | core.IntOut = core.attr(int, computed=True)

    backup_retention_period: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The cluster identifier of the RDS cluster.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    cluster_members: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    database_name: str | core.StringOut = core.attr(str, computed=True)

    db_cluster_parameter_group_name: str | core.StringOut = core.attr(str, computed=True)

    db_subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    final_snapshot_identifier: str | core.StringOut = core.attr(str, computed=True)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    iam_database_authentication_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    iam_roles: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    master_username: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    preferred_backup_window: str | core.StringOut = core.attr(str, computed=True)

    preferred_maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    reader_endpoint: str | core.StringOut = core.attr(str, computed=True)

    replication_source_identifier: str | core.StringOut = core.attr(str, computed=True)

    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                cluster_identifier=cluster_identifier,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_identifier: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
