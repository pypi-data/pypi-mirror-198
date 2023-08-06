import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_route", namespace="transit_gateway")
class Ec2TransitGatewayRoute(core.Resource):
    """
    (Optional) Indicates whether to drop traffic that matches this route (default to `false`).
    """

    blackhole: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) IPv4 or IPv6 RFC1924 CIDR used for destination matches. Routing decisions are based on th
    e most specific match.
    """
    destination_cidr_block: str | core.StringOut = core.attr(str)

    """
    EC2 Transit Gateway Route Table identifier combined with destination
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Identifier of EC2 Transit Gateway Attachment (required if `blackhole` is set to false).
    """
    transit_gateway_attachment_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Identifier of EC2 Transit Gateway Route Table.
    """
    transit_gateway_route_table_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_cidr_block: str | core.StringOut,
        transit_gateway_route_table_id: str | core.StringOut,
        blackhole: bool | core.BoolOut | None = None,
        transit_gateway_attachment_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayRoute.Args(
                destination_cidr_block=destination_cidr_block,
                transit_gateway_route_table_id=transit_gateway_route_table_id,
                blackhole=blackhole,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        blackhole: bool | core.BoolOut | None = core.arg(default=None)

        destination_cidr_block: str | core.StringOut = core.arg()

        transit_gateway_attachment_id: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_route_table_id: str | core.StringOut = core.arg()
