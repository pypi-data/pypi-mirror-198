import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway", namespace="transit_gateway")
class Ec2TransitGateway(core.Resource):
    """
    (Optional) Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is
    64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value:
    64512`.
    """

    amazon_side_asn: int | core.IntOut | None = core.attr(int, default=None)

    """
    EC2 Transit Gateway Amazon Resource Name (ARN)
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the default association route table
    """
    association_default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether resource attachment requests are automatically accepted. Valid values: `disable`,
    enable`. Default value: `disable`.
    """
    auto_accept_shared_attachments: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether resource attachments are automatically associated with the default association ro
    ute table. Valid values: `disable`, `enable`. Default value: `enable`.
    """
    default_route_table_association: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether resource attachments automatically propagate routes to the default propagation ro
    ute table. Valid values: `disable`, `enable`. Default value: `enable`.
    """
    default_route_table_propagation: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Description of the EC2 Transit Gateway.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable
    .
    """
    dns_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    EC2 Transit Gateway identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether Multicast support is enabled. Required to use `ec2_transit_gateway_multicast_doma
    in`. Valid values: `disable`, `enable`. Default value: `disable`.
    """
    multicast_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    Identifier of the AWS account that owns the EC2 Transit Gateway
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the default propagation route table
    """
    propagation_default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value tags for the EC2 Transit Gateway. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level.
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
    (Optional) One or more IPv4 or IPv6 CIDR blocks for the transit gateway. Must be a size /24 CIDR blo
    ck or larger for IPv4, or a size /64 CIDR block or larger for IPv6.
    """
    transit_gateway_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `e
    nable`. Default value: `enable`.
    """
    vpn_ecmp_support: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        amazon_side_asn: int | core.IntOut | None = None,
        auto_accept_shared_attachments: str | core.StringOut | None = None,
        default_route_table_association: str | core.StringOut | None = None,
        default_route_table_propagation: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        dns_support: str | core.StringOut | None = None,
        multicast_support: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        vpn_ecmp_support: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGateway.Args(
                amazon_side_asn=amazon_side_asn,
                auto_accept_shared_attachments=auto_accept_shared_attachments,
                default_route_table_association=default_route_table_association,
                default_route_table_propagation=default_route_table_propagation,
                description=description,
                dns_support=dns_support,
                multicast_support=multicast_support,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_cidr_blocks=transit_gateway_cidr_blocks,
                vpn_ecmp_support=vpn_ecmp_support,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        amazon_side_asn: int | core.IntOut | None = core.arg(default=None)

        auto_accept_shared_attachments: str | core.StringOut | None = core.arg(default=None)

        default_route_table_association: str | core.StringOut | None = core.arg(default=None)

        default_route_table_propagation: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        dns_support: str | core.StringOut | None = core.arg(default=None)

        multicast_support: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        vpn_ecmp_support: str | core.StringOut | None = core.arg(default=None)
