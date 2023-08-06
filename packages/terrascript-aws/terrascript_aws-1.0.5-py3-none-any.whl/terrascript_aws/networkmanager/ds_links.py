import terrascript.core as core


@core.data(type="aws_networkmanager_links", namespace="networkmanager")
class DsLinks(core.Data):
    """
    (Required) The ID of the Global Network of the links to retrieve.
    """

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IDs of the links.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The link provider to retrieve.
    """
    provider_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of the site of the links to retrieve.
    """
    site_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Restricts the list to the links with these tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) The link type to retrieve.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: str | core.StringOut,
        provider_name: str | core.StringOut | None = None,
        site_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLinks.Args(
                global_network_id=global_network_id,
                provider_name=provider_name,
                site_id=site_id,
                tags=tags,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: str | core.StringOut = core.arg()

        provider_name: str | core.StringOut | None = core.arg(default=None)

        site_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
