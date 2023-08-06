import terrascript.core as core


@core.resource(type="aws_ec2_local_gateway_route", namespace="outposts")
class Ec2LocalGatewayRoute(core.Resource):
    """
    (Required) IPv4 CIDR range used for destination matches. Routing decisions are based on the most spe
    cific match.
    """

    destination_cidr_block: str | core.StringOut = core.attr(str)

    """
    EC2 Local Gateway Route Table identifier and destination CIDR block separated by underscores (`_`)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Identifier of EC2 Local Gateway Route Table.
    """
    local_gateway_route_table_id: str | core.StringOut = core.attr(str)

    """
    (Required) Identifier of EC2 Local Gateway Virtual Interface Group.
    """
    local_gateway_virtual_interface_group_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_cidr_block: str | core.StringOut,
        local_gateway_route_table_id: str | core.StringOut,
        local_gateway_virtual_interface_group_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2LocalGatewayRoute.Args(
                destination_cidr_block=destination_cidr_block,
                local_gateway_route_table_id=local_gateway_route_table_id,
                local_gateway_virtual_interface_group_id=local_gateway_virtual_interface_group_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_cidr_block: str | core.StringOut = core.arg()

        local_gateway_route_table_id: str | core.StringOut = core.arg()

        local_gateway_virtual_interface_group_id: str | core.StringOut = core.arg()
