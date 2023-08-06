import terrascript.core as core


@core.resource(
    type="aws_networkmanager_transit_gateway_route_table_attachment", namespace="networkmanager"
)
class TransitGatewayRouteTableAttachment(core.Resource):
    """
    Attachment Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The policy rule number associated with the attachment.
    """
    attachment_policy_rule_number: int | core.IntOut = core.attr(int, computed=True)

    """
    The type of attachment.
    """
    attachment_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the core network.
    """
    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the core network.
    """
    core_network_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The edge location for the peer.
    """
    edge_location: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the attachment.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the attachment account owner.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the peer for the attachment.
    """
    peering_id: str | core.StringOut = core.attr(str)

    """
    The attachment resource ARN.
    """
    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the segment attachment.
    """
    segment_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the attachment.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value tags for the attachment. If configured with a provider [`default_tags` configur
    ation block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configur
    ation-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The ARN of the transit gateway route table for the attachment.
    """
    transit_gateway_route_table_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        peering_id: str | core.StringOut,
        transit_gateway_route_table_arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayRouteTableAttachment.Args(
                peering_id=peering_id,
                transit_gateway_route_table_arn=transit_gateway_route_table_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        peering_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_route_table_arn: str | core.StringOut = core.arg()
