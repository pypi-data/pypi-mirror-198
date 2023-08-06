import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_route", namespace="aws_transit_gateway")
class Ec2TransitGatewayRoute(core.Resource):

    blackhole: bool | core.BoolOut | None = core.attr(bool, default=None)

    destination_cidr_block: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    transit_gateway_attachment_id: str | core.StringOut | None = core.attr(str, default=None)

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
