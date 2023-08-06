import terrascript.core as core


@core.schema
class Rules(core.Schema):

    description: str | core.StringOut | None = core.attr(str, default=None)

    source: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source: str | core.StringOut,
        description: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Rules.Args(
                source=source,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut | None = core.arg(default=None)

        source: str | core.StringOut = core.arg()


@core.resource(type="aws_workspaces_ip_group", namespace="workspaces")
class IpGroup(core.Resource):

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    rules: list[Rules] | core.ArrayOut[Rules] | None = core.attr(
        Rules, default=None, kind=core.Kind.array
    )

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
        description: str | core.StringOut | None = None,
        rules: list[Rules] | core.ArrayOut[Rules] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IpGroup.Args(
                name=name,
                description=description,
                rules=rules,
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

        rules: list[Rules] | core.ArrayOut[Rules] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
