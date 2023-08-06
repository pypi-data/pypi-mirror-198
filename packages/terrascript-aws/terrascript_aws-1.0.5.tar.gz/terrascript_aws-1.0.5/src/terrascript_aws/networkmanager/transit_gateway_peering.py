import terrascript.core as core


@core.resource(type="aws_networkmanager_transit_gateway_peering", namespace="networkmanager")
class TransitGatewayPeering(core.Resource):
    """
    Peering Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the core network.
    """
    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of a core network.
    """
    core_network_id: str | core.StringOut = core.attr(str)

    """
    The edge location for the peer.
    """
    edge_location: str | core.StringOut = core.attr(str, computed=True)

    """
    Peering ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the account owner.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of peering. This will be `TRANSIT_GATEWAY`.
    """
    peering_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The resource ARN of the peer.
    """
    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value tags for the peering. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Required) The ARN of the transit gateway for the peering request.
    """
    transit_gateway_arn: str | core.StringOut = core.attr(str)

    """
    The ID of the transit gateway peering attachment.
    """
    transit_gateway_peering_attachment_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        core_network_id: str | core.StringOut,
        transit_gateway_arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayPeering.Args(
                core_network_id=core_network_id,
                transit_gateway_arn=transit_gateway_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        core_network_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_arn: str | core.StringOut = core.arg()
