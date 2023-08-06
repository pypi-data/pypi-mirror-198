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


@core.resource(type="aws_elb", namespace="elb")
class Main(core.Resource):
    """
    (Optional) An Access Logs block. Access Logs documented below.
    """

    access_logs: AccessLogs | None = core.attr(AccessLogs, default=None)

    """
    The ARN of the ELB
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required for an EC2-classic ELB) The AZ's to serve traffic in.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Boolean to enable connection draining. Default: `false`
    """
    connection_draining: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The time in seconds to allow for connections to drain. Default: `300`
    """
    connection_draining_timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Enable cross-zone load balancing. Default: `true`
    """
    cross_zone_load_balancing: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Determines how the load balancer handles requests that might pose a security risk to an a
    pplication due to HTTP desync. Valid values are `monitor`, `defensive` (default), `strictest`.
    """
    desync_mitigation_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    The DNS name of the ELB
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A health_check block. Health Check documented below.
    """
    health_check: HealthCheck | None = core.attr(HealthCheck, default=None, computed=True)

    """
    The name of the ELB
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The time in seconds that the connection is allowed to be idle. Default: `60`
    """
    idle_timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) A list of instance ids to place in the ELB pool.
    """
    instances: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) If true, ELB will be an internal ELB.
    """
    internal: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Required) A list of listener blocks. Listeners documented below.
    """
    listener: list[Listener] | core.ArrayOut[Listener] = core.attr(Listener, kind=core.Kind.array)

    """
    (Optional) The name of the ELB. By default generated by Terraform.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of security group IDs to assign to the ELB.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The name of the security group that you can use as
    """
    source_security_group: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the security group that you can use as
    """
    source_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required for a VPC ELB) A list of subnet IDs to attach to the ELB.
    """
    subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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
    The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
    """
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
