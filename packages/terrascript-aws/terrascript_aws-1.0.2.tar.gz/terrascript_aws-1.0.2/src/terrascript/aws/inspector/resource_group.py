import terrascript.core as core


@core.resource(type="aws_inspector_resource_group", namespace="aws_inspector")
class ResourceGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    def __init__(
        self,
        resource_name: str,
        *,
        tags: dict[str, str] | core.MapOut[core.StringOut],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceGroup.Args(
                tags=tags,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        tags: dict[str, str] | core.MapOut[core.StringOut] = core.arg()
