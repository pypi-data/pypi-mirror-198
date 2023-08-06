import terrascript.core as core


@core.resource(type="aws_wafregional_regex_pattern_set", namespace="wafregional")
class RegexPatternSet(core.Resource):
    """
    The ID of the WAF Regional Regex Pattern Set.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or description of the Regex Pattern Set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of regular expression (regex) patterns that you want AWS WAF to search for, such a
    s `B[a@]dB[o0]t`.
    """
    regex_pattern_strings: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        regex_pattern_strings: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegexPatternSet.Args(
                name=name,
                regex_pattern_strings=regex_pattern_strings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        regex_pattern_strings: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
