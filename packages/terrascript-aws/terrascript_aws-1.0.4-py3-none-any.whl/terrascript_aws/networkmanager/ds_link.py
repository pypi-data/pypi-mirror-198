import terrascript.core as core


@core.schema
class Bandwidth(core.Schema):

    download_speed: int | core.IntOut = core.attr(int, computed=True)

    upload_speed: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        download_speed: int | core.IntOut,
        upload_speed: int | core.IntOut,
    ):
        super().__init__(
            args=Bandwidth.Args(
                download_speed=download_speed,
                upload_speed=upload_speed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        download_speed: int | core.IntOut = core.arg()

        upload_speed: int | core.IntOut = core.arg()


@core.data(type="aws_networkmanager_link", namespace="networkmanager")
class DsLink(core.Data):
    """
    The ARN of the link.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The upload speed and download speed of the link as documented below
    """
    bandwidth: list[Bandwidth] | core.ArrayOut[Bandwidth] = core.attr(
        Bandwidth, computed=True, kind=core.Kind.array
    )

    """
    The description of the link.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Global Network of the link to retrieve.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The id of the specific link to retrieve.
    """
    link_id: str | core.StringOut = core.attr(str)

    """
    The provider of the link.
    """
    provider_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the site.
    """
    site_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the link.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The type of the link.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: str | core.StringOut,
        link_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLink.Args(
                global_network_id=global_network_id,
                link_id=link_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: str | core.StringOut = core.arg()

        link_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
