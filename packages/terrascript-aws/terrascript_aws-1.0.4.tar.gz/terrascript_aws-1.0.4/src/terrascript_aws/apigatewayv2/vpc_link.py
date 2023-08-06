import terrascript.core as core


@core.resource(type="aws_apigatewayv2_vpc_link", namespace="apigatewayv2")
class VpcLink(core.Resource):
    """
    The VPC Link ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The VPC Link identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the VPC Link. Must be between 1 and 128 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Security group IDs for the VPC Link.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) Subnet IDs for the VPC Link.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the VPC Link. If configured with a provider [`default_tags` co
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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VpcLink.Args(
                name=name,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
