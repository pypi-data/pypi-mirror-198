import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_peering_attachment", namespace="transit_gateway")
class Ec2TransitGatewayPeeringAttachment(core.Resource):
    """
    EC2 Transit Gateway Attachment identifier
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Account ID of EC2 Transit Gateway to peer with. Defaults to the account ID the [AWS provi
    der][1] is currently connected to.
    """
    peer_account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Region of EC2 Transit Gateway to peer with.
    """
    peer_region: str | core.StringOut = core.attr(str)

    """
    (Required) Identifier of EC2 Transit Gateway to peer with.
    """
    peer_transit_gateway_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value tags for the EC2 Transit Gateway Peering Attachment. If configured with a provi
    der [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/lates
    t/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those defin
    ed at the provider-level.
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
    (Required) Identifier of EC2 Transit Gateway.
    """
    transit_gateway_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        peer_region: str | core.StringOut,
        peer_transit_gateway_id: str | core.StringOut,
        transit_gateway_id: str | core.StringOut,
        peer_account_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayPeeringAttachment.Args(
                peer_region=peer_region,
                peer_transit_gateway_id=peer_transit_gateway_id,
                transit_gateway_id=transit_gateway_id,
                peer_account_id=peer_account_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        peer_account_id: str | core.StringOut | None = core.arg(default=None)

        peer_region: str | core.StringOut = core.arg()

        peer_transit_gateway_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut = core.arg()
