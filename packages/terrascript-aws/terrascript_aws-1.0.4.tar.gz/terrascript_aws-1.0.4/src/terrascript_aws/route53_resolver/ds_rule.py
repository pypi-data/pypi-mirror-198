import terrascript.core as core


@core.data(type="aws_route53_resolver_rule", namespace="route53_resolver")
class DsRule(core.Data):
    """
    The ARN (Amazon Resource Name) for the resolver rule.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The domain name the desired resolver rule forwards DNS queries for. Conflicts with `resol
    ver_rule_id`.
    """
    domain_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the resolver rule.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The friendly name of the desired resolver rule. Conflicts with `resolver_rule_id`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    When a rule is shared with another AWS account, the account ID of the account that the rule is share
    d with.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    resolver_endpoint_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    resolver_rule_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The rule type of the desired resolver rule. Valid values are `FORWARD`, `SYSTEM` and `REC
    URSIVE`. Conflicts with `resolver_rule_id`.
    """
    rule_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Whether the rules is shared and, if so, whether the current account is sharing the rule with another
    account, or another account is sharing the rule with the current account.
    """
    share_status: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the resolver rule.
    """
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
