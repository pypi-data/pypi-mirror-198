import terrascript.core as core


@core.schema
class LogConfiguration(core.Schema):

    destination: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    level: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        destination: str | core.StringOut | None = None,
        level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LogConfiguration.Args(
                destination=destination,
                level=level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: str | core.StringOut | None = core.arg(default=None)

        level: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_fsx_lustre_file_system", namespace="aws_fsx")
class LustreFileSystem(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_import_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    automatic_backup_retention_days: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    backup_id: str | core.StringOut | None = core.attr(str, default=None)

    copy_tags_to_backups: bool | core.BoolOut | None = core.attr(bool, default=None)

    daily_automatic_backup_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    data_compression_type: str | core.StringOut | None = core.attr(str, default=None)

    deployment_type: str | core.StringOut | None = core.attr(str, default=None)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    drive_cache_type: str | core.StringOut | None = core.attr(str, default=None)

    export_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    file_system_type_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    import_path: str | core.StringOut | None = core.attr(str, default=None)

    imported_file_chunk_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    log_configuration: LogConfiguration | None = core.attr(
        LogConfiguration, default=None, computed=True
    )

    mount_name: str | core.StringOut = core.attr(str, computed=True)

    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    per_unit_storage_throughput: int | core.IntOut | None = core.attr(int, default=None)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    storage_capacity: int | core.IntOut | None = core.attr(int, default=None)

    storage_type: str | core.StringOut | None = core.attr(str, default=None)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    weekly_maintenance_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        auto_import_policy: str | core.StringOut | None = None,
        automatic_backup_retention_days: int | core.IntOut | None = None,
        backup_id: str | core.StringOut | None = None,
        copy_tags_to_backups: bool | core.BoolOut | None = None,
        daily_automatic_backup_start_time: str | core.StringOut | None = None,
        data_compression_type: str | core.StringOut | None = None,
        deployment_type: str | core.StringOut | None = None,
        drive_cache_type: str | core.StringOut | None = None,
        export_path: str | core.StringOut | None = None,
        file_system_type_version: str | core.StringOut | None = None,
        import_path: str | core.StringOut | None = None,
        imported_file_chunk_size: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        log_configuration: LogConfiguration | None = None,
        per_unit_storage_throughput: int | core.IntOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        storage_capacity: int | core.IntOut | None = None,
        storage_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        weekly_maintenance_start_time: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LustreFileSystem.Args(
                subnet_ids=subnet_ids,
                auto_import_policy=auto_import_policy,
                automatic_backup_retention_days=automatic_backup_retention_days,
                backup_id=backup_id,
                copy_tags_to_backups=copy_tags_to_backups,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                data_compression_type=data_compression_type,
                deployment_type=deployment_type,
                drive_cache_type=drive_cache_type,
                export_path=export_path,
                file_system_type_version=file_system_type_version,
                import_path=import_path,
                imported_file_chunk_size=imported_file_chunk_size,
                kms_key_id=kms_key_id,
                log_configuration=log_configuration,
                per_unit_storage_throughput=per_unit_storage_throughput,
                security_group_ids=security_group_ids,
                storage_capacity=storage_capacity,
                storage_type=storage_type,
                tags=tags,
                tags_all=tags_all,
                weekly_maintenance_start_time=weekly_maintenance_start_time,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_import_policy: str | core.StringOut | None = core.arg(default=None)

        automatic_backup_retention_days: int | core.IntOut | None = core.arg(default=None)

        backup_id: str | core.StringOut | None = core.arg(default=None)

        copy_tags_to_backups: bool | core.BoolOut | None = core.arg(default=None)

        daily_automatic_backup_start_time: str | core.StringOut | None = core.arg(default=None)

        data_compression_type: str | core.StringOut | None = core.arg(default=None)

        deployment_type: str | core.StringOut | None = core.arg(default=None)

        drive_cache_type: str | core.StringOut | None = core.arg(default=None)

        export_path: str | core.StringOut | None = core.arg(default=None)

        file_system_type_version: str | core.StringOut | None = core.arg(default=None)

        import_path: str | core.StringOut | None = core.arg(default=None)

        imported_file_chunk_size: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        log_configuration: LogConfiguration | None = core.arg(default=None)

        per_unit_storage_throughput: int | core.IntOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        storage_capacity: int | core.IntOut | None = core.arg(default=None)

        storage_type: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        weekly_maintenance_start_time: str | core.StringOut | None = core.arg(default=None)
