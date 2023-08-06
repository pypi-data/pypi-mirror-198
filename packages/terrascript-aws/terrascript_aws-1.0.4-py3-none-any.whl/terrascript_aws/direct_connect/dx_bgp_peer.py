import terrascript.core as core


@core.resource(type="aws_dx_bgp_peer", namespace="direct_connect")
class DxBgpPeer(core.Resource):
    """
    (Required) The address family for the BGP peer. `ipv4 ` or `ipv6`.
    """

    address_family: str | core.StringOut = core.attr(str)

    """
    (Optional) The IPv4 CIDR address to use to send traffic to Amazon.
    """
    amazon_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The Direct Connect endpoint on which the BGP peer terminates.
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
    The ID of the BGP peer.
    """
    bgp_peer_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Up/Down state of the BGP peer.
    """
    bgp_status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The IPv4 CIDR destination address to which Amazon should send traffic.
    """
    customer_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the BGP peer resource.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Direct Connect virtual interface on which to create the BGP peer.
    """
    virtual_interface_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: str | core.StringOut,
        bgp_asn: int | core.IntOut,
        virtual_interface_id: str | core.StringOut,
        amazon_address: str | core.StringOut | None = None,
        bgp_auth_key: str | core.StringOut | None = None,
        customer_address: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxBgpPeer.Args(
                address_family=address_family,
                bgp_asn=bgp_asn,
                virtual_interface_id=virtual_interface_id,
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

        customer_address: str | core.StringOut | None = core.arg(default=None)

        virtual_interface_id: str | core.StringOut = core.arg()
