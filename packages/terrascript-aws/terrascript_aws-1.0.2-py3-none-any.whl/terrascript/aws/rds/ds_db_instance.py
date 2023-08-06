import terrascript.core as core


@core.data(type="aws_db_instance", namespace="aws_rds")
class DsDbInstance(core.Data):

    address: str | core.StringOut = core.attr(str, computed=True)

    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    auto_minor_version_upgrade: bool | core.BoolOut = core.attr(bool, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    backup_retention_period: int | core.IntOut = core.attr(int, computed=True)

    ca_cert_identifier: str | core.StringOut = core.attr(str, computed=True)

    db_cluster_identifier: str | core.StringOut = core.attr(str, computed=True)

    db_instance_arn: str | core.StringOut = core.attr(str, computed=True)

    db_instance_class: str | core.StringOut = core.attr(str, computed=True)

    db_instance_identifier: str | core.StringOut = core.attr(str)

    db_instance_port: int | core.IntOut = core.attr(int, computed=True)

    db_name: str | core.StringOut = core.attr(str, computed=True)

    db_parameter_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    db_security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    db_subnet_group: str | core.StringOut = core.attr(str, computed=True)

    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    license_model: str | core.StringOut = core.attr(str, computed=True)

    master_username: str | core.StringOut = core.attr(str, computed=True)

    monitoring_interval: int | core.IntOut = core.attr(int, computed=True)

    monitoring_role_arn: str | core.StringOut = core.attr(str, computed=True)

    multi_az: bool | core.BoolOut = core.attr(bool, computed=True)

    network_type: str | core.StringOut = core.attr(str, computed=True)

    option_group_memberships: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    port: int | core.IntOut = core.attr(int, computed=True)

    preferred_backup_window: str | core.StringOut = core.attr(str, computed=True)

    preferred_maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    publicly_accessible: bool | core.BoolOut = core.attr(bool, computed=True)

    replicate_source_db: str | core.StringOut = core.attr(str, computed=True)

    resource_id: str | core.StringOut = core.attr(str, computed=True)

    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    storage_type: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timezone: str | core.StringOut = core.attr(str, computed=True)

    vpc_security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        db_instance_identifier: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbInstance.Args(
                db_instance_identifier=db_instance_identifier,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_instance_identifier: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
