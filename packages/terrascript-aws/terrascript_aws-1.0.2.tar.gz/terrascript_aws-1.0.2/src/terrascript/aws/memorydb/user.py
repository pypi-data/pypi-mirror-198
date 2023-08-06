import terrascript.core as core


@core.schema
class AuthenticationMode(core.Schema):

    password_count: int | core.IntOut = core.attr(int, computed=True)

    passwords: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password_count: int | core.IntOut,
        passwords: list[str] | core.ArrayOut[core.StringOut],
        type: str | core.StringOut,
    ):
        super().__init__(
            args=AuthenticationMode.Args(
                password_count=password_count,
                passwords=passwords,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password_count: int | core.IntOut = core.arg()

        passwords: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_memorydb_user", namespace="aws_memorydb")
class User(core.Resource):

    access_string: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_mode: AuthenticationMode = core.attr(AuthenticationMode)

    id: str | core.StringOut = core.attr(str, computed=True)

    minimum_engine_version: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        access_string: str | core.StringOut,
        authentication_mode: AuthenticationMode,
        user_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                access_string=access_string,
                authentication_mode=authentication_mode,
                user_name=user_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_string: str | core.StringOut = core.arg()

        authentication_mode: AuthenticationMode = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
