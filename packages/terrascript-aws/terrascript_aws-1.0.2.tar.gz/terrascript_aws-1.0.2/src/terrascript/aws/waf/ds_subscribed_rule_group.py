import terrascript.core as core


@core.data(type="aws_waf_subscribed_rule_group", namespace="aws_waf")
class DsSubscribedRuleGroup(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    metric_name: str | core.StringOut | None = core.attr(str, default=None)

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
