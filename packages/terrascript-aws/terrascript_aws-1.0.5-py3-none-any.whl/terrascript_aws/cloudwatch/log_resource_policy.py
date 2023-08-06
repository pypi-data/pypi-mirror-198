import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_resource_policy", namespace="cloudwatch")
class LogResourcePolicy(core.Resource):
    """
    The name of the CloudWatch log resource policy
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Details of the resource policy, including the identity of the principal that is enabled t
    o put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.
    """
    policy_document: str | core.StringOut = core.attr(str)

    """
    (Required) Name of the resource policy.
    """
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
