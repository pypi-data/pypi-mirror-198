import terrascript.core as core


@core.resource(type="aws_ce_anomaly_monitor", namespace="aws_ce")
class AnomalyMonitor(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    monitor_dimension: str | core.StringOut | None = core.attr(str, default=None)

    monitor_specification: str | core.StringOut | None = core.attr(str, default=None)

    monitor_type: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

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
        monitor_type: str | core.StringOut,
        name: str | core.StringOut,
        monitor_dimension: str | core.StringOut | None = None,
        monitor_specification: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AnomalyMonitor.Args(
                monitor_type=monitor_type,
                name=name,
                monitor_dimension=monitor_dimension,
                monitor_specification=monitor_specification,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        monitor_dimension: str | core.StringOut | None = core.arg(default=None)

        monitor_specification: str | core.StringOut | None = core.arg(default=None)

        monitor_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
