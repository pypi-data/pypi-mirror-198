import terrascript.core as core


@core.resource(type="aws_prometheus_alert_manager_definition", namespace="amp")
class PrometheusAlertManagerDefinition(core.Resource):
    """
    (Required) the alert manager definition that you want to be applied. See more [in AWS Docs](https://
    docs.aws.amazon.com/prometheus/latest/userguide/AMP-alert-manager.html).
    """

    definition: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The id of the prometheus workspace the alert manager definition should be linked to
    """
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
