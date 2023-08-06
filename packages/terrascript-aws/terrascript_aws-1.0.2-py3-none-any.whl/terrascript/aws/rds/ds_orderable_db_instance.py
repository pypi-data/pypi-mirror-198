import terrascript.core as core


@core.data(type="aws_rds_orderable_db_instance", namespace="aws_rds")
class DsOrderableDbInstance(core.Data):
    """
    (Optional) Availability zone group.
    """

    availability_zone_group: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    Availability zones where the instance is available.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) DB engine. Engine values include `aurora`, `aurora-mysql`, `aurora-postgresql`, `docdb`,
    mariadb`, `mysql`, `neptune`, `oracle-ee`, `oracle-se`, `oracle-se1`, `oracle-se2`, `postgres`, `sq
    lserver-ee`, `sqlserver-ex`, `sqlserver-se`, and `sqlserver-web`.
    """
    engine: str | core.StringOut = core.attr(str)

    """
    (Optional) Version of the DB engine. If none is provided, the AWS-defined default version will be us
    ed.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) DB instance class. Examples of classes are `db.m3.2xlarge`, `db.t2.small`, and `db.m3.med
    ium`.
    """
    instance_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) License model. Examples of license models are `general-public-license`, `bring-your-own-l
    icense`, and `amazon-license`.
    """
    license_model: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Maximum total provisioned IOPS for a DB instance.
    """
    max_iops_per_db_instance: int | core.IntOut = core.attr(int, computed=True)

    """
    Maximum provisioned IOPS per GiB for a DB instance.
    """
    max_iops_per_gib: float | core.FloatOut = core.attr(float, computed=True)

    """
    Maximum storage size for a DB instance.
    """
    max_storage_size: int | core.IntOut = core.attr(int, computed=True)

    """
    Minimum total provisioned IOPS for a DB instance.
    """
    min_iops_per_db_instance: int | core.IntOut = core.attr(int, computed=True)

    """
    Minimum provisioned IOPS per GiB for a DB instance.
    """
    min_iops_per_gib: float | core.FloatOut = core.attr(float, computed=True)

    """
    Minimum storage size for a DB instance.
    """
    min_storage_size: int | core.IntOut = core.attr(int, computed=True)

    """
    Whether a DB instance is Multi-AZ capable.
    """
    multi_az_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether a DB instance supports RDS on Outposts.
    """
    outpost_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Ordered list of preferred RDS DB instance engine versions. The first match in this list w
    ill be returned. If no preferred matches are found and the original search returned more than one re
    sult, an error is returned.
    """
    preferred_engine_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Ordered list of preferred RDS DB instance classes. The first match in this list will be r
    eturned. If no preferred matches are found and the original search returned more than one result, an
    error is returned.
    """
    preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Whether a DB instance can have a read replica.
    """
    read_replica_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Storage types. Examples of storage types are `standard`, `io1`, `gp2`, and `aurora`.
    """
    storage_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A list of the supported DB engine modes.
    """
    supported_engine_modes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The network types supported by the DB instance (`IPV4` or `DUAL`).
    """
    supported_network_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Enable this to ensure a DB instance supports Enhanced Monitoring at intervals from 1 to 6
    0 seconds.
    """
    supports_enhanced_monitoring: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Enable this to ensure a DB instance supports Aurora global databases with a specific comb
    ination of other DB engine attributes.
    """
    supports_global_databases: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Enable this to ensure a DB instance supports IAM database authentication.
    """
    supports_iam_database_authentication: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Enable this to ensure a DB instance supports provisioned IOPS.
    """
    supports_iops: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Enable this to ensure a DB instance supports Kerberos Authentication.
    """
    supports_kerberos_authentication: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Enable this to ensure a DB instance supports Performance Insights.
    """
    supports_performance_insights: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Enable this to ensure Amazon RDS can automatically scale storage for DB instances that us
    e the specified DB instance class.
    """
    supports_storage_autoscaling: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Enable this to ensure a DB instance supports encrypted storage.
    """
    supports_storage_encryption: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Boolean that indicates whether to show only VPC or non-VPC offerings.
    """
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
