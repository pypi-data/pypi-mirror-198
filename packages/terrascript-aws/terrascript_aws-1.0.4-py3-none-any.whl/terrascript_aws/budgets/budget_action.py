import terrascript.core as core


@core.schema
class ActionThreshold(core.Schema):

    action_threshold_type: str | core.StringOut = core.attr(str)

    action_threshold_value: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        *,
        action_threshold_type: str | core.StringOut,
        action_threshold_value: float | core.FloatOut,
    ):
        super().__init__(
            args=ActionThreshold.Args(
                action_threshold_type=action_threshold_type,
                action_threshold_value=action_threshold_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_threshold_type: str | core.StringOut = core.arg()

        action_threshold_value: float | core.FloatOut = core.arg()


@core.schema
class Subscriber(core.Schema):

    address: str | core.StringOut = core.attr(str)

    subscription_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        subscription_type: str | core.StringOut,
    ):
        super().__init__(
            args=Subscriber.Args(
                address=address,
                subscription_type=subscription_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        subscription_type: str | core.StringOut = core.arg()


@core.schema
class IamActionDefinition(core.Schema):

    groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    policy_arn: str | core.StringOut = core.attr(str)

    roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    users: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        policy_arn: str | core.StringOut,
        groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        roles: list[str] | core.ArrayOut[core.StringOut] | None = None,
        users: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=IamActionDefinition.Args(
                policy_arn=policy_arn,
                groups=groups,
                roles=roles,
                users=users,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        policy_arn: str | core.StringOut = core.arg()

        roles: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        users: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class SsmActionDefinition(core.Schema):

    action_sub_type: str | core.StringOut = core.attr(str)

    instance_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    region: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        action_sub_type: str | core.StringOut,
        instance_ids: list[str] | core.ArrayOut[core.StringOut],
        region: str | core.StringOut,
    ):
        super().__init__(
            args=SsmActionDefinition.Args(
                action_sub_type=action_sub_type,
                instance_ids=instance_ids,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_sub_type: str | core.StringOut = core.arg()

        instance_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        region: str | core.StringOut = core.arg()


@core.schema
class ScpActionDefinition(core.Schema):

    policy_id: str | core.StringOut = core.attr(str)

    target_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        policy_id: str | core.StringOut,
        target_ids: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=ScpActionDefinition.Args(
                policy_id=policy_id,
                target_ids=target_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        policy_id: str | core.StringOut = core.arg()

        target_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Definition(core.Schema):

    iam_action_definition: IamActionDefinition | None = core.attr(IamActionDefinition, default=None)

    scp_action_definition: ScpActionDefinition | None = core.attr(ScpActionDefinition, default=None)

    ssm_action_definition: SsmActionDefinition | None = core.attr(SsmActionDefinition, default=None)

    def __init__(
        self,
        *,
        iam_action_definition: IamActionDefinition | None = None,
        scp_action_definition: ScpActionDefinition | None = None,
        ssm_action_definition: SsmActionDefinition | None = None,
    ):
        super().__init__(
            args=Definition.Args(
                iam_action_definition=iam_action_definition,
                scp_action_definition=scp_action_definition,
                ssm_action_definition=ssm_action_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam_action_definition: IamActionDefinition | None = core.arg(default=None)

        scp_action_definition: ScpActionDefinition | None = core.arg(default=None)

        ssm_action_definition: SsmActionDefinition | None = core.arg(default=None)


@core.resource(type="aws_budgets_budget_action", namespace="budgets")
class BudgetAction(core.Resource):
    """
    (Optional) The ID of the target account for budget. Will use current user's account_id by default if
    omitted.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The id of the budget action.
    """
    action_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The trigger threshold of the action. See [Action Threshold](#action-threshold).
    """
    action_threshold: ActionThreshold = core.attr(ActionThreshold)

    """
    (Required) The type of action. This defines the type of tasks that can be carried out by this action
    . This field also determines the format for definition. Valid values are `APPLY_IAM_POLICY`, `APPLY_
    SCP_POLICY`, and `RUN_SSM_DOCUMENTS`.
    """
    action_type: str | core.StringOut = core.attr(str)

    """
    (Required) This specifies if the action needs manual or automatic approval. Valid values are `AUTOMA
    TIC` and `MANUAL`.
    """
    approval_model: str | core.StringOut = core.attr(str)

    """
    The ARN of the budget action.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of a budget.
    """
    budget_name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies all of the type-specific parameters. See [Definition](#definition).
    """
    definition: Definition = core.attr(Definition)

    """
    (Required) The role passed for action execution and reversion. Roles and actions must be in the same
    account.
    """
    execution_role_arn: str | core.StringOut = core.attr(str)

    """
    ID of resource.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of a notification. Valid values are `ACTUAL` or `FORECASTED`.
    """
    notification_type: str | core.StringOut = core.attr(str)

    """
    The status of the budget action.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A list of subscribers. See [Subscriber](#subscriber).
    """
    subscriber: list[Subscriber] | core.ArrayOut[Subscriber] = core.attr(
        Subscriber, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        action_threshold: ActionThreshold,
        action_type: str | core.StringOut,
        approval_model: str | core.StringOut,
        budget_name: str | core.StringOut,
        definition: Definition,
        execution_role_arn: str | core.StringOut,
        notification_type: str | core.StringOut,
        subscriber: list[Subscriber] | core.ArrayOut[Subscriber],
        account_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BudgetAction.Args(
                action_threshold=action_threshold,
                action_type=action_type,
                approval_model=approval_model,
                budget_name=budget_name,
                definition=definition,
                execution_role_arn=execution_role_arn,
                notification_type=notification_type,
                subscriber=subscriber,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        action_threshold: ActionThreshold = core.arg()

        action_type: str | core.StringOut = core.arg()

        approval_model: str | core.StringOut = core.arg()

        budget_name: str | core.StringOut = core.arg()

        definition: Definition = core.arg()

        execution_role_arn: str | core.StringOut = core.arg()

        notification_type: str | core.StringOut = core.arg()

        subscriber: list[Subscriber] | core.ArrayOut[Subscriber] = core.arg()
