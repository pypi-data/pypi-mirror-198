import terrascript.core as core


@core.resource(type="aws_ssoadmin_account_assignment", namespace="aws_ssoadmin")
class AccountAssignment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_arn: str | core.StringOut = core.attr(str)

    permission_set_arn: str | core.StringOut = core.attr(str)

    principal_id: str | core.StringOut = core.attr(str)

    principal_type: str | core.StringOut = core.attr(str)

    target_id: str | core.StringOut = core.attr(str)

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
