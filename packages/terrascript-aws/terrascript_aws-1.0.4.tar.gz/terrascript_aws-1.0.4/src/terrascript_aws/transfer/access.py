import terrascript.core as core


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


@core.resource(type="aws_transfer_access", namespace="transfer")
class Access(core.Resource):
    """
    (Required) The SID of a group in the directory connected to the Transfer Server (e.g., `S-1-1-12-123
    4567890-123456789-1234567890-1234`)
    """

    external_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The landing directory (folder) for a user when they log in to the server using their SFTP
    client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (ac
    cessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible a
    s `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set
    the home bucket to `example-bucket-1234` and the home directory to `username`.
    """
    home_directory: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Logical directory mappings that specify what S3 paths and keys should be visible to your
    user and how you want to make them visible. See [Home Directory Mappings](#home-directory-mappings)
    below.
    """
    home_directory_mappings: list[HomeDirectoryMappings] | core.ArrayOut[
        HomeDirectoryMappings
    ] | None = core.attr(HomeDirectoryMappings, default=None, kind=core.Kind.array)

    """
    (Optional) The type of landing directory (folder) you mapped for your users' home directory. Valid v
    alues are `PATH` and `LOGICAL`.
    """
    home_directory_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An IAM JSON policy document that scopes down user access to portions of their Amazon S3 b
    ucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:Home
    Directory}`, and `${Transfer:HomeBucket}`. Since the IAM variable syntax matches Terraform's interpo
    lation syntax, they must be escaped inside Terraform configuration strings (`$${Transfer:UserName}`)
    .  These are evaluated on-the-fly when navigating the bucket.
    """
    policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the full POSIX identity, including user ID (Uid), group ID (Gid), and any secon
    dary groups IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. S
    ee [Posix Profile](#posix-profile) below.
    """
    posix_profile: PosixProfile | None = core.attr(PosixProfile, default=None)

    """
    (Required) Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s
    access to your Amazon S3 bucket.
    """
    role: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The Server ID of the Transfer Server (e.g., `s-12345678`)
    """
    server_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        external_id: str | core.StringOut,
        server_id: str | core.StringOut,
        home_directory: str | core.StringOut | None = None,
        home_directory_mappings: list[HomeDirectoryMappings]
        | core.ArrayOut[HomeDirectoryMappings]
        | None = None,
        home_directory_type: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        posix_profile: PosixProfile | None = None,
        role: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Access.Args(
                external_id=external_id,
                server_id=server_id,
                home_directory=home_directory,
                home_directory_mappings=home_directory_mappings,
                home_directory_type=home_directory_type,
                policy=policy,
                posix_profile=posix_profile,
                role=role,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        external_id: str | core.StringOut = core.arg()

        home_directory: str | core.StringOut | None = core.arg(default=None)

        home_directory_mappings: list[HomeDirectoryMappings] | core.ArrayOut[
            HomeDirectoryMappings
        ] | None = core.arg(default=None)

        home_directory_type: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        posix_profile: PosixProfile | None = core.arg(default=None)

        role: str | core.StringOut | None = core.arg(default=None)

        server_id: str | core.StringOut = core.arg()
