import terrascript.core as core


@core.resource(type="aws_athena_data_catalog", namespace="athena")
class DataCatalog(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    parameters: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut,
        name: str | core.StringOut,
        parameters: dict[str, str] | core.MapOut[core.StringOut],
        type: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataCatalog.Args(
                description=description,
                name=name,
                parameters=parameters,
                type=type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
