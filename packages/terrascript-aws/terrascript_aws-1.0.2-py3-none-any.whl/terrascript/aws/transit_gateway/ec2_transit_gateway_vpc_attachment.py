import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_vpc_attachment", namespace="aws_transit_gateway")
class Ec2TransitGatewayVpcAttachment(core.Resource):

    appliance_mode_support: str | core.StringOut | None = core.attr(str, default=None)

    dns_support: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_support: str | core.StringOut | None = core.attr(str, default=None)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_default_route_table_association: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    transit_gateway_id: str | core.StringOut = core.attr(str)

    vpc_id: str | core.StringOut = core.attr(str)

    vpc_owner_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        transit_gateway_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        appliance_mode_support: str | core.StringOut | None = None,
        dns_support: str | core.StringOut | None = None,
        ipv6_support: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_default_route_table_association: bool | core.BoolOut | None = None,
        transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayVpcAttachment.Args(
                subnet_ids=subnet_ids,
                transit_gateway_id=transit_gateway_id,
                vpc_id=vpc_id,
                appliance_mode_support=appliance_mode_support,
                dns_support=dns_support,
                ipv6_support=ipv6_support,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_default_route_table_association=transit_gateway_default_route_table_association,
                transit_gateway_default_route_table_propagation=transit_gateway_default_route_table_propagation,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        appliance_mode_support: str | core.StringOut | None = core.arg(default=None)

        dns_support: str | core.StringOut | None = core.arg(default=None)

        ipv6_support: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_default_route_table_association: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()
