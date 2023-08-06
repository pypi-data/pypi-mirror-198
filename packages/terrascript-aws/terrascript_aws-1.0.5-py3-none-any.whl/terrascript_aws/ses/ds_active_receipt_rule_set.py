import terrascript.core as core


@core.data(type="aws_ses_active_receipt_rule_set", namespace="ses")
class DsActiveReceiptRuleSet(core.Data):
    """
    The SES receipt rule set ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the rule set
    """
    rule_set_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsActiveReceiptRuleSet.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
