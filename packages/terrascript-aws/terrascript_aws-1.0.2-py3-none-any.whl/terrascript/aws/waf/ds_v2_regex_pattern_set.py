import terrascript.core as core


@core.schema
class RegularExpression(core.Schema):

    regex_string: str | core.StringOut = core.attr(str, computed=True)

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


@core.data(type="aws_wafv2_regex_pattern_set", namespace="aws_waf")
class DsV2RegexPatternSet(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    regular_expression: list[RegularExpression] | core.ArrayOut[RegularExpression] = core.attr(
        RegularExpression, computed=True, kind=core.Kind.array
    )

    scope: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        scope: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsV2RegexPatternSet.Args(
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        scope: str | core.StringOut = core.arg()
