import terrascript.core as core


@core.resource(type="aws_inspector_assessment_target", namespace="inspector")
class AssessmentTarget(core.Resource):
    """
    The target assessment ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the assessment target.
    """
    name: str | core.StringOut = core.attr(str)

    resource_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        resource_group_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AssessmentTarget.Args(
                name=name,
                resource_group_arn=resource_group_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        resource_group_arn: str | core.StringOut | None = core.arg(default=None)
