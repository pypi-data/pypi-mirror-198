import terrascript.core as core


@core.resource(type="aws_ssoadmin_managed_policy_attachment", namespace="ssoadmin")
class ManagedPolicyAttachment(core.Resource):
    """
    The Amazon Resource Names (ARNs) of the Managed Policy, Permission Set, and SSO Instance, separated
    by a comma (`,`).
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the SSO Instance under which the o
    peration will be executed.
    """
    instance_arn: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The IAM managed policy Amazon Resource Name (ARN) to be attached to
    the Permission Set.
    """
    managed_policy_arn: str | core.StringOut = core.attr(str)

    """
    The name of the IAM Managed Policy.
    """
    managed_policy_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the Permission Set.
    """
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
