import terrascript.core as core


@core.resource(
    type="aws_ec2_transit_gateway_route_table_propagation", namespace="aws_transit_gateway"
)
class Ec2TransitGatewayRouteTablePropagation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    resource_id: str | core.StringOut = core.attr(str, computed=True)

    resource_type: str | core.StringOut = core.attr(str, computed=True)

    transit_gateway_attachment_id: str | core.StringOut = core.attr(str)

    transit_gateway_route_table_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_attachment_id: str | core.StringOut,
        transit_gateway_route_table_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayRouteTablePropagation.Args(
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                transit_gateway_route_table_id=transit_gateway_route_table_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        transit_gateway_attachment_id: str | core.StringOut = core.arg()

        transit_gateway_route_table_id: str | core.StringOut = core.arg()
