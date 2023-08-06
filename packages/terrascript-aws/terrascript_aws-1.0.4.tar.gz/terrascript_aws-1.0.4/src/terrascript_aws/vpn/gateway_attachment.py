import terrascript.core as core


@core.resource(type="aws_vpn_gateway_attachment", namespace="vpn")
class GatewayAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the VPC.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the Virtual Private Gateway.
    """
    vpn_gateway_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: str | core.StringOut,
        vpn_gateway_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GatewayAttachment.Args(
                vpc_id=vpc_id,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        vpc_id: str | core.StringOut = core.arg()

        vpn_gateway_id: str | core.StringOut = core.arg()
