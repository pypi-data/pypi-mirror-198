import terrascript.core as core


@core.schema
class Filter(core.Schema):

    contains: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    criteria: str | core.StringOut = core.attr(str)

    eq: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    exists: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    neq: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        criteria: str | core.StringOut,
        contains: list[str] | core.ArrayOut[core.StringOut] | None = None,
        eq: list[str] | core.ArrayOut[core.StringOut] | None = None,
        exists: str | core.StringOut | None = None,
        neq: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                criteria=criteria,
                contains=contains,
                eq=eq,
                exists=exists,
                neq=neq,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contains: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        criteria: str | core.StringOut = core.arg()

        eq: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        exists: str | core.StringOut | None = core.arg(default=None)

        neq: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_accessanalyzer_archive_rule", namespace="accessanalyzer")
class ArchiveRule(core.Resource):
    """
    (Required) Analyzer name.
    """

    analyzer_name: str | core.StringOut = core.attr(str)

    """
    (Required) The filter criteria for the archive rule. See [Filter](#filter) for more details.
    """
    filter: list[Filter] | core.ArrayOut[Filter] = core.attr(Filter, kind=core.Kind.array)

    """
    Resource ID in the format: `analyzer_name/rule_name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Rule name.
    """
    rule_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        analyzer_name: str | core.StringOut,
        filter: list[Filter] | core.ArrayOut[Filter],
        rule_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ArchiveRule.Args(
                analyzer_name=analyzer_name,
                filter=filter,
                rule_name=rule_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        analyzer_name: str | core.StringOut = core.arg()

        filter: list[Filter] | core.ArrayOut[Filter] = core.arg()

        rule_name: str | core.StringOut = core.arg()
