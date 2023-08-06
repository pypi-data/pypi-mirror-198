import terrascript.core as core


@core.schema
class Predicates(core.Schema):

    data_id: str | core.StringOut = core.attr(str)

    negated: bool | core.BoolOut = core.attr(bool)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        data_id: str | core.StringOut,
        negated: bool | core.BoolOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Predicates.Args(
                data_id=data_id,
                negated=negated,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_id: str | core.StringOut = core.arg()

        negated: bool | core.BoolOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_waf_rate_based_rule", namespace="aws_waf")
class RateBasedRule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    metric_name: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    predicates: list[Predicates] | core.ArrayOut[Predicates] | None = core.attr(
        Predicates, default=None, kind=core.Kind.array
    )

    rate_key: str | core.StringOut = core.attr(str)

    rate_limit: int | core.IntOut = core.attr(int)

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
        metric_name: str | core.StringOut,
        name: str | core.StringOut,
        rate_key: str | core.StringOut,
        rate_limit: int | core.IntOut,
        predicates: list[Predicates] | core.ArrayOut[Predicates] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RateBasedRule.Args(
                metric_name=metric_name,
                name=name,
                rate_key=rate_key,
                rate_limit=rate_limit,
                predicates=predicates,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        metric_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        predicates: list[Predicates] | core.ArrayOut[Predicates] | None = core.arg(default=None)

        rate_key: str | core.StringOut = core.arg()

        rate_limit: int | core.IntOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
