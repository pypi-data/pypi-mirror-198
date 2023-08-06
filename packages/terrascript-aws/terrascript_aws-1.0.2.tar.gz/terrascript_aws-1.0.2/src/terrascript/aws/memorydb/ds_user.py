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


@core.data(type="aws_memorydb_user", namespace="aws_memorydb")
class DsUser(core.Data):

    access_string: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_mode: list[AuthenticationMode] | core.ArrayOut[AuthenticationMode] = core.attr(
        AuthenticationMode, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    minimum_engine_version: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
