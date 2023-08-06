import terrascript.core as core


@core.schema
class Notification(core.Schema):

    comparison_operator: str | core.StringOut = core.attr(str)

    notification_type: str | core.StringOut = core.attr(str)

    subscriber_email_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subscriber_sns_topic_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    threshold: float | core.FloatOut = core.attr(float)

    threshold_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison_operator: str | core.StringOut,
        notification_type: str | core.StringOut,
        threshold: float | core.FloatOut,
        threshold_type: str | core.StringOut,
        subscriber_email_addresses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subscriber_sns_topic_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Notification.Args(
                comparison_operator=comparison_operator,
                notification_type=notification_type,
                threshold=threshold,
                threshold_type=threshold_type,
                subscriber_email_addresses=subscriber_email_addresses,
                subscriber_sns_topic_arns=subscriber_sns_topic_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison_operator: str | core.StringOut = core.arg()

        notification_type: str | core.StringOut = core.arg()

        subscriber_email_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subscriber_sns_topic_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        threshold: float | core.FloatOut = core.arg()

        threshold_type: str | core.StringOut = core.arg()


@core.schema
class CostTypes(core.Schema):

    include_credit: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_discount: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_other_subscription: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_recurring: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_refund: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_subscription: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_support: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_tax: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_upfront: bool | core.BoolOut | None = core.attr(bool, default=None)

    use_amortized: bool | core.BoolOut | None = core.attr(bool, default=None)

    use_blended: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        include_credit: bool | core.BoolOut | None = None,
        include_discount: bool | core.BoolOut | None = None,
        include_other_subscription: bool | core.BoolOut | None = None,
        include_recurring: bool | core.BoolOut | None = None,
        include_refund: bool | core.BoolOut | None = None,
        include_subscription: bool | core.BoolOut | None = None,
        include_support: bool | core.BoolOut | None = None,
        include_tax: bool | core.BoolOut | None = None,
        include_upfront: bool | core.BoolOut | None = None,
        use_amortized: bool | core.BoolOut | None = None,
        use_blended: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=CostTypes.Args(
                include_credit=include_credit,
                include_discount=include_discount,
                include_other_subscription=include_other_subscription,
                include_recurring=include_recurring,
                include_refund=include_refund,
                include_subscription=include_subscription,
                include_support=include_support,
                include_tax=include_tax,
                include_upfront=include_upfront,
                use_amortized=use_amortized,
                use_blended=use_blended,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        include_credit: bool | core.BoolOut | None = core.arg(default=None)

        include_discount: bool | core.BoolOut | None = core.arg(default=None)

        include_other_subscription: bool | core.BoolOut | None = core.arg(default=None)

        include_recurring: bool | core.BoolOut | None = core.arg(default=None)

        include_refund: bool | core.BoolOut | None = core.arg(default=None)

        include_subscription: bool | core.BoolOut | None = core.arg(default=None)

        include_support: bool | core.BoolOut | None = core.arg(default=None)

        include_tax: bool | core.BoolOut | None = core.arg(default=None)

        include_upfront: bool | core.BoolOut | None = core.arg(default=None)

        use_amortized: bool | core.BoolOut | None = core.arg(default=None)

        use_blended: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class CostFilter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=CostFilter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_budgets_budget", namespace="budgets")
class Budget(core.Resource):
    """
    (Optional) The ID of the target account for budget. Will use current user's account_id by default if
    omitted.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ARN of the budget.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Whether this budget tracks monetary cost or usage.
    """
    budget_type: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of [CostFilter](#cost-filter) name/values pair to apply to budget.
    """
    cost_filter: list[CostFilter] | core.ArrayOut[CostFilter] | None = core.attr(
        CostFilter, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional, **Deprecated**) Map of [CostFilters](#cost-filters) key/value pairs to apply to the budge
    t.
    """
    cost_filters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Object containing [CostTypes](#cost-types) The types of cost included in a budget, such a
    s tax and subscriptions.
    """
    cost_types: CostTypes | None = core.attr(CostTypes, default=None, computed=True)

    """
    id of resource.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The amount of cost or usage being measured for a budget.
    """
    limit_amount: str | core.StringOut = core.attr(str)

    """
    (Required) The unit of measurement used for the budget forecast, actual spend, or budget threshold,
    such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-
    type-spend.html) documentation.
    """
    limit_unit: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of a budget. Unique within accounts.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The prefix of the name of a budget. Unique within accounts.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Object containing [Budget Notifications](#budget-notification). Can be used multiple time
    s to define more than one budget notification
    """
    notification: list[Notification] | core.ArrayOut[Notification] | None = core.attr(
        Notification, default=None, kind=core.Kind.array
    )

    """
    (Optional) The end of the time period covered by the budget. There are no restrictions on the end da
    te. Format: `2017-01-01_12:00`.
    """
    time_period_end: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The start of the time period covered by the budget. If you don't specify a start date, AW
    S defaults to the start of your chosen time period. The start date must come before the end date. Fo
    rmat: `2017-01-01_12:00`.
    """
    time_period_start: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The length of time until a budget resets the actual and forecasted spend. Valid values: `
    MONTHLY`, `QUARTERLY`, `ANNUALLY`, and `DAILY`.
    """
    time_unit: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        budget_type: str | core.StringOut,
        limit_amount: str | core.StringOut,
        limit_unit: str | core.StringOut,
        time_unit: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        cost_filter: list[CostFilter] | core.ArrayOut[CostFilter] | None = None,
        cost_filters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        cost_types: CostTypes | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        notification: list[Notification] | core.ArrayOut[Notification] | None = None,
        time_period_end: str | core.StringOut | None = None,
        time_period_start: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Budget.Args(
                budget_type=budget_type,
                limit_amount=limit_amount,
                limit_unit=limit_unit,
                time_unit=time_unit,
                account_id=account_id,
                cost_filter=cost_filter,
                cost_filters=cost_filters,
                cost_types=cost_types,
                name=name,
                name_prefix=name_prefix,
                notification=notification,
                time_period_end=time_period_end,
                time_period_start=time_period_start,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        budget_type: str | core.StringOut = core.arg()

        cost_filter: list[CostFilter] | core.ArrayOut[CostFilter] | None = core.arg(default=None)

        cost_filters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        cost_types: CostTypes | None = core.arg(default=None)

        limit_amount: str | core.StringOut = core.arg()

        limit_unit: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        notification: list[Notification] | core.ArrayOut[Notification] | None = core.arg(
            default=None
        )

        time_period_end: str | core.StringOut | None = core.arg(default=None)

        time_period_start: str | core.StringOut | None = core.arg(default=None)

        time_unit: str | core.StringOut = core.arg()
