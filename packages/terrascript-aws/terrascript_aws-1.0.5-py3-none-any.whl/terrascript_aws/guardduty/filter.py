import terrascript.core as core


@core.schema
class Criterion(core.Schema):

    equals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    field: str | core.StringOut = core.attr(str)

    greater_than: str | core.StringOut | None = core.attr(str, default=None)

    greater_than_or_equal: str | core.StringOut | None = core.attr(str, default=None)

    less_than: str | core.StringOut | None = core.attr(str, default=None)

    less_than_or_equal: str | core.StringOut | None = core.attr(str, default=None)

    not_equals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field: str | core.StringOut,
        equals: list[str] | core.ArrayOut[core.StringOut] | None = None,
        greater_than: str | core.StringOut | None = None,
        greater_than_or_equal: str | core.StringOut | None = None,
        less_than: str | core.StringOut | None = None,
        less_than_or_equal: str | core.StringOut | None = None,
        not_equals: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Criterion.Args(
                field=field,
                equals=equals,
                greater_than=greater_than,
                greater_than_or_equal=greater_than_or_equal,
                less_than=less_than,
                less_than_or_equal=less_than_or_equal,
                not_equals=not_equals,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        equals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        field: str | core.StringOut = core.arg()

        greater_than: str | core.StringOut | None = core.arg(default=None)

        greater_than_or_equal: str | core.StringOut | None = core.arg(default=None)

        less_than: str | core.StringOut | None = core.arg(default=None)

        less_than_or_equal: str | core.StringOut | None = core.arg(default=None)

        not_equals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class FindingCriteria(core.Schema):

    criterion: list[Criterion] | core.ArrayOut[Criterion] = core.attr(
        Criterion, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        criterion: list[Criterion] | core.ArrayOut[Criterion],
    ):
        super().__init__(
            args=FindingCriteria.Args(
                criterion=criterion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        criterion: list[Criterion] | core.ArrayOut[Criterion] = core.arg()


@core.resource(type="aws_guardduty_filter", namespace="guardduty")
class Filter(core.Resource):
    """
    (Required) Specifies the action that is to be applied to the findings that match the filter. Can be
    one of `ARCHIVE` or `NOOP`.
    """

    action: str | core.StringOut = core.attr(str)

    """
    The ARN of the GuardDuty filter.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the filter.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) ID of a GuardDuty detector, attached to your account.
    """
    detector_id: str | core.StringOut = core.attr(str)

    finding_criteria: FindingCriteria = core.attr(FindingCriteria)

    """
    A compound field, consisting of the ID of the GuardDuty detector and the name of the filter.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of your filter.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the position of the filter in the list of current filters. Also specifies the o
    rder in which this filter is applied to the findings.
    """
    rank: int | core.IntOut = core.attr(int)

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
        action: str | core.StringOut,
        detector_id: str | core.StringOut,
        finding_criteria: FindingCriteria,
        name: str | core.StringOut,
        rank: int | core.IntOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Filter.Args(
                action=action,
                detector_id=detector_id,
                finding_criteria=finding_criteria,
                name=name,
                rank=rank,
                description=description,
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

        detector_id: str | core.StringOut = core.arg()

        finding_criteria: FindingCriteria = core.arg()

        name: str | core.StringOut = core.arg()

        rank: int | core.IntOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
