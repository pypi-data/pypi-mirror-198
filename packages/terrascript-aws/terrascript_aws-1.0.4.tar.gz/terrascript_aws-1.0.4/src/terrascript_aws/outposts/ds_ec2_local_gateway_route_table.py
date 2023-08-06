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


@core.data(type="aws_ec2_local_gateway_route_table", namespace="outposts")
class DsEc2LocalGatewayRouteTable(core.Data):

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The id of the specific local gateway route table to retrieve.
    """
    local_gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Local Gateway Route Table Id assigned to desired local gateway route table
    """
    local_gateway_route_table_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The arn of the Outpost the local gateway route table is associated with.
    """
    outpost_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The state of the local gateway route table.
    """
    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
        local_gateway_id: str | core.StringOut | None = None,
        local_gateway_route_table_id: str | core.StringOut | None = None,
        outpost_arn: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2LocalGatewayRouteTable.Args(
                filter=filter,
                local_gateway_id=local_gateway_id,
                local_gateway_route_table_id=local_gateway_route_table_id,
                outpost_arn=outpost_arn,
                state=state,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        local_gateway_id: str | core.StringOut | None = core.arg(default=None)

        local_gateway_route_table_id: str | core.StringOut | None = core.arg(default=None)

        outpost_arn: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
