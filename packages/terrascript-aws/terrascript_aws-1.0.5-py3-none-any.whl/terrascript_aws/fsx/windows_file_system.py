import terrascript.core as core


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


@core.resource(type="aws_fsx_windows_file_system", namespace="fsx")
class WindowsFileSystem(core.Resource):
    """
    (Optional) The ID for an existing Microsoft Active Directory instance that the file system should jo
    in when it's created. Cannot be specified with `self_managed_active_directory`.
    """

    active_directory_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) An array DNS alias names that you want to associate with the Amazon FSx file system.  For
    more information, see [Working with DNS Aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuid
    e/managing-dns-aliases.html)
    """
    aliases: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Amazon Resource Name of the file system.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The configuration that Amazon FSx for Windows File Server uses to audit and log user acce
    sses of files, folders, and file shares on the Amazon FSx for Windows File Server file system. See b
    elow.
    """
    audit_log_configuration: AuditLogConfiguration | None = core.attr(
        AuditLogConfiguration, default=None, computed=True
    )

    """
    (Optional) The number of days to retain automatic backups. Minimum of `0` and maximum of `90`. Defau
    lts to `7`. Set to `0` to disable.
    """
    automatic_backup_retention_days: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The ID of the source backup to create the filesystem from.
    """
    backup_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A boolean flag indicating whether tags on the file system should be copied to backups. De
    faults to `false`.
    """
    copy_tags_to_backups: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time z
    one.
    """
    daily_automatic_backup_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Specifies the file system deployment type, valid values are `MULTI_AZ_1`, `SINGLE_AZ_1` a
    nd `SINGLE_AZ_2`. Default value is `SINGLE_AZ_1`.
    """
    deployment_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    DNS name for the file system, e.g., `fs-12345678.corp.example.com` (domain name matching the Active
    Directory domain name)
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the file system, e.g., `fs-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Ke
    y.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Set of Elastic Network Interface identifiers from which the file system is accessible.
    """
    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    AWS account identifier that created the file system.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IP address of the primary, or preferred, file server.
    """
    preferred_file_server_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the subnet in which you want the preferred file server to be located. Required
    for when deployment type is `MULTI_AZ_1`.
    """
    preferred_subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the fil
    e system using Amazon FSx Remote PowerShell. For `SINGLE_AZ_1` deployment types, this is the DNS nam
    e of the file system.
    """
    remote_administration_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of IDs for the security groups that apply to the specified network interfaces crea
    ted for file system access. These security groups will apply to all network interfaces.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block that Amazon FSx uses to join the Windows File Server instance to your
    self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified
    with `active_directory_id`. Detailed below.
    """
    self_managed_active_directory: SelfManagedActiveDirectory | None = core.attr(
        SelfManagedActiveDirectory, default=None
    )

    """
    (Optional) When enabled, will skip the default final backup taken when the file system is deleted. T
    his configuration must be applied separately before attempting to delete the resource to have the de
    sired behavior. Defaults to `false`.
    """
    skip_final_backup: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536. If the sto
    rage type is set to `HDD` the minimum value is 2000. Required when not creating filesystem for a bac
    kup.
    """
    storage_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Specifies the storage type, Valid values are `SSD` and `HDD`. `HDD` is supported on `SING
    LE_AZ_2` and `MULTI_AZ_1` Windows file system deployment types. Default value is `SSD`.
    """
    storage_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A list of IDs for the subnets that the file system will be accessible from. To specify mo
    re than a single subnet set `deployment_type` to `MULTI_AZ_1`.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the file system. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level.
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
    (Required) Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of
    8` and maximum of `2048`.
    """
    throughput_capacity: int | core.IntOut = core.attr(int)

    """
    Identifier of the Virtual Private Cloud for the file system.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC
    time zone.
    """
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
