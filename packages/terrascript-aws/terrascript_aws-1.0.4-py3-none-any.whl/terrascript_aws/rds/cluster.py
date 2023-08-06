import terrascript.core as core


@core.schema
class Serverlessv2ScalingConfiguration(core.Schema):

    max_capacity: float | core.FloatOut = core.attr(float)

    min_capacity: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        *,
        max_capacity: float | core.FloatOut,
        min_capacity: float | core.FloatOut,
    ):
        super().__init__(
            args=Serverlessv2ScalingConfiguration.Args(
                max_capacity=max_capacity,
                min_capacity=min_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_capacity: float | core.FloatOut = core.arg()

        min_capacity: float | core.FloatOut = core.arg()


@core.schema
class ScalingConfiguration(core.Schema):

    auto_pause: bool | core.BoolOut | None = core.attr(bool, default=None)

    max_capacity: int | core.IntOut | None = core.attr(int, default=None)

    min_capacity: int | core.IntOut | None = core.attr(int, default=None)

    seconds_until_auto_pause: int | core.IntOut | None = core.attr(int, default=None)

    timeout_action: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auto_pause: bool | core.BoolOut | None = None,
        max_capacity: int | core.IntOut | None = None,
        min_capacity: int | core.IntOut | None = None,
        seconds_until_auto_pause: int | core.IntOut | None = None,
        timeout_action: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ScalingConfiguration.Args(
                auto_pause=auto_pause,
                max_capacity=max_capacity,
                min_capacity=min_capacity,
                seconds_until_auto_pause=seconds_until_auto_pause,
                timeout_action=timeout_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_pause: bool | core.BoolOut | None = core.arg(default=None)

        max_capacity: int | core.IntOut | None = core.arg(default=None)

        min_capacity: int | core.IntOut | None = core.arg(default=None)

        seconds_until_auto_pause: int | core.IntOut | None = core.arg(default=None)

        timeout_action: str | core.StringOut | None = core.arg(default=None)


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

    restore_to_time: str | core.StringOut | None = core.attr(str, default=None)

    restore_type: str | core.StringOut | None = core.attr(str, default=None)

    source_cluster_identifier: str | core.StringOut = core.attr(str)

    use_latest_restorable_time: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        source_cluster_identifier: str | core.StringOut,
        restore_to_time: str | core.StringOut | None = None,
        restore_type: str | core.StringOut | None = None,
        use_latest_restorable_time: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=RestoreToPointInTime.Args(
                source_cluster_identifier=source_cluster_identifier,
                restore_to_time=restore_to_time,
                restore_type=restore_type,
                use_latest_restorable_time=use_latest_restorable_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        restore_to_time: str | core.StringOut | None = core.arg(default=None)

        restore_type: str | core.StringOut | None = core.arg(default=None)

        source_cluster_identifier: str | core.StringOut = core.arg()

        use_latest_restorable_time: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_rds_cluster", namespace="rds")
class Cluster(core.Resource):
    """
    (Optional) The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ
    DB cluster. (This setting is required to create a Multi-AZ DB cluster).
    """

    allocated_storage: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Enable to allow major engine version upgrades when changing engine versions. Defaults to
    false`.
    """
    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether any cluster modifications are applied immediately, or during the next m
    aintenance window. Default is `false`. See [Amazon RDS Documentation for more information.](https://
    docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
    """
    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of cluster
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of EC2 Availability Zones for the DB cluster storage where DB cluster instances can
    be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a
    difference requiring resource recreation next Terraform apply. We recommend specifying 3 AZs or usin
    g [the `lifecycle` configuration block `ignore_changes` argument](https://www.terraform.io/docs/conf
    iguration/meta-arguments/lifecycle.html#ignore_changes) if necessary.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The target backtrack window, in seconds. Only available for `aurora` and `aurora-mysql` e
    ngines currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `
    0` and `259200` (72 hours)
    """
    backtrack_window: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The days to retain backups for. Default `1`
    """
    backup_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Forces new resources) The cluster identifier. If omitted, Terraform will assign a random,
    unique identifier.
    """
    cluster_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique cluster identifier beginning with the specified pre
    fix. Conflicts with `cluster_identifier`.
    """
    cluster_identifier_prefix: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cluster_members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The RDS Cluster Resource ID
    """
    cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    copy_tags_to_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Name for an automatically created database on cluster creation. There are different namin
    g restrictions per database engine: [RDS Naming Constraints][5]
    """
    database_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for examp
    le db.m6g.xlarge. Not all DB instance classes are available in all AWS Regions, or for all database
    engines. For the full list of DB instance classes and availability for your engine, see [DB instance
    class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the
    Amazon RDS User Guide. (This setting is required to create a Multi-AZ DB cluster).
    """
    db_cluster_instance_class: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A cluster parameter group to associate with the cluster.
    """
    db_cluster_parameter_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Instance parameter group to associate with all instances of the DB cluster. The `db_insta
    nce_parameter_group_name` parameter is only valid in combination with the `allow_major_version_upgra
    de` parameter.
    """
    db_instance_parameter_group_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_s
    ubnet_group_name` specified on every [`aws_rds_cluster_instance`](/docs/providers/aws/r/rds_cluster_
    instance.html) in the cluster.
    """
    db_subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) If the DB instance should have deletion protection enabled. The database can't be deleted
    when this value is set to `true`. The default is `false`.
    """
    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether cluster should forward writes to an associated global cluster. Applied to seconda
    ry clusters to enable them to forward writes to an [`aws_rds_global_cluster`](/docs/providers/aws/r/
    rds_global_cluster.html)'s primary cluster. See the [Aurora Userguide documentation](https://docs.aw
    s.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding.html) for more
    information.
    """
    enable_global_write_forwarding: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.
    """
    enable_http_endpoint: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Set of log types to export to cloudwatch. If omitted, no logs will be exported. The follo
    wing log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).
    """
    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The DNS address of the RDS instance
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Val
    id Values: `aurora`, `aurora-mysql`, `aurora-postgresql`, `mysql`, `postgres`. (Note that `mysql` an
    d `postgres` are Multi-AZ RDS clusters).
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The database engine mode. Valid values: `global` (only valid for Aurora MySQL 1.21 and ea
    rlier), `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See
    the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html)
    for limitations when using `serverless`.
    """
    engine_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The database engine version. Updating this argument results in an outage. See the [Aurora
    MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [
    Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updat
    es.html) documentation for your configured engine to determine this value. For example with Aurora M
    ySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`. The value can contain a pa
    rtial version where supported by the API. The actual engine version used is returned in the attribut
    e `engine_version_actual`, , see [Attributes Reference](#attributes-reference) below.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The running version of the database.
    """
    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of your final DB snapshot when this DB cluster is deleted. If omitted, no final
    snapshot will be made.
    """
    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The global cluster identifier specified on [`aws_rds_global_cluster`](/docs/providers/aws
    /r/rds_global_cluster.html).
    """
    global_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Route53 Hosted Zone ID of the endpoint
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether or not mappings of AWS Identity and Access Management (IAM) accounts to
    database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/
    latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.
    """
    iam_database_authentication_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A List of ARNs for the IAM roles to associate to the RDS Cluster.
    """
    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The RDS Cluster Identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The amount of Provisioned IOPS (input/output operations per second) to be initially alloc
    ated for each DB instance in the Multi-AZ DB cluster. For information about valid Iops values, see [
    Amazon RDS Provisioned IOPS storage to improve performance](https://docs.aws.amazon.com/AmazonRDS/la
    test/UserGuide/CHAP_Storage.html#USER_PIOPS) in the Amazon RDS User Guide. (This setting is required
    to create a Multi-AZ DB cluster). Must be a multiple between .5 and 50 of the storage amount for th
    e DB cluster.
    """
    iops: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` nee
    ds to be set to true.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required unless a `snapshot_identifier` or `replication_source_identifier` is provided or unless a
    global_cluster_identifier` is provided when the cluster is the "secondary" cluster of a global data
    base) Password for the master DB user. Note that this may show up in logs, and it will be stored in
    the state file. Please refer to the [RDS Naming Constraints][5]
    """
    master_password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required unless a `snapshot_identifier` or `replication_source_identifier` is provided or unless a
    global_cluster_identifier` is provided when the cluster is the "secondary" cluster of a global data
    base) Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argumen
    t does not support in-place updates and cannot be changed during a restore from snapshot.
    """
    master_username: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The port on which the DB accepts connections
    """
    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The daily time range during which automated backups are created if automated backups are
    enabled using the BackupRetentionPeriod parameter.Time in UTC. Default: A 30-minute window selected
    at random from an 8-hour block of time per regionE.g., 04:00-09:00
    """
    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The weekly time range during which system maintenance can occur, in (UTC) e.g., wed:04:00
    wed:04:30
    """
    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    A read-only endpoint for the Aurora cluster, automatically
    """
    reader_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read R
    eplica. If DB Cluster is part of a Global Cluster, use the [`lifecycle` configuration block `ignore_
    changes` argument](https://www.terraform.io/docs/configuration/meta-arguments/lifecycle.html#ignore_
    changes) to prevent Terraform from showing differences for this argument instead of configuring this
    value.
    """
    replication_source_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Nested attribute for [point in time restore](https://docs.aws.amazon.com/AmazonRDS/latest
    /AuroraUserGuide/USER_PIT.html). More details below.
    """
    restore_to_point_in_time: RestoreToPointInTime | None = core.attr(
        RestoreToPointInTime, default=None
    )

    s3_import: S3Import | None = core.attr(S3Import, default=None)

    """
    (Optional) Nested attribute with scaling properties. Only valid when `engine_mode` is set to `server
    less`. More details below.
    """
    scaling_configuration: ScalingConfiguration | None = core.attr(
        ScalingConfiguration, default=None
    )

    serverlessv2_scaling_configuration: Serverlessv2ScalingConfiguration | None = core.attr(
        Serverlessv2ScalingConfiguration, default=None
    )

    """
    (Optional) Determines whether a final DB snapshot is created before the DB cluster is deleted. If tr
    ue is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before t
    he DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
    """
    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether or not to create this cluster from a snapshot. You can use either the n
    ame or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
    """
    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The source region for an encrypted replica DB cluster.
    """
    source_region: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `
    engine_mode` and `true` for `serverless` `engine_mode`. When restoring an unencrypted `snapshot_iden
    tifier`, the `kms_key_id` argument must be provided to encrypt the restored cluster. Terraform will
    only perform drift detection if a configuration value is provided.
    """
    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Specifies the storage type to be associated with the DB cluster. (This setting is require
    d to create a Multi-AZ DB cluster). Valid values: `io1`, Default: `io1`.
    """
    storage_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the DB cluster. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-l
    evel.
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
    (Optional) List of VPC security groups to associate with the Cluster
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        allocated_storage: int | core.IntOut | None = None,
        allow_major_version_upgrade: bool | core.BoolOut | None = None,
        apply_immediately: bool | core.BoolOut | None = None,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        backtrack_window: int | core.IntOut | None = None,
        backup_retention_period: int | core.IntOut | None = None,
        cluster_identifier: str | core.StringOut | None = None,
        cluster_identifier_prefix: str | core.StringOut | None = None,
        cluster_members: list[str] | core.ArrayOut[core.StringOut] | None = None,
        copy_tags_to_snapshot: bool | core.BoolOut | None = None,
        database_name: str | core.StringOut | None = None,
        db_cluster_instance_class: str | core.StringOut | None = None,
        db_cluster_parameter_group_name: str | core.StringOut | None = None,
        db_instance_parameter_group_name: str | core.StringOut | None = None,
        db_subnet_group_name: str | core.StringOut | None = None,
        deletion_protection: bool | core.BoolOut | None = None,
        enable_global_write_forwarding: bool | core.BoolOut | None = None,
        enable_http_endpoint: bool | core.BoolOut | None = None,
        enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = None,
        engine: str | core.StringOut | None = None,
        engine_mode: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        global_cluster_identifier: str | core.StringOut | None = None,
        iam_database_authentication_enabled: bool | core.BoolOut | None = None,
        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        master_password: str | core.StringOut | None = None,
        master_username: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_backup_window: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        replication_source_identifier: str | core.StringOut | None = None,
        restore_to_point_in_time: RestoreToPointInTime | None = None,
        s3_import: S3Import | None = None,
        scaling_configuration: ScalingConfiguration | None = None,
        serverlessv2_scaling_configuration: Serverlessv2ScalingConfiguration | None = None,
        skip_final_snapshot: bool | core.BoolOut | None = None,
        snapshot_identifier: str | core.StringOut | None = None,
        source_region: str | core.StringOut | None = None,
        storage_encrypted: bool | core.BoolOut | None = None,
        storage_type: str | core.StringOut | None = None,
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
                allocated_storage=allocated_storage,
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                availability_zones=availability_zones,
                backtrack_window=backtrack_window,
                backup_retention_period=backup_retention_period,
                cluster_identifier=cluster_identifier,
                cluster_identifier_prefix=cluster_identifier_prefix,
                cluster_members=cluster_members,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                database_name=database_name,
                db_cluster_instance_class=db_cluster_instance_class,
                db_cluster_parameter_group_name=db_cluster_parameter_group_name,
                db_instance_parameter_group_name=db_instance_parameter_group_name,
                db_subnet_group_name=db_subnet_group_name,
                deletion_protection=deletion_protection,
                enable_global_write_forwarding=enable_global_write_forwarding,
                enable_http_endpoint=enable_http_endpoint,
                enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                engine=engine,
                engine_mode=engine_mode,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                global_cluster_identifier=global_cluster_identifier,
                iam_database_authentication_enabled=iam_database_authentication_enabled,
                iam_roles=iam_roles,
                iops=iops,
                kms_key_id=kms_key_id,
                master_password=master_password,
                master_username=master_username,
                port=port,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                replication_source_identifier=replication_source_identifier,
                restore_to_point_in_time=restore_to_point_in_time,
                s3_import=s3_import,
                scaling_configuration=scaling_configuration,
                serverlessv2_scaling_configuration=serverlessv2_scaling_configuration,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_identifier=snapshot_identifier,
                source_region=source_region,
                storage_encrypted=storage_encrypted,
                storage_type=storage_type,
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
        allocated_storage: int | core.IntOut | None = core.arg(default=None)

        allow_major_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        backtrack_window: int | core.IntOut | None = core.arg(default=None)

        backup_retention_period: int | core.IntOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        cluster_identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        cluster_members: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        copy_tags_to_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        database_name: str | core.StringOut | None = core.arg(default=None)

        db_cluster_instance_class: str | core.StringOut | None = core.arg(default=None)

        db_cluster_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        db_instance_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        db_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        deletion_protection: bool | core.BoolOut | None = core.arg(default=None)

        enable_global_write_forwarding: bool | core.BoolOut | None = core.arg(default=None)

        enable_http_endpoint: bool | core.BoolOut | None = core.arg(default=None)

        enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_mode: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        global_cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        iam_database_authentication_enabled: bool | core.BoolOut | None = core.arg(default=None)

        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        master_password: str | core.StringOut | None = core.arg(default=None)

        master_username: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_backup_window: str | core.StringOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        replication_source_identifier: str | core.StringOut | None = core.arg(default=None)

        restore_to_point_in_time: RestoreToPointInTime | None = core.arg(default=None)

        s3_import: S3Import | None = core.arg(default=None)

        scaling_configuration: ScalingConfiguration | None = core.arg(default=None)

        serverlessv2_scaling_configuration: Serverlessv2ScalingConfiguration | None = core.arg(
            default=None
        )

        skip_final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        source_region: str | core.StringOut | None = core.arg(default=None)

        storage_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        storage_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
