import terrascript.core as core


@core.data(type="aws_waf_rate_based_rule", namespace="waf")
class DsRateBasedRule(core.Data):
    """
    The ID of the WAF rate based rule.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the WAF rate based rule.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsRateBasedRule.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
