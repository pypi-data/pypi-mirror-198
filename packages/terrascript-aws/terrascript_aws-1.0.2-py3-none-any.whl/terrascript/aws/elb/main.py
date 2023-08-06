import terrascript.core as core


@core.schema
class AccessLogs(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    interval: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        bucket_prefix: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        interval: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AccessLogs.Args(
                bucket=bucket,
                bucket_prefix=bucket_prefix,
                enabled=enabled,
                interval=interval,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        interval: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Listener(core.Schema):

    instance_port: int | core.IntOut = core.attr(int)

    instance_protocol: str | core.StringOut = core.attr(str)

    lb_port: int | core.IntOut = core.attr(int)

    lb_protocol: str | core.StringOut = core.attr(str)

    ssl_certificate_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_port: int | core.IntOut,
        instance_protocol: str | core.StringOut,
        lb_port: int | core.IntOut,
        lb_protocol: str | core.StringOut,
        ssl_certificate_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Listener.Args(
                instance_port=instance_port,
                instance_protocol=instance_protocol,
                lb_port=lb_port,
                lb_protocol=lb_protocol,
                ssl_certificate_id=ssl_certificate_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_port: int | core.IntOut = core.arg()

        instance_protocol: str | core.StringOut = core.arg()

        lb_port: int | core.IntOut = core.arg()

        lb_protocol: str | core.StringOut = core.arg()

        ssl_certificate_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: int | core.IntOut = core.attr(int)

    interval: int | core.IntOut = core.attr(int)

    target: str | core.StringOut = core.attr(str)

    timeout: int | core.IntOut = core.attr(int)

    unhealthy_threshold: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        healthy_threshold: int | core.IntOut,
        interval: int | core.IntOut,
        target: str | core.StringOut,
        timeout: int | core.IntOut,
        unhealthy_threshold: int | core.IntOut,
    ):
        super().__init__(
            args=HealthCheck.Args(
                healthy_threshold=healthy_threshold,
                interval=interval,
                target=target,
                timeout=timeout,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: int | core.IntOut = core.arg()

        interval: int | core.IntOut = core.arg()

        target: str | core.StringOut = core.arg()

        timeout: int | core.IntOut = core.arg()

        unhealthy_threshold: int | core.IntOut = core.arg()


@core.resource(type="aws_elb", namespace="aws_elb")
class Main(core.Resource):

    access_logs: AccessLogs | None = core.attr(AccessLogs, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    connection_draining: bool | core.BoolOut | None = core.attr(bool, default=None)

    connection_draining_timeout: int | core.IntOut | None = core.attr(int, default=None)

    cross_zone_load_balancing: bool | core.BoolOut | None = core.attr(bool, default=None)

    desync_mitigation_mode: str | core.StringOut | None = core.attr(str, default=None)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    health_check: HealthCheck | None = core.attr(HealthCheck, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_timeout: int | core.IntOut | None = core.attr(int, default=None)

    instances: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    internal: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    listener: list[Listener] | core.ArrayOut[Listener] = core.attr(Listener, kind=core.Kind.array)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    source_security_group: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    source_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        listener: list[Listener] | core.ArrayOut[Listener],
        access_logs: AccessLogs | None = None,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        connection_draining: bool | core.BoolOut | None = None,
        connection_draining_timeout: int | core.IntOut | None = None,
        cross_zone_load_balancing: bool | core.BoolOut | None = None,
        desync_mitigation_mode: str | core.StringOut | None = None,
        health_check: HealthCheck | None = None,
        idle_timeout: int | core.IntOut | None = None,
        instances: list[str] | core.ArrayOut[core.StringOut] | None = None,
        internal: bool | core.BoolOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        source_security_group: str | core.StringOut | None = None,
        subnets: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                listener=listener,
                access_logs=access_logs,
                availability_zones=availability_zones,
                connection_draining=connection_draining,
                connection_draining_timeout=connection_draining_timeout,
                cross_zone_load_balancing=cross_zone_load_balancing,
                desync_mitigation_mode=desync_mitigation_mode,
                health_check=health_check,
                idle_timeout=idle_timeout,
                instances=instances,
                internal=internal,
                name=name,
                name_prefix=name_prefix,
                security_groups=security_groups,
                source_security_group=source_security_group,
                subnets=subnets,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_logs: AccessLogs | None = core.arg(default=None)

        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        connection_draining: bool | core.BoolOut | None = core.arg(default=None)

        connection_draining_timeout: int | core.IntOut | None = core.arg(default=None)

        cross_zone_load_balancing: bool | core.BoolOut | None = core.arg(default=None)

        desync_mitigation_mode: str | core.StringOut | None = core.arg(default=None)

        health_check: HealthCheck | None = core.arg(default=None)

        idle_timeout: int | core.IntOut | None = core.arg(default=None)

        instances: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        internal: bool | core.BoolOut | None = core.arg(default=None)

        listener: list[Listener] | core.ArrayOut[Listener] = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        source_security_group: str | core.StringOut | None = core.arg(default=None)

        subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
