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


@core.resource(type="aws_iot_thing_type", namespace="aws_iot")
class ThingType(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    deprecated: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    properties: Properties | None = core.attr(Properties, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
