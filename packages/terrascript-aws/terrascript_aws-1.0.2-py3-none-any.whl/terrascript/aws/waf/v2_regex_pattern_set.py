import terrascript.core as core


@core.schema
class RegularExpression(core.Schema):

    regex_string: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        regex_string: str | core.StringOut,
    ):
        super().__init__(
            args=RegularExpression.Args(
                regex_string=regex_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        regex_string: str | core.StringOut = core.arg()


@core.resource(type="aws_wafv2_regex_pattern_set", namespace="aws_waf")
class V2RegexPatternSet(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    lock_token: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    regular_expression: list[RegularExpression] | core.ArrayOut[
        RegularExpression
    ] | None = core.attr(RegularExpression, default=None, kind=core.Kind.array)

    scope: str | core.StringOut = core.attr(str)

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
        scope: str | core.StringOut,
        description: str | core.StringOut | None = None,
        regular_expression: list[RegularExpression]
        | core.ArrayOut[RegularExpression]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2RegexPatternSet.Args(
                name=name,
                scope=scope,
                description=description,
                regular_expression=regular_expression,
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

        regular_expression: list[RegularExpression] | core.ArrayOut[
            RegularExpression
        ] | None = core.arg(default=None)

        scope: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
