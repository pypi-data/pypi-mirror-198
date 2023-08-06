import terrascript.core as core


@core.data(type="aws_route53_resolver_rule", namespace="aws_route53_resolver")
class DsRule(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    resolver_endpoint_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    resolver_rule_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    rule_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    share_status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain_name: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        resolver_endpoint_id: str | core.StringOut | None = None,
        resolver_rule_id: str | core.StringOut | None = None,
        rule_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRule.Args(
                domain_name=domain_name,
                name=name,
                resolver_endpoint_id=resolver_endpoint_id,
                resolver_rule_id=resolver_rule_id,
                rule_type=rule_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        resolver_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        resolver_rule_id: str | core.StringOut | None = core.arg(default=None)

        rule_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
