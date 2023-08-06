import terrascript.core as core


@core.resource(type="aws_cognito_user_group", namespace="cognito")
class UserGroup(core.Resource):
    """
    (Optional) The description of the user group.
    """

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the user group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The precedence of the user group.
    """
    precedence: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The ARN of the IAM role to be associated with the user group.
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The user pool ID.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        precedence: int | core.IntOut | None = None,
        role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroup.Args(
                name=name,
                user_pool_id=user_pool_id,
                description=description,
                precedence=precedence,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        precedence: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        user_pool_id: str | core.StringOut = core.arg()
