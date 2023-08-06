import terrascript.core as core


@core.resource(type="aws_securityhub_standards_control", namespace="securityhub")
class StandardsControl(core.Resource):

    control_id: str | core.StringOut = core.attr(str, computed=True)

    control_status: str | core.StringOut = core.attr(str)

    control_status_updated_at: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    disabled_reason: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    related_requirements: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    remediation_url: str | core.StringOut = core.attr(str, computed=True)

    severity_rating: str | core.StringOut = core.attr(str, computed=True)

    standards_control_arn: str | core.StringOut = core.attr(str)

    title: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        control_status: str | core.StringOut,
        standards_control_arn: str | core.StringOut,
        disabled_reason: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StandardsControl.Args(
                control_status=control_status,
                standards_control_arn=standards_control_arn,
                disabled_reason=disabled_reason,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        control_status: str | core.StringOut = core.arg()

        disabled_reason: str | core.StringOut | None = core.arg(default=None)

        standards_control_arn: str | core.StringOut = core.arg()
