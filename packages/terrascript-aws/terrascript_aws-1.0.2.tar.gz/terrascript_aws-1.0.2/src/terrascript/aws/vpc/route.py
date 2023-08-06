import terrascript.core as core


@core.resource(type="aws_route", namespace="aws_vpc")
class Route(core.Resource):

    carrier_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    core_network_arn: str | core.StringOut | None = core.attr(str, default=None)

    destination_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    destination_ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    destination_prefix_list_id: str | core.StringOut | None = core.attr(str, default=None)

    egress_only_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    instance_owner_id: str | core.StringOut = core.attr(str, computed=True)

    local_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    nat_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    network_interface_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    origin: str | core.StringOut = core.attr(str, computed=True)

    route_table_id: str | core.StringOut = core.attr(str)

    state: str | core.StringOut = core.attr(str, computed=True)

    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_peering_connection_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: str | core.StringOut,
        carrier_gateway_id: str | core.StringOut | None = None,
        core_network_arn: str | core.StringOut | None = None,
        destination_cidr_block: str | core.StringOut | None = None,
        destination_ipv6_cidr_block: str | core.StringOut | None = None,
        destination_prefix_list_id: str | core.StringOut | None = None,
        egress_only_gateway_id: str | core.StringOut | None = None,
        gateway_id: str | core.StringOut | None = None,
        instance_id: str | core.StringOut | None = None,
        local_gateway_id: str | core.StringOut | None = None,
        nat_gateway_id: str | core.StringOut | None = None,
        network_interface_id: str | core.StringOut | None = None,
        transit_gateway_id: str | core.StringOut | None = None,
        vpc_endpoint_id: str | core.StringOut | None = None,
        vpc_peering_connection_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Route.Args(
                route_table_id=route_table_id,
                carrier_gateway_id=carrier_gateway_id,
                core_network_arn=core_network_arn,
                destination_cidr_block=destination_cidr_block,
                destination_ipv6_cidr_block=destination_ipv6_cidr_block,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_gateway_id=egress_only_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                local_gateway_id=local_gateway_id,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                transit_gateway_id=transit_gateway_id,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        carrier_gateway_id: str | core.StringOut | None = core.arg(default=None)

        core_network_arn: str | core.StringOut | None = core.arg(default=None)

        destination_cidr_block: str | core.StringOut | None = core.arg(default=None)

        destination_ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        destination_prefix_list_id: str | core.StringOut | None = core.arg(default=None)

        egress_only_gateway_id: str | core.StringOut | None = core.arg(default=None)

        gateway_id: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)

        local_gateway_id: str | core.StringOut | None = core.arg(default=None)

        nat_gateway_id: str | core.StringOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut | None = core.arg(default=None)

        route_table_id: str | core.StringOut = core.arg()

        transit_gateway_id: str | core.StringOut | None = core.arg(default=None)

        vpc_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        vpc_peering_connection_id: str | core.StringOut | None = core.arg(default=None)
