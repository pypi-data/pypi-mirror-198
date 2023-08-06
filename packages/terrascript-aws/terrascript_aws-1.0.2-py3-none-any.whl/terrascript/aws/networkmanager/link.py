import terrascript.core as core


@core.schema
class Bandwidth(core.Schema):

    download_speed: int | core.IntOut | None = core.attr(int, default=None)

    upload_speed: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        download_speed: int | core.IntOut | None = None,
        upload_speed: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Bandwidth.Args(
                download_speed=download_speed,
                upload_speed=upload_speed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        download_speed: int | core.IntOut | None = core.arg(default=None)

        upload_speed: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_networkmanager_link", namespace="aws_networkmanager")
class Link(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bandwidth: Bandwidth = core.attr(Bandwidth)

    description: str | core.StringOut | None = core.attr(str, default=None)

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    provider_name: str | core.StringOut | None = core.attr(str, default=None)

    site_id: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: Bandwidth,
        global_network_id: str | core.StringOut,
        site_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        provider_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Link.Args(
                bandwidth=bandwidth,
                global_network_id=global_network_id,
                site_id=site_id,
                description=description,
                provider_name=provider_name,
                tags=tags,
                tags_all=tags_all,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: Bandwidth = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        global_network_id: str | core.StringOut = core.arg()

        provider_name: str | core.StringOut | None = core.arg(default=None)

        site_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
