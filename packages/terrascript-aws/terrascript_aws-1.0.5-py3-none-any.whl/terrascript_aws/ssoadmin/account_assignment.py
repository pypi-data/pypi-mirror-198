import terrascript.core as core


@core.resource(type="aws_ssoadmin_account_assignment", namespace="ssoadmin")
class AccountAssignment(core.Resource):
    """
    The identifier of the Account Assignment i.e., `principal_id`, `principal_type`, `target_id`, `targe
    t_type`, `permission_set_arn`, `instance_arn` separated by commas (`,`).
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the SSO Instance.
    """
    instance_arn: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the Permission Set that the admin
    wants to grant the principal access to.
    """
    permission_set_arn: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) An identifier for an object in SSO, such as a user or group. Princip
    alIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
    """
    principal_id: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The entity type for which the assignment will be created. Valid valu
    es: `USER`, `GROUP`.
    """
    principal_type: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) An AWS account identifier, typically a 10-12 digit string.
    """
    target_id: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The entity type for which the assignment will be created. Valid valu
    es: `AWS_ACCOUNT`.
    """
    target_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_arn: str | core.StringOut,
        permission_set_arn: str | core.StringOut,
        principal_id: str | core.StringOut,
        principal_type: str | core.StringOut,
        target_id: str | core.StringOut,
        target_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccountAssignment.Args(
                instance_arn=instance_arn,
                permission_set_arn=permission_set_arn,
                principal_id=principal_id,
                principal_type=principal_type,
                target_id=target_id,
                target_type=target_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_arn: str | core.StringOut = core.arg()

        permission_set_arn: str | core.StringOut = core.arg()

        principal_id: str | core.StringOut = core.arg()

        principal_type: str | core.StringOut = core.arg()

        target_id: str | core.StringOut = core.arg()

        target_type: str | core.StringOut | None = core.arg(default=None)
