import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_resource_policy", namespace="aws_cloudwatch")
class LogResourcePolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    policy_document: str | core.StringOut = core.attr(str)

    policy_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy_document: str | core.StringOut,
        policy_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogResourcePolicy.Args(
                policy_document=policy_document,
                policy_name=policy_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy_document: str | core.StringOut = core.arg()

        policy_name: str | core.StringOut = core.arg()
