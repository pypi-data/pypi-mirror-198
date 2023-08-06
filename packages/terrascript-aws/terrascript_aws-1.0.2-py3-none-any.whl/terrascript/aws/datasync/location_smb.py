import terrascript.core as core


@core.schema
class MountOptions(core.Schema):

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MountOptions.Args(
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        version: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_datasync_location_smb", namespace="aws_datasync")
class LocationSmb(core.Resource):

    agent_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    arn: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    mount_options: MountOptions | None = core.attr(MountOptions, default=None)

    password: str | core.StringOut = core.attr(str)

    server_hostname: str | core.StringOut = core.attr(str)

    subdirectory: str | core.StringOut = core.attr(str)

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
        agent_arns: list[str] | core.ArrayOut[core.StringOut],
        password: str | core.StringOut,
        server_hostname: str | core.StringOut,
        subdirectory: str | core.StringOut,
        user: str | core.StringOut,
        domain: str | core.StringOut | None = None,
        mount_options: MountOptions | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationSmb.Args(
                agent_arns=agent_arns,
                password=password,
                server_hostname=server_hostname,
                subdirectory=subdirectory,
                user=user,
                domain=domain,
                mount_options=mount_options,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        agent_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        domain: str | core.StringOut | None = core.arg(default=None)

        mount_options: MountOptions | None = core.arg(default=None)

        password: str | core.StringOut = core.arg()

        server_hostname: str | core.StringOut = core.arg()

        subdirectory: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user: str | core.StringOut = core.arg()
