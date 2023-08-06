import terrascript.core as core


@core.schema
class IncludeMetric(core.Schema):

    metric_name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        metric_name: str | core.StringOut,
        namespace: str | core.StringOut,
    ):
        super().__init__(
            args=IncludeMetric.Args(
                metric_name=metric_name,
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()


@core.schema
class StatisticsConfiguration(core.Schema):

    additional_statistics: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    include_metric: list[IncludeMetric] | core.ArrayOut[IncludeMetric] = core.attr(
        IncludeMetric, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        additional_statistics: list[str] | core.ArrayOut[core.StringOut],
        include_metric: list[IncludeMetric] | core.ArrayOut[IncludeMetric],
    ):
        super().__init__(
            args=StatisticsConfiguration.Args(
                additional_statistics=additional_statistics,
                include_metric=include_metric,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_statistics: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        include_metric: list[IncludeMetric] | core.ArrayOut[IncludeMetric] = core.arg()


@core.schema
class IncludeFilter(core.Schema):

    namespace: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        namespace: str | core.StringOut,
    ):
        super().__init__(
            args=IncludeFilter.Args(
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        namespace: str | core.StringOut = core.arg()


@core.schema
class ExcludeFilter(core.Schema):

    namespace: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        namespace: str | core.StringOut,
    ):
        super().__init__(
            args=ExcludeFilter.Args(
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        namespace: str | core.StringOut = core.arg()


@core.resource(type="aws_cloudwatch_metric_stream", namespace="cloudwatch")
class MetricStream(core.Resource):
    """
    ARN of the metric stream.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the metric s
    tream was created.
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of exclusive metric filters. If you specify this parameter, the stream sends metrics
    from all metric namespaces except for the namespaces that you specify here. Conflicts with `include
    _filter`.
    """
    exclude_filter: list[ExcludeFilter] | core.ArrayOut[ExcludeFilter] | None = core.attr(
        ExcludeFilter, default=None, kind=core.Kind.array
    )

    """
    (Required) ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream.
    """
    firehose_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of inclusive metric filters. If you specify this parameter, the stream sends only th
    e metrics from the metric namespaces that you specify here. Conflicts with `exclude_filter`.
    """
    include_filter: list[IncludeFilter] | core.ArrayOut[IncludeFilter] | None = core.attr(
        IncludeFilter, default=None, kind=core.Kind.array
    )

    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the metric s
    tream was last updated.
    """
    last_update_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) Friendly name of the metric stream. If omitted, Terraform will assig
    n a random, unique name. Conflicts with `name_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique friendly name beginning with the specified prefix.
    Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Output format for the stream. Possible values are `json` and `opentelemetry0.7`. For more
    information about output formats, see [Metric streams output formats](https://docs.aws.amazon.com/A
    mazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html).
    """
    output_format: str | core.StringOut = core.attr(str)

    """
    (Required) ARN of the IAM role that this metric stream will use to access Amazon Kinesis Firehose re
    sources. For more information about role permissions, see [Trust between CloudWatch and Kinesis Data
    Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-
    trustpolicy.html).
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    State of the metric stream. Possible values are `running` and `stopped`.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) For each entry in this array, you specify one or more metrics and the list of additional
    statistics to stream for those metrics. The additional statistics that you can stream depend on the
    stream's `output_format`. If the OutputFormat is `json`, you can stream any additional statistic tha
    t is supported by CloudWatch, listed in [CloudWatch statistics definitions](https://docs.aws.amazon.
    com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html.html). If the OutputFormat is `op
    entelemetry0.7`, you can stream percentile statistics (p99 etc.). See details below.
    """
    statistics_configuration: list[StatisticsConfiguration] | core.ArrayOut[
        StatisticsConfiguration
    ] | None = core.attr(StatisticsConfiguration, default=None, kind=core.Kind.array)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
        firehose_arn: str | core.StringOut,
        output_format: str | core.StringOut,
        role_arn: str | core.StringOut,
        exclude_filter: list[ExcludeFilter] | core.ArrayOut[ExcludeFilter] | None = None,
        include_filter: list[IncludeFilter] | core.ArrayOut[IncludeFilter] | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        statistics_configuration: list[StatisticsConfiguration]
        | core.ArrayOut[StatisticsConfiguration]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MetricStream.Args(
                firehose_arn=firehose_arn,
                output_format=output_format,
                role_arn=role_arn,
                exclude_filter=exclude_filter,
                include_filter=include_filter,
                name=name,
                name_prefix=name_prefix,
                statistics_configuration=statistics_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        exclude_filter: list[ExcludeFilter] | core.ArrayOut[ExcludeFilter] | None = core.arg(
            default=None
        )

        firehose_arn: str | core.StringOut = core.arg()

        include_filter: list[IncludeFilter] | core.ArrayOut[IncludeFilter] | None = core.arg(
            default=None
        )

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        output_format: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        statistics_configuration: list[StatisticsConfiguration] | core.ArrayOut[
            StatisticsConfiguration
        ] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
