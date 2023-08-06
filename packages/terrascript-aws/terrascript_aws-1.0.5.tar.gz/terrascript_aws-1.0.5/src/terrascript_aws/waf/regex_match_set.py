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
class RegexMatchTuple(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    regex_pattern_set_id: str | core.StringOut = core.attr(str)

    text_transformation: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        regex_pattern_set_id: str | core.StringOut,
        text_transformation: str | core.StringOut,
    ):
        super().__init__(
            args=RegexMatchTuple.Args(
                field_to_match=field_to_match,
                regex_pattern_set_id=regex_pattern_set_id,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        regex_pattern_set_id: str | core.StringOut = core.arg()

        text_transformation: str | core.StringOut = core.arg()


@core.resource(type="aws_waf_regex_match_set", namespace="waf")
class RegexMatchSet(core.Resource):
    """
    Amazon Resource Name (ARN)
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the WAF Regex Match Set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or description of the Regex Match Set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The regular expression pattern that you want AWS WAF to search for in web requests, the l
    ocation in requests that you want AWS WAF to search, and other settings. See below.
    """
    regex_match_tuple: list[RegexMatchTuple] | core.ArrayOut[RegexMatchTuple] | None = core.attr(
        RegexMatchTuple, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        regex_match_tuple: list[RegexMatchTuple] | core.ArrayOut[RegexMatchTuple] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegexMatchSet.Args(
                name=name,
                regex_match_tuple=regex_match_tuple,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        regex_match_tuple: list[RegexMatchTuple] | core.ArrayOut[RegexMatchTuple] | None = core.arg(
            default=None
        )
