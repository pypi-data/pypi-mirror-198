import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_connect_peer", namespace="transit_gateway")
class Ec2TransitGatewayConnectPeer(core.Resource):
    """
    EC2 Transit Gateway Connect Peer ARN
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The BGP ASN number assigned customer device. If not provided, it will use the same BGP AS
    N as is associated with Transit Gateway.
    """
    bgp_asn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    EC2 Transit Gateway Connect Peer identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The CIDR block that will be used for addressing within the tunnel. It must contain exactl
    y one IPv4 CIDR block and up to one IPv6 CIDR block. The IPv4 CIDR block must be /29 size and must b
    e within 169.254.0.0/16 range, with exception of: 169.254.0.0/29, 169.254.1.0/29, 169.254.2.0/29, 16
    9.254.3.0/29, 169.254.4.0/29, 169.254.5.0/29, 169.254.169.248/29. The IPv6 CIDR block must be /125 s
    ize and must be within fd00::/8. The first IP from each CIDR block is assigned for customer gateway,
    the second and third is for Transit Gateway (An example: from range 169.254.100.0/29, .1 is assigne
    d to customer gateway and .2 and .3 are assigned to Transit Gateway)
    """
    inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) The IP addressed assigned to customer device, which will be used as tunnel endpoint. It c
    an be IPv4 or IPv6 address, but must be the same address family as `transit_gateway_address`
    """
    peer_address: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value tags for the EC2 Transit Gateway Connect Peer. If configured with a provider [`
    default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs
    #default_tags-configuration-block) present, tags with matching keys will overwrite those defined at
    the provider-level.
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
    (Optional) The IP address assigned to Transit Gateway, which will be used as tunnel endpoint. This a
    ddress must be from associated Transit Gateway CIDR block. The address must be from the same address
    family as `peer_address`. If not set explicitly, it will be selected from associated Transit Gatewa
    y CIDR blocks
    """
    transit_gateway_address: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) The Transit Gateway Connect
    """
    transit_gateway_attachment_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut],
        peer_address: str | core.StringOut,
        transit_gateway_attachment_id: str | core.StringOut,
        bgp_asn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_address: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayConnectPeer.Args(
                inside_cidr_blocks=inside_cidr_blocks,
                peer_address=peer_address,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                bgp_asn=bgp_asn,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_address=transit_gateway_address,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bgp_asn: str | core.StringOut | None = core.arg(default=None)

        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        peer_address: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_address: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_attachment_id: str | core.StringOut = core.arg()
