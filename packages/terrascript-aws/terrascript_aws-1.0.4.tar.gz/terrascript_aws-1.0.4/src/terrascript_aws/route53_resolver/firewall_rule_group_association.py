import terrascript.core as core


@core.resource(
    type="aws_route53_resolver_firewall_rule_group_association", namespace="route53_resolver"
)
class FirewallRuleGroupAssociation(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    firewall_rule_group_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    mutation_protection: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    priority: int | core.IntOut = core.attr(int)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_rule_group_id: str | core.StringOut,
        name: str | core.StringOut,
        priority: int | core.IntOut,
        vpc_id: str | core.StringOut,
        mutation_protection: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallRuleGroupAssociation.Args(
                firewall_rule_group_id=firewall_rule_group_id,
                name=name,
                priority=priority,
                vpc_id=vpc_id,
                mutation_protection=mutation_protection,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        firewall_rule_group_id: str | core.StringOut = core.arg()

        mutation_protection: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        priority: int | core.IntOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
