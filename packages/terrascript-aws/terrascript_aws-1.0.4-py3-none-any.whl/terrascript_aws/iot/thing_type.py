import terrascript.core as core


@core.schema
class Properties(core.Schema):

    description: str | core.StringOut | None = core.attr(str, default=None)

    searchable_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        description: str | core.StringOut | None = None,
        searchable_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Properties.Args(
                description=description,
                searchable_attributes=searchable_attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut | None = core.arg(default=None)

        searchable_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.resource(type="aws_iot_thing_type", namespace="iot")
class ThingType(core.Resource):
    """
    The ARN of the created AWS IoT Thing Type.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Defaults to false) Whether the thing type is deprecated. If true, no new things could be
    associated with this type.
    """
    deprecated: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces New Resource) The name of the thing type.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional), Configuration block that can contain the following properties of the thing type:
    """
    properties: Properties | None = core.attr(Properties, default=None)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        deprecated: bool | core.BoolOut | None = None,
        properties: Properties | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingType.Args(
                name=name,
                deprecated=deprecated,
                properties=properties,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        deprecated: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        properties: Properties | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
