import terrascript.core as core


@core.resource(type="aws_dynamodb_contributor_insights", namespace="dynamodb")
class ContributorInsights(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The global secondary index name
    """
    index_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the table to enable contributor insights
    """
    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        table_name: str | core.StringOut,
        index_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContributorInsights.Args(
                table_name=table_name,
                index_name=index_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        index_name: str | core.StringOut | None = core.arg(default=None)

        table_name: str | core.StringOut = core.arg()
