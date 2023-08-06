import terrascript.core as core


@core.schema
class HomeDirectoryMappings(core.Schema):

    entry: str | core.StringOut = core.attr(str)

    target: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        entry: str | core.StringOut,
        target: str | core.StringOut,
    ):
        super().__init__(
            args=HomeDirectoryMappings.Args(
                entry=entry,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        entry: str | core.StringOut = core.arg()

        target: str | core.StringOut = core.arg()


@core.schema
class PosixProfile(core.Schema):

    gid: int | core.IntOut = core.attr(int)

    secondary_gids: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    uid: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        gid: int | core.IntOut,
        uid: int | core.IntOut,
        secondary_gids: list[int] | core.ArrayOut[core.IntOut] | None = None,
    ):
        super().__init__(
            args=PosixProfile.Args(
                gid=gid,
                uid=uid,
                secondary_gids=secondary_gids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        gid: int | core.IntOut = core.arg()

        secondary_gids: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(default=None)

        uid: int | core.IntOut = core.arg()


@core.resource(type="aws_transfer_user", namespace="aws_transfer")
class User(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    home_directory: str | core.StringOut | None = core.attr(str, default=None)

    home_directory_mappings: list[HomeDirectoryMappings] | core.ArrayOut[
        HomeDirectoryMappings
    ] | None = core.attr(HomeDirectoryMappings, default=None, kind=core.Kind.array)

    home_directory_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None)

    posix_profile: PosixProfile | None = core.attr(PosixProfile, default=None)

    role: str | core.StringOut = core.attr(str)

    server_id: str | core.StringOut = core.attr(str)

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
        role: str | core.StringOut,
        server_id: str | core.StringOut,
        user_name: str | core.StringOut,
        home_directory: str | core.StringOut | None = None,
        home_directory_mappings: list[HomeDirectoryMappings]
        | core.ArrayOut[HomeDirectoryMappings]
        | None = None,
        home_directory_type: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        posix_profile: PosixProfile | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                role=role,
                server_id=server_id,
                user_name=user_name,
                home_directory=home_directory,
                home_directory_mappings=home_directory_mappings,
                home_directory_type=home_directory_type,
                policy=policy,
                posix_profile=posix_profile,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        home_directory: str | core.StringOut | None = core.arg(default=None)

        home_directory_mappings: list[HomeDirectoryMappings] | core.ArrayOut[
            HomeDirectoryMappings
        ] | None = core.arg(default=None)

        home_directory_type: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        posix_profile: PosixProfile | None = core.arg(default=None)

        role: str | core.StringOut = core.arg()

        server_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
