import terrascript.core as core


@core.schema
class Configuration(core.Schema):

    style: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        style: str | core.StringOut,
    ):
        super().__init__(
            args=Configuration.Args(
                style=style,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        style: str | core.StringOut = core.arg()


@core.resource(type="aws_location_map", namespace="aws_location")
class Map(core.Resource):

    configuration: Configuration = core.attr(Configuration)

    create_time: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    map_arn: str | core.StringOut = core.attr(str, computed=True)

    map_name: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        configuration: Configuration,
        map_name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Map.Args(
                configuration=configuration,
                map_name=map_name,
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
        configuration: Configuration = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        map_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
