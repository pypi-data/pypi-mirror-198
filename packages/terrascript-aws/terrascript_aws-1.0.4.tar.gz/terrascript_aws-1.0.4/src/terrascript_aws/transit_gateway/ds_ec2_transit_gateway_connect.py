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


@core.data(type="aws_ec2_transit_gateway_connect", namespace="transit_gateway")
class DsEc2TransitGatewayConnect(core.Data):
    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The tunnel protocol
    """
    protocol: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the EC2 Transit Gateway Connect
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Identifier of the EC2 Transit Gateway Connect.
    """
    transit_gateway_connect_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    EC2 Transit Gateway identifier
    """
    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The underlaying VPC attachment
    """
    transport_attachment_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_connect_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGatewayConnect.Args(
                filter=filter,
                tags=tags,
                transit_gateway_connect_id=transit_gateway_connect_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_connect_id: str | core.StringOut | None = core.arg(default=None)
