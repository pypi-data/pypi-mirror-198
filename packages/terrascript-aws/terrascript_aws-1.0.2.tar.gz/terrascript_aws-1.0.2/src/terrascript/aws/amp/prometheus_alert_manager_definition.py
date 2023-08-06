import terrascript.core as core


@core.resource(type="aws_prometheus_alert_manager_definition", namespace="aws_amp")
class PrometheusAlertManagerDefinition(core.Resource):

    definition: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        definition: str | core.StringOut,
        workspace_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PrometheusAlertManagerDefinition.Args(
                definition=definition,
                workspace_id=workspace_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        definition: str | core.StringOut = core.arg()

        workspace_id: str | core.StringOut = core.arg()
