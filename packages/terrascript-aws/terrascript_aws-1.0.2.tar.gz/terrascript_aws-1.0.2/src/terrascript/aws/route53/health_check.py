import terrascript.core as core


@core.resource(type="aws_route53_health_check", namespace="aws_route53")
class HealthCheck(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    child_health_threshold: int | core.IntOut | None = core.attr(int, default=None)

    child_healthchecks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cloudwatch_alarm_name: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatch_alarm_region: str | core.StringOut | None = core.attr(str, default=None)

    disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_sni: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    failure_threshold: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    fqdn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    insufficient_data_health_status: str | core.StringOut | None = core.attr(str, default=None)

    invert_healthcheck: bool | core.BoolOut | None = core.attr(bool, default=None)

    ip_address: str | core.StringOut | None = core.attr(str, default=None)

    measure_latency: bool | core.BoolOut | None = core.attr(bool, default=None)

    port: int | core.IntOut | None = core.attr(int, default=None)

    reference_name: str | core.StringOut | None = core.attr(str, default=None)

    regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    request_interval: int | core.IntOut | None = core.attr(int, default=None)

    resource_path: str | core.StringOut | None = core.attr(str, default=None)

    routing_control_arn: str | core.StringOut | None = core.attr(str, default=None)

    search_string: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        type: str | core.StringOut,
        child_health_threshold: int | core.IntOut | None = None,
        child_healthchecks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        cloudwatch_alarm_name: str | core.StringOut | None = None,
        cloudwatch_alarm_region: str | core.StringOut | None = None,
        disabled: bool | core.BoolOut | None = None,
        enable_sni: bool | core.BoolOut | None = None,
        failure_threshold: int | core.IntOut | None = None,
        fqdn: str | core.StringOut | None = None,
        insufficient_data_health_status: str | core.StringOut | None = None,
        invert_healthcheck: bool | core.BoolOut | None = None,
        ip_address: str | core.StringOut | None = None,
        measure_latency: bool | core.BoolOut | None = None,
        port: int | core.IntOut | None = None,
        reference_name: str | core.StringOut | None = None,
        regions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        request_interval: int | core.IntOut | None = None,
        resource_path: str | core.StringOut | None = None,
        routing_control_arn: str | core.StringOut | None = None,
        search_string: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=HealthCheck.Args(
                type=type,
                child_health_threshold=child_health_threshold,
                child_healthchecks=child_healthchecks,
                cloudwatch_alarm_name=cloudwatch_alarm_name,
                cloudwatch_alarm_region=cloudwatch_alarm_region,
                disabled=disabled,
                enable_sni=enable_sni,
                failure_threshold=failure_threshold,
                fqdn=fqdn,
                insufficient_data_health_status=insufficient_data_health_status,
                invert_healthcheck=invert_healthcheck,
                ip_address=ip_address,
                measure_latency=measure_latency,
                port=port,
                reference_name=reference_name,
                regions=regions,
                request_interval=request_interval,
                resource_path=resource_path,
                routing_control_arn=routing_control_arn,
                search_string=search_string,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        child_health_threshold: int | core.IntOut | None = core.arg(default=None)

        child_healthchecks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        cloudwatch_alarm_name: str | core.StringOut | None = core.arg(default=None)

        cloudwatch_alarm_region: str | core.StringOut | None = core.arg(default=None)

        disabled: bool | core.BoolOut | None = core.arg(default=None)

        enable_sni: bool | core.BoolOut | None = core.arg(default=None)

        failure_threshold: int | core.IntOut | None = core.arg(default=None)

        fqdn: str | core.StringOut | None = core.arg(default=None)

        insufficient_data_health_status: str | core.StringOut | None = core.arg(default=None)

        invert_healthcheck: bool | core.BoolOut | None = core.arg(default=None)

        ip_address: str | core.StringOut | None = core.arg(default=None)

        measure_latency: bool | core.BoolOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        reference_name: str | core.StringOut | None = core.arg(default=None)

        regions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        request_interval: int | core.IntOut | None = core.arg(default=None)

        resource_path: str | core.StringOut | None = core.arg(default=None)

        routing_control_arn: str | core.StringOut | None = core.arg(default=None)

        search_string: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
