import terrascript.core as core


@core.schema
class FieldToMatch(core.Schema):

    data: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        data: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FieldToMatch.Args(
                type=type,
                data=data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class SqlInjectionMatchTuples(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    text_transformation: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        text_transformation: str | core.StringOut,
    ):
        super().__init__(
            args=SqlInjectionMatchTuples.Args(
                field_to_match=field_to_match,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        text_transformation: str | core.StringOut = core.arg()


@core.resource(type="aws_waf_sql_injection_match_set", namespace="waf")
class SqlInjectionMatchSet(core.Resource):
    """
    The ID of the WAF SQL Injection Match Set.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or description of the SQL Injection Match Set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if
    you want AWS WAF to inspect a header, the name of the header.
    """
    sql_injection_match_tuples: list[SqlInjectionMatchTuples] | core.ArrayOut[
        SqlInjectionMatchTuples
    ] | None = core.attr(SqlInjectionMatchTuples, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        sql_injection_match_tuples: list[SqlInjectionMatchTuples]
        | core.ArrayOut[SqlInjectionMatchTuples]
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SqlInjectionMatchSet.Args(
                name=name,
                sql_injection_match_tuples=sql_injection_match_tuples,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        sql_injection_match_tuples: list[SqlInjectionMatchTuples] | core.ArrayOut[
            SqlInjectionMatchTuples
        ] | None = core.arg(default=None)
