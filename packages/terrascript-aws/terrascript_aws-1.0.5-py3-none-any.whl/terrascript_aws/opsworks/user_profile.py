import terrascript.core as core


@core.resource(type="aws_opsworks_user_profile", namespace="opsworks")
class UserProfile(core.Resource):
    """
    (Optional) Whether users can specify their own SSH public key through the My Settings page
    """

    allow_self_management: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Same value as `user_arn`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The users public key
    """
    ssh_public_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ssh username, with witch this user wants to log in
    """
    ssh_username: str | core.StringOut = core.attr(str)

    """
    (Required) The user's IAM ARN
    """
    user_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ssh_username: str | core.StringOut,
        user_arn: str | core.StringOut,
        allow_self_management: bool | core.BoolOut | None = None,
        ssh_public_key: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserProfile.Args(
                ssh_username=ssh_username,
                user_arn=user_arn,
                allow_self_management=allow_self_management,
                ssh_public_key=ssh_public_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_self_management: bool | core.BoolOut | None = core.arg(default=None)

        ssh_public_key: str | core.StringOut | None = core.arg(default=None)

        ssh_username: str | core.StringOut = core.arg()

        user_arn: str | core.StringOut = core.arg()
