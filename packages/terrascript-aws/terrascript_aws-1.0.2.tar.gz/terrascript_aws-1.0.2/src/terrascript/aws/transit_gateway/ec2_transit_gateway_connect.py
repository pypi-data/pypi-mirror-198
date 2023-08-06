import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_connect", namespace="aws_transit_gateway")
class Ec2TransitGatewayConnect(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    protocol: str | core.StringOut | None = core.attr(str, default=None)

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

    transport_attachment_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_id: str | core.StringOut,
        transport_attachment_id: str | core.StringOut,
        protocol: str | core.StringOut | None = None,
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
            args=Ec2TransitGatewayConnect.Args(
                transit_gateway_id=transit_gateway_id,
                transport_attachment_id=transport_attachment_id,
                protocol=protocol,
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
        protocol: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_default_route_table_association: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_id: str | core.StringOut = core.arg()

        transport_attachment_id: str | core.StringOut = core.arg()
