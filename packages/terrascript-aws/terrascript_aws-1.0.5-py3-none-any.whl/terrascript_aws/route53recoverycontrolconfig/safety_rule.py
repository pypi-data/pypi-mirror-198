import terrascript.core as core


@core.schema
class RuleConfig(core.Schema):

    inverted: bool | core.BoolOut = core.attr(bool)

    threshold: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        inverted: bool | core.BoolOut,
        threshold: int | core.IntOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=RuleConfig.Args(
                inverted=inverted,
                threshold=threshold,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        inverted: bool | core.BoolOut = core.arg()

        threshold: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.resource(
    type="aws_route53recoverycontrolconfig_safety_rule", namespace="route53recoverycontrolconfig"
)
class SafetyRule(core.Resource):
    """
    ARN of the safety rule.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Routing controls that are part of transactions that are evaluated to determine if a reque
    st to change a routing control state is allowed.
    """
    asserted_controls: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) ARN of the control panel in which this safety rule will reside.
    """
    control_panel_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Gating controls for the new gating rule. That is, routing controls that are evaluated by
    the rule configuration that you specify.
    """
    gating_controls: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name describing the safety rule.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block for safety rule criteria. See below.
    """
    rule_config: RuleConfig = core.attr(RuleConfig)

    """
    Status of the safety rule. `PENDING` when it is being created/updated, `PENDING_DELETION` when it is
    being deleted, and `DEPLOYED` otherwise.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Routing controls that can only be set or unset if the specified `rule_config` evaluates t
    o true for the specified `gating_controls`.
    """
    target_controls: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) Evaluation period, in milliseconds (ms), during which any request against the target rout
    ing controls will fail.
    """
    wait_period_ms: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        control_panel_arn: str | core.StringOut,
        name: str | core.StringOut,
        rule_config: RuleConfig,
        wait_period_ms: int | core.IntOut,
        asserted_controls: list[str] | core.ArrayOut[core.StringOut] | None = None,
        gating_controls: list[str] | core.ArrayOut[core.StringOut] | None = None,
        target_controls: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SafetyRule.Args(
                control_panel_arn=control_panel_arn,
                name=name,
                rule_config=rule_config,
                wait_period_ms=wait_period_ms,
                asserted_controls=asserted_controls,
                gating_controls=gating_controls,
                target_controls=target_controls,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        asserted_controls: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        control_panel_arn: str | core.StringOut = core.arg()

        gating_controls: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rule_config: RuleConfig = core.arg()

        target_controls: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        wait_period_ms: int | core.IntOut = core.arg()
