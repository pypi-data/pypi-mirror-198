import terrascript.core as core


@core.resource(type="aws_iam_group_policy_attachment", namespace="iam")
class GroupPolicyAttachment(core.Resource):

    group: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group: str | core.StringOut,
        policy_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupPolicyAttachment.Args(
                group=group,
                policy_arn=policy_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group: str | core.StringOut = core.arg()

        policy_arn: str | core.StringOut = core.arg()
