import terrascript.core as core


@core.schema
class Route(core.Schema):

    carrier_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    core_network_arn: str | core.StringOut | None = core.attr(str, default=None)

    destination_prefix_list_id: str | core.StringOut | None = core.attr(str, default=None)

    egress_only_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    instance_id: str | core.StringOut | None = core.attr(str, default=None)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    local_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    nat_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    network_interface_id: str | core.StringOut | None = core.attr(str, default=None)

    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_peering_connection_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        carrier_gateway_id: str | core.StringOut | None = None,
        cidr_block: str | core.StringOut | None = None,
        core_network_arn: str | core.StringOut | None = None,
        destination_prefix_list_id: str | core.StringOut | None = None,
        egress_only_gateway_id: str | core.StringOut | None = None,
        gateway_id: str | core.StringOut | None = None,
        instance_id: str | core.StringOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        local_gateway_id: str | core.StringOut | None = None,
        nat_gateway_id: str | core.StringOut | None = None,
        network_interface_id: str | core.StringOut | None = None,
        transit_gateway_id: str | core.StringOut | None = None,
        vpc_endpoint_id: str | core.StringOut | None = None,
        vpc_peering_connection_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Route.Args(
                carrier_gateway_id=carrier_gateway_id,
                cidr_block=cidr_block,
                core_network_arn=core_network_arn,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_gateway_id=egress_only_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                ipv6_cidr_block=ipv6_cidr_block,
                local_gateway_id=local_gateway_id,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                transit_gateway_id=transit_gateway_id,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        carrier_gateway_id: str | core.StringOut | None = core.arg(default=None)

        cidr_block: str | core.StringOut | None = core.arg(default=None)

        core_network_arn: str | core.StringOut | None = core.arg(default=None)

        destination_prefix_list_id: str | core.StringOut | None = core.arg(default=None)

        egress_only_gateway_id: str | core.StringOut | None = core.arg(default=None)

        gateway_id: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        local_gateway_id: str | core.StringOut | None = core.arg(default=None)

        nat_gateway_id: str | core.StringOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut | None = core.arg(default=None)

        vpc_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        vpc_peering_connection_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_route_table", namespace="vpc")
class RouteTable(core.Resource):
    """
    The ARN of the route table.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the routing table.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the route table.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of virtual gateways for propagation.
    """
    propagating_vgws: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A list of route objects. Their keys are documented below. This argument is processed in [
    attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
    """
    route: list[Route] | core.ArrayOut[Route] | None = core.attr(
        Route, default=None, computed=True, kind=core.Kind.array
    )

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
    (Required) The VPC ID.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: str | core.StringOut,
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
            args=RouteTable.Args(
                vpc_id=vpc_id,
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
        propagating_vgws: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        route: list[Route] | core.ArrayOut[Route] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
