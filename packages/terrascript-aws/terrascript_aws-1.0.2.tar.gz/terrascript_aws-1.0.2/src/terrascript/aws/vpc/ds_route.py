import terrascript.core as core


@core.data(type="aws_route", namespace="aws_vpc")
class DsRoute(core.Data):

    carrier_gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    core_network_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    destination_cidr_block: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    destination_ipv6_cidr_block: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    destination_prefix_list_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    egress_only_gateway_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    local_gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    nat_gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interface_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    route_table_id: str | core.StringOut = core.attr(str)

    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    vpc_peering_connection_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        data_name: str,
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
        vpc_peering_connection_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRoute.Args(
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
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
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

        vpc_peering_connection_id: str | core.StringOut | None = core.arg(default=None)
