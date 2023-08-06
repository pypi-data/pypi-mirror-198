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


@core.data(type="aws_prefix_list", namespace="vpc")
class DsPrefixList(core.Data):
    """
    The list of CIDR blocks for the AWS service associated with the prefix list.
    """

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    The ID of the selected prefix list.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the prefix list to select.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The ID of the prefix list to select.
    """
    prefix_list_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        name: str | core.StringOut | None = None,
        prefix_list_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPrefixList.Args(
                filter=filter,
                name=name,
                prefix_list_id=prefix_list_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        prefix_list_id: str | core.StringOut | None = core.arg(default=None)
