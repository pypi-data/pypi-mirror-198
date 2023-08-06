import terrascript.core as core


@core.schema
class HealthCheck(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    healthy_threshold: int | core.IntOut = core.attr(int, computed=True)

    interval: int | core.IntOut = core.attr(int, computed=True)

    matcher: str | core.StringOut = core.attr(str, computed=True)

    path: str | core.StringOut = core.attr(str, computed=True)

    port: str | core.StringOut = core.attr(str, computed=True)

    protocol: str | core.StringOut = core.attr(str, computed=True)

    timeout: int | core.IntOut = core.attr(int, computed=True)

    unhealthy_threshold: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        healthy_threshold: int | core.IntOut,
        interval: int | core.IntOut,
        matcher: str | core.StringOut,
        path: str | core.StringOut,
        port: str | core.StringOut,
        protocol: str | core.StringOut,
        timeout: int | core.IntOut,
        unhealthy_threshold: int | core.IntOut,
    ):
        super().__init__(
            args=HealthCheck.Args(
                enabled=enabled,
                healthy_threshold=healthy_threshold,
                interval=interval,
                matcher=matcher,
                path=path,
                port=port,
                protocol=protocol,
                timeout=timeout,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        healthy_threshold: int | core.IntOut = core.arg()

        interval: int | core.IntOut = core.arg()

        matcher: str | core.StringOut = core.arg()

        path: str | core.StringOut = core.arg()

        port: str | core.StringOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        timeout: int | core.IntOut = core.arg()

        unhealthy_threshold: int | core.IntOut = core.arg()


@core.schema
class Stickiness(core.Schema):

    cookie_duration: int | core.IntOut = core.attr(int, computed=True)

    cookie_name: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cookie_duration: int | core.IntOut,
        cookie_name: str | core.StringOut,
        enabled: bool | core.BoolOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Stickiness.Args(
                cookie_duration=cookie_duration,
                cookie_name=cookie_name,
                enabled=enabled,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookie_duration: int | core.IntOut = core.arg()

        cookie_name: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.data(type="aws_lb_target_group", namespace="elb")
class DsLbTargetGroup(core.Data):
    """
    (Optional) The full ARN of the target group.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn_suffix: str | core.StringOut = core.attr(str, computed=True)

    connection_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    deregistration_delay: int | core.IntOut = core.attr(int, computed=True)

    health_check: list[HealthCheck] | core.ArrayOut[HealthCheck] = core.attr(
        HealthCheck, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    lambda_multi_value_headers_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    load_balancing_algorithm_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The unique name of the target group.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    preserve_client_ip: str | core.StringOut = core.attr(str, computed=True)

    protocol: str | core.StringOut = core.attr(str, computed=True)

    protocol_version: str | core.StringOut = core.attr(str, computed=True)

    proxy_protocol_v2: bool | core.BoolOut = core.attr(bool, computed=True)

    slow_start: int | core.IntOut = core.attr(int, computed=True)

    stickiness: list[Stickiness] | core.ArrayOut[Stickiness] = core.attr(
        Stickiness, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_type: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLbTargetGroup.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
