import terrascript.core as core


@core.schema
class IngestEndpoints(core.Schema):

    password: str | core.StringOut = core.attr(str, computed=True)

    url: str | core.StringOut = core.attr(str, computed=True)

    username: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        url: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=IngestEndpoints.Args(
                password=password,
                url=url,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        url: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class HlsIngest(core.Schema):

    ingest_endpoints: list[IngestEndpoints] | core.ArrayOut[IngestEndpoints] = core.attr(
        IngestEndpoints, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ingest_endpoints: list[IngestEndpoints] | core.ArrayOut[IngestEndpoints],
    ):
        super().__init__(
            args=HlsIngest.Args(
                ingest_endpoints=ingest_endpoints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ingest_endpoints: list[IngestEndpoints] | core.ArrayOut[IngestEndpoints] = core.arg()


@core.resource(type="aws_media_package_channel", namespace="aws_elemental_mediapackage")
class MediaPackageChannel(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    channel_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    hls_ingest: list[HlsIngest] | core.ArrayOut[HlsIngest] = core.attr(
        HlsIngest, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        channel_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MediaPackageChannel.Args(
                channel_id=channel_id,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        channel_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
