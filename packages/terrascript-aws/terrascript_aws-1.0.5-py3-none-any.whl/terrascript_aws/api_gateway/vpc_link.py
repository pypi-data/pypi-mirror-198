import terrascript.core as core


@core.resource(type="aws_api_gateway_vpc_link", namespace="api_gateway")
class VpcLink(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the VPC link.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The identifier of the VpcLink.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name used to label and identify the VPC link.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
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
    (Required, ForceNew) The list of network load balancer arns in the VPC targeted by the VPC link. Cur
    rently AWS only supports 1 target.
    """
    target_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        target_arns: list[str] | core.ArrayOut[core.StringOut],
        description: str | core.StringOut | None = None,
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
                target_arns=target_arns,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()
