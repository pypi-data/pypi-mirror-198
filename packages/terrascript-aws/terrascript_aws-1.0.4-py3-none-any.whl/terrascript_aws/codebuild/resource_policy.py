import terrascript.core as core


@core.resource(type="aws_codebuild_resource_policy", namespace="codebuild")
class ResourcePolicy(core.Resource):
    """
    The ARN of Resource.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A JSON-formatted resource policy. For more information, see [Sharing a Projec](https://do
    cs.aws.amazon.com/codebuild/latest/userguide/project-sharing.html#project-sharing-share) and [Sharin
    g a Report Group](https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing.html#
    report-groups-sharing-share).
    """
    policy: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of the Project or ReportGroup resource you want to associate with a resource poli
    cy.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        resource_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourcePolicy.Args(
                policy=policy,
                resource_arn=resource_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()
