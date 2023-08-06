import terrascript.core as core


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


@core.resource(type="aws_db_instance", namespace="aws_rds")
class DbInstance(core.Resource):

    address: str | core.StringOut = core.attr(str, computed=True)

    allocated_storage: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    backup_retention_period: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    backup_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ca_cert_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    character_set_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    copy_tags_to_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    customer_owned_ip_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    db_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    db_subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    delete_automated_backups: bool | core.BoolOut | None = core.attr(bool, default=None)

    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    domain: str | core.StringOut | None = core.attr(str, default=None)

    domain_iam_role_name: str | core.StringOut | None = core.attr(str, default=None)

    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    iam_database_authentication_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    identifier_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    instance_class: str | core.StringOut = core.attr(str)

    iops: int | core.IntOut | None = core.attr(int, default=None)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    latest_restorable_time: str | core.StringOut = core.attr(str, computed=True)

    license_model: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    max_allocated_storage: int | core.IntOut | None = core.attr(int, default=None)

    monitoring_interval: int | core.IntOut | None = core.attr(int, default=None)

    monitoring_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    multi_az: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    nchar_character_set_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    network_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    option_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    password: str | core.StringOut | None = core.attr(str, default=None)

    performance_insights_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    performance_insights_kms_key_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    performance_insights_retention_period: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    replica_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    replicas: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    replicate_source_db: str | core.StringOut | None = core.attr(str, default=None)

    resource_id: str | core.StringOut = core.attr(str, computed=True)

    restore_to_point_in_time: RestoreToPointInTime | None = core.attr(
        RestoreToPointInTime, default=None
    )

    s3_import: S3Import | None = core.attr(S3Import, default=None)

    security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    storage_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timezone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    username: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
