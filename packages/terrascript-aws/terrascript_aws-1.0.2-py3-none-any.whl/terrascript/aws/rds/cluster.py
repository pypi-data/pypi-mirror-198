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


@core.resource(type="aws_rds_cluster", namespace="aws_rds")
class Cluster(core.Resource):

    allocated_storage: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    backtrack_window: int | core.IntOut | None = core.attr(int, default=None)

    backup_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    cluster_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cluster_identifier_prefix: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cluster_members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    copy_tags_to_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    database_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    db_cluster_instance_class: str | core.StringOut | None = core.attr(str, default=None)

    db_cluster_parameter_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    db_instance_parameter_group_name: str | core.StringOut | None = core.attr(str, default=None)

    db_subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_global_write_forwarding: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_http_endpoint: bool | core.BoolOut | None = core.attr(bool, default=None)

    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut | None = core.attr(str, default=None)

    engine_mode: str | core.StringOut | None = core.attr(str, default=None)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    global_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    iam_database_authentication_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    master_password: str | core.StringOut | None = core.attr(str, default=None)

    master_username: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    reader_endpoint: str | core.StringOut = core.attr(str, computed=True)

    replication_source_identifier: str | core.StringOut | None = core.attr(str, default=None)

    restore_to_point_in_time: RestoreToPointInTime | None = core.attr(
        RestoreToPointInTime, default=None
    )

    s3_import: S3Import | None = core.attr(S3Import, default=None)

    scaling_configuration: ScalingConfiguration | None = core.attr(
        ScalingConfiguration, default=None
    )

    serverlessv2_scaling_configuration: Serverlessv2ScalingConfiguration | None = core.attr(
        Serverlessv2ScalingConfiguration, default=None
    )

    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    source_region: str | core.StringOut | None = core.attr(str, default=None)

    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    storage_type: str | core.StringOut | None = core.attr(str, default=None)

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
