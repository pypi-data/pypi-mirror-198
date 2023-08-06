import terrascript.core as core


@core.schema
class Criterion(core.Schema):

    eq: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    eq_exact_match: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    field: str | core.StringOut = core.attr(str)

    gt: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lt: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    neq: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field: str | core.StringOut,
        eq: list[str] | core.ArrayOut[core.StringOut] | None = None,
        eq_exact_match: list[str] | core.ArrayOut[core.StringOut] | None = None,
        gt: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lt: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
        neq: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Criterion.Args(
                field=field,
                eq=eq,
                eq_exact_match=eq_exact_match,
                gt=gt,
                gte=gte,
                lt=lt,
                lte=lte,
                neq=neq,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        eq_exact_match: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        field: str | core.StringOut = core.arg()

        gt: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lt: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)

        neq: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class FindingCriteria(core.Schema):

    criterion: list[Criterion] | core.ArrayOut[Criterion] | None = core.attr(
        Criterion, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        criterion: list[Criterion] | core.ArrayOut[Criterion] | None = None,
    ):
        super().__init__(
            args=FindingCriteria.Args(
                criterion=criterion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        criterion: list[Criterion] | core.ArrayOut[Criterion] | None = core.arg(default=None)


@core.resource(type="aws_macie2_findings_filter", namespace="macie2")
class FindingsFilter(core.Resource):
    """
    (Required) The action to perform on findings that meet the filter criteria (`finding_criteria`). Val
    id values are: `ARCHIVE`, suppress (automatically archive) the findings; and, `NOOP`, don't perform
    any action on the findings.
    """

    action: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the Findings Filter.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A custom description of the filter. The description can contain as many as 512 characters
    .
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The criteria to use to filter findings.
    """
    finding_criteria: FindingCriteria = core.attr(FindingCriteria)

    """
    The unique identifier (ID) of the macie Findings Filter.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A custom name for the filter. The name must contain at least 3 characters and can contain
    as many as 64 characters. If omitted, Terraform will assign a random, unique name. Conflicts with `
    name_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The position of the filter in the list of saved filters on the Amazon Macie console. This
    value also determines the order in which the filter is applied to findings, relative to other filte
    rs that are also applied to the findings.
    """
    position: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) A map of key-value pairs that specifies the tags to associate with the filter.
    """
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
        action: str | core.StringOut,
        finding_criteria: FindingCriteria,
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        position: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FindingsFilter.Args(
                action=action,
                finding_criteria=finding_criteria,
                description=description,
                name=name,
                name_prefix=name_prefix,
                position=position,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        finding_criteria: FindingCriteria = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        position: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
