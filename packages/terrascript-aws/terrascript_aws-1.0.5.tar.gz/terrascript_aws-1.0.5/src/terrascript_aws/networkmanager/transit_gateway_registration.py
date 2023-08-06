import terrascript.core as core


@core.resource(type="aws_networkmanager_transit_gateway_registration", namespace="networkmanager")
class TransitGatewayRegistration(core.Resource):
    """
    (Required) The ID of the Global Network to register to.
    """

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of the Transit Gateway to register.
    """
    transit_gateway_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        global_network_id: str | core.StringOut,
        transit_gateway_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayRegistration.Args(
                global_network_id=global_network_id,
                transit_gateway_arn=transit_gateway_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        global_network_id: str | core.StringOut = core.arg()

        transit_gateway_arn: str | core.StringOut = core.arg()
