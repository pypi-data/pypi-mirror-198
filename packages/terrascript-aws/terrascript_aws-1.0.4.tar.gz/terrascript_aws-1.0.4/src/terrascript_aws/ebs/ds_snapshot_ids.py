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


@core.data(type="aws_ebs_snapshot_ids", namespace="ebs")
class DsSnapshotIds(core.Data):
    """
    (Optional) One or more name/value pairs to filter off of. There are
    """

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    AWS Region.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of EBS snapshot IDs, sorted by creation time in descending order.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Returns the snapshots owned by the specified owner id. Multiple owners can be specified.
    """
    owners: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) One or more AWS accounts IDs that can create volumes from the snapshot.
    """
    restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        owners: list[str] | core.ArrayOut[core.StringOut] | None = None,
        restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSnapshotIds.Args(
                filter=filter,
                owners=owners,
                restorable_by_user_ids=restorable_by_user_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        owners: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
