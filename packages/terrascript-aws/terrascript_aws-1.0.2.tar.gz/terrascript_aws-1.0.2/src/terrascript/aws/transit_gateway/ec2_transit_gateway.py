import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway", namespace="aws_transit_gateway")
class Ec2TransitGateway(core.Resource):

    amazon_side_asn: int | core.IntOut | None = core.attr(int, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    association_default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    auto_accept_shared_attachments: str | core.StringOut | None = core.attr(str, default=None)

    default_route_table_association: str | core.StringOut | None = core.attr(str, default=None)

    default_route_table_propagation: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    dns_support: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    multicast_support: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    propagation_default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
