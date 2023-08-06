import terrascript.core as core


@core.resource(type="aws_dx_hosted_public_virtual_interface", namespace="direct_connect")
class DxHostedPublicVirtualInterface(core.Resource):
    """
    (Required) The address family for the BGP peer. `ipv4 ` or `ipv6`.
    """

    address_family: str | core.StringOut = core.attr(str)

    """
    (Optional) The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
    """
    amazon_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    amazon_side_asn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the virtual interface.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Direct Connect endpoint on which the virtual interface terminates.
    """
    aws_device: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
    """
    bgp_asn: int | core.IntOut = core.attr(int)

    """
    (Optional) The authentication key for BGP configuration.
    """
    bgp_auth_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The ID of the Direct Connect connection (or LAG) on which to create the virtual interface
    .
    """
    connection_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4
    BGP peers.
    """
    customer_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the virtual interface.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for the virtual interface.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The AWS account that will own the new virtual interface.
    """
    owner_account_id: str | core.StringOut = core.attr(str)

    """
    (Required) A list of routes to be advertised to the AWS network in this region.
    """
    route_filter_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) The VLAN ID.
    """
    vlan: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: str | core.StringOut,
        bgp_asn: int | core.IntOut,
        connection_id: str | core.StringOut,
        name: str | core.StringOut,
        owner_account_id: str | core.StringOut,
        route_filter_prefixes: list[str] | core.ArrayOut[core.StringOut],
        vlan: int | core.IntOut,
        amazon_address: str | core.StringOut | None = None,
        bgp_auth_key: str | core.StringOut | None = None,
        customer_address: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxHostedPublicVirtualInterface.Args(
                address_family=address_family,
                bgp_asn=bgp_asn,
                connection_id=connection_id,
                name=name,
                owner_account_id=owner_account_id,
                route_filter_prefixes=route_filter_prefixes,
                vlan=vlan,
                amazon_address=amazon_address,
                bgp_auth_key=bgp_auth_key,
                customer_address=customer_address,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address_family: str | core.StringOut = core.arg()

        amazon_address: str | core.StringOut | None = core.arg(default=None)

        bgp_asn: int | core.IntOut = core.arg()

        bgp_auth_key: str | core.StringOut | None = core.arg(default=None)

        connection_id: str | core.StringOut = core.arg()

        customer_address: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        owner_account_id: str | core.StringOut = core.arg()

        route_filter_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vlan: int | core.IntOut = core.arg()
