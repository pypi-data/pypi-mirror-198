import terrascript.core as core


@core.resource(type="aws_ssoadmin_managed_policy_attachment", namespace="aws_ssoadmin")
class ManagedPolicyAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_arn: str | core.StringOut = core.attr(str)

    managed_policy_arn: str | core.StringOut = core.attr(str)

    managed_policy_name: str | core.StringOut = core.attr(str, computed=True)

    permission_set_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_arn: str | core.StringOut,
        managed_policy_arn: str | core.StringOut,
        permission_set_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ManagedPolicyAttachment.Args(
                instance_arn=instance_arn,
                managed_policy_arn=managed_policy_arn,
                permission_set_arn=permission_set_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_arn: str | core.StringOut = core.arg()

        managed_policy_arn: str | core.StringOut = core.arg()

        permission_set_arn: str | core.StringOut = core.arg()
