import terrascript.core as core


@core.resource(
    type="aws_networkmanager_transit_gateway_route_table_attachment", namespace="aws_networkmanager"
)
class TransitGatewayRouteTableAttachment(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    attachment_policy_rule_number: int | core.IntOut = core.attr(int, computed=True)

    attachment_type: str | core.StringOut = core.attr(str, computed=True)

    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    core_network_id: str | core.StringOut = core.attr(str, computed=True)

    edge_location: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    peering_id: str | core.StringOut = core.attr(str)

    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    segment_name: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_route_table_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        peering_id: str | core.StringOut,
        transit_gateway_route_table_arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayRouteTableAttachment.Args(
                peering_id=peering_id,
                transit_gateway_route_table_arn=transit_gateway_route_table_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        peering_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_route_table_arn: str | core.StringOut = core.arg()
