import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_multicast_domain", namespace="transit_gateway")
class Ec2TransitGatewayMulticastDomain(core.Resource):
    """
    EC2 Transit Gateway Multicast Domain Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to automatically accept cross-account subnet associations that are associated wit
    h the EC2 Transit Gateway Multicast Domain. Valid values: `disable`, `enable`. Default value: `disab
    le`.
    """
    auto_accept_shared_associations: str | core.StringOut | None = core.attr(str, default=None)

    """
    EC2 Transit Gateway Multicast Domain identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to enable Internet Group Management Protocol (IGMP) version 2 for the EC2 Transit
    Gateway Multicast Domain. Valid values: `disable`, `enable`. Default value: `disable`.
    """
    igmpv2_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    Identifier of the AWS account that owns the EC2 Transit Gateway Multicast Domain.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to enable support for statically configuring multicast group sources for the EC2
    Transit Gateway Multicast Domain. Valid values: `disable`, `enable`. Default value: `disable`.
    """
    static_sources_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value tags for the EC2 Transit Gateway Multicast Domain. If configured with a provide
    r [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/
    docs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
    at the provider-level.
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
    (Required) EC2 Transit Gateway identifier. The EC2 Transit Gateway must have `multicast_support` ena
    bled.
    """
    transit_gateway_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_id: str | core.StringOut,
        auto_accept_shared_associations: str | core.StringOut | None = None,
        igmpv2_support: str | core.StringOut | None = None,
        static_sources_support: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayMulticastDomain.Args(
                transit_gateway_id=transit_gateway_id,
                auto_accept_shared_associations=auto_accept_shared_associations,
                igmpv2_support=igmpv2_support,
                static_sources_support=static_sources_support,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_accept_shared_associations: str | core.StringOut | None = core.arg(default=None)

        igmpv2_support: str | core.StringOut | None = core.arg(default=None)

        static_sources_support: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut = core.arg()
