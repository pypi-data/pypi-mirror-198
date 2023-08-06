import terrascript.core as core


@core.schema
class Location(core.Schema):

    address: str | core.StringOut = core.attr(str, computed=True)

    latitude: str | core.StringOut = core.attr(str, computed=True)

    longitude: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        latitude: str | core.StringOut,
        longitude: str | core.StringOut,
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
        address: str | core.StringOut = core.arg()

        latitude: str | core.StringOut = core.arg()

        longitude: str | core.StringOut = core.arg()


@core.data(type="aws_networkmanager_site", namespace="networkmanager")
class DsSite(core.Data):
    """
    The ARN of the site.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the site.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Global Network of the site to retrieve.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The site location as documented below.
    """
    location: list[Location] | core.ArrayOut[Location] = core.attr(
        Location, computed=True, kind=core.Kind.array
    )

    """
    (Required) The id of the specific site to retrieve.
    """
    site_id: str | core.StringOut = core.attr(str)

    """
    Key-value tags for the Site.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: str | core.StringOut,
        site_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSite.Args(
                global_network_id=global_network_id,
                site_id=site_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: str | core.StringOut = core.arg()

        site_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
