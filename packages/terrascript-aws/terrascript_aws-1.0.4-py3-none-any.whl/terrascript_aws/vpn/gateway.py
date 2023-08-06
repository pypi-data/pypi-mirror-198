import terrascript.core as core


@core.resource(type="aws_vpn_gateway", namespace="vpn")
class Gateway(core.Resource):
    """
    (Optional) The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don't speci
    fy an ASN, the virtual private gateway is created with the default ASN.
    """

    amazon_side_asn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of the VPN Gateway.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Availability Zone for the virtual private gateway.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the VPN Gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
    (Optional) The VPC ID to create in.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        amazon_side_asn: str | core.StringOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Gateway.Args(
                amazon_side_asn=amazon_side_asn,
                availability_zone=availability_zone,
                tags=tags,
                tags_all=tags_all,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        amazon_side_asn: str | core.StringOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
