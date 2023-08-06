import terrascript.core as core


@core.resource(type="aws_cloudwatch_query_definition", namespace="cloudwatch")
class QueryDefinition(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specific log groups to use with the query.
    """
    log_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The name of the query.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The query definition ID.
    """
    query_definition_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The query to save. You can read more about CloudWatch Logs Query Syntax in the [documenta
    tion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).
    """
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
