import terrascript.core as core


@core.schema
class HealthCheck(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    healthy_threshold: int | core.IntOut | None = core.attr(int, default=None)

    interval: int | core.IntOut | None = core.attr(int, default=None)

    matcher: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: str | core.StringOut | None = core.attr(str, default=None)

    protocol: str | core.StringOut | None = core.attr(str, default=None)

    timeout: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    unhealthy_threshold: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        healthy_threshold: int | core.IntOut | None = None,
        interval: int | core.IntOut | None = None,
        matcher: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
        port: str | core.StringOut | None = None,
        protocol: str | core.StringOut | None = None,
        timeout: int | core.IntOut | None = None,
        unhealthy_threshold: int | core.IntOut | None = None,
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
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        healthy_threshold: int | core.IntOut | None = core.arg(default=None)

        interval: int | core.IntOut | None = core.arg(default=None)

        matcher: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        port: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut | None = core.arg(default=None)

        timeout: int | core.IntOut | None = core.arg(default=None)

        unhealthy_threshold: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Stickiness(core.Schema):

    cookie_duration: int | core.IntOut | None = core.attr(int, default=None)

    cookie_name: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        cookie_duration: int | core.IntOut | None = None,
        cookie_name: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Stickiness.Args(
                type=type,
                cookie_duration=cookie_duration,
                cookie_name=cookie_name,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookie_duration: int | core.IntOut | None = core.arg(default=None)

        cookie_name: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_lb_target_group", namespace="aws_elb")
class LbTargetGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    arn_suffix: str | core.StringOut = core.attr(str, computed=True)

    connection_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    deregistration_delay: str | core.StringOut | None = core.attr(str, default=None)

    health_check: HealthCheck | None = core.attr(HealthCheck, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    lambda_multi_value_headers_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    load_balancing_algorithm_type: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    port: int | core.IntOut | None = core.attr(int, default=None)

    preserve_client_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    protocol: str | core.StringOut | None = core.attr(str, default=None)

    protocol_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    proxy_protocol_v2: bool | core.BoolOut | None = core.attr(bool, default=None)

    slow_start: int | core.IntOut | None = core.attr(int, default=None)

    stickiness: Stickiness | None = core.attr(Stickiness, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_type: str | core.StringOut | None = core.attr(str, default=None)

    vpc_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_termination: bool | core.BoolOut | None = None,
        deregistration_delay: str | core.StringOut | None = None,
        health_check: HealthCheck | None = None,
        ip_address_type: str | core.StringOut | None = None,
        lambda_multi_value_headers_enabled: bool | core.BoolOut | None = None,
        load_balancing_algorithm_type: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preserve_client_ip: str | core.StringOut | None = None,
        protocol: str | core.StringOut | None = None,
        protocol_version: str | core.StringOut | None = None,
        proxy_protocol_v2: bool | core.BoolOut | None = None,
        slow_start: int | core.IntOut | None = None,
        stickiness: Stickiness | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_type: str | core.StringOut | None = None,
        vpc_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbTargetGroup.Args(
                connection_termination=connection_termination,
                deregistration_delay=deregistration_delay,
                health_check=health_check,
                ip_address_type=ip_address_type,
                lambda_multi_value_headers_enabled=lambda_multi_value_headers_enabled,
                load_balancing_algorithm_type=load_balancing_algorithm_type,
                name=name,
                name_prefix=name_prefix,
                port=port,
                preserve_client_ip=preserve_client_ip,
                protocol=protocol,
                protocol_version=protocol_version,
                proxy_protocol_v2=proxy_protocol_v2,
                slow_start=slow_start,
                stickiness=stickiness,
                tags=tags,
                tags_all=tags_all,
                target_type=target_type,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_termination: bool | core.BoolOut | None = core.arg(default=None)

        deregistration_delay: str | core.StringOut | None = core.arg(default=None)

        health_check: HealthCheck | None = core.arg(default=None)

        ip_address_type: str | core.StringOut | None = core.arg(default=None)

        lambda_multi_value_headers_enabled: bool | core.BoolOut | None = core.arg(default=None)

        load_balancing_algorithm_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preserve_client_ip: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut | None = core.arg(default=None)

        protocol_version: str | core.StringOut | None = core.arg(default=None)

        proxy_protocol_v2: bool | core.BoolOut | None = core.arg(default=None)

        slow_start: int | core.IntOut | None = core.arg(default=None)

        stickiness: Stickiness | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_type: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
