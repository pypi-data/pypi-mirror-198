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


@core.resource(type="aws_route53_resolver_rule", namespace="route53_resolver")
class Rule(core.Resource):
    """
    The ARN (Amazon Resource Name) for the resolver rule.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) DNS queries for this domain name are forwarded to the IP addresses that are specified usi
    ng `target_ip`.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    The ID of the resolver rule.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 5
    3 console.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    When a rule is shared with another AWS account, the account ID of the account that the rule is share
    d with.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    resolver_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The rule type. Valid values are `FORWARD`, `SYSTEM` and `RECURSIVE`.
    """
    rule_type: str | core.StringOut = core.attr(str)

    """
    Whether the rules is shared and, if so, whether the current account is sharing the rule with another
    account, or another account is sharing the rule with the current account.
    """
    share_status: str | core.StringOut = core.attr(str, computed=True)

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
    (Optional) Configuration block(s) indicating the IPs that you want Resolver to forward DNS queries t
    o (documented below).
    """
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
