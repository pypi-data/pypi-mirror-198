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


@core.data(type="aws_ec2_coip_pool", namespace="outposts")
class DsEc2CoipPool(core.Data):
    """
    ARN of the COIP pool
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Local Gateway Route Table Id assigned to desired COIP Pool
    """
    local_gateway_route_table_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    Set of CIDR blocks in pool
    """
    pool_cidrs: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The id of the specific COIP Pool to retrieve.
    """
    pool_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A mapping of tags, each pair of which must exactly match
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        local_gateway_route_table_id: str | core.StringOut | None = None,
        pool_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2CoipPool.Args(
                filter=filter,
                local_gateway_route_table_id=local_gateway_route_table_id,
                pool_id=pool_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        local_gateway_route_table_id: str | core.StringOut | None = core.arg(default=None)

        pool_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
