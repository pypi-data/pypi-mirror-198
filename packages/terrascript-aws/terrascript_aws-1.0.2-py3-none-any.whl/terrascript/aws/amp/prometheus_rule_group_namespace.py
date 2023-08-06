import terrascript.core as core


@core.resource(type="aws_prometheus_rule_group_namespace", namespace="aws_amp")
class PrometheusRuleGroupNamespace(core.Resource):

    data: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        data: str | core.StringOut,
        name: str | core.StringOut,
        workspace_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PrometheusRuleGroupNamespace.Args(
                data=data,
                name=name,
                workspace_id=workspace_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        data: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        workspace_id: str | core.StringOut = core.arg()
