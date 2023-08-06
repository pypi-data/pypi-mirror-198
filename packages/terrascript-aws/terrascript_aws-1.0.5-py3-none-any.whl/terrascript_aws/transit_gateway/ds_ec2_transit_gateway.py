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


@core.data(type="aws_ec2_transit_gateway", namespace="transit_gateway")
class DsEc2TransitGateway(core.Data):
    """
    Private Autonomous System Number (ASN) for the Amazon side of a BGP session
    """

    amazon_side_asn: int | core.IntOut = core.attr(int, computed=True)

    """
    EC2 Transit Gateway Amazon Resource Name (ARN)
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the default association route table
    """
    association_default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether resource attachment requests are automatically accepted
    """
    auto_accept_shared_attachments: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether resource attachments are automatically associated with the default association route table
    """
    default_route_table_association: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether resource attachments automatically propagate routes to the default propagation route table
    """
    default_route_table_propagation: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the EC2 Transit Gateway
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether DNS support is enabled
    """
    dns_support: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) Identifier of the EC2 Transit Gateway.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Whether Multicast support is enabled
    """
    multicast_support: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the AWS account that owns the EC2 Transit Gateway
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the default propagation route table
    """
    propagation_default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the EC2 Transit Gateway
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The list of associated CIDR blocks
    """
    transit_gateway_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Whether VPN Equal Cost Multipath Protocol support is enabled
    """
    vpn_ecmp_support: str | core.StringOut = core.attr(str, computed=True)

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
            args=DsEc2TransitGateway.Args(
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
