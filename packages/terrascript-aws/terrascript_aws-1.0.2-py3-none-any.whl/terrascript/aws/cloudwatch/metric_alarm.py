import terrascript.core as core


@core.schema
class Metric(core.Schema):

    dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    metric_name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut | None = core.attr(str, default=None)

    period: int | core.IntOut = core.attr(int)

    stat: str | core.StringOut = core.attr(str)

    unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_name: str | core.StringOut,
        period: int | core.IntOut,
        stat: str | core.StringOut,
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        namespace: str | core.StringOut | None = None,
        unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Metric.Args(
                metric_name=metric_name,
                period=period,
                stat=stat,
                dimensions=dimensions,
                namespace=namespace,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        metric_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut | None = core.arg(default=None)

        period: int | core.IntOut = core.arg()

        stat: str | core.StringOut = core.arg()

        unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MetricQuery(core.Schema):

    account_id: str | core.StringOut | None = core.attr(str, default=None)

    expression: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str)

    label: str | core.StringOut | None = core.attr(str, default=None)

    metric: Metric | None = core.attr(Metric, default=None)

    return_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        expression: str | core.StringOut | None = None,
        label: str | core.StringOut | None = None,
        metric: Metric | None = None,
        return_data: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=MetricQuery.Args(
                id=id,
                account_id=account_id,
                expression=expression,
                label=label,
                metric=metric,
                return_data=return_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut | None = core.arg(default=None)

        expression: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        label: str | core.StringOut | None = core.arg(default=None)

        metric: Metric | None = core.arg(default=None)

        return_data: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_cloudwatch_metric_alarm", namespace="aws_cloudwatch")
class MetricAlarm(core.Resource):

    actions_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    alarm_description: str | core.StringOut | None = core.attr(str, default=None)

    alarm_name: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    comparison_operator: str | core.StringOut = core.attr(str)

    datapoints_to_alarm: int | core.IntOut | None = core.attr(int, default=None)

    dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    evaluate_low_sample_count_percentiles: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    evaluation_periods: int | core.IntOut = core.attr(int)

    extended_statistic: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    metric_name: str | core.StringOut | None = core.attr(str, default=None)

    metric_query: list[MetricQuery] | core.ArrayOut[MetricQuery] | None = core.attr(
        MetricQuery, default=None, kind=core.Kind.array
    )

    namespace: str | core.StringOut | None = core.attr(str, default=None)

    ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    period: int | core.IntOut | None = core.attr(int, default=None)

    statistic: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    threshold: float | core.FloatOut | None = core.attr(float, default=None)

    threshold_metric_id: str | core.StringOut | None = core.attr(str, default=None)

    treat_missing_data: str | core.StringOut | None = core.attr(str, default=None)

    unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        alarm_name: str | core.StringOut,
        comparison_operator: str | core.StringOut,
        evaluation_periods: int | core.IntOut,
        actions_enabled: bool | core.BoolOut | None = None,
        alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        alarm_description: str | core.StringOut | None = None,
        datapoints_to_alarm: int | core.IntOut | None = None,
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        evaluate_low_sample_count_percentiles: str | core.StringOut | None = None,
        extended_statistic: str | core.StringOut | None = None,
        insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        metric_name: str | core.StringOut | None = None,
        metric_query: list[MetricQuery] | core.ArrayOut[MetricQuery] | None = None,
        namespace: str | core.StringOut | None = None,
        ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        period: int | core.IntOut | None = None,
        statistic: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        threshold: float | core.FloatOut | None = None,
        threshold_metric_id: str | core.StringOut | None = None,
        treat_missing_data: str | core.StringOut | None = None,
        unit: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MetricAlarm.Args(
                alarm_name=alarm_name,
                comparison_operator=comparison_operator,
                evaluation_periods=evaluation_periods,
                actions_enabled=actions_enabled,
                alarm_actions=alarm_actions,
                alarm_description=alarm_description,
                datapoints_to_alarm=datapoints_to_alarm,
                dimensions=dimensions,
                evaluate_low_sample_count_percentiles=evaluate_low_sample_count_percentiles,
                extended_statistic=extended_statistic,
                insufficient_data_actions=insufficient_data_actions,
                metric_name=metric_name,
                metric_query=metric_query,
                namespace=namespace,
                ok_actions=ok_actions,
                period=period,
                statistic=statistic,
                tags=tags,
                tags_all=tags_all,
                threshold=threshold,
                threshold_metric_id=threshold_metric_id,
                treat_missing_data=treat_missing_data,
                unit=unit,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions_enabled: bool | core.BoolOut | None = core.arg(default=None)

        alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        alarm_description: str | core.StringOut | None = core.arg(default=None)

        alarm_name: str | core.StringOut = core.arg()

        comparison_operator: str | core.StringOut = core.arg()

        datapoints_to_alarm: int | core.IntOut | None = core.arg(default=None)

        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        evaluate_low_sample_count_percentiles: str | core.StringOut | None = core.arg(default=None)

        evaluation_periods: int | core.IntOut = core.arg()

        extended_statistic: str | core.StringOut | None = core.arg(default=None)

        insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        metric_name: str | core.StringOut | None = core.arg(default=None)

        metric_query: list[MetricQuery] | core.ArrayOut[MetricQuery] | None = core.arg(default=None)

        namespace: str | core.StringOut | None = core.arg(default=None)

        ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        period: int | core.IntOut | None = core.arg(default=None)

        statistic: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        threshold: float | core.FloatOut | None = core.arg(default=None)

        threshold_metric_id: str | core.StringOut | None = core.arg(default=None)

        treat_missing_data: str | core.StringOut | None = core.arg(default=None)

        unit: str | core.StringOut | None = core.arg(default=None)
