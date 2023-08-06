import terrascript.core as core


@core.resource(
    type="aws_route53recoverycontrolconfig_control_panel", namespace="route53recoverycontrolconfig"
)
class ControlPanel(core.Resource):
    """
    ARN of the control panel.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ARN of the cluster in which this control panel will reside.
    """
    cluster_arn: str | core.StringOut = core.attr(str)

    """
    Whether a control panel is default.
    """
    default_control_panel: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name describing the control panel.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Number routing controls in a control panel.
    """
    routing_control_count: int | core.IntOut = core.attr(int, computed=True)

    """
    Status of control panel: `PENDING` when it is being created/updated, `PENDING_DELETION` when it is b
    eing deleted, and `DEPLOYED` otherwise.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_arn: str | core.StringOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ControlPanel.Args(
                cluster_arn=cluster_arn,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
