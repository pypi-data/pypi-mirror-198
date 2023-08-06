import terrascript.core as core


@core.schema
class IpSet(core.Schema):

    definition: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        definition: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=IpSet.Args(
                definition=definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        definition: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class IpSets(core.Schema):

    ip_set: IpSet = core.attr(IpSet)

    key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        ip_set: IpSet,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=IpSets.Args(
                ip_set=ip_set,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_set: IpSet = core.arg()

        key: str | core.StringOut = core.arg()


@core.schema
class PortSet(core.Schema):

    definition: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        definition: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=PortSet.Args(
                definition=definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        definition: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class PortSets(core.Schema):

    key: str | core.StringOut = core.attr(str)

    port_set: PortSet = core.attr(PortSet)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        port_set: PortSet,
    ):
        super().__init__(
            args=PortSets.Args(
                key=key,
                port_set=port_set,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        port_set: PortSet = core.arg()


@core.schema
class RuleVariables(core.Schema):

    ip_sets: list[IpSets] | core.ArrayOut[IpSets] | None = core.attr(
        IpSets, default=None, kind=core.Kind.array
    )

    port_sets: list[PortSets] | core.ArrayOut[PortSets] | None = core.attr(
        PortSets, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ip_sets: list[IpSets] | core.ArrayOut[IpSets] | None = None,
        port_sets: list[PortSets] | core.ArrayOut[PortSets] | None = None,
    ):
        super().__init__(
            args=RuleVariables.Args(
                ip_sets=ip_sets,
                port_sets=port_sets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_sets: list[IpSets] | core.ArrayOut[IpSets] | None = core.arg(default=None)

        port_sets: list[PortSets] | core.ArrayOut[PortSets] | None = core.arg(default=None)


@core.schema
class Header(core.Schema):

    destination: str | core.StringOut = core.attr(str)

    destination_port: str | core.StringOut = core.attr(str)

    direction: str | core.StringOut = core.attr(str)

    protocol: str | core.StringOut = core.attr(str)

    source: str | core.StringOut = core.attr(str)

    source_port: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination: str | core.StringOut,
        destination_port: str | core.StringOut,
        direction: str | core.StringOut,
        protocol: str | core.StringOut,
        source: str | core.StringOut,
        source_port: str | core.StringOut,
    ):
        super().__init__(
            args=Header.Args(
                destination=destination,
                destination_port=destination_port,
                direction=direction,
                protocol=protocol,
                source=source,
                source_port=source_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: str | core.StringOut = core.arg()

        destination_port: str | core.StringOut = core.arg()

        direction: str | core.StringOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        source: str | core.StringOut = core.arg()

        source_port: str | core.StringOut = core.arg()


@core.schema
class RuleOption(core.Schema):

    keyword: str | core.StringOut = core.attr(str)

    settings: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        keyword: str | core.StringOut,
        settings: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=RuleOption.Args(
                keyword=keyword,
                settings=settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        keyword: str | core.StringOut = core.arg()

        settings: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class StatefulRule(core.Schema):

    action: str | core.StringOut = core.attr(str)

    header: Header = core.attr(Header)

    rule_option: list[RuleOption] | core.ArrayOut[RuleOption] = core.attr(
        RuleOption, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        action: str | core.StringOut,
        header: Header,
        rule_option: list[RuleOption] | core.ArrayOut[RuleOption],
    ):
        super().__init__(
            args=StatefulRule.Args(
                action=action,
                header=header,
                rule_option=rule_option,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut = core.arg()

        header: Header = core.arg()

        rule_option: list[RuleOption] | core.ArrayOut[RuleOption] = core.arg()


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
class CustomAction(core.Schema):

    action_definition: ActionDefinition = core.attr(ActionDefinition)

    action_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        action_definition: ActionDefinition,
        action_name: str | core.StringOut,
    ):
        super().__init__(
            args=CustomAction.Args(
                action_definition=action_definition,
                action_name=action_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_definition: ActionDefinition = core.arg()

        action_name: str | core.StringOut = core.arg()


@core.schema
class DestinationPort(core.Schema):

    from_port: int | core.IntOut = core.attr(int)

    to_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut,
        to_port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DestinationPort.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: int | core.IntOut = core.arg()

        to_port: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Source(core.Schema):

    address_definition: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        address_definition: str | core.StringOut,
    ):
        super().__init__(
            args=Source.Args(
                address_definition=address_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_definition: str | core.StringOut = core.arg()


@core.schema
class SourcePort(core.Schema):

    from_port: int | core.IntOut = core.attr(int)

    to_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut,
        to_port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SourcePort.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: int | core.IntOut = core.arg()

        to_port: int | core.IntOut | None = core.arg(default=None)


@core.schema
class TcpFlag(core.Schema):

    flags: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    masks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        flags: list[str] | core.ArrayOut[core.StringOut],
        masks: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=TcpFlag.Args(
                flags=flags,
                masks=masks,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        flags: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        masks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    address_definition: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        address_definition: str | core.StringOut,
    ):
        super().__init__(
            args=Destination.Args(
                address_definition=address_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_definition: str | core.StringOut = core.arg()


@core.schema
class MatchAttributes(core.Schema):

    destination: list[Destination] | core.ArrayOut[Destination] | None = core.attr(
        Destination, default=None, kind=core.Kind.array
    )

    destination_port: list[DestinationPort] | core.ArrayOut[DestinationPort] | None = core.attr(
        DestinationPort, default=None, kind=core.Kind.array
    )

    protocols: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    source: list[Source] | core.ArrayOut[Source] | None = core.attr(
        Source, default=None, kind=core.Kind.array
    )

    source_port: list[SourcePort] | core.ArrayOut[SourcePort] | None = core.attr(
        SourcePort, default=None, kind=core.Kind.array
    )

    tcp_flag: list[TcpFlag] | core.ArrayOut[TcpFlag] | None = core.attr(
        TcpFlag, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        destination: list[Destination] | core.ArrayOut[Destination] | None = None,
        destination_port: list[DestinationPort] | core.ArrayOut[DestinationPort] | None = None,
        protocols: list[int] | core.ArrayOut[core.IntOut] | None = None,
        source: list[Source] | core.ArrayOut[Source] | None = None,
        source_port: list[SourcePort] | core.ArrayOut[SourcePort] | None = None,
        tcp_flag: list[TcpFlag] | core.ArrayOut[TcpFlag] | None = None,
    ):
        super().__init__(
            args=MatchAttributes.Args(
                destination=destination,
                destination_port=destination_port,
                protocols=protocols,
                source=source,
                source_port=source_port,
                tcp_flag=tcp_flag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: list[Destination] | core.ArrayOut[Destination] | None = core.arg(default=None)

        destination_port: list[DestinationPort] | core.ArrayOut[DestinationPort] | None = core.arg(
            default=None
        )

        protocols: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(default=None)

        source: list[Source] | core.ArrayOut[Source] | None = core.arg(default=None)

        source_port: list[SourcePort] | core.ArrayOut[SourcePort] | None = core.arg(default=None)

        tcp_flag: list[TcpFlag] | core.ArrayOut[TcpFlag] | None = core.arg(default=None)


@core.schema
class RuleDefinition(core.Schema):

    actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    match_attributes: MatchAttributes = core.attr(MatchAttributes)

    def __init__(
        self,
        *,
        actions: list[str] | core.ArrayOut[core.StringOut],
        match_attributes: MatchAttributes,
    ):
        super().__init__(
            args=RuleDefinition.Args(
                actions=actions,
                match_attributes=match_attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        match_attributes: MatchAttributes = core.arg()


@core.schema
class StatelessRule(core.Schema):

    priority: int | core.IntOut = core.attr(int)

    rule_definition: RuleDefinition = core.attr(RuleDefinition)

    def __init__(
        self,
        *,
        priority: int | core.IntOut,
        rule_definition: RuleDefinition,
    ):
        super().__init__(
            args=StatelessRule.Args(
                priority=priority,
                rule_definition=rule_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: int | core.IntOut = core.arg()

        rule_definition: RuleDefinition = core.arg()


@core.schema
class StatelessRulesAndCustomActions(core.Schema):

    custom_action: list[CustomAction] | core.ArrayOut[CustomAction] | None = core.attr(
        CustomAction, default=None, kind=core.Kind.array
    )

    stateless_rule: list[StatelessRule] | core.ArrayOut[StatelessRule] = core.attr(
        StatelessRule, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        stateless_rule: list[StatelessRule] | core.ArrayOut[StatelessRule],
        custom_action: list[CustomAction] | core.ArrayOut[CustomAction] | None = None,
    ):
        super().__init__(
            args=StatelessRulesAndCustomActions.Args(
                stateless_rule=stateless_rule,
                custom_action=custom_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_action: list[CustomAction] | core.ArrayOut[CustomAction] | None = core.arg(
            default=None
        )

        stateless_rule: list[StatelessRule] | core.ArrayOut[StatelessRule] = core.arg()


@core.schema
class RulesSourceList(core.Schema):

    generated_rules_type: str | core.StringOut = core.attr(str)

    target_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    targets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        generated_rules_type: str | core.StringOut,
        target_types: list[str] | core.ArrayOut[core.StringOut],
        targets: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=RulesSourceList.Args(
                generated_rules_type=generated_rules_type,
                target_types=target_types,
                targets=targets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        generated_rules_type: str | core.StringOut = core.arg()

        target_types: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        targets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class RulesSource(core.Schema):

    rules_source_list: RulesSourceList | None = core.attr(RulesSourceList, default=None)

    rules_string: str | core.StringOut | None = core.attr(str, default=None)

    stateful_rule: list[StatefulRule] | core.ArrayOut[StatefulRule] | None = core.attr(
        StatefulRule, default=None, kind=core.Kind.array
    )

    stateless_rules_and_custom_actions: StatelessRulesAndCustomActions | None = core.attr(
        StatelessRulesAndCustomActions, default=None
    )

    def __init__(
        self,
        *,
        rules_source_list: RulesSourceList | None = None,
        rules_string: str | core.StringOut | None = None,
        stateful_rule: list[StatefulRule] | core.ArrayOut[StatefulRule] | None = None,
        stateless_rules_and_custom_actions: StatelessRulesAndCustomActions | None = None,
    ):
        super().__init__(
            args=RulesSource.Args(
                rules_source_list=rules_source_list,
                rules_string=rules_string,
                stateful_rule=stateful_rule,
                stateless_rules_and_custom_actions=stateless_rules_and_custom_actions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rules_source_list: RulesSourceList | None = core.arg(default=None)

        rules_string: str | core.StringOut | None = core.arg(default=None)

        stateful_rule: list[StatefulRule] | core.ArrayOut[StatefulRule] | None = core.arg(
            default=None
        )

        stateless_rules_and_custom_actions: StatelessRulesAndCustomActions | None = core.arg(
            default=None
        )


@core.schema
class StatefulRuleOptions(core.Schema):

    rule_order: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        rule_order: str | core.StringOut,
    ):
        super().__init__(
            args=StatefulRuleOptions.Args(
                rule_order=rule_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule_order: str | core.StringOut = core.arg()


@core.schema
class RuleGroupBlk(core.Schema):

    rule_variables: RuleVariables | None = core.attr(RuleVariables, default=None)

    rules_source: RulesSource = core.attr(RulesSource)

    stateful_rule_options: StatefulRuleOptions | None = core.attr(StatefulRuleOptions, default=None)

    def __init__(
        self,
        *,
        rules_source: RulesSource,
        rule_variables: RuleVariables | None = None,
        stateful_rule_options: StatefulRuleOptions | None = None,
    ):
        super().__init__(
            args=RuleGroupBlk.Args(
                rules_source=rules_source,
                rule_variables=rule_variables,
                stateful_rule_options=stateful_rule_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule_variables: RuleVariables | None = core.arg(default=None)

        rules_source: RulesSource = core.arg()

        stateful_rule_options: StatefulRuleOptions | None = core.arg(default=None)


@core.resource(type="aws_networkfirewall_rule_group", namespace="networkfirewall")
class RuleGroup(core.Resource):
    """
    The Amazon Resource Name (ARN) that identifies the rule group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The maximum number of operating resources that this rule group can u
    se. For a stateless rule group, the capacity required is the sum of the capacity requirements of the
    individual rules. For a stateful rule group, the minimum capacity required is the number of individ
    ual rules.
    """
    capacity: int | core.IntOut = core.attr(int)

    """
    (Optional) A friendly description of the rule group.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) that identifies the rule group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) A friendly name of the rule group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A configuration block that defines the rule group rules. Required unless `rules` is speci
    fied. See [Rule Group](#rule-group) below for details.
    """
    rule_group: RuleGroupBlk | None = core.attr(RuleGroupBlk, default=None, computed=True)

    """
    (Optional) The stateful rule group rules specifications in Suricata file format, with one rule per l
    ine. Use this to import your existing Suricata compatible rule groups. Required unless `rule_group`
    is specified.
    """
    rules: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of key:value pairs to associate with the resource. If configured with a provider [`
    default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs
    #default_tags-configuration-block) present, tags with matching keys will overwrite those defined at
    the provider-level.
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
    (Required) Whether the rule group is stateless (containing stateless rules) or stateful (containing
    stateful rules). Valid values include: `STATEFUL` or `STATELESS`.
    """
    type: str | core.StringOut = core.attr(str)

    """
    A string token used when updating the rule group.
    """
    update_token: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        capacity: int | core.IntOut,
        name: str | core.StringOut,
        type: str | core.StringOut,
        description: str | core.StringOut | None = None,
        rule_group: RuleGroupBlk | None = None,
        rules: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RuleGroup.Args(
                capacity=capacity,
                name=name,
                type=type,
                description=description,
                rule_group=rule_group,
                rules=rules,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity: int | core.IntOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rule_group: RuleGroupBlk | None = core.arg(default=None)

        rules: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
