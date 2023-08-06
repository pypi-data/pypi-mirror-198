import terrascript.core as core


@core.resource(type="aws_vpn_gateway_route_propagation", namespace="vpn")
class GatewayRoutePropagation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The id of the `aws_route_table` to propagate routes into.
    """
    route_table_id: str | core.StringOut = core.attr(str)

    """
    The id of the `aws_vpn_gateway` to propagate routes from.
    """
    vpn_gateway_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: str | core.StringOut,
        vpn_gateway_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GatewayRoutePropagation.Args(
                route_table_id=route_table_id,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        route_table_id: str | core.StringOut = core.arg()

        vpn_gateway_id: str | core.StringOut = core.arg()
