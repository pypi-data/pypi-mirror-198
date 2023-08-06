import terrascript.core as core


@core.data(type="aws_rds_orderable_db_instance", namespace="rds")
class DsOrderableDbInstance(core.Data):

    availability_zone_group: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    engine: str | core.StringOut = core.attr(str)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    license_model: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    max_iops_per_db_instance: int | core.IntOut = core.attr(int, computed=True)

    max_iops_per_gib: float | core.FloatOut = core.attr(float, computed=True)

    max_storage_size: int | core.IntOut = core.attr(int, computed=True)

    min_iops_per_db_instance: int | core.IntOut = core.attr(int, computed=True)

    min_iops_per_gib: float | core.FloatOut = core.attr(float, computed=True)

    min_storage_size: int | core.IntOut = core.attr(int, computed=True)

    multi_az_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    outpost_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    preferred_engine_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    read_replica_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    storage_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    supported_engine_modes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_network_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supports_enhanced_monitoring: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    supports_global_databases: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    supports_iam_database_authentication: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    supports_iops: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    supports_kerberos_authentication: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    supports_performance_insights: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    supports_storage_autoscaling: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    supports_storage_encryption: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    vpc: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        engine: str | core.StringOut,
        availability_zone_group: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        instance_class: str | core.StringOut | None = None,
        license_model: str | core.StringOut | None = None,
        preferred_engine_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        storage_type: str | core.StringOut | None = None,
        supports_enhanced_monitoring: bool | core.BoolOut | None = None,
        supports_global_databases: bool | core.BoolOut | None = None,
        supports_iam_database_authentication: bool | core.BoolOut | None = None,
        supports_iops: bool | core.BoolOut | None = None,
        supports_kerberos_authentication: bool | core.BoolOut | None = None,
        supports_performance_insights: bool | core.BoolOut | None = None,
        supports_storage_autoscaling: bool | core.BoolOut | None = None,
        supports_storage_encryption: bool | core.BoolOut | None = None,
        vpc: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOrderableDbInstance.Args(
                engine=engine,
                availability_zone_group=availability_zone_group,
                engine_version=engine_version,
                instance_class=instance_class,
                license_model=license_model,
                preferred_engine_versions=preferred_engine_versions,
                preferred_instance_classes=preferred_instance_classes,
                storage_type=storage_type,
                supports_enhanced_monitoring=supports_enhanced_monitoring,
                supports_global_databases=supports_global_databases,
                supports_iam_database_authentication=supports_iam_database_authentication,
                supports_iops=supports_iops,
                supports_kerberos_authentication=supports_kerberos_authentication,
                supports_performance_insights=supports_performance_insights,
                supports_storage_autoscaling=supports_storage_autoscaling,
                supports_storage_encryption=supports_storage_encryption,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone_group: str | core.StringOut | None = core.arg(default=None)

        engine: str | core.StringOut = core.arg()

        engine_version: str | core.StringOut | None = core.arg(default=None)

        instance_class: str | core.StringOut | None = core.arg(default=None)

        license_model: str | core.StringOut | None = core.arg(default=None)

        preferred_engine_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        storage_type: str | core.StringOut | None = core.arg(default=None)

        supports_enhanced_monitoring: bool | core.BoolOut | None = core.arg(default=None)

        supports_global_databases: bool | core.BoolOut | None = core.arg(default=None)

        supports_iam_database_authentication: bool | core.BoolOut | None = core.arg(default=None)

        supports_iops: bool | core.BoolOut | None = core.arg(default=None)

        supports_kerberos_authentication: bool | core.BoolOut | None = core.arg(default=None)

        supports_performance_insights: bool | core.BoolOut | None = core.arg(default=None)

        supports_storage_autoscaling: bool | core.BoolOut | None = core.arg(default=None)

        supports_storage_encryption: bool | core.BoolOut | None = core.arg(default=None)

        vpc: bool | core.BoolOut | None = core.arg(default=None)
