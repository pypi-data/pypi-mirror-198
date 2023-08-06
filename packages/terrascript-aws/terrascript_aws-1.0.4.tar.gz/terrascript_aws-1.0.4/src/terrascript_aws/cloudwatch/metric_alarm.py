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


@core.resource(type="aws_cloudwatch_metric_alarm", namespace="cloudwatch")
class MetricAlarm(core.Resource):
    """
    (Optional) Indicates whether or not actions should be executed during any changes to the alarm's sta
    te. Defaults to `true`.
    """

    actions_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The list of actions to execute when this alarm transitions into an ALARM state from any o
    ther state. Each action is specified as an Amazon Resource Name (ARN).
    """
    alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The description for the alarm.
    """
    alarm_description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The descriptive name for the alarm. This name must be unique within the user's AWS accoun
    t
    """
    alarm_name: str | core.StringOut = core.attr(str)

    """
    The ARN of the CloudWatch Metric Alarm.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The arithmetic operation to use when comparing the specified Statistic and Threshold. The
    specified Statistic value is used as the first operand. Either of the following is supported: `Grea
    terThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold
    . Additionally, the values  `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, a
    nd `GreaterThanUpperThreshold` are used only for alarms based on anomaly detection models.
    """
    comparison_operator: str | core.StringOut = core.attr(str)

    """
    (Optional) The number of datapoints that must be breaching to trigger the alarm.
    """
    datapoints_to_alarm: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The dimensions for the alarm's associated metric.  For the list of available dimensions s
    ee the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW
    _Support_For_AWS.html).
    """
    dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Used only for alarms
    """
    evaluate_low_sample_count_percentiles: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) The number of periods over which data is compared to the specified threshold.
    """
    evaluation_periods: int | core.IntOut = core.attr(int)

    """
    (Optional) The percentile statistic for the metric associated with the alarm. Specify a value betwee
    n p0.0 and p100.
    """
    extended_statistic: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A short name used to tie this object to the results in the response. If you are performin
    g math expressions on this set of data, this name represents that data and can serve as a variable i
    n the mathematical expression. The valid characters are letters, numbers, and underscore. The first
    character must be a lowercase letter.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA stat
    e from any other state. Each action is specified as an Amazon Resource Name (ARN).
    """
    insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The name for the alarm's associated metric.
    """
    metric_name: str | core.StringOut | None = core.attr(str, default=None)

    metric_query: list[MetricQuery] | core.ArrayOut[MetricQuery] | None = core.attr(
        MetricQuery, default=None, kind=core.Kind.array
    )

    """
    (Optional) The namespace for the alarm's associated metric. See docs for the [list of namespaces](ht
    tps://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
    """
    namespace: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The list of actions to execute when this alarm transitions into an OK state from any othe
    r state. Each action is specified as an Amazon Resource Name (ARN).
    """
    ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The period in seconds over which the specified `statistic` is applied.
    """
    period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The statistic to apply to the alarm's associated metric.
    """
    statistic: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    """
    (Optional) The value against which the specified statistic is compared. This parameter is required f
    or alarms based on static thresholds, but should not be used for alarms based on anomaly detection m
    odels.
    """
    threshold: float | core.FloatOut | None = core.attr(float, default=None)

    """
    (Optional) If this is an alarm based on an anomaly detection model, make this value match the ID of
    the ANOMALY_DETECTION_BAND function.
    """
    threshold_metric_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Sets how this alarm is to handle missing data points. The following values are supported:
    missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.
    """
    treat_missing_data: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The unit for the alarm's associated metric.
    """
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
