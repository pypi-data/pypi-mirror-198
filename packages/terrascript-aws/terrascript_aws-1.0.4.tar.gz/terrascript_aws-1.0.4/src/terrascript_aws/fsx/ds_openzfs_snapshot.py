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


@core.data(type="aws_fsx_openzfs_snapshot", namespace="fsx")
class DsOpenzfsSnapshot(core.Data):
    """
    Amazon Resource Name of the snapshot.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The time that the resource was created.
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more name/value pairs to filter off of. The
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    Identifier of the snapshot, e.g., `fsvolsnap-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If more than one result is returned, use the most recent snapshot.
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The name of the snapshot.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the snapshot.
    """
    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific snapshot_id.
    """
    snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    A list of Tag values, with a maximum of 50 elements.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The ID of the volume that the snapshot is of.
    """
    volume_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        most_recent: bool | core.BoolOut | None = None,
        name: str | core.StringOut | None = None,
        snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOpenzfsSnapshot.Args(
                filter=filter,
                most_recent=most_recent,
                name=name,
                snapshot_ids=snapshot_ids,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
