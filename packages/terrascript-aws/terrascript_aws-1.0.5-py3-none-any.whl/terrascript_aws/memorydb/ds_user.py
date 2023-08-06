import terrascript.core as core


@core.schema
class AuthenticationMode(core.Schema):

    password_count: int | core.IntOut = core.attr(int, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        password_count: int | core.IntOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=AuthenticationMode.Args(
                password_count=password_count,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password_count: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.data(type="aws_memorydb_user", namespace="memorydb")
class DsUser(core.Data):
    """
    The access permissions string used for this user.
    """

    access_string: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the user.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Denotes the user's authentication properties.
    """
    authentication_mode: list[AuthenticationMode] | core.ArrayOut[AuthenticationMode] = core.attr(
        AuthenticationMode, computed=True, kind=core.Kind.array
    )

    """
    Name of the user.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The minimum engine version supported for the user.
    """
    minimum_engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the subnet group.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) Name of the user.
    """
    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        user_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUser.Args(
                user_name=user_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
