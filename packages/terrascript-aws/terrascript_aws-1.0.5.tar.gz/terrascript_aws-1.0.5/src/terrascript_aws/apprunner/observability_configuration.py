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


@core.resource(type="aws_apprunner_observability_configuration", namespace="apprunner")
class ObservabilityConfiguration(core.Resource):
    """
    ARN of this observability configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the observability configuration has the highest `observability_configuration_revision` among
    all configurations that share the same `observability_configuration_name`.
    """
    latest: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required, Forces new resource) Name of the observability configuration.
    """
    observability_configuration_name: str | core.StringOut = core.attr(str)

    """
    The revision of this observability configuration.
    """
    observability_configuration_revision: int | core.IntOut = core.attr(int, computed=True)

    """
    The current state of the observability configuration. An INACTIVE configuration revision has been de
    leted and can't be used. It is permanently removed some time after deletion.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) The configuration of the tracing feature within this observability configuration. If you
    don't specify it, App Runner doesn't enable tracing. See [Trace Configuration](#trace-configuration)
    below for more details.
    """
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
