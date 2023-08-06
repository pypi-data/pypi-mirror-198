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


@core.data(type="aws_ec2_transit_gateway_attachment", namespace="transit_gateway")
class DsEc2TransitGatewayAttachment(core.Data):
    """
    The ARN of the attachment.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the resource.
    """
    resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the resource.
    """
    resource_owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The resource type.
    """
    resource_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The attachment state.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the attachment.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) The ID of the attachment.
    """
    transit_gateway_attachment_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The ID of the transit gateway.
    """
    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the transit gateway.
    """
    transit_gateway_owner_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_attachment_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGatewayAttachment.Args(
                filter=filter,
                tags=tags,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_attachment_id: str | core.StringOut | None = core.arg(default=None)
