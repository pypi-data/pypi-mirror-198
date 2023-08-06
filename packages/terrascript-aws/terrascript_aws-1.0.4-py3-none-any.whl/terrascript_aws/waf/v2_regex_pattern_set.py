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


@core.resource(type="aws_wafv2_regex_pattern_set", namespace="waf")
class V2RegexPatternSet(core.Resource):
    """
    The Amazon Resource Name (ARN) that identifies the cluster.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A friendly description of the regular expression pattern set.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    A unique identifier for the set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    lock_token: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A friendly name of the regular expression pattern set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) One or more blocks of regular expression patterns that you want AWS WAF to search for, su
    ch as `B[a@]dB[o0]t`. See [Regular Expression](#regular-expression) below for details.
    """
    regular_expression: list[RegularExpression] | core.ArrayOut[
        RegularExpression
    ] | None = core.attr(RegularExpression, default=None, kind=core.Kind.array)

    """
    (Required) Specifies whether this is for an AWS CloudFront distribution or for a regional applicatio
    n. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the r
    egion `us-east-1` (N. Virginia) on the AWS provider.
    """
    scope: str | core.StringOut = core.attr(str)

    """
    (Optional) An array of key:value pairs to associate with the resource. If configured with a provider
    [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/d
    ocs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
    at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
