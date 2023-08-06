import terrascript.core as core


@core.schema
class PosixUser(core.Schema):

    gid: int | core.IntOut = core.attr(int, computed=True)

    secondary_gids: list[int] | core.ArrayOut[core.IntOut] = core.attr(
        int, computed=True, kind=core.Kind.array
    )

    uid: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        gid: int | core.IntOut,
        secondary_gids: list[int] | core.ArrayOut[core.IntOut],
        uid: int | core.IntOut,
    ):
        super().__init__(
            args=PosixUser.Args(
                gid=gid,
                secondary_gids=secondary_gids,
                uid=uid,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        gid: int | core.IntOut = core.arg()

        secondary_gids: list[int] | core.ArrayOut[core.IntOut] = core.arg()

        uid: int | core.IntOut = core.arg()


@core.schema
class CreationInfo(core.Schema):

    owner_gid: int | core.IntOut = core.attr(int, computed=True)

    owner_uid: int | core.IntOut = core.attr(int, computed=True)

    permissions: str | core.StringOut = core.attr(str, computed=True)

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

    creation_info: list[CreationInfo] | core.ArrayOut[CreationInfo] = core.attr(
        CreationInfo, computed=True, kind=core.Kind.array
    )

    path: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        creation_info: list[CreationInfo] | core.ArrayOut[CreationInfo],
        path: str | core.StringOut,
    ):
        super().__init__(
            args=RootDirectory.Args(
                creation_info=creation_info,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_info: list[CreationInfo] | core.ArrayOut[CreationInfo] = core.arg()

        path: str | core.StringOut = core.arg()


@core.data(type="aws_efs_access_point", namespace="efs")
class DsAccessPoint(core.Data):
    """
    (Required) The ID that identifies the file system.
    """

    access_point_id: str | core.StringOut = core.attr(str)

    """
    Amazon Resource Name of the file system.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name of the file system.
    """
    file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the file system for which the access point is intended.
    """
    file_system_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the access point.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Single element list containing operating system user and group applied to all file system requests m
    ade using the access point.
    """
    posix_user: list[PosixUser] | core.ArrayOut[PosixUser] = core.attr(
        PosixUser, computed=True, kind=core.Kind.array
    )

    root_directory: list[RootDirectory] | core.ArrayOut[RootDirectory] = core.attr(
        RootDirectory, computed=True, kind=core.Kind.array
    )

    """
    Key-value mapping of resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        access_point_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAccessPoint.Args(
                access_point_id=access_point_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_point_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
