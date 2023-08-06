import terrascript.core as core


@core.resource(type="aws_xray_sampling_rule", namespace="aws_x_ray")
class XraySamplingRule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    fixed_rate: float | core.FloatOut = core.attr(float)

    host: str | core.StringOut = core.attr(str)

    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    priority: int | core.IntOut = core.attr(int)

    reservoir_size: int | core.IntOut = core.attr(int)

    resource_arn: str | core.StringOut = core.attr(str)

    rule_name: str | core.StringOut | None = core.attr(str, default=None)

    service_name: str | core.StringOut = core.attr(str)

    service_type: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url_path: str | core.StringOut = core.attr(str)

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
