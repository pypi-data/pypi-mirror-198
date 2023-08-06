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


@core.data(type="aws_ec2_transit_gateway_vpn_attachment", namespace="transit_gateway")
class DsEc2TransitGatewayVpnAttachment(core.Data):
    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    EC2 Transit Gateway VPN Attachment identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags, each pair of which must exactly match a pair on the desired Transit Gatewa
    y VPN Attachment.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Identifier of the EC2 Transit Gateway.
    """
    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Identifier of the EC2 VPN Connection.
    """
    vpn_connection_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_id: str | core.StringOut | None = None,
        vpn_connection_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGatewayVpnAttachment.Args(
                filter=filter,
                tags=tags,
                transit_gateway_id=transit_gateway_id,
                vpn_connection_id=vpn_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut | None = core.arg(default=None)

        vpn_connection_id: str | core.StringOut | None = core.arg(default=None)
