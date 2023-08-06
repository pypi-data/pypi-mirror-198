import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_connect_peer", namespace="aws_transit_gateway")
class Ec2TransitGatewayConnectPeer(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bgp_asn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    peer_address: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_address: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    transit_gateway_attachment_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut],
        peer_address: str | core.StringOut,
        transit_gateway_attachment_id: str | core.StringOut,
        bgp_asn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_address: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayConnectPeer.Args(
                inside_cidr_blocks=inside_cidr_blocks,
                peer_address=peer_address,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                bgp_asn=bgp_asn,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_address=transit_gateway_address,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bgp_asn: str | core.StringOut | None = core.arg(default=None)

        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        peer_address: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_address: str | core.StringOut | None = core.arg(default=None)

        transit_gateway_attachment_id: str | core.StringOut = core.arg()
