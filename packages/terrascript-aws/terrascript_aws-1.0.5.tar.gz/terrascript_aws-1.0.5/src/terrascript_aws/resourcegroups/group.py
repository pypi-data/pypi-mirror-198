import terrascript.core as core


@core.schema
class ResourceQuery(core.Schema):

    query: str | core.StringOut = core.attr(str)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        query: str | core.StringOut,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ResourceQuery.Args(
                query=query,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        query: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_resourcegroups_group", namespace="resourcegroups")
class Group(core.Resource):
    """
    The ARN assigned by AWS for this resource group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of the resource group.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The resource group's name. A resource group name can have a maximum of 127 characters, in
    cluding letters, numbers, hyphens, dots, and underscores. The name cannot start with `AWS` or `aws`.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) A `resource_query` block. Resource queries are documented below.
    """
    resource_query: ResourceQuery = core.attr(ResourceQuery)

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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        resource_query: ResourceQuery,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Group.Args(
                name=name,
                resource_query=resource_query,
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

        resource_query: ResourceQuery = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
