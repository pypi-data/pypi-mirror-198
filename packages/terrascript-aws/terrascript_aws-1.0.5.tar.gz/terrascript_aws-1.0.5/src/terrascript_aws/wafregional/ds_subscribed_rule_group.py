import terrascript.core as core


@core.data(type="aws_wafregional_subscribed_rule_group", namespace="wafregional")
class DsSubscribedRuleGroup(core.Data):
    """
    The ID of the WAF rule group.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the WAF rule group.
    """
    metric_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the WAF rule group.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        metric_name: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSubscribedRuleGroup.Args(
                metric_name=metric_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
