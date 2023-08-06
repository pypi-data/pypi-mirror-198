import terrascript.core as core


@core.schema
class SelfManagedActiveDirectory(core.Schema):

    dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    domain_name: str | core.StringOut = core.attr(str)

    file_system_administrators_group: str | core.StringOut | None = core.attr(str, default=None)

    organizational_unit_distinguished_name: str | core.StringOut | None = core.attr(
        str, default=None
    )

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        dns_ips: list[str] | core.ArrayOut[core.StringOut],
        domain_name: str | core.StringOut,
        password: str | core.StringOut,
        username: str | core.StringOut,
        file_system_administrators_group: str | core.StringOut | None = None,
        organizational_unit_distinguished_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SelfManagedActiveDirectory.Args(
                dns_ips=dns_ips,
                domain_name=domain_name,
                password=password,
                username=username,
                file_system_administrators_group=file_system_administrators_group,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        domain_name: str | core.StringOut = core.arg()

        file_system_administrators_group: str | core.StringOut | None = core.arg(default=None)

        organizational_unit_distinguished_name: str | core.StringOut | None = core.arg(default=None)

        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class AuditLogConfiguration(core.Schema):

    audit_log_destination: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    file_access_audit_log_level: str | core.StringOut | None = core.attr(str, default=None)

    file_share_access_audit_log_level: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        audit_log_destination: str | core.StringOut | None = None,
        file_access_audit_log_level: str | core.StringOut | None = None,
        file_share_access_audit_log_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AuditLogConfiguration.Args(
                audit_log_destination=audit_log_destination,
                file_access_audit_log_level=file_access_audit_log_level,
                file_share_access_audit_log_level=file_share_access_audit_log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit_log_destination: str | core.StringOut | None = core.arg(default=None)

        file_access_audit_log_level: str | core.StringOut | None = core.arg(default=None)

        file_share_access_audit_log_level: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_fsx_windows_file_system", namespace="aws_fsx")
class WindowsFileSystem(core.Resource):

    active_directory_id: str | core.StringOut | None = core.attr(str, default=None)

    aliases: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    audit_log_configuration: AuditLogConfiguration | None = core.attr(
        AuditLogConfiguration, default=None, computed=True
    )

    automatic_backup_retention_days: int | core.IntOut | None = core.attr(int, default=None)

    backup_id: str | core.StringOut | None = core.attr(str, default=None)

    copy_tags_to_backups: bool | core.BoolOut | None = core.attr(bool, default=None)

    daily_automatic_backup_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    deployment_type: str | core.StringOut | None = core.attr(str, default=None)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    preferred_file_server_ip: str | core.StringOut = core.attr(str, computed=True)

    preferred_subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    remote_administration_endpoint: str | core.StringOut = core.attr(str, computed=True)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_managed_active_directory: SelfManagedActiveDirectory | None = core.attr(
        SelfManagedActiveDirectory, default=None
    )

    skip_final_backup: bool | core.BoolOut | None = core.attr(bool, default=None)

    storage_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    storage_type: str | core.StringOut | None = core.attr(str, default=None)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput_capacity: int | core.IntOut = core.attr(int)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    weekly_maintenance_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        throughput_capacity: int | core.IntOut,
        active_directory_id: str | core.StringOut | None = None,
        aliases: list[str] | core.ArrayOut[core.StringOut] | None = None,
        audit_log_configuration: AuditLogConfiguration | None = None,
        automatic_backup_retention_days: int | core.IntOut | None = None,
        backup_id: str | core.StringOut | None = None,
        copy_tags_to_backups: bool | core.BoolOut | None = None,
        daily_automatic_backup_start_time: str | core.StringOut | None = None,
        deployment_type: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        preferred_subnet_id: str | core.StringOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        self_managed_active_directory: SelfManagedActiveDirectory | None = None,
        skip_final_backup: bool | core.BoolOut | None = None,
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
            args=WindowsFileSystem.Args(
                subnet_ids=subnet_ids,
                throughput_capacity=throughput_capacity,
                active_directory_id=active_directory_id,
                aliases=aliases,
                audit_log_configuration=audit_log_configuration,
                automatic_backup_retention_days=automatic_backup_retention_days,
                backup_id=backup_id,
                copy_tags_to_backups=copy_tags_to_backups,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                deployment_type=deployment_type,
                kms_key_id=kms_key_id,
                preferred_subnet_id=preferred_subnet_id,
                security_group_ids=security_group_ids,
                self_managed_active_directory=self_managed_active_directory,
                skip_final_backup=skip_final_backup,
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
        active_directory_id: str | core.StringOut | None = core.arg(default=None)

        aliases: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        audit_log_configuration: AuditLogConfiguration | None = core.arg(default=None)

        automatic_backup_retention_days: int | core.IntOut | None = core.arg(default=None)

        backup_id: str | core.StringOut | None = core.arg(default=None)

        copy_tags_to_backups: bool | core.BoolOut | None = core.arg(default=None)

        daily_automatic_backup_start_time: str | core.StringOut | None = core.arg(default=None)

        deployment_type: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        preferred_subnet_id: str | core.StringOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        self_managed_active_directory: SelfManagedActiveDirectory | None = core.arg(default=None)

        skip_final_backup: bool | core.BoolOut | None = core.arg(default=None)

        storage_capacity: int | core.IntOut | None = core.arg(default=None)

        storage_type: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput_capacity: int | core.IntOut = core.arg()

        weekly_maintenance_start_time: str | core.StringOut | None = core.arg(default=None)
