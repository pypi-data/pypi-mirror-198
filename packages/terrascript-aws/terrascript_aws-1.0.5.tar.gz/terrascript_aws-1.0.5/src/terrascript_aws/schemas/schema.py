import terrascript.core as core


@core.resource(type="aws_schemas_schema", namespace="schemas")
class Schema(core.Resource):
    """
    The Amazon Resource Name (ARN) of the discoverer.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The schema specification. Must be a valid Open API 3.0 spec.
    """
    content: str | core.StringOut = core.attr(str)

    """
    (Optional) The description of the schema. Maximum of 256 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last modified date of the schema.
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the schema. Maximum of 385 characters consisting of lower case letters, upper
    case letters, ., -, _, @.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the registry in which this schema belongs.
    """
    registry_name: str | core.StringOut = core.attr(str)

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
    (Required) The type of the schema. Valid values: `OpenApi3`.
    """
    type: str | core.StringOut = core.attr(str)

    """
    The version of the schema.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    The created date of the version of the schema.
    """
    version_created_date: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        content: str | core.StringOut,
        name: str | core.StringOut,
        registry_name: str | core.StringOut,
        type: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Schema.Args(
                content=content,
                name=name,
                registry_name=registry_name,
                type=type,
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
        content: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        registry_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
