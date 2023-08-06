import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ec2_transit_gateway_connect_peer", namespace="transit_gateway")
class DsEc2TransitGatewayConnectPeer(core.Data):
    """
    EC2 Transit Gateway Connect Peer ARN
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The BGP ASN number assigned customer device
    """
    bgp_asn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The CIDR blocks that will be used for addressing within the tunnel.
    """
    inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The IP addressed assigned to customer device, which is used as tunnel endpoint
    """
    peer_address: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the EC2 Transit Gateway Connect Peer
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The IP address assigned to Transit Gateway, which is used as tunnel endpoint.
    """
    transit_gateway_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The Transit Gateway Connect
    """
    transit_gateway_attachment_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Identifier of the EC2 Transit Gateway Connect Peer.
    """
    transit_gateway_connect_peer_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_connect_peer_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGatewayConnectPeer.Args(
                filter=filter,
                tags=tags,
                transit_gateway_connect_peer_id=transit_gateway_connect_peer_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_connect_peer_id: str | core.StringOut | None = core.arg(default=None)
