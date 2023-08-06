import terrascript.core as core


@core.schema
class Dimension(core.Schema):

    value: str | core.StringOut = core.attr(str, computed=True)

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
        Dimension, computed=True, kind=core.Kind.array
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

    publish_metric_action: list[PublishMetricAction] | core.ArrayOut[
        PublishMetricAction
    ] = core.attr(PublishMetricAction, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        publish_metric_action: list[PublishMetricAction] | core.ArrayOut[PublishMetricAction],
    ):
        super().__init__(
            args=ActionDefinition.Args(
                publish_metric_action=publish_metric_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        publish_metric_action: list[PublishMetricAction] | core.ArrayOut[
            PublishMetricAction
        ] = core.arg()


@core.schema
class StatelessCustomAction(core.Schema):

    action_definition: list[ActionDefinition] | core.ArrayOut[ActionDefinition] = core.attr(
        ActionDefinition, computed=True, kind=core.Kind.array
    )

    action_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        action_definition: list[ActionDefinition] | core.ArrayOut[ActionDefinition],
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
        action_definition: list[ActionDefinition] | core.ArrayOut[ActionDefinition] = core.arg()

        action_name: str | core.StringOut = core.arg()


@core.schema
class StatelessRuleGroupReference(core.Schema):

    priority: int | core.IntOut = core.attr(int, computed=True)

    resource_arn: str | core.StringOut = core.attr(str, computed=True)

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
class StatefulEngineOptions(core.Schema):

    rule_order: str | core.StringOut = core.attr(str, computed=True)

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

    priority: int | core.IntOut = core.attr(int, computed=True)

    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        priority: int | core.IntOut,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=StatefulRuleGroupReference.Args(
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

    stateful_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    stateful_engine_options: list[StatefulEngineOptions] | core.ArrayOut[
        StatefulEngineOptions
    ] = core.attr(StatefulEngineOptions, computed=True, kind=core.Kind.array)

    stateful_rule_group_reference: list[StatefulRuleGroupReference] | core.ArrayOut[
        StatefulRuleGroupReference
    ] = core.attr(StatefulRuleGroupReference, computed=True, kind=core.Kind.array)

    stateless_custom_action: list[StatelessCustomAction] | core.ArrayOut[
        StatelessCustomAction
    ] = core.attr(StatelessCustomAction, computed=True, kind=core.Kind.array)

    stateless_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    stateless_fragment_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    stateless_rule_group_reference: list[StatelessRuleGroupReference] | core.ArrayOut[
        StatelessRuleGroupReference
    ] = core.attr(StatelessRuleGroupReference, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        stateful_default_actions: list[str] | core.ArrayOut[core.StringOut],
        stateful_engine_options: list[StatefulEngineOptions] | core.ArrayOut[StatefulEngineOptions],
        stateful_rule_group_reference: list[StatefulRuleGroupReference]
        | core.ArrayOut[StatefulRuleGroupReference],
        stateless_custom_action: list[StatelessCustomAction] | core.ArrayOut[StatelessCustomAction],
        stateless_default_actions: list[str] | core.ArrayOut[core.StringOut],
        stateless_fragment_default_actions: list[str] | core.ArrayOut[core.StringOut],
        stateless_rule_group_reference: list[StatelessRuleGroupReference]
        | core.ArrayOut[StatelessRuleGroupReference],
    ):
        super().__init__(
            args=FirewallPolicyBlk.Args(
                stateful_default_actions=stateful_default_actions,
                stateful_engine_options=stateful_engine_options,
                stateful_rule_group_reference=stateful_rule_group_reference,
                stateless_custom_action=stateless_custom_action,
                stateless_default_actions=stateless_default_actions,
                stateless_fragment_default_actions=stateless_fragment_default_actions,
                stateless_rule_group_reference=stateless_rule_group_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stateful_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        stateful_engine_options: list[StatefulEngineOptions] | core.ArrayOut[
            StatefulEngineOptions
        ] = core.arg()

        stateful_rule_group_reference: list[StatefulRuleGroupReference] | core.ArrayOut[
            StatefulRuleGroupReference
        ] = core.arg()

        stateless_custom_action: list[StatelessCustomAction] | core.ArrayOut[
            StatelessCustomAction
        ] = core.arg()

        stateless_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        stateless_fragment_default_actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        stateless_rule_group_reference: list[StatelessRuleGroupReference] | core.ArrayOut[
            StatelessRuleGroupReference
        ] = core.arg()


@core.data(type="aws_networkfirewall_firewall_policy", namespace="networkfirewall")
class DsFirewallPolicy(core.Data):
    """
    The Amazon Resource Name (ARN) of the firewall policy.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    A description of the firewall policy.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The [policy][2] for the specified firewall policy.
    """
    firewall_policy: list[FirewallPolicyBlk] | core.ArrayOut[FirewallPolicyBlk] = core.attr(
        FirewallPolicyBlk, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The descriptive name of the firewall policy.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    Key-value tags for the firewall policy.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    A token used for optimistic locking.
    """
    update_token: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFirewallPolicy.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
