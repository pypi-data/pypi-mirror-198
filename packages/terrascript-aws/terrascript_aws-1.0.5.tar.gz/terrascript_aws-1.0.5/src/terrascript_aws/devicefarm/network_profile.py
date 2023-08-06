import terrascript.core as core


@core.resource(type="aws_devicefarm_network_profile", namespace="devicefarm")
class NetworkProfile(core.Resource):
    """
    The Amazon Resource Name of this network profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the network profile.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The data throughput rate in bits per second, as an integer from `0` to `104857600`. Defau
    lt value is `104857600`.
    """
    downlink_bandwidth_bits: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Delay time for all packets to destination in milliseconds as an integer from `0` to `2000
    .
    """
    downlink_delay_ms: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Time variation in the delay of received packets in milliseconds as an integer from `0` to
    2000`.
    """
    downlink_jitter_ms: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Proportion of received packets that fail to arrive from `0` to `100` percent.
    """
    downlink_loss_percent: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for the network profile.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of the project for the network profile.
    """
    project_arn: str | core.StringOut = core.attr(str)

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
    (Optional) The type of network profile to create. Valid values are listed are `PRIVATE` and `CURATED
    .
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The data throughput rate in bits per second, as an integer from `0` to `104857600`. Defau
    lt value is `104857600`.
    """
    uplink_bandwidth_bits: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Delay time for all packets to destination in milliseconds as an integer from `0` to `2000
    .
    """
    uplink_delay_ms: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Time variation in the delay of received packets in milliseconds as an integer from `0` to
    2000`.
    """
    uplink_jitter_ms: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Proportion of received packets that fail to arrive from `0` to `100` percent.
    """
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
