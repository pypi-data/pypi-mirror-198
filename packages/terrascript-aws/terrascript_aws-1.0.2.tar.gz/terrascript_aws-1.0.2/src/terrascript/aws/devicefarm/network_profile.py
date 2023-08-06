import terrascript.core as core


@core.resource(type="aws_devicefarm_network_profile", namespace="aws_devicefarm")
class NetworkProfile(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    downlink_bandwidth_bits: int | core.IntOut | None = core.attr(int, default=None)

    downlink_delay_ms: int | core.IntOut | None = core.attr(int, default=None)

    downlink_jitter_ms: int | core.IntOut | None = core.attr(int, default=None)

    downlink_loss_percent: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    project_arn: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    uplink_bandwidth_bits: int | core.IntOut | None = core.attr(int, default=None)

    uplink_delay_ms: int | core.IntOut | None = core.attr(int, default=None)

    uplink_jitter_ms: int | core.IntOut | None = core.attr(int, default=None)

    uplink_loss_percent: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        project_arn: str | core.StringOut,
        description: str | core.StringOut | None = None,
        downlink_bandwidth_bits: int | core.IntOut | None = None,
        downlink_delay_ms: int | core.IntOut | None = None,
        downlink_jitter_ms: int | core.IntOut | None = None,
        downlink_loss_percent: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        uplink_bandwidth_bits: int | core.IntOut | None = None,
        uplink_delay_ms: int | core.IntOut | None = None,
        uplink_jitter_ms: int | core.IntOut | None = None,
        uplink_loss_percent: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkProfile.Args(
                name=name,
                project_arn=project_arn,
                description=description,
                downlink_bandwidth_bits=downlink_bandwidth_bits,
                downlink_delay_ms=downlink_delay_ms,
                downlink_jitter_ms=downlink_jitter_ms,
                downlink_loss_percent=downlink_loss_percent,
                tags=tags,
                tags_all=tags_all,
                type=type,
                uplink_bandwidth_bits=uplink_bandwidth_bits,
                uplink_delay_ms=uplink_delay_ms,
                uplink_jitter_ms=uplink_jitter_ms,
                uplink_loss_percent=uplink_loss_percent,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        downlink_bandwidth_bits: int | core.IntOut | None = core.arg(default=None)

        downlink_delay_ms: int | core.IntOut | None = core.arg(default=None)

        downlink_jitter_ms: int | core.IntOut | None = core.arg(default=None)

        downlink_loss_percent: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        project_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        uplink_bandwidth_bits: int | core.IntOut | None = core.arg(default=None)

        uplink_delay_ms: int | core.IntOut | None = core.arg(default=None)

        uplink_jitter_ms: int | core.IntOut | None = core.arg(default=None)

        uplink_loss_percent: int | core.IntOut | None = core.arg(default=None)
