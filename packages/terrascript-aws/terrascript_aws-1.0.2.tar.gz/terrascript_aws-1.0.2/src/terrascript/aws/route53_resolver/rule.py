import terrascript.core as core


@core.schema
class TargetIp(core.Schema):

    ip: str | core.StringOut = core.attr(str)

    port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        ip: str | core.StringOut,
        port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TargetIp.Args(
                ip=ip,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip: str | core.StringOut = core.arg()

        port: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_route53_resolver_rule", namespace="aws_route53_resolver")
class Rule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    resolver_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    rule_type: str | core.StringOut = core.attr(str)

    share_status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_ip: list[TargetIp] | core.ArrayOut[TargetIp] | None = core.attr(
        TargetIp, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut,
        rule_type: str | core.StringOut,
        name: str | core.StringOut | None = None,
        resolver_endpoint_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_ip: list[TargetIp] | core.ArrayOut[TargetIp] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Rule.Args(
                domain_name=domain_name,
                rule_type=rule_type,
                name=name,
                resolver_endpoint_id=resolver_endpoint_id,
                tags=tags,
                tags_all=tags_all,
                target_ip=target_ip,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        resolver_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        rule_type: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_ip: list[TargetIp] | core.ArrayOut[TargetIp] | None = core.arg(default=None)
