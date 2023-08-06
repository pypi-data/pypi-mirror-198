import terrascript.core as core


@core.resource(type="aws_rds_cluster_instance", namespace="aws_rds")
class ClusterInstance(core.Resource):

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ca_cert_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cluster_identifier: str | core.StringOut = core.attr(str)

    copy_tags_to_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    db_parameter_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    db_subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    dbi_resource_id: str | core.StringOut = core.attr(str, computed=True)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut | None = core.attr(str, default=None)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    identifier_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    instance_class: str | core.StringOut = core.attr(str)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    monitoring_interval: int | core.IntOut | None = core.attr(int, default=None)

    monitoring_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    performance_insights_enabled: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    performance_insights_kms_key_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    performance_insights_retention_period: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    port: int | core.IntOut = core.attr(int, computed=True)

    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    promotion_tier: int | core.IntOut | None = core.attr(int, default=None)

    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    writer: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        instance_class: str | core.StringOut,
        apply_immediately: bool | core.BoolOut | None = None,
        auto_minor_version_upgrade: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        ca_cert_identifier: str | core.StringOut | None = None,
        copy_tags_to_snapshot: bool | core.BoolOut | None = None,
        db_parameter_group_name: str | core.StringOut | None = None,
        db_subnet_group_name: str | core.StringOut | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        identifier: str | core.StringOut | None = None,
        identifier_prefix: str | core.StringOut | None = None,
        monitoring_interval: int | core.IntOut | None = None,
        monitoring_role_arn: str | core.StringOut | None = None,
        performance_insights_enabled: bool | core.BoolOut | None = None,
        performance_insights_kms_key_id: str | core.StringOut | None = None,
        performance_insights_retention_period: int | core.IntOut | None = None,
        preferred_backup_window: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        promotion_tier: int | core.IntOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterInstance.Args(
                cluster_identifier=cluster_identifier,
                instance_class=instance_class,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                ca_cert_identifier=ca_cert_identifier,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                db_parameter_group_name=db_parameter_group_name,
                db_subnet_group_name=db_subnet_group_name,
                engine=engine,
                engine_version=engine_version,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                monitoring_interval=monitoring_interval,
                monitoring_role_arn=monitoring_role_arn,
                performance_insights_enabled=performance_insights_enabled,
                performance_insights_kms_key_id=performance_insights_kms_key_id,
                performance_insights_retention_period=performance_insights_retention_period,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                promotion_tier=promotion_tier,
                publicly_accessible=publicly_accessible,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        auto_minor_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        ca_cert_identifier: str | core.StringOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut = core.arg()

        copy_tags_to_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        db_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        db_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        identifier: str | core.StringOut | None = core.arg(default=None)

        identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        instance_class: str | core.StringOut = core.arg()

        monitoring_interval: int | core.IntOut | None = core.arg(default=None)

        monitoring_role_arn: str | core.StringOut | None = core.arg(default=None)

        performance_insights_enabled: bool | core.BoolOut | None = core.arg(default=None)

        performance_insights_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        performance_insights_retention_period: int | core.IntOut | None = core.arg(default=None)

        preferred_backup_window: str | core.StringOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        promotion_tier: int | core.IntOut | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
