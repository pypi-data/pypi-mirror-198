import terrascript.core as core


@core.resource(type="aws_route53_resolver_firewall_rule", namespace="route53_resolver")
class FirewallRule(core.Resource):

    action: str | core.StringOut = core.attr(str)

    block_override_dns_type: str | core.StringOut | None = core.attr(str, default=None)

    block_override_domain: str | core.StringOut | None = core.attr(str, default=None)

    block_override_ttl: int | core.IntOut | None = core.attr(int, default=None)

    block_response: str | core.StringOut | None = core.attr(str, default=None)

    firewall_domain_list_id: str | core.StringOut = core.attr(str)

    firewall_rule_group_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    priority: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        action: str | core.StringOut,
        firewall_domain_list_id: str | core.StringOut,
        firewall_rule_group_id: str | core.StringOut,
        name: str | core.StringOut,
        priority: int | core.IntOut,
        block_override_dns_type: str | core.StringOut | None = None,
        block_override_domain: str | core.StringOut | None = None,
        block_override_ttl: int | core.IntOut | None = None,
        block_response: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallRule.Args(
                action=action,
                firewall_domain_list_id=firewall_domain_list_id,
                firewall_rule_group_id=firewall_rule_group_id,
                name=name,
                priority=priority,
                block_override_dns_type=block_override_dns_type,
                block_override_domain=block_override_domain,
                block_override_ttl=block_override_ttl,
                block_response=block_response,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: str | core.StringOut = core.arg()

        block_override_dns_type: str | core.StringOut | None = core.arg(default=None)

        block_override_domain: str | core.StringOut | None = core.arg(default=None)

        block_override_ttl: int | core.IntOut | None = core.arg(default=None)

        block_response: str | core.StringOut | None = core.arg(default=None)

        firewall_domain_list_id: str | core.StringOut = core.arg()

        firewall_rule_group_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        priority: int | core.IntOut = core.arg()
