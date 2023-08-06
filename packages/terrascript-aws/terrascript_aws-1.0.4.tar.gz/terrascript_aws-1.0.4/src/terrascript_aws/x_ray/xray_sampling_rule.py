import terrascript.core as core


@core.resource(type="aws_xray_sampling_rule", namespace="x_ray")
class XraySamplingRule(core.Resource):
    """
    The ARN of the sampling rule.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Matches attributes derived from the request.
    """
    attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Required) The percentage of matching requests to instrument, after the reservoir is exhausted.
    """
    fixed_rate: float | core.FloatOut = core.attr(float)

    """
    (Required) Matches the hostname from a request URL.
    """
    host: str | core.StringOut = core.attr(str)

    """
    (Required) Matches the HTTP method of a request.
    """
    http_method: str | core.StringOut = core.attr(str)

    """
    The name of the sampling rule.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The priority of the sampling rule.
    """
    priority: int | core.IntOut = core.attr(int)

    """
    (Required) A fixed number of matching requests to instrument per second, prior to applying the fixed
    rate. The reservoir is not used directly by services, but applies to all services using the rule co
    llectively.
    """
    reservoir_size: int | core.IntOut = core.attr(int)

    """
    (Required) Matches the ARN of the AWS resource on which the service runs.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the sampling rule.
    """
    rule_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Matches the `name` that the service uses to identify itself in segments.
    """
    service_name: str | core.StringOut = core.attr(str)

    """
    (Required) Matches the `origin` that the service uses to identify its type in segments.
    """
    service_type: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Required) Matches the path from a request URL.
    """
    url_path: str | core.StringOut = core.attr(str)

    """
    (Required) The version of the sampling rule format (`1` )
    """
    version: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        fixed_rate: float | core.FloatOut,
        host: str | core.StringOut,
        http_method: str | core.StringOut,
        priority: int | core.IntOut,
        reservoir_size: int | core.IntOut,
        resource_arn: str | core.StringOut,
        service_name: str | core.StringOut,
        service_type: str | core.StringOut,
        url_path: str | core.StringOut,
        version: int | core.IntOut,
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        rule_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=XraySamplingRule.Args(
                fixed_rate=fixed_rate,
                host=host,
                http_method=http_method,
                priority=priority,
                reservoir_size=reservoir_size,
                resource_arn=resource_arn,
                service_name=service_name,
                service_type=service_type,
                url_path=url_path,
                version=version,
                attributes=attributes,
                rule_name=rule_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        fixed_rate: float | core.FloatOut = core.arg()

        host: str | core.StringOut = core.arg()

        http_method: str | core.StringOut = core.arg()

        priority: int | core.IntOut = core.arg()

        reservoir_size: int | core.IntOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()

        rule_name: str | core.StringOut | None = core.arg(default=None)

        service_name: str | core.StringOut = core.arg()

        service_type: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        url_path: str | core.StringOut = core.arg()

        version: int | core.IntOut = core.arg()
