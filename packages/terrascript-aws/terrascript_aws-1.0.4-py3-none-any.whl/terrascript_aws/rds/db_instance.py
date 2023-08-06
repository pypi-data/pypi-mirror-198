import terrascript.core as core


@core.schema
class S3Import(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    ingestion_role: str | core.StringOut = core.attr(str)

    source_engine: str | core.StringOut = core.attr(str)

    source_engine_version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        ingestion_role: str | core.StringOut,
        source_engine: str | core.StringOut,
        source_engine_version: str | core.StringOut,
        bucket_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Import.Args(
                bucket_name=bucket_name,
                ingestion_role=ingestion_role,
                source_engine=source_engine,
                source_engine_version=source_engine_version,
                bucket_prefix=bucket_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        ingestion_role: str | core.StringOut = core.arg()

        source_engine: str | core.StringOut = core.arg()

        source_engine_version: str | core.StringOut = core.arg()


@core.schema
class RestoreToPointInTime(core.Schema):

    restore_time: str | core.StringOut | None = core.attr(str, default=None)

    source_db_instance_automated_backups_arn: str | core.StringOut | None = core.attr(
        str, default=None
    )

    source_db_instance_identifier: str | core.StringOut | None = core.attr(str, default=None)

    source_dbi_resource_id: str | core.StringOut | None = core.attr(str, default=None)

    use_latest_restorable_time: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        restore_time: str | core.StringOut | None = None,
        source_db_instance_automated_backups_arn: str | core.StringOut | None = None,
        source_db_instance_identifier: str | core.StringOut | None = None,
        source_dbi_resource_id: str | core.StringOut | None = None,
        use_latest_restorable_time: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=RestoreToPointInTime.Args(
                restore_time=restore_time,
                source_db_instance_automated_backups_arn=source_db_instance_automated_backups_arn,
                source_db_instance_identifier=source_db_instance_identifier,
                source_dbi_resource_id=source_dbi_resource_id,
                use_latest_restorable_time=use_latest_restorable_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        restore_time: str | core.StringOut | None = core.arg(default=None)

        source_db_instance_automated_backups_arn: str | core.StringOut | None = core.arg(
            default=None
        )

        source_db_instance_identifier: str | core.StringOut | None = core.arg(default=None)

        source_dbi_resource_id: str | core.StringOut | None = core.arg(default=None)

        use_latest_restorable_time: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_db_instance", namespace="rds")
class DbInstance(core.Resource):
    """
    The hostname of the RDS instance. See also `endpoint` and `port`.
    """

    address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required unless a `snapshot_identifier` or `replicate_source_db` is provided) The allocated storage
    in gibibytes. If `max_allocated_storage` is configured, this argument represents the initial storag
    e allocation and differences from the configuration will be ignored automatically when Storage Autos
    caling occurs. If `replicate_source_db` is set, the value is ignored during the creation of the inst
    ance.
    """
    allocated_storage: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Indicates that major version
    """
    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether any database modifications
    """
    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The ARN of the RDS instance.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates that minor engine upgrades
    """
    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The AZ for the RDS instance.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The days to retain backups for. Must be
    """
    backup_retention_period: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The daily time range (in UTC) during which
    """
    backup_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The identifier of the CA certificate for the DB instance.
    """
    ca_cert_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The character set name to use for DB
    """
    character_set_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    copy_tags_to_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Indicates whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB
    instance. See [CoIP for RDS on Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-
    on-outposts.html#rds-on-outposts.coip) for more information.
    """
    customer_owned_ip_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The name of the database to create when the DB instance is created. If this parameter is
    not specified, no database is created in the DB instance. Note that this does not apply for Oracle o
    r SQL Server engines. See the [AWS documentation](https://awscli.amazonaws.com/v2/documentation/api/
    latest/reference/rds/create-db-instance.html) for more details on what applies for those engines. If
    you are providing an Oracle db name, it needs to be in all upper case. Cannot be specified for a re
    plica.
    """
    db_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of [DB subnet group](/docs/providers/aws/r/db_subnet_group.html). DB instance will
    """
    db_subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies whether to remove automated backups immediately after the DB instance is delete
    d. Default is `true`.
    """
    delete_automated_backups: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If the DB instance should have deletion protection enabled. The database can't be deleted
    when this value is set to `true`. The default is `false`.
    """
    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The ID of the Directory Service Active Directory domain to create the instance in.
    """
    domain: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, but required if domain is provided) The name of the IAM role to be used when making API c
    alls to the Directory Service.
    """
    domain_iam_role_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Set of log types to enable for exporting to CloudWatch logs. If omitted, no logs will be
    exported. Valid values (depending on `engine`). MySQL and MariaDB: `audit`, `error`, `general`, `slo
    wquery`. PostgreSQL: `postgresql`, `upgrade`. MSSQL: `agent` , `error`. Oracle: `alert`, `audit`, `l
    istener`, `trace`.
    """
    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The connection endpoint in `address:port` format.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required unless a `snapshot_identifier` or `replicate_source_db`
    """
    engine: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The engine version to use. If `auto_minor_version_upgrade`
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The running version of the database.
    """
    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of your final DB snapshot
    """
    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    The canonical hosted zone ID of the DB instance (to be used
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether or
    """
    iam_database_authentication_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The RDS instance ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The name of the RDS instance,
    """
    identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique
    """
    identifier_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The instance type of the RDS instance.
    """
    instance_class: str | core.StringOut = core.attr(str)

    """
    (Optional) The amount of provisioned IOPS. Setting this implies a
    """
    iops: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The ARN for the KMS encryption key. If creating an
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The latest time, in UTC [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8), to which
    a database can be restored with point-in-time restore.
    """
    latest_restorable_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, but required for some DB engines, i.e., Oracle
    """
    license_model: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The window to perform maintenance in.
    """
    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) When configured, the upper limit to which Amazon RDS can automatically scale the storage
    of the DB instance. Configuring this will automatically ignore differences to `allocated_storage`. M
    ust be greater than or equal to `allocated_storage` or `0` to disable Storage Autoscaling.
    """
    max_allocated_storage: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The interval, in seconds, between points
    """
    monitoring_interval: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The ARN for the IAM role that permits RDS
    """
    monitoring_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies if the RDS instance is multi-AZ
    """
    multi_az: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional, **Deprecated** use `db_name` instead) The name of the database to create when the DB inst
    ance is created. If this parameter is not specified, no database is created in the DB instance. Note
    that this does not apply for Oracle or SQL Server engines. See the [AWS documentation](https://awsc
    li.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html) for more details
    on what applies for those engines. If you are providing an Oracle db name, it needs to be in all up
    per case. Cannot be specified for a replica.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) The national character set is used in the NCHAR, NVARCHAR2, and NCLO
    B data types for Oracle instances. This can't be changed. See [Oracle Character Sets
    """
    nchar_character_set_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The network type of the DB instance. Valid values: `IPV4`, `DUAL`.
    """
    network_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the DB option group to associate.
    """
    option_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the DB parameter group to
    """
    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required unless a `snapshot_identifier` or `replicate_source_db`
    """
    password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether Performance Insights are enabled. Defaults to false.
    """
    performance_insights_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The ARN for the KMS key to encrypt Performance Insights data. When specifying `performanc
    e_insights_kms_key_id`, `performance_insights_enabled` needs to be set to true. Once KMS key is set,
    it can never be changed.
    """
    performance_insights_kms_key_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The amount of time in days to retain Performance Insights data. Either 7 (7 days) or 731
    (2 years). When specifying `performance_insights_retention_period`, `performance_insights_enabled` n
    eeds to be set to true. Defaults to '7'.
    """
    performance_insights_retention_period: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) The port on which the DB accepts connections.
    """
    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Bool to control if instance is publicly
    """
    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether the replica is in either `mounted` or `open-read-only` mode. This attri
    bute
    """
    replica_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    replicas: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Specifies that this resource is a Replicate
    """
    replicate_source_db: str | core.StringOut | None = core.attr(str, default=None)

    """
    The RDS Resource ID of this instance.
    """
    resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) A configuration block for restoring a DB instance to an arbitrary po
    int in time. Requires the `identifier` argument to be set with the name of the new DB instance to be
    created. See [Restore To Point In Time](#restore-to-point-in-time) below for details.
    """
    restore_to_point_in_time: RestoreToPointInTime | None = core.attr(
        RestoreToPointInTime, default=None
    )

    """
    (Optional) Restore from a Percona Xtrabackup in S3.  See [Importing Data into an Amazon RDS MySQL DB
    Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html)
    """
    s3_import: S3Import | None = core.attr(S3Import, default=None)

    """
    (Optional/Deprecated) List of DB Security Groups to
    """
    security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Determines whether a final DB snapshot is
    """
    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether or not to create this
    """
    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The RDS instance status.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether the DB instance is
    """
    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) One of "standard" (magnetic), "gp2" (general
    """
    storage_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Time zone of the DB instance. `timezone` is currently
    """
    timezone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required unless a `snapshot_identifier` or `replicate_source_db`
    """
    username: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) List of VPC security groups to
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        instance_class: str | core.StringOut,
        allocated_storage: int | core.IntOut | None = None,
        allow_major_version_upgrade: bool | core.BoolOut | None = None,
        apply_immediately: bool | core.BoolOut | None = None,
        auto_minor_version_upgrade: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        backup_retention_period: int | core.IntOut | None = None,
        backup_window: str | core.StringOut | None = None,
        ca_cert_identifier: str | core.StringOut | None = None,
        character_set_name: str | core.StringOut | None = None,
        copy_tags_to_snapshot: bool | core.BoolOut | None = None,
        customer_owned_ip_enabled: bool | core.BoolOut | None = None,
        db_name: str | core.StringOut | None = None,
        db_subnet_group_name: str | core.StringOut | None = None,
        delete_automated_backups: bool | core.BoolOut | None = None,
        deletion_protection: bool | core.BoolOut | None = None,
        domain: str | core.StringOut | None = None,
        domain_iam_role_name: str | core.StringOut | None = None,
        enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        iam_database_authentication_enabled: bool | core.BoolOut | None = None,
        identifier: str | core.StringOut | None = None,
        identifier_prefix: str | core.StringOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        license_model: str | core.StringOut | None = None,
        maintenance_window: str | core.StringOut | None = None,
        max_allocated_storage: int | core.IntOut | None = None,
        monitoring_interval: int | core.IntOut | None = None,
        monitoring_role_arn: str | core.StringOut | None = None,
        multi_az: bool | core.BoolOut | None = None,
        name: str | core.StringOut | None = None,
        nchar_character_set_name: str | core.StringOut | None = None,
        network_type: str | core.StringOut | None = None,
        option_group_name: str | core.StringOut | None = None,
        parameter_group_name: str | core.StringOut | None = None,
        password: str | core.StringOut | None = None,
        performance_insights_enabled: bool | core.BoolOut | None = None,
        performance_insights_kms_key_id: str | core.StringOut | None = None,
        performance_insights_retention_period: int | core.IntOut | None = None,
        port: int | core.IntOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        replica_mode: str | core.StringOut | None = None,
        replicate_source_db: str | core.StringOut | None = None,
        restore_to_point_in_time: RestoreToPointInTime | None = None,
        s3_import: S3Import | None = None,
        security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        skip_final_snapshot: bool | core.BoolOut | None = None,
        snapshot_identifier: str | core.StringOut | None = None,
        storage_encrypted: bool | core.BoolOut | None = None,
        storage_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timezone: str | core.StringOut | None = None,
        username: str | core.StringOut | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbInstance.Args(
                instance_class=instance_class,
                allocated_storage=allocated_storage,
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                backup_retention_period=backup_retention_period,
                backup_window=backup_window,
                ca_cert_identifier=ca_cert_identifier,
                character_set_name=character_set_name,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                customer_owned_ip_enabled=customer_owned_ip_enabled,
                db_name=db_name,
                db_subnet_group_name=db_subnet_group_name,
                delete_automated_backups=delete_automated_backups,
                deletion_protection=deletion_protection,
                domain=domain,
                domain_iam_role_name=domain_iam_role_name,
                enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                iam_database_authentication_enabled=iam_database_authentication_enabled,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                iops=iops,
                kms_key_id=kms_key_id,
                license_model=license_model,
                maintenance_window=maintenance_window,
                max_allocated_storage=max_allocated_storage,
                monitoring_interval=monitoring_interval,
                monitoring_role_arn=monitoring_role_arn,
                multi_az=multi_az,
                name=name,
                nchar_character_set_name=nchar_character_set_name,
                network_type=network_type,
                option_group_name=option_group_name,
                parameter_group_name=parameter_group_name,
                password=password,
                performance_insights_enabled=performance_insights_enabled,
                performance_insights_kms_key_id=performance_insights_kms_key_id,
                performance_insights_retention_period=performance_insights_retention_period,
                port=port,
                publicly_accessible=publicly_accessible,
                replica_mode=replica_mode,
                replicate_source_db=replicate_source_db,
                restore_to_point_in_time=restore_to_point_in_time,
                s3_import=s3_import,
                security_group_names=security_group_names,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_identifier=snapshot_identifier,
                storage_encrypted=storage_encrypted,
                storage_type=storage_type,
                tags=tags,
                tags_all=tags_all,
                timezone=timezone,
                username=username,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocated_storage: int | core.IntOut | None = core.arg(default=None)

        allow_major_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        auto_minor_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        backup_retention_period: int | core.IntOut | None = core.arg(default=None)

        backup_window: str | core.StringOut | None = core.arg(default=None)

        ca_cert_identifier: str | core.StringOut | None = core.arg(default=None)

        character_set_name: str | core.StringOut | None = core.arg(default=None)

        copy_tags_to_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        customer_owned_ip_enabled: bool | core.BoolOut | None = core.arg(default=None)

        db_name: str | core.StringOut | None = core.arg(default=None)

        db_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        delete_automated_backups: bool | core.BoolOut | None = core.arg(default=None)

        deletion_protection: bool | core.BoolOut | None = core.arg(default=None)

        domain: str | core.StringOut | None = core.arg(default=None)

        domain_iam_role_name: str | core.StringOut | None = core.arg(default=None)

        enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        iam_database_authentication_enabled: bool | core.BoolOut | None = core.arg(default=None)

        identifier: str | core.StringOut | None = core.arg(default=None)

        identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        instance_class: str | core.StringOut = core.arg()

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        license_model: str | core.StringOut | None = core.arg(default=None)

        maintenance_window: str | core.StringOut | None = core.arg(default=None)

        max_allocated_storage: int | core.IntOut | None = core.arg(default=None)

        monitoring_interval: int | core.IntOut | None = core.arg(default=None)

        monitoring_role_arn: str | core.StringOut | None = core.arg(default=None)

        multi_az: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        nchar_character_set_name: str | core.StringOut | None = core.arg(default=None)

        network_type: str | core.StringOut | None = core.arg(default=None)

        option_group_name: str | core.StringOut | None = core.arg(default=None)

        parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        password: str | core.StringOut | None = core.arg(default=None)

        performance_insights_enabled: bool | core.BoolOut | None = core.arg(default=None)

        performance_insights_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        performance_insights_retention_period: int | core.IntOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        replica_mode: str | core.StringOut | None = core.arg(default=None)

        replicate_source_db: str | core.StringOut | None = core.arg(default=None)

        restore_to_point_in_time: RestoreToPointInTime | None = core.arg(default=None)

        s3_import: S3Import | None = core.arg(default=None)

        security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        skip_final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        storage_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        storage_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        timezone: str | core.StringOut | None = core.arg(default=None)

        username: str | core.StringOut | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
