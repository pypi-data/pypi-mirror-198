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


@core.resource(type="aws_cloudwatch_metric_stream", namespace="aws_cloudwatch")
class MetricStream(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    exclude_filter: list[ExcludeFilter] | core.ArrayOut[ExcludeFilter] | None = core.attr(
        ExcludeFilter, default=None, kind=core.Kind.array
    )

    firehose_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    include_filter: list[IncludeFilter] | core.ArrayOut[IncludeFilter] | None = core.attr(
        IncludeFilter, default=None, kind=core.Kind.array
    )

    last_update_date: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    output_format: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    state: str | core.StringOut = core.attr(str, computed=True)

    statistics_configuration: list[StatisticsConfiguration] | core.ArrayOut[
        StatisticsConfiguration
    ] | None = core.attr(StatisticsConfiguration, default=None, kind=core.Kind.array)

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
