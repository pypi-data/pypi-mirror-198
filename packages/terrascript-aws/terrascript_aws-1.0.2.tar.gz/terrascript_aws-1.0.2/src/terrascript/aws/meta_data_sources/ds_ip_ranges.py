import terrascript.core as core


@core.data(type="aws_ip_ranges", namespace="aws_meta_data_sources")
class DsIpRanges(core.Data):

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    create_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    services: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    sync_token: int | core.IntOut = core.attr(int, computed=True)

    url: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        services: list[str] | core.ArrayOut[core.StringOut],
        regions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        url: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsIpRanges.Args(
                services=services,
                regions=regions,
                url=url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        regions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        services: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        url: str | core.StringOut | None = core.arg(default=None)
