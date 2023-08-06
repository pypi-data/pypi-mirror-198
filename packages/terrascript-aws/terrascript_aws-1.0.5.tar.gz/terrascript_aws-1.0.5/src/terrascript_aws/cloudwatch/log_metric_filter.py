import terrascript.core as core


@core.schema
class MetricTransformation(core.Schema):

    default_value: str | core.StringOut | None = core.attr(str, default=None)

    dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut = core.attr(str)

    unit: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        namespace: str | core.StringOut,
        value: str | core.StringOut,
        default_value: str | core.StringOut | None = None,
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MetricTransformation.Args(
                name=name,
                namespace=namespace,
                value=value,
                default_value=default_value,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_value: str | core.StringOut | None = core.arg(default=None)

        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()

        unit: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_cloudwatch_log_metric_filter", namespace="cloudwatch")
class LogMetricFilter(core.Resource):
    """
    The name of the metric filter.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the log group to associate the metric filter with.
    """
    log_group_name: str | core.StringOut = core.attr(str)

    """
    (Required) A block defining collection of information needed to define how metric data gets emitted.
    See below.
    """
    metric_transformation: MetricTransformation = core.attr(MetricTransformation)

    """
    (Required) A name for the metric filter.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/lat
    est/DeveloperGuide/FilterAndPatternSyntax.html)
    """
    pattern: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        log_group_name: str | core.StringOut,
        metric_transformation: MetricTransformation,
        name: str | core.StringOut,
        pattern: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogMetricFilter.Args(
                log_group_name=log_group_name,
                metric_transformation=metric_transformation,
                name=name,
                pattern=pattern,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_group_name: str | core.StringOut = core.arg()

        metric_transformation: MetricTransformation = core.arg()

        name: str | core.StringOut = core.arg()

        pattern: str | core.StringOut = core.arg()
