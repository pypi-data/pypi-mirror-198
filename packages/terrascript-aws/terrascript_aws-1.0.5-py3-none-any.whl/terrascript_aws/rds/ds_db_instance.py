import terrascript.core as core


@core.data(type="aws_db_instance", namespace="rds")
class DsDbInstance(core.Data):
    """
    The hostname of the RDS instance. See also `endpoint` and `port`.
    """

    address: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the allocated storage size specified in gigabytes.
    """
    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    """
    Indicates that minor version patches are applied automatically.
    """
    auto_minor_version_upgrade: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies the name of the Availability Zone the DB instance is located in.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the number of days for which automatic DB snapshots are retained.
    """
    backup_retention_period: int | core.IntOut = core.attr(int, computed=True)

    """
    Specifies the identifier of the CA certificate for the DB instance.
    """
    ca_cert_identifier: str | core.StringOut = core.attr(str, computed=True)

    """
    If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB inst
    ance is a member of.
    """
    db_cluster_identifier: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) for the DB instance.
    """
    db_instance_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Contains the name of the compute and memory capacity class of the DB instance.
    """
    db_instance_class: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the RDS instance
    """
    db_instance_identifier: str | core.StringOut = core.attr(str)

    """
    Specifies the port that the DB instance listens on.
    """
    db_instance_port: int | core.IntOut = core.attr(int, computed=True)

    """
    Contains the name of the initial database of this instance that was provided at create time, if one
    was specified when the DB instance was created. This same name is returned for the life of the DB in
    stance.
    """
    db_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides the list of DB parameter groups applied to this DB instance.
    """
    db_parameter_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Provides List of DB security groups associated to this DB instance.
    """
    db_security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Specifies the name of the subnet group associated with the DB instance.
    """
    db_subnet_group: str | core.StringOut = core.attr(str, computed=True)

    """
    List of log types to export to cloudwatch.
    """
    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The connection endpoint in `address:port` format.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides the name of the database engine to be used for this DB instance.
    """
    engine: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates the database engine version.
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the Provisioned IOPS (I/O operations per second) value.
    """
    iops: int | core.IntOut = core.attr(int, computed=True)

    """
    If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    License model information for this DB instance.
    """
    license_model: str | core.StringOut = core.attr(str, computed=True)

    """
    Contains the master username for the DB instance.
    """
    master_username: str | core.StringOut = core.attr(str, computed=True)

    """
    The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB i
    nstance.
    """
    monitoring_interval: int | core.IntOut = core.attr(int, computed=True)

    """
    The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.
    """
    monitoring_role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies if the DB instance is a Multi-AZ deployment.
    """
    multi_az: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The network type of the DB instance.
    """
    network_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides the list of option group memberships for this DB instance.
    """
    option_group_memberships: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The database port.
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    """
    Specifies the daily time range during which automated backups are created.
    """
    preferred_backup_window: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the weekly time range during which system maintenance can occur in UTC.
    """
    preferred_maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the accessibility options for the DB instance.
    """
    publicly_accessible: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The identifier of the source DB that this is a replica of.
    """
    replicate_source_db: str | core.StringOut = core.attr(str, computed=True)

    """
    The RDS Resource ID of this instance.
    """
    resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether the DB instance is encrypted.
    """
    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies the storage type associated with DB instance.
    """
    storage_type: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The time zone of the DB instance.
    """
    timezone: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides a list of VPC security group elements that the DB instance belongs to.
    """
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
