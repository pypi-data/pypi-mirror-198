import terrascript.core as core


@core.data(type="aws_wafregional_rule", namespace="wafregional")
class DsRule(core.Data):
    """
    The ID of the WAF Regional rule.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the WAF Regional rule.
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
