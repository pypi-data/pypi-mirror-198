import terrascript.core as core


@core.resource(type="aws_route", namespace="vpc")
class Route(core.Resource):
    """
    (Optional) Identifier of a carrier gateway. This attribute can only be used when the VPC contains a
    subnet which is associated with a Wavelength Zone.
    """

    carrier_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) of a core network.
    """
    core_network_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The destination CIDR block.
    """
    destination_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The destination IPv6 CIDR block.
    """
    destination_ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of a [managed prefix list](ec2_managed_prefix_list.html) destination.
    """
    destination_prefix_list_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of a VPC Egress Only Internet Gateway.
    """
    egress_only_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of a VPC internet gateway or a virtual private gateway.
    """
    gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    Route identifier computed from the routing table identifier and route destination.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, **Deprecated** use `network_interface_id` instead) Identifier of an EC2 instance.
    """
    instance_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The AWS account ID of the owner of the EC2 instance.
    """
    instance_owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Identifier of a Outpost local gateway.
    """
    local_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of a VPC NAT gateway.
    """
    nat_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of an EC2 network interface.
    """
    network_interface_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    How the route was created - `CreateRouteTable`, `CreateRoute` or `EnableVgwRoutePropagation`.
    """
    origin: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the routing table.
    """
    route_table_id: str | core.StringOut = core.attr(str)

    """
    The state of the route - `active` or `blackhole`.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Identifier of an EC2 Transit Gateway.
    """
    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of a VPC Endpoint.
    """
    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of a VPC peering connection.
    """
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
