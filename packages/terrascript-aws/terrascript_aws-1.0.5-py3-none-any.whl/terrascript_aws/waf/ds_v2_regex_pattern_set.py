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


@core.data(type="aws_wafv2_regex_pattern_set", namespace="waf")
class DsV2RegexPatternSet(core.Data):
    """
    The Amazon Resource Name (ARN) of the entity.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the set that helps with identification.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier for the set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the WAFv2 Regex Pattern Set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    One or more blocks of regular expression patterns that AWS WAF is searching for. See [Regular Expres
    sion](#regular-expression) below for details.
    """
    regular_expression: list[RegularExpression] | core.ArrayOut[RegularExpression] = core.attr(
        RegularExpression, computed=True, kind=core.Kind.array
    )

    """
    (Required) Specifies whether this is for an AWS CloudFront distribution or for a regional applicatio
    n. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the r
    egion `us-east-1` (N. Virginia) on the AWS provider.
    """
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
