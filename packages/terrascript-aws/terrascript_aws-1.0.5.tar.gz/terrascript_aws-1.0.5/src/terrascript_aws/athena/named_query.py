import terrascript.core as core


@core.resource(type="aws_athena_named_query", namespace="athena")
class NamedQuery(core.Resource):
    """
    (Required) The database to which the query belongs.
    """

    database: str | core.StringOut = core.attr(str)

    """
    (Optional) A brief explanation of the query. Maximum length of 1024.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique ID of the query.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The plain language name for the query. Maximum length of 128.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The text of the query itself. In other words, all query statements. Maximum length of 262
    144.
    """
    query: str | core.StringOut = core.attr(str)

    """
    (Optional) The workgroup to which the query belongs. Defaults to `primary`
    """
    workgroup: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        database: str | core.StringOut,
        name: str | core.StringOut,
        query: str | core.StringOut,
        description: str | core.StringOut | None = None,
        workgroup: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NamedQuery.Args(
                database=database,
                name=name,
                query=query,
                description=description,
                workgroup=workgroup,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        database: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        query: str | core.StringOut = core.arg()

        workgroup: str | core.StringOut | None = core.arg(default=None)
