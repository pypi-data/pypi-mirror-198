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


@core.data(type="aws_ec2_transit_gateway_route_table", namespace="transit_gateway")
class DsEc2TransitGatewayRouteTable(core.Data):
    """
    EC2 Transit Gateway Route Table Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Boolean whether this is the default association route table for the EC2 Transit Gateway
    """
    default_association_route_table: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Boolean whether this is the default propagation route table for the EC2 Transit Gateway
    """
    default_propagation_route_table: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) Identifier of the EC2 Transit Gateway Route Table.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Key-value tags for the EC2 Transit Gateway Route Table
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    EC2 Transit Gateway identifier
    """
    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGatewayRouteTable.Args(
                filter=filter,
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
