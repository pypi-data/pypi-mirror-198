import terrascript.core as core


@core.resource(
    type="aws_route53recoverycontrolconfig_routing_control",
    namespace="aws_route53recoverycontrolconfig",
)
class RoutingControl(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_arn: str | core.StringOut = core.attr(str)

    control_panel_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

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
