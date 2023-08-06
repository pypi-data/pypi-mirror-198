import terrascript.core as core


@core.resource(type="aws_dx_transit_virtual_interface", namespace="direct_connect")
class DxTransitVirtualInterface(core.Resource):
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
    (Required) The ID of the Direct Connect gateway to which to connect the virtual interface.
    """
    dx_gateway_id: str | core.StringOut = core.attr(str)

    """
    The ID of the virtual interface.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether jumbo frames (8500 MTU) are supported.
    """
    jumbo_frame_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible pac
    ket that can be passed over the connection.
    """
    mtu: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The name for the virtual interface.
    """
    name: str | core.StringOut = core.attr(str)

    sitelink_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
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
        dx_gateway_id: str | core.StringOut,
        name: str | core.StringOut,
        vlan: int | core.IntOut,
        amazon_address: str | core.StringOut | None = None,
        bgp_auth_key: str | core.StringOut | None = None,
        customer_address: str | core.StringOut | None = None,
        mtu: int | core.IntOut | None = None,
        sitelink_enabled: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxTransitVirtualInterface.Args(
                address_family=address_family,
                bgp_asn=bgp_asn,
                connection_id=connection_id,
                dx_gateway_id=dx_gateway_id,
                name=name,
                vlan=vlan,
                amazon_address=amazon_address,
                bgp_auth_key=bgp_auth_key,
                customer_address=customer_address,
                mtu=mtu,
                sitelink_enabled=sitelink_enabled,
                tags=tags,
                tags_all=tags_all,
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

        dx_gateway_id: str | core.StringOut = core.arg()

        mtu: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        sitelink_enabled: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vlan: int | core.IntOut = core.arg()
