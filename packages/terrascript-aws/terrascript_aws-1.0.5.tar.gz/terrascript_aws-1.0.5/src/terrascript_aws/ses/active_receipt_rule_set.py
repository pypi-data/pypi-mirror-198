import terrascript.core as core


@core.resource(type="aws_ses_active_receipt_rule_set", namespace="ses")
class ActiveReceiptRuleSet(core.Resource):
    """
    The SES receipt rule set ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The SES receipt rule set name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the rule set
    """
    rule_set_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        rule_set_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ActiveReceiptRuleSet.Args(
                rule_set_name=rule_set_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        rule_set_name: str | core.StringOut = core.arg()
