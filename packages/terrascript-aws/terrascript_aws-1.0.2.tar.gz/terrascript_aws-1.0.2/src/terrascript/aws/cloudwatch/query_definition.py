import terrascript.core as core


@core.resource(type="aws_cloudwatch_query_definition", namespace="aws_cloudwatch")
class QueryDefinition(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    log_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    query_definition_id: str | core.StringOut = core.attr(str, computed=True)

    query_string: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        query_string: str | core.StringOut,
        log_group_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueryDefinition.Args(
                name=name,
                query_string=query_string,
                log_group_names=log_group_names,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        query_string: str | core.StringOut = core.arg()
