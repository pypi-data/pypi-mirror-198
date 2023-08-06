import terrascript.core as core


@core.schema
class Listener(core.Schema):

    instance_port: int | core.IntOut = core.attr(int, computed=True)

    instance_protocol: str | core.StringOut = core.attr(str, computed=True)

    lb_port: int | core.IntOut = core.attr(int, computed=True)

    lb_protocol: str | core.StringOut = core.attr(str, computed=True)

    ssl_certificate_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        instance_port: int | core.IntOut,
        instance_protocol: str | core.StringOut,
        lb_port: int | core.IntOut,
        lb_protocol: str | core.StringOut,
        ssl_certificate_id: str | core.StringOut,
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

        ssl_certificate_id: str | core.StringOut = core.arg()


@core.schema
class AccessLogs(core.Schema):

    bucket: str | core.StringOut = core.attr(str, computed=True)

    bucket_prefix: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    interval: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        bucket_prefix: str | core.StringOut,
        enabled: bool | core.BoolOut,
        interval: int | core.IntOut,
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

        bucket_prefix: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut = core.arg()

        interval: int | core.IntOut = core.arg()


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: int | core.IntOut = core.attr(int, computed=True)

    interval: int | core.IntOut = core.attr(int, computed=True)

    target: str | core.StringOut = core.attr(str, computed=True)

    timeout: int | core.IntOut = core.attr(int, computed=True)

    unhealthy_threshold: int | core.IntOut = core.attr(int, computed=True)

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


@core.data(type="aws_elb", namespace="elb")
class DsMain(core.Data):

    access_logs: list[AccessLogs] | core.ArrayOut[AccessLogs] = core.attr(
        AccessLogs, computed=True, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    connection_draining: bool | core.BoolOut = core.attr(bool, computed=True)

    connection_draining_timeout: int | core.IntOut = core.attr(int, computed=True)

    cross_zone_load_balancing: bool | core.BoolOut = core.attr(bool, computed=True)

    desync_mitigation_mode: str | core.StringOut = core.attr(str, computed=True)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    health_check: list[HealthCheck] | core.ArrayOut[HealthCheck] = core.attr(
        HealthCheck, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_timeout: int | core.IntOut = core.attr(int, computed=True)

    instances: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    internal: bool | core.BoolOut = core.attr(bool, computed=True)

    listener: list[Listener] | core.ArrayOut[Listener] = core.attr(
        Listener, computed=True, kind=core.Kind.array
    )

    """
    (Required) The unique name of the load balancer.
    """
    name: str | core.StringOut = core.attr(str)

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_security_group: str | core.StringOut = core.attr(str, computed=True)

    source_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMain.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
