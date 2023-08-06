import terrascript.core as core


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


@core.resource(type="aws_lb_target_group", namespace="elb")
class LbTargetGroup(core.Resource):
    """
    ARN of the Target Group (matches `id`).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN suffix for use with CloudWatch Metrics.
    """
    arn_suffix: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to terminate connections at the end of the deregistration timeout on Network Load
    Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-
    target-groups.html#deregistration-delay) for more information. Default is `false`.
    """
    connection_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Amount time for Elastic Load Balancing to wait before changing the state of a deregisteri
    ng target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
    """
    deregistration_delay: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Maximum of 1) Health Check configuration block. Detailed below.
    """
    health_check: HealthCheck | None = core.attr(HealthCheck, default=None, computed=True)

    """
    ARN of the Target Group (matches `arn`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether the request and response headers exchanged between the load balancer and the Lamb
    da function include arrays of values or strings. Only applies when `target_type` is `lambda`. Defaul
    t is `false`.
    """
    lambda_multi_value_headers_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Determines how the load balancer selects targets when routing requests. Only applicable f
    or Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_request
    s`. The default is `round_robin`.
    """
    load_balancing_algorithm_type: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Forces new resource) Name of the target group. If omitted, Terraform will assign a random
    , unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`. Cannot be longer than 6 characters.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (May be required, Forces new resource) Port on which targets receive traffic, unless overridden when
    registering a specific target. Required when `target_type` is `instance`, `ip` or `alb`. Does not a
    pply when `target_type` is `lambda`.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Whether client IP preservation is enabled. See [doc](https://docs.aws.amazon.com/elasticl
    oadbalancing/latest/network/load-balancer-target-groups.html#client-ip-preservation) for more inform
    ation.
    """
    preserve_client_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (May be required, Forces new resource) Protocol to use for routing traffic to the targets. Should be
    one of `GENEVE`, `HTTP`, `HTTPS`, `TCP`, `TCP_UDP`, `TLS`, or `UDP`. Required when `target_type` is
    instance`, `ip` or `alb`. Does not apply when `target_type` is `lambda`.
    """
    protocol: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Forces new resource) Only applicable when `protocol` is `HTTP` or `HTTPS`. The protocol v
    ersion. Specify GRPC to send requests to targets using gRPC. Specify HTTP2 to send requests to targe
    ts using HTTP/2. The default is HTTP1, which sends requests to targets using HTTP/1.1
    """
    protocol_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether to enable support for proxy protocol v2 on Network Load Balancers. See [doc](http
    s://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-p
    rotocol) for more information. Default is `false`.
    """
    proxy_protocol_v2: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Amount time for targets to warm up before the load balancer sends them a full share of re
    quests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
    """
    slow_start: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Maximum of 1) Stickiness configuration block. Detailed below.
    """
    stickiness: Stickiness | None = core.attr(Stickiness, default=None, computed=True)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
    (May be required, Forces new resource) Type of target that you must specify when registering targets
    with this target group. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIRefere
    nce/API_CreateTargetGroup.html) for supported values. The default is `instance`.
    """
    target_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Forces new resource) Identifier of the VPC in which to create the target group. Required
    when `target_type` is `instance`, `ip` or `alb`. Does not apply when `target_type` is `lambda`.
    """
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
