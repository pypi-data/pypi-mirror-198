import terrascript.core as core


@core.resource(
    type="aws_ec2_transit_gateway_peering_attachment_accepter", namespace="aws_transit_gateway"
)
class Ec2TransitGatewayPeeringAttachmentAccepter(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    peer_account_id: str | core.StringOut = core.attr(str, computed=True)

    peer_region: str | core.StringOut = core.attr(str, computed=True)

    peer_transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_attachment_id: str | core.StringOut = core.attr(str)

    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_attachment_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayPeeringAttachmentAccepter.Args(
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_attachment_id: str | core.StringOut = core.arg()
