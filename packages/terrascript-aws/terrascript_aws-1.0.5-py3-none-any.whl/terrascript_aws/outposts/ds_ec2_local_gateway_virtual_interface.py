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


@core.data(type="aws_ec2_local_gateway_virtual_interface", namespace="outposts")
class DsEc2LocalGatewayVirtualInterface(core.Data):
    """
    (Optional) One or more configuration blocks containing name-values filters. See the [EC2 API Referen
    ce](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayVirtualInterfaces
    .html) for supported filters. Detailed below.
    """

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) Identifier of EC2 Local Gateway Virtual Interface.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Local address.
    """
    local_address: str | core.StringOut = core.attr(str, computed=True)

    """
    Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the EC2 Local Gateway.
    """
    local_bgp_asn: int | core.IntOut = core.attr(int, computed=True)

    """
    Identifier of the EC2 Local Gateway.
    """
    local_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    local_gateway_virtual_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Peer address.
    """
    peer_address: str | core.StringOut = core.attr(str, computed=True)

    """
    Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the peer.
    """
    peer_bgp_asn: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Key-value map of resource tags, each pair of which must exactly match a pair on the desir
    ed local gateway route table.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Virtual Local Area Network.
    """
    vlan: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2LocalGatewayVirtualInterface.Args(
                filter=filter,
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
