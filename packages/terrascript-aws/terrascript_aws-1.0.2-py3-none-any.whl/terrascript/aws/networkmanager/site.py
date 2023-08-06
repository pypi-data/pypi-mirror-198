import terrascript.core as core


@core.schema
class Location(core.Schema):

    address: str | core.StringOut | None = core.attr(str, default=None)

    latitude: str | core.StringOut | None = core.attr(str, default=None)

    longitude: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address: str | core.StringOut | None = None,
        latitude: str | core.StringOut | None = None,
        longitude: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Location.Args(
                address=address,
                latitude=latitude,
                longitude=longitude,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut | None = core.arg(default=None)

        latitude: str | core.StringOut | None = core.arg(default=None)

        longitude: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_networkmanager_site", namespace="aws_networkmanager")
class Site(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    location: Location | None = core.attr(Location, default=None)

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
        global_network_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        location: Location | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Site.Args(
                global_network_id=global_network_id,
                description=description,
                location=location,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        global_network_id: str | core.StringOut = core.arg()

        location: Location | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
