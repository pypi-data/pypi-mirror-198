import terrascript.core as core


@core.resource(type="aws_neptune_cluster", namespace="aws_neptune")
class Cluster(core.Resource):

    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    backup_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    cluster_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cluster_identifier_prefix: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cluster_members: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    copy_tags_to_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut | None = core.attr(str, default=None)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    iam_database_authentication_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    neptune_cluster_parameter_group_name: str | core.StringOut | None = core.attr(str, default=None)

    neptune_subnet_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    port: int | core.IntOut | None = core.attr(int, default=None)

    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    reader_endpoint: str | core.StringOut = core.attr(str, computed=True)

    replication_source_identifier: str | core.StringOut | None = core.attr(str, default=None)

    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        allow_major_version_upgrade: bool | core.BoolOut | None = None,
        apply_immediately: bool | core.BoolOut | None = None,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        backup_retention_period: int | core.IntOut | None = None,
        cluster_identifier: str | core.StringOut | None = None,
        cluster_identifier_prefix: str | core.StringOut | None = None,
        copy_tags_to_snapshot: bool | core.BoolOut | None = None,
        deletion_protection: bool | core.BoolOut | None = None,
        enable_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        iam_database_authentication_enabled: bool | core.BoolOut | None = None,
        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        neptune_cluster_parameter_group_name: str | core.StringOut | None = None,
        neptune_subnet_group_name: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_backup_window: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        replication_source_identifier: str | core.StringOut | None = None,
        skip_final_snapshot: bool | core.BoolOut | None = None,
        snapshot_identifier: str | core.StringOut | None = None,
        storage_encrypted: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                availability_zones=availability_zones,
                backup_retention_period=backup_retention_period,
                cluster_identifier=cluster_identifier,
                cluster_identifier_prefix=cluster_identifier_prefix,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                deletion_protection=deletion_protection,
                enable_cloudwatch_logs_exports=enable_cloudwatch_logs_exports,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                iam_database_authentication_enabled=iam_database_authentication_enabled,
                iam_roles=iam_roles,
                kms_key_arn=kms_key_arn,
                neptune_cluster_parameter_group_name=neptune_cluster_parameter_group_name,
                neptune_subnet_group_name=neptune_subnet_group_name,
                port=port,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                replication_source_identifier=replication_source_identifier,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_identifier=snapshot_identifier,
                storage_encrypted=storage_encrypted,
                tags=tags,
                tags_all=tags_all,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_major_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        backup_retention_period: int | core.IntOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        cluster_identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        copy_tags_to_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        deletion_protection: bool | core.BoolOut | None = core.arg(default=None)

        enable_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        iam_database_authentication_enabled: bool | core.BoolOut | None = core.arg(default=None)

        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        neptune_cluster_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        neptune_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_backup_window: str | core.StringOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        replication_source_identifier: str | core.StringOut | None = core.arg(default=None)

        skip_final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        storage_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
