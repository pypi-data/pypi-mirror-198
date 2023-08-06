import terrascript.core as core


@core.resource(type="aws_directory_service_radius_settings", namespace="ds")
class DirectoryServiceRadiusSettings(core.Resource):

    authentication_protocol: str | core.StringOut = core.attr(str)

    directory_id: str | core.StringOut = core.attr(str)

    display_label: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    radius_port: int | core.IntOut = core.attr(int)

    radius_retries: int | core.IntOut = core.attr(int)

    radius_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    radius_timeout: int | core.IntOut = core.attr(int)

    shared_secret: str | core.StringOut = core.attr(str)

    use_same_username: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_protocol: str | core.StringOut,
        directory_id: str | core.StringOut,
        display_label: str | core.StringOut,
        radius_port: int | core.IntOut,
        radius_retries: int | core.IntOut,
        radius_servers: list[str] | core.ArrayOut[core.StringOut],
        radius_timeout: int | core.IntOut,
        shared_secret: str | core.StringOut,
        use_same_username: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceRadiusSettings.Args(
                authentication_protocol=authentication_protocol,
                directory_id=directory_id,
                display_label=display_label,
                radius_port=radius_port,
                radius_retries=radius_retries,
                radius_servers=radius_servers,
                radius_timeout=radius_timeout,
                shared_secret=shared_secret,
                use_same_username=use_same_username,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_protocol: str | core.StringOut = core.arg()

        directory_id: str | core.StringOut = core.arg()

        display_label: str | core.StringOut = core.arg()

        radius_port: int | core.IntOut = core.arg()

        radius_retries: int | core.IntOut = core.arg()

        radius_servers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        radius_timeout: int | core.IntOut = core.arg()

        shared_secret: str | core.StringOut = core.arg()

        use_same_username: bool | core.BoolOut | None = core.arg(default=None)
