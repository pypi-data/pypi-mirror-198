import terrascript.core as core


@core.schema
class Route(core.Schema):

    cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    core_network_arn: str | core.StringOut | None = core.attr(str, default=None)

    destination_prefix_list_id: str | core.StringOut | None = core.attr(str, default=None)

    egress_only_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    instance_id: str | core.StringOut | None = core.attr(str, default=None)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    nat_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    network_interface_id: str | core.StringOut | None = core.attr(str, default=None)

    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_peering_connection_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cidr_block: str | core.StringOut | None = None,
        core_network_arn: str | core.StringOut | None = None,
        destination_prefix_list_id: str | core.StringOut | None = None,
        egress_only_gateway_id: str | core.StringOut | None = None,
        gateway_id: str | core.StringOut | None = None,
        instance_id: str | core.StringOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        nat_gateway_id: str | core.StringOut | None = None,
        network_interface_id: str | core.StringOut | None = None,
        transit_gateway_id: str | core.StringOut | None = None,
        vpc_endpoint_id: str | core.StringOut | None = None,
        vpc_peering_connection_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Route.Args(
                cidr_block=cidr_block,
                core_network_arn=core_network_arn,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_gateway_id=egress_only_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                ipv6_cidr_block=ipv6_cidr_block,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                transit_gateway_id=transit_gateway_id,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: str | core.StringOut | None = core.arg(default=None)

        core_network_arn: str | core.StringOut | None = core.arg(default=None)

        destination_prefix_list_id: str | core.StringOut | None = core.arg(default=None)

        egress_only_gateway_id: str | core.StringOut | None = core.arg(default=None)

        gateway_id: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        nat_gateway_id: str | core.StringOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut | None = core.arg(default=None)

        vpc_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        vpc_peering_connection_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_default_route_table", namespace="aws_vpc")
class DefaultRouteTable(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_route_table_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    propagating_vgws: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    route: list[Route] | core.ArrayOut[Route] | None = core.attr(
        Route, default=None, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        default_route_table_id: str | core.StringOut,
        propagating_vgws: list[str] | core.ArrayOut[core.StringOut] | None = None,
        route: list[Route] | core.ArrayOut[Route] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultRouteTable.Args(
                default_route_table_id=default_route_table_id,
                propagating_vgws=propagating_vgws,
                route=route,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_route_table_id: str | core.StringOut = core.arg()

        propagating_vgws: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        route: list[Route] | core.ArrayOut[Route] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
