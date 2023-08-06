import terrascript.core as core


@core.resource(type="aws_iam_role_policy_attachment", namespace="iam")
class RolePolicyAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    policy_arn: str | core.StringOut = core.attr(str)

    role: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy_arn: str | core.StringOut,
        role: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RolePolicyAttachment.Args(
                policy_arn=policy_arn,
                role=role,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy_arn: str | core.StringOut = core.arg()

        role: str | core.StringOut = core.arg()
