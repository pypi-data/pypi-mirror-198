import terrascript.core as core


@core.schema
class Action(core.Schema):

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Action.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class ActivatedRule(core.Schema):

    action: Action = core.attr(Action)

    priority: int | core.IntOut = core.attr(int)

    rule_id: str | core.StringOut = core.attr(str)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        action: Action,
        priority: int | core.IntOut,
        rule_id: str | core.StringOut,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ActivatedRule.Args(
                action=action,
                priority=priority,
                rule_id=rule_id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        priority: int | core.IntOut = core.arg()

        rule_id: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_wafregional_rule_group", namespace="wafregional")
class RuleGroup(core.Resource):
    """
    (Optional) A list of activated rules, see below
    """

    activated_rule: list[ActivatedRule] | core.ArrayOut[ActivatedRule] | None = core.attr(
        ActivatedRule, default=None, kind=core.Kind.array
    )

    """
    The ARN of the WAF Regional Rule Group.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the WAF Regional Rule Group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A friendly name for the metrics from the rule group
    """
    metric_name: str | core.StringOut = core.attr(str)

    """
    (Required) A friendly name of the rule group
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        metric_name: str | core.StringOut,
        name: str | core.StringOut,
        activated_rule: list[ActivatedRule] | core.ArrayOut[ActivatedRule] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RuleGroup.Args(
                metric_name=metric_name,
                name=name,
                activated_rule=activated_rule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activated_rule: list[ActivatedRule] | core.ArrayOut[ActivatedRule] | None = core.arg(
            default=None
        )

        metric_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
