import terrascript.core as core


@core.resource(type="aws_route53_resolver_firewall_rule", namespace="aws_route53_resolver")
class FirewallRule(core.Resource):
    """
    (Required) The action that DNS Firewall should take on a DNS query when it matches one of the domain
    s in the rule's domain list. Valid values: `ALLOW`, `BLOCK`, `ALERT`.
    """

    action: str | core.StringOut = core.attr(str)

    """
    (Required if `block_response` is `OVERRIDE`) The DNS record's type. This determines the format of th
    e record value that you provided in BlockOverrideDomain. Value values: `CNAME`.
    """
    block_override_dns_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required if `block_response` is `OVERRIDE`) The custom DNS record to send back in response to the q
    uery.
    """
    block_override_domain: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required if `block_response` is `OVERRIDE`) The recommended amount of time, in seconds, for the DNS
    resolver or web browser to cache the provided override record. Minimum value of 0. Maximum value of
    604800.
    """
    block_override_ttl: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required if `action` is `BLOCK`) The way that you want DNS Firewall to block the request. Valid val
    ues: `NODATA`, `NXDOMAIN`, `OVERRIDE`.
    """
    block_response: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the domain list that you want to use in the rule.
    """
    firewall_domain_list_id: str | core.StringOut = core.attr(str)

    """
    (Required) The unique identifier of the firewall rule group where you want to create the rule.
    """
    firewall_rule_group_id: str | core.StringOut = core.attr(str)

    """
    The ID of the rule.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A name that lets you identify the rule, to manage and use it.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The setting that determines the processing order of the rule in the rule group. DNS Firew
    all processes the rules in a rule group by order of priority, starting from the lowest setting.
    """
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
