import terrascript.core as core


@core.resource(type="aws_mq_configuration", namespace="aws_mq")
class Configuration(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_strategy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    data: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    engine_type: str | core.StringOut = core.attr(str)

    engine_version: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str)

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
        data: str | core.StringOut,
        engine_type: str | core.StringOut,
        engine_version: str | core.StringOut,
        name: str | core.StringOut,
        authentication_strategy: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Configuration.Args(
                data=data,
                engine_type=engine_type,
                engine_version=engine_version,
                name=name,
                authentication_strategy=authentication_strategy,
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
        authentication_strategy: str | core.StringOut | None = core.arg(default=None)

        data: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        engine_type: str | core.StringOut = core.arg()

        engine_version: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
