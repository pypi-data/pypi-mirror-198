import terrascript.core as core


@core.resource(type="aws_neptune_subnet_group", namespace="neptune")
class SubnetGroup(core.Resource):
    """
    The ARN of the neptune subnet group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the neptune subnet group. Defaults to "Managed by Terraform".
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The neptune subnet group name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The name of the neptune subnet group. If omitted, Terraform will ass
    ign a random, unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) A list of VPC subnet IDs.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

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

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SubnetGroup.Args(
                subnet_ids=subnet_ids,
                description=description,
                name=name,
                name_prefix=name_prefix,
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

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
