import terrascript.core as core


@core.resource(type="aws_datasync_location_fsx_windows_file_system", namespace="aws_datasync")
class LocationFsxWindowsFileSystem(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    creation_time: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut | None = core.attr(str, default=None)

    fsx_filesystem_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    password: str | core.StringOut = core.attr(str)

    security_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subdirectory: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    uri: str | core.StringOut = core.attr(str, computed=True)

    user: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        fsx_filesystem_arn: str | core.StringOut,
        password: str | core.StringOut,
        security_group_arns: list[str] | core.ArrayOut[core.StringOut],
        user: str | core.StringOut,
        domain: str | core.StringOut | None = None,
        subdirectory: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationFsxWindowsFileSystem.Args(
                fsx_filesystem_arn=fsx_filesystem_arn,
                password=password,
                security_group_arns=security_group_arns,
                user=user,
                domain=domain,
                subdirectory=subdirectory,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain: str | core.StringOut | None = core.arg(default=None)

        fsx_filesystem_arn: str | core.StringOut = core.arg()

        password: str | core.StringOut = core.arg()

        security_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subdirectory: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user: str | core.StringOut = core.arg()
