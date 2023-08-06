import terrascript.core as core


@core.resource(type="aws_opsworks_permission", namespace="opsworks")
class Permission(core.Resource):
    """
    (Optional) Whether the user is allowed to use SSH to communicate with the instance
    """

    allow_ssh: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Whether the user is allowed to use sudo to elevate privileges
    """
    allow_sudo: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The computed id of the permission. Please note that this is only used internally to identify the per
    mission. This value is not used in aws.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`
    """
    level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The stack to set the permissions for
    """
    stack_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The user's IAM ARN to set permissions for
    """
    user_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_arn: str | core.StringOut,
        allow_ssh: bool | core.BoolOut | None = None,
        allow_sudo: bool | core.BoolOut | None = None,
        level: str | core.StringOut | None = None,
        stack_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                user_arn=user_arn,
                allow_ssh=allow_ssh,
                allow_sudo=allow_sudo,
                level=level,
                stack_id=stack_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_ssh: bool | core.BoolOut | None = core.arg(default=None)

        allow_sudo: bool | core.BoolOut | None = core.arg(default=None)

        level: str | core.StringOut | None = core.arg(default=None)

        stack_id: str | core.StringOut | None = core.arg(default=None)

        user_arn: str | core.StringOut = core.arg()
