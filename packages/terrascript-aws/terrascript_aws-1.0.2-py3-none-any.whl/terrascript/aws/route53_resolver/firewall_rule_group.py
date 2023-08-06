import terrascript.core as core


@core.resource(type="aws_route53_resolver_firewall_rule_group", namespace="aws_route53_resolver")
class FirewallRuleGroup(core.Resource):
    """
    The ARN (Amazon Resource Name) of the rule group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the rule group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A name that lets you identify the rule group, to manage and use it.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The AWS account ID for the account that created the rule group. When a rule group is shared with you
    r account, this is the account that has shared the rule group with you.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the rule group is shared with other AWS accounts, or was shared with the current account by
    another AWS account. Sharing is configured through AWS Resource Access Manager (AWS RAM). Valid valu
    es: `NOT_SHARED`, `SHARED_BY_ME`, `SHARED_WITH_ME`
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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallRuleGroup.Args(
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
