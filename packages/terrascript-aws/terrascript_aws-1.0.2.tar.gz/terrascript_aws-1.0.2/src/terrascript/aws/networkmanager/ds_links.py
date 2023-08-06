import terrascript.core as core


@core.data(type="aws_networkmanager_links", namespace="aws_networkmanager")
class DsLinks(core.Data):

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    provider_name: str | core.StringOut | None = core.attr(str, default=None)

    site_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
