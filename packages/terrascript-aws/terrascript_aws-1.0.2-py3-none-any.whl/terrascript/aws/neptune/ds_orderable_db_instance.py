import terrascript.core as core


@core.data(type="aws_neptune_orderable_db_instance", namespace="aws_neptune")
class DsOrderableDbInstance(core.Data):
    """
    Availability zones where the instance is available.
    """

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) DB engine. (Default: `neptune`)
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Version of the DB engine. For example, `1.0.1.0`, `1.0.1.2`, `1.0.2.2`, and `1.0.3.0`.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) DB instance class. Examples of classes are `db.r5.large`, `db.r5.xlarge`, `db.r4.large`,
    db.r5.4xlarge`, `db.r5.12xlarge`, `db.r4.xlarge`, and `db.t3.medium`.
    """
    instance_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) License model. (Default: `amazon-license`)
    """
    license_model: str | core.StringOut | None = core.attr(str, default=None)

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
    (Optional) Ordered list of preferred Neptune DB instance classes. The first match in this list will
    be returned. If no preferred matches are found and the original search returned more than one result
    , an error is returned.
    """
    preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Whether a DB instance can have a read replica.
    """
    read_replica_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The storage type for a DB instance.
    """
    storage_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.
    """
    supports_enhanced_monitoring: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether a DB instance supports IAM database authentication.
    """
    supports_iam_database_authentication: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether a DB instance supports provisioned IOPS.
    """
    supports_iops: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether a DB instance supports Performance Insights.
    """
    supports_performance_insights: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether a DB instance supports encrypted storage.
    """
    supports_storage_encryption: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Enable to show only VPC offerings.
    """
    vpc: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        instance_class: str | core.StringOut | None = None,
        license_model: str | core.StringOut | None = None,
        preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        vpc: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOrderableDbInstance.Args(
                engine=engine,
                engine_version=engine_version,
                instance_class=instance_class,
                license_model=license_model,
                preferred_instance_classes=preferred_instance_classes,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        instance_class: str | core.StringOut | None = core.arg(default=None)

        license_model: str | core.StringOut | None = core.arg(default=None)

        preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        vpc: bool | core.BoolOut | None = core.arg(default=None)
