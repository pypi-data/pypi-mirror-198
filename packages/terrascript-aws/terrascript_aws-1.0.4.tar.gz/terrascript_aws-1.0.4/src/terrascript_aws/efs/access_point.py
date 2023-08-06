import terrascript.core as core


@core.schema
class PosixUser(core.Schema):

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
            args=PosixUser.Args(
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


@core.schema
class CreationInfo(core.Schema):

    owner_gid: int | core.IntOut = core.attr(int)

    owner_uid: int | core.IntOut = core.attr(int)

    permissions: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        owner_gid: int | core.IntOut,
        owner_uid: int | core.IntOut,
        permissions: str | core.StringOut,
    ):
        super().__init__(
            args=CreationInfo.Args(
                owner_gid=owner_gid,
                owner_uid=owner_uid,
                permissions=permissions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        owner_gid: int | core.IntOut = core.arg()

        owner_uid: int | core.IntOut = core.arg()

        permissions: str | core.StringOut = core.arg()


@core.schema
class RootDirectory(core.Schema):

    creation_info: CreationInfo | None = core.attr(CreationInfo, default=None, computed=True)

    path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        creation_info: CreationInfo | None = None,
        path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RootDirectory.Args(
                creation_info=creation_info,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_info: CreationInfo | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_efs_access_point", namespace="efs")
class AccessPoint(core.Resource):
    """
    ARN of the access point.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the file system.
    """
    file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID of the file system for which the access point is intended.
    """
    file_system_id: str | core.StringOut = core.attr(str)

    """
    ID of the access point.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Operating system user and group applied to all file system requests made using the access
    point. [Detailed](#posix_user) below.
    """
    posix_user: PosixUser | None = core.attr(PosixUser, default=None)

    root_directory: RootDirectory | None = core.attr(RootDirectory, default=None, computed=True)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: str | core.StringOut,
        posix_user: PosixUser | None = None,
        root_directory: RootDirectory | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessPoint.Args(
                file_system_id=file_system_id,
                posix_user=posix_user,
                root_directory=root_directory,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        file_system_id: str | core.StringOut = core.arg()

        posix_user: PosixUser | None = core.arg(default=None)

        root_directory: RootDirectory | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
