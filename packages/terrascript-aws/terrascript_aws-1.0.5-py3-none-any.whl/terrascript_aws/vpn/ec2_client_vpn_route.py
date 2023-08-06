import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_route", namespace="vpn")
class Ec2ClientVpnRoute(core.Resource):
    """
    (Required) The ID of the Client VPN endpoint.
    """

    client_vpn_endpoint_id: str | core.StringOut = core.attr(str)

    """
    (Optional) A brief description of the authorization rule.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The IPv4 address range, in CIDR notation, of the route destination.
    """
    destination_cidr_block: str | core.StringOut = core.attr(str)

    """
    The ID of the Client VPN endpoint.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates how the Client VPN route was added. Will be `add-route` for routes created by this resourc
    e.
    """
    origin: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Subnet to route the traffic through. It must already be attached to the Cli
    ent VPN.
    """
    target_vpc_subnet_id: str | core.StringOut = core.attr(str)

    """
    The type of the route.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        client_vpn_endpoint_id: str | core.StringOut,
        destination_cidr_block: str | core.StringOut,
        target_vpc_subnet_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnRoute.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                destination_cidr_block=destination_cidr_block,
                target_vpc_subnet_id=target_vpc_subnet_id,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_vpn_endpoint_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        destination_cidr_block: str | core.StringOut = core.arg()

        target_vpc_subnet_id: str | core.StringOut = core.arg()
