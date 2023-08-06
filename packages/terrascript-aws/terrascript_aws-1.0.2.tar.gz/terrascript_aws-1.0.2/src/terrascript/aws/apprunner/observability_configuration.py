import terrascript.core as core


@core.schema
class TraceConfiguration(core.Schema):

    vendor: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        vendor: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TraceConfiguration.Args(
                vendor=vendor,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vendor: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_apprunner_observability_configuration", namespace="aws_apprunner")
class ObservabilityConfiguration(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    latest: bool | core.BoolOut = core.attr(bool, computed=True)

    observability_configuration_name: str | core.StringOut = core.attr(str)

    observability_configuration_revision: int | core.IntOut = core.attr(int, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    trace_configuration: TraceConfiguration | None = core.attr(TraceConfiguration, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        observability_configuration_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        trace_configuration: TraceConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ObservabilityConfiguration.Args(
                observability_configuration_name=observability_configuration_name,
                tags=tags,
                tags_all=tags_all,
                trace_configuration=trace_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        observability_configuration_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        trace_configuration: TraceConfiguration | None = core.arg(default=None)
