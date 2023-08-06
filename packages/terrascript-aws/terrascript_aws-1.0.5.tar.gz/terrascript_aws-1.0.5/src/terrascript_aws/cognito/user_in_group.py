import terrascript.core as core


@core.resource(type="aws_cognito_user_in_group", namespace="cognito")
class UserInGroup(core.Resource):
    """
    (Required) The name of the group to which the user is to be added.
    """

    group_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The user pool ID of the user and group.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    """
    (Required) The username of the user to be added to the group.
    """
    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_name: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        username: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserInGroup.Args(
                group_name=group_name,
                user_pool_id=user_pool_id,
                username=username,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_name: str | core.StringOut = core.arg()

        user_pool_id: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()
