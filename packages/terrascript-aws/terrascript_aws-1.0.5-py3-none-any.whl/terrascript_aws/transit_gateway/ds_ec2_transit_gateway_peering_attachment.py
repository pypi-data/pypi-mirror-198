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


@core.data(type="aws_ec2_transit_gateway_peering_attachment", namespace="transit_gateway")
class DsEc2TransitGatewayPeeringAttachment(core.Data):
    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) Identifier of the EC2 Transit Gateway Peering Attachment.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Identifier of the peer AWS account
    """
    peer_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the peer AWS region
    """
    peer_region: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the peer EC2 Transit Gateway
    """
    peer_transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A mapping of tags, each pair of which must exactly match
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Identifier of the local EC2 Transit Gateway
    """
    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

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
            args=DsEc2TransitGatewayPeeringAttachment.Args(
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
