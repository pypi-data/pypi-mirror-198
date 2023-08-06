import terrascript.core as core


@core.resource(type="aws_securityhub_standards_subscription", namespace="aws_securityhub")
class StandardsSubscription(core.Resource):
    """
    The ARN of a resource that represents your subscription to a supported standard.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of a standard - see below.
    """
    standards_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        standards_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StandardsSubscription.Args(
                standards_arn=standards_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        standards_arn: str | core.StringOut = core.arg()
