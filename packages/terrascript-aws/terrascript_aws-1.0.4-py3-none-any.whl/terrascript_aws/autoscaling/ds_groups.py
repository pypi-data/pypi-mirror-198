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


@core.data(type="aws_autoscaling_groups", namespace="autoscaling")
class DsGroups(core.Data):
    """
    A list of the Autoscaling Groups Arns in the current region.
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A filter used to scope the list e.g., by tags. See [related docs](http://docs.aws.amazon.
    com/AutoScaling/latest/APIReference/API_Filter.html).
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    AWS Region.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of autoscaling group names
    """
    names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        names: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsGroups.Args(
                filter=filter,
                names=names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
