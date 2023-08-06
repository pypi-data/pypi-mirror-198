import terrascript.core as core


@core.schema
class StatefulEngineOptions(core.Schema):

    rule_order: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        rule_order: str | core.StringOut,
    ):
        super().__init__(
            args=StatefulEngineOptions.Args(
                rule_order=rule_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule_order: str | core.StringOut = core.arg()


@core.schema
class StatefulRuleGroupReference(core.Schema):

    priority: int | core.IntOut | None = core.attr(int, default=None)

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
        priority: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=StatefulRuleGroupReference.Args(
                resource_arn=resource_arn,
                priority=priority,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: int | core.IntOut | None = core.arg(default=None)

        resource_arn: str | core.StringOut = core.arg()


@core.schema
class Dimension(core.Schema):

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Dimension.Args(
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        value: str | core.StringOut = core.arg()


@core.schema
class PublishMetricAction(core.Schema):

    dimension: list[Dimension] | core.ArrayOut[Dimension] = core.attr(
        Dimension, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dimension: list[Dimension] | core.ArrayOut[Dimension],
    ):
        super().__init__(
            args=PublishMetricAction.Args(
                dimension=dimension,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimension: list[Dimension] | core.ArrayOut[Dimension] = core.arg()


@core.schema
class ActionDefinition(core.Schema):

    publish_metric_action: PublishMetricAction = core.attr(PublishMetricAction)

    def __init__(
        self,
        *,
        publish_metric_action: PublishMetricAction,
    ):
        super().__init__(
            args=ActionDefinition.Args(
                publish_metric_action=publish_metric_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        publish_metric_action: PublishMetricAction = core.arg()


@core.schema
class StatelessCustomAction(core.Schema):

    action_definition: ActionDefinition = core.attr(ActionDefinition)

    action_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        action_definition: ActionDefinition,
        action_name: str | core.StringOut,
    ):
        super().__init__(
            args=StatelessCustomAction.Args(
                action_definition=action_definition,
                action_name=action_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_definition: ActionDefinition = core.arg()

        action_name: str | core.StringOut = core.arg()


@core.schema
class StatelessRuleGroupReference(core.Schema):

    priority: int | core.IntOut = core.attr(int)

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        priority: int | core.IntOut,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=StatelessRuleGroupReference.Args(
                priority=priority,
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: int | core.IntOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()


@core.schema
class FirewallPolicyBlk(core.Schema):

    stateful_default_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    stateful_engine_options: StatefulEngineOptions | None = core.attr(
        StatefulEngineOptions, default=None
    )

    stateful_rule_group_reference: list[StatefulRuleGroupReference] | core.ArrayOut[
        StatefulRuleGroupReference
    ] | None = core.attr(StatefulRuleGroupReference, default=None, kind=core.Kind.array)

    stateless_custom_action: list[StatelessCustomAction] | core.ArrayOut[
        StatelessCustomAction
    ] | None = core.attr(StatelessCustomAction, default=None, kind=core.Kind.array)

    stateless_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    stateless_fragment_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    stateless_rule_group_reference: list[StatelessRuleGroupReference] | core.ArrayOut[
        StatelessRuleGroupReference
    ] | None = core.attr(StatelessRuleGroupReference, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        stateless_default_actions: list[str] | core.ArrayOut[core.StringOut],
        stateless_fragment_default_actions: list[str] | core.ArrayOut[core.StringOut],
        stateful_default_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        stateful_engine_options: StatefulEngineOptions | None = None,
        stateful_rule_group_reference: list[StatefulRuleGroupReference]
        | core.ArrayOut[StatefulRuleGroupReference]
        | None = None,
        stateless_custom_action: list[StatelessCustomAction]
        | core.ArrayOut[StatelessCustomAction]
        | None = None,
        stateless_rule_group_reference: list[StatelessRuleGroupReference]
        | core.ArrayOut[StatelessRuleGroupReference]
        | None = None,
    ):
        super().__init__(
            args=FirewallPolicyBlk.Args(
                stateless_default_actions=stateless_default_actions,
                stateless_fragment_default_actions=stateless_fragment_default_actions,
                stateful_default_actions=stateful_default_actions,
                stateful_engine_options=stateful_engine_options,
                stateful_rule_group_reference=stateful_rule_group_reference,
                stateless_custom_action=stateless_custom_action,
                stateless_rule_group_reference=stateless_rule_group_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stateful_default_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        stateful_engine_options: StatefulEngineOptions | None = core.arg(default=None)

        stateful_rule_group_reference: list[StatefulRuleGroupReference] | core.ArrayOut[
            StatefulRuleGroupReference
        ] | None = core.arg(default=None)

        stateless_custom_action: list[StatelessCustomAction] | core.ArrayOut[
            StatelessCustomAction
        ] | None = core.arg(default=None)

        stateless_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        stateless_fragment_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        stateless_rule_group_reference: list[StatelessRuleGroupReference] | core.ArrayOut[
            StatelessRuleGroupReference
        ] | None = core.arg(default=None)


@core.resource(type="aws_networkfirewall_firewall_policy", namespace="networkfirewall")
class FirewallPolicy(core.Resource):
    """
    The Amazon Resource Name (ARN) that identifies the firewall policy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A friendly description of the firewall policy.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A configuration block describing the rule groups and policy actions to use in the firewal
    l policy. See [Firewall Policy](#firewall-policy) below for details.
    """
    firewall_policy: FirewallPolicyBlk = core.attr(FirewallPolicyBlk)

    """
    The Amazon Resource Name (ARN) that identifies the firewall policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) A friendly name of the firewall policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of resource tags to associate with the resource. If configured with a provider [`defa
    ult_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#def
    ault_tags-configuration-block) present, tags with matching keys will overwrite those defined at the
    provider-level.
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
    A string token used when updating a firewall policy.
    """
    update_token: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_policy: FirewallPolicyBlk,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallPolicy.Args(
                firewall_policy=firewall_policy,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        firewall_policy: FirewallPolicyBlk = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
