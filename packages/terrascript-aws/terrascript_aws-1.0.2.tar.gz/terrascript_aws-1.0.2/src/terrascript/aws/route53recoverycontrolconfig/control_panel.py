import terrascript.core as core


@core.resource(
    type="aws_route53recoverycontrolconfig_control_panel",
    namespace="aws_route53recoverycontrolconfig",
)
class ControlPanel(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_arn: str | core.StringOut = core.attr(str)

    default_control_panel: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    routing_control_count: int | core.IntOut = core.attr(int, computed=True)

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
