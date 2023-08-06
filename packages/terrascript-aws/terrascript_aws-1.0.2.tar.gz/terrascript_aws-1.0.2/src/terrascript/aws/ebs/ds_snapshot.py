import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ebs_snapshot", namespace="aws_ebs")
class DsSnapshot(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    data_encryption_key_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    owner_alias: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    owners: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    state: str | core.StringOut = core.attr(str, computed=True)

    storage_tier: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        most_recent: bool | core.BoolOut | None = None,
        owners: list[str] | core.ArrayOut[core.StringOut] | None = None,
        restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSnapshot.Args(
                filter=filter,
                most_recent=most_recent,
                owners=owners,
                restorable_by_user_ids=restorable_by_user_ids,
                snapshot_ids=snapshot_ids,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        owners: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
