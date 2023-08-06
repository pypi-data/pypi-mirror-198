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


@core.data(type="aws_ec2_transit_gateway_vpc_attachment", namespace="transit_gateway")
class DsEc2TransitGatewayVpcAttachment(core.Data):
    """
    Whether Appliance Mode support is enabled.
    """

    appliance_mode_support: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether DNS support is enabled.
    """
    dns_support: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) Identifier of the EC2 Transit Gateway VPC Attachment.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Whether IPv6 support is enabled.
    """
    ipv6_support: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifiers of EC2 Subnets.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Key-value tags for the EC2 Transit Gateway VPC Attachment
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    EC2 Transit Gateway identifier
    """
    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of EC2 VPC.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the AWS account that owns the EC2 VPC.
    """
    vpc_owner_id: str | core.StringOut = core.attr(str, computed=True)

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
            args=DsEc2TransitGatewayVpcAttachment.Args(
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
