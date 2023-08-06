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
class XssMatchTuples(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    text_transformation: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        text_transformation: str | core.StringOut,
    ):
        super().__init__(
            args=XssMatchTuples.Args(
                field_to_match=field_to_match,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        text_transformation: str | core.StringOut = core.arg()


@core.resource(type="aws_waf_xss_match_set", namespace="waf")
class XssMatchSet(core.Resource):
    """
    Amazon Resource Name (ARN)
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the WAF XssMatchSet.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or description of the SizeConstraintSet.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The parts of web requests that you want to inspect for cross-site scripting attacks.
    """
    xss_match_tuples: list[XssMatchTuples] | core.ArrayOut[XssMatchTuples] | None = core.attr(
        XssMatchTuples, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        xss_match_tuples: list[XssMatchTuples] | core.ArrayOut[XssMatchTuples] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=XssMatchSet.Args(
                name=name,
                xss_match_tuples=xss_match_tuples,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        xss_match_tuples: list[XssMatchTuples] | core.ArrayOut[XssMatchTuples] | None = core.arg(
            default=None
        )
