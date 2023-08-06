import terrascript.core as core


@core.data(type="aws_waf_rule", namespace="waf")
class DsRule(core.Data):
    """
    The ID of the WAF rule.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the WAF rule.
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
            args=DsRule.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
