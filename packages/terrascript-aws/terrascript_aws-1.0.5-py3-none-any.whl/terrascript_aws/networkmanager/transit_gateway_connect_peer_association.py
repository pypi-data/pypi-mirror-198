import terrascript.core as core


@core.resource(
    type="aws_networkmanager_transit_gateway_connect_peer_association", namespace="networkmanager"
)
class TransitGatewayConnectPeerAssociation(core.Resource):
    """
    (Required) The ID of the device.
    """

    device_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the global network.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the link.
    """
    link_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The Amazon Resource Name (ARN) of the Connect peer.
    """
    transit_gateway_connect_peer_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        device_id: str | core.StringOut,
        global_network_id: str | core.StringOut,
        transit_gateway_connect_peer_arn: str | core.StringOut,
        link_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayConnectPeerAssociation.Args(
                device_id=device_id,
                global_network_id=global_network_id,
                transit_gateway_connect_peer_arn=transit_gateway_connect_peer_arn,
                link_id=link_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device_id: str | core.StringOut = core.arg()

        global_network_id: str | core.StringOut = core.arg()

        link_id: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_connect_peer_arn: str | core.StringOut = core.arg()
