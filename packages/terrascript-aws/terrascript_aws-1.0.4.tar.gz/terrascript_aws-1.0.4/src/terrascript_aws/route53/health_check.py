import terrascript.core as core


@core.resource(type="aws_route53_health_check", namespace="route53")
class HealthCheck(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Health Check.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The minimum number of child health checks that must be healthy for Route 53 to consider t
    he parent health check to be healthy. Valid values are integers between 0 and 256, inclusive
    """
    child_health_threshold: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) For a specified parent health check, a list of HealthCheckId values for the associated ch
    ild health checks.
    """
    child_healthchecks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The name of the CloudWatch alarm.
    """
    cloudwatch_alarm_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The CloudWatchRegion that the CloudWatch alarm was created in.
    """
    cloudwatch_alarm_region: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A boolean value that stops Route 53 from performing health checks. When set to true, Rout
    e 53 will do the following depending on the type of health check:
    """
    disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint whe
    n performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sn
    i` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.
    """
    enable_sni: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) The number of consecutive health checks that an endpoint must pass or fail.
    """
    failure_threshold: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The fully qualified domain name of the endpoint to be checked.
    """
    fqdn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The id of the health check
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The status of the health check when CloudWatch has insufficient data about the state of a
    ssociated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.
    """
    insufficient_data_health_status: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A boolean value that indicates whether the status of health check should be inverted. For
    example, if a health check is healthy but Inverted is True , then Route 53 considers the health che
    ck to be unhealthy.
    """
    invert_healthcheck: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The IP address of the endpoint to be checked.
    """
    ip_address: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A Boolean value that indicates whether you want Route 53 to measure the latency between h
    ealth checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in
    the Route 53 console.
    """
    measure_latency: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The port of the endpoint to be checked.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) This is a reference name used in Caller Reference
    """
    reference_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of AWS regions that you want Amazon Route 53 health checkers to check the specifie
    d endpoint from.
    """
    regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The number of seconds between the time that Amazon Route 53 gets a response from your end
    point and the time that it sends the next health-check request.
    """
    request_interval: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The path that you want Amazon Route 53 to request when performing health checks.
    """
    resource_path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) for the Route 53 Application Recovery Controller routing c
    ontrol. This is used when health check type is `RECOVERY_CONTROL`
    """
    routing_control_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) String searched in the first 5120 bytes of the response body for check to be considered h
    ealthy. Only valid with `HTTP_STR_MATCH` and `HTTPS_STR_MATCH`.
    """
    search_string: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the health check. If configured with a provider [`default_tags
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tag
    s-configuration-block) present, tags with matching keys will overwrite those defined at the provider
    level.
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
    (Required) The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTT
    P_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED`, `CLOUDWATCH_METRIC` and `RECOVERY_CONTROL`.
    """
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
