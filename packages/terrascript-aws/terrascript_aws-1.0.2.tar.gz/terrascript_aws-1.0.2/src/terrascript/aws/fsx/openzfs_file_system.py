import terrascript.core as core


@core.schema
class ClientConfigurations(core.Schema):

    clients: str | core.StringOut = core.attr(str)

    options: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        clients: str | core.StringOut,
        options: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=ClientConfigurations.Args(
                clients=clients,
                options=options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        clients: str | core.StringOut = core.arg()

        options: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class NfsExports(core.Schema):

    client_configurations: list[ClientConfigurations] | core.ArrayOut[
        ClientConfigurations
    ] = core.attr(ClientConfigurations, kind=core.Kind.array)

    def __init__(
        self,
        *,
        client_configurations: list[ClientConfigurations] | core.ArrayOut[ClientConfigurations],
    ):
        super().__init__(
            args=NfsExports.Args(
                client_configurations=client_configurations,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_configurations: list[ClientConfigurations] | core.ArrayOut[
            ClientConfigurations
        ] = core.arg()


@core.schema
class UserAndGroupQuotas(core.Schema):

    id: int | core.IntOut = core.attr(int)

    storage_capacity_quota_gib: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        id: int | core.IntOut,
        storage_capacity_quota_gib: int | core.IntOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=UserAndGroupQuotas.Args(
                id=id,
                storage_capacity_quota_gib=storage_capacity_quota_gib,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: int | core.IntOut = core.arg()

        storage_capacity_quota_gib: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class RootVolumeConfiguration(core.Schema):

    copy_tags_to_snapshots: bool | core.BoolOut | None = core.attr(bool, default=None)

    data_compression_type: str | core.StringOut | None = core.attr(str, default=None)

    nfs_exports: NfsExports | None = core.attr(NfsExports, default=None)

    read_only: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    record_size_kib: int | core.IntOut | None = core.attr(int, default=None)

    user_and_group_quotas: list[UserAndGroupQuotas] | core.ArrayOut[
        UserAndGroupQuotas
    ] | None = core.attr(UserAndGroupQuotas, default=None, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        copy_tags_to_snapshots: bool | core.BoolOut | None = None,
        data_compression_type: str | core.StringOut | None = None,
        nfs_exports: NfsExports | None = None,
        read_only: bool | core.BoolOut | None = None,
        record_size_kib: int | core.IntOut | None = None,
        user_and_group_quotas: list[UserAndGroupQuotas]
        | core.ArrayOut[UserAndGroupQuotas]
        | None = None,
    ):
        super().__init__(
            args=RootVolumeConfiguration.Args(
                copy_tags_to_snapshots=copy_tags_to_snapshots,
                data_compression_type=data_compression_type,
                nfs_exports=nfs_exports,
                read_only=read_only,
                record_size_kib=record_size_kib,
                user_and_group_quotas=user_and_group_quotas,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_tags_to_snapshots: bool | core.BoolOut | None = core.arg(default=None)

        data_compression_type: str | core.StringOut | None = core.arg(default=None)

        nfs_exports: NfsExports | None = core.arg(default=None)

        read_only: bool | core.BoolOut | None = core.arg(default=None)

        record_size_kib: int | core.IntOut | None = core.arg(default=None)

        user_and_group_quotas: list[UserAndGroupQuotas] | core.ArrayOut[
            UserAndGroupQuotas
        ] | None = core.arg(default=None)


@core.schema
class DiskIopsConfiguration(core.Schema):

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        iops: int | core.IntOut | None = None,
        mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DiskIopsConfiguration.Args(
                iops=iops,
                mode=mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: int | core.IntOut | None = core.arg(default=None)

        mode: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_fsx_openzfs_file_system", namespace="aws_fsx")
class OpenzfsFileSystem(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    automatic_backup_retention_days: int | core.IntOut | None = core.attr(int, default=None)

    backup_id: str | core.StringOut | None = core.attr(str, default=None)

    copy_tags_to_backups: bool | core.BoolOut | None = core.attr(bool, default=None)

    copy_tags_to_volumes: bool | core.BoolOut | None = core.attr(bool, default=None)

    daily_automatic_backup_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    deployment_type: str | core.StringOut = core.attr(str)

    disk_iops_configuration: DiskIopsConfiguration | None = core.attr(
        DiskIopsConfiguration, default=None, computed=True
    )

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    root_volume_configuration: RootVolumeConfiguration | None = core.attr(
        RootVolumeConfiguration, default=None, computed=True
    )

    root_volume_id: str | core.StringOut = core.attr(str, computed=True)

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

    throughput_capacity: int | core.IntOut = core.attr(int)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    weekly_maintenance_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_type: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        throughput_capacity: int | core.IntOut,
        automatic_backup_retention_days: int | core.IntOut | None = None,
        backup_id: str | core.StringOut | None = None,
        copy_tags_to_backups: bool | core.BoolOut | None = None,
        copy_tags_to_volumes: bool | core.BoolOut | None = None,
        daily_automatic_backup_start_time: str | core.StringOut | None = None,
        disk_iops_configuration: DiskIopsConfiguration | None = None,
        kms_key_id: str | core.StringOut | None = None,
        root_volume_configuration: RootVolumeConfiguration | None = None,
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
            args=OpenzfsFileSystem.Args(
                deployment_type=deployment_type,
                subnet_ids=subnet_ids,
                throughput_capacity=throughput_capacity,
                automatic_backup_retention_days=automatic_backup_retention_days,
                backup_id=backup_id,
                copy_tags_to_backups=copy_tags_to_backups,
                copy_tags_to_volumes=copy_tags_to_volumes,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                disk_iops_configuration=disk_iops_configuration,
                kms_key_id=kms_key_id,
                root_volume_configuration=root_volume_configuration,
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
        automatic_backup_retention_days: int | core.IntOut | None = core.arg(default=None)

        backup_id: str | core.StringOut | None = core.arg(default=None)

        copy_tags_to_backups: bool | core.BoolOut | None = core.arg(default=None)

        copy_tags_to_volumes: bool | core.BoolOut | None = core.arg(default=None)

        daily_automatic_backup_start_time: str | core.StringOut | None = core.arg(default=None)

        deployment_type: str | core.StringOut = core.arg()

        disk_iops_configuration: DiskIopsConfiguration | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        root_volume_configuration: RootVolumeConfiguration | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        storage_capacity: int | core.IntOut | None = core.arg(default=None)

        storage_type: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput_capacity: int | core.IntOut = core.arg()

        weekly_maintenance_start_time: str | core.StringOut | None = core.arg(default=None)
