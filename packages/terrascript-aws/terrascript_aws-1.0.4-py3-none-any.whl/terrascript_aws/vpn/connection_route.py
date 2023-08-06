import terrascript.core as core


@core.resource(type="aws_vpn_connection_route", namespace="vpn")
class ConnectionRoute(core.Resource):
    """
    (Required) The CIDR block associated with the local subnet of the customer network.
    """

    destination_cidr_block: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the VPN connection.
    """
    vpn_connection_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_cidr_block: str | core.StringOut,
        vpn_connection_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConnectionRoute.Args(
                destination_cidr_block=destination_cidr_block,
                vpn_connection_id=vpn_connection_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_cidr_block: str | core.StringOut = core.arg()

        vpn_connection_id: str | core.StringOut = core.arg()
