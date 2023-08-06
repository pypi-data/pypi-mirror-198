import terrascript.core as core


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
class OriginSnapshot(core.Schema):

    copy_strategy: str | core.StringOut = core.attr(str)

    snapshot_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        copy_strategy: str | core.StringOut,
        snapshot_arn: str | core.StringOut,
    ):
        super().__init__(
            args=OriginSnapshot.Args(
                copy_strategy=copy_strategy,
                snapshot_arn=snapshot_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_strategy: str | core.StringOut = core.arg()

        snapshot_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_fsx_openzfs_volume", namespace="aws_fsx")
class OpenzfsVolume(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    copy_tags_to_snapshots: bool | core.BoolOut | None = core.attr(bool, default=None)

    data_compression_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    nfs_exports: NfsExports | None = core.attr(NfsExports, default=None)

    origin_snapshot: OriginSnapshot | None = core.attr(OriginSnapshot, default=None)

    parent_volume_id: str | core.StringOut = core.attr(str)

    read_only: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    record_size_kib: int | core.IntOut | None = core.attr(int, default=None)

    storage_capacity_quota_gib: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    storage_capacity_reservation_gib: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_and_group_quotas: list[UserAndGroupQuotas] | core.ArrayOut[
        UserAndGroupQuotas
    ] | None = core.attr(UserAndGroupQuotas, default=None, computed=True, kind=core.Kind.array)

    volume_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        parent_volume_id: str | core.StringOut,
        copy_tags_to_snapshots: bool | core.BoolOut | None = None,
        data_compression_type: str | core.StringOut | None = None,
        nfs_exports: NfsExports | None = None,
        origin_snapshot: OriginSnapshot | None = None,
        read_only: bool | core.BoolOut | None = None,
        record_size_kib: int | core.IntOut | None = None,
        storage_capacity_quota_gib: int | core.IntOut | None = None,
        storage_capacity_reservation_gib: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_and_group_quotas: list[UserAndGroupQuotas]
        | core.ArrayOut[UserAndGroupQuotas]
        | None = None,
        volume_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OpenzfsVolume.Args(
                name=name,
                parent_volume_id=parent_volume_id,
                copy_tags_to_snapshots=copy_tags_to_snapshots,
                data_compression_type=data_compression_type,
                nfs_exports=nfs_exports,
                origin_snapshot=origin_snapshot,
                read_only=read_only,
                record_size_kib=record_size_kib,
                storage_capacity_quota_gib=storage_capacity_quota_gib,
                storage_capacity_reservation_gib=storage_capacity_reservation_gib,
                tags=tags,
                tags_all=tags_all,
                user_and_group_quotas=user_and_group_quotas,
                volume_type=volume_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        copy_tags_to_snapshots: bool | core.BoolOut | None = core.arg(default=None)

        data_compression_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        nfs_exports: NfsExports | None = core.arg(default=None)

        origin_snapshot: OriginSnapshot | None = core.arg(default=None)

        parent_volume_id: str | core.StringOut = core.arg()

        read_only: bool | core.BoolOut | None = core.arg(default=None)

        record_size_kib: int | core.IntOut | None = core.arg(default=None)

        storage_capacity_quota_gib: int | core.IntOut | None = core.arg(default=None)

        storage_capacity_reservation_gib: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_and_group_quotas: list[UserAndGroupQuotas] | core.ArrayOut[
            UserAndGroupQuotas
        ] | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)
