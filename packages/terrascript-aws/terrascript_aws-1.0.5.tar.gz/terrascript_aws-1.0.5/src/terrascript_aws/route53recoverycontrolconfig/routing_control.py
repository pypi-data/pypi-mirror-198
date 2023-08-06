import terrascript.core as core


@core.resource(
    type="aws_route53recoverycontrolconfig_routing_control",
    namespace="route53recoverycontrolconfig",
)
class RoutingControl(core.Resource):
    """
    ARN of the routing control.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ARN of the cluster in which this routing control will reside.
    """
    cluster_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) ARN of the control panel in which this routing control will reside.
    """
    control_panel_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name describing the routing control.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Status of routing control. `PENDING` when it is being created/updated, `PENDING_DELETION` when it is
    being deleted, and `DEPLOYED` otherwise.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_arn: str | core.StringOut,
        name: str | core.StringOut,
        control_panel_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoutingControl.Args(
                cluster_arn=cluster_arn,
                name=name,
                control_panel_arn=control_panel_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_arn: str | core.StringOut = core.arg()

        control_panel_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
