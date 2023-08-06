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


@core.resource(type="aws_fsx_lustre_file_system", namespace="fsx")
class LustreFileSystem(core.Resource):
    """
    Amazon Resource Name of the file system.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) How Amazon FSx keeps your file and directory listings up to date as you add or modify obj
    ects in your linked S3 bucket. see [Auto Import Data Repo](https://docs.aws.amazon.com/fsx/latest/Lu
    streGuide/autoimport-data-repo.html) for more details. Only supported on `PERSISTENT_1` deployment t
    ypes.
    """
    auto_import_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The number of days to retain automatic backups. Setting this to 0 disables automatic back
    ups. You can retain automatic backups for a maximum of 90 days. only valid for `PERSISTENT_1` and `P
    ERSISTENT_2` deployment_type.
    """
    automatic_backup_retention_days: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) The ID of the source backup to create the filesystem from.
    """
    backup_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A boolean flag indicating whether tags for the file system should be copied to backups. A
    pplicable for `PERSISTENT_1` and `PERSISTENT_2` deployment_type. The default value is false.
    """
    copy_tags_to_backups: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A recurring daily time, in the format HH:MM. HH is the zero-padded hour of the day (0-23)
    , and MM is the zero-padded minute of the hour. For example, 05:00 specifies 5 AM daily. only valid
    for `PERSISTENT_1` and `PERSISTENT_2` deployment_type. Requires `automatic_backup_retention_days` to
    be set.
    """
    daily_automatic_backup_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Sets the data compression configuration for the file system. Valid values are `LZ4` and `
    NONE`. Default value is `NONE`. Unsetting this value reverts the compression type back to `NONE`.
    """
    data_compression_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) - The filesystem deployment type. One of: `SCRATCH_1`, `SCRATCH_2`, `PERSISTENT_1`, `PERS
    ISTENT_2`.
    """
    deployment_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    DNS name for the file system, e.g., `fs-12345678.fsx.us-west-2.amazonaws.com`
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) - The type of drive cache used by `PERSISTENT_1` filesystems that are provisioned with `H
    DD` storage_type. Required for `HDD` storage_type, set to either `READ` or `NONE`.
    """
    drive_cache_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 URI (with optional prefix) where the root of your Amazon FSx file system is exported.
    Can only be specified with `import_path` argument and the path must use the same Amazon S3 bucket as
    specified in `import_path`. Set equal to `import_path` to overwrite files on export. Defaults to `s
    3://{IMPORT BUCKET}/FSxLustre{CREATION TIMESTAMP}`. Only supported on `PERSISTENT_1` deployment type
    s.
    """
    export_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Sets the Lustre version for the file system that you're creating. Valid values are 2.10 f
    or `SCRATCH_1`, `SCRATCH_2` and `PERSISTENT_1` deployment types. Valid values for 2.12 include all d
    eployment types.
    """
    file_system_type_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    Identifier of the file system, e.g., `fs-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) S3 URI (with optional prefix) that you're using as the data repository for your FSx for L
    ustre file system. For example, `s3://example-bucket/optional-prefix/`. Only supported on `PERSISTEN
    T_1` deployment types.
    """
    import_path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) For files imported from a data repository, this value determines the stripe count and max
    imum amount of data per file (in MiB) stored on a single physical disk. Can only be specified with `
    import_path` argument. Defaults to `1024`. Minimum of `1` and maximum of `512000`. Only supported on
    PERSISTENT_1` deployment types.
    """
    imported_file_chunk_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) ARN for the KMS Key to encrypt the file system at rest, applicable for `PERSISTENT_1` and
    PERSISTENT_2` deployment_type. Defaults to an AWS managed KMS Key.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The Lustre logging configuration used when creating an Amazon FSx for Lustre file system.
    When logging is enabled, Lustre logs error and warning events for data repositories associated with
    your file system to Amazon CloudWatch Logs.
    """
    log_configuration: LogConfiguration | None = core.attr(
        LogConfiguration, default=None, computed=True
    )

    """
    The value to be used when mounting the filesystem.
    """
    mount_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of Elastic Network Interface identifiers from which the file system is accessible. As explained
    in the [documentation](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-on-premises.html)
    , the first network interface returned is the primary network interface.
    """
    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    AWS account identifier that created the file system.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) - Describes the amount of read and write throughput for each 1 tebibyte of storage, in MB
    /s/TiB, required for the `PERSISTENT_1` and `PERSISTENT_2` deployment_type. Valid values for `PERSIS
    TENT_1` deployment_type and `SSD` storage_type are 50, 100, 200. Valid values for `PERSISTENT_1` dep
    loyment_type and `HDD` storage_type are 12, 40. Valid values for `PERSISTENT_2` deployment_type and
    SSD` storage_type are 125, 250, 500, 1000.
    """
    per_unit_storage_throughput: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) A list of IDs for the security groups that apply to the specified network interfaces crea
    ted for file system access. These security groups will apply to all network interfaces.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The storage capacity (GiB) of the file system. Minimum of `1200`. See more details at [Al
    lowed values for Fsx storage capacity](https://docs.aws.amazon.com/fsx/latest/APIReference/API_Creat
    eFileSystem.html#FSx-CreateFileSystem-request-StorageCapacity). Update is allowed only for `SCRATCH_
    2`, `PERSISTENT_1` and `PERSISTENT_2` deployment types, See more details at [Fsx Storage Capacity Up
    date](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateFileSystem.html#FSx-UpdateFileSy
    stem-request-StorageCapacity). Required when not creating filesystem for a backup.
    """
    storage_capacity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) - The filesystem storage type. Either `SSD` or `HDD`, defaults to `SSD`. `HDD` is only su
    pported on `PERSISTENT_1` deployment types.
    """
    storage_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A list of IDs for the subnets that the file system will be accessible from. File systems
    currently support only one subnet. The file server is also launched in that subnet's Availability Zo
    ne.
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
