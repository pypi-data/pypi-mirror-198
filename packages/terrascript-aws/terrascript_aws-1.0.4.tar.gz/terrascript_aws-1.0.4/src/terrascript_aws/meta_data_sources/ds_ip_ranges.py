import terrascript.core as core


@core.data(type="aws_ip_ranges", namespace="meta_data_sources")
class DsIpRanges(core.Data):
    """
    The lexically ordered list of CIDR blocks.
    """

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The publication time of the IP ranges (e.g., `2016-08-03-23-46-05`).
    """
    create_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The lexically ordered list of IPv6 CIDR blocks.
    """
    ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Filter IP ranges by regions (or include all regions, if
    """
    regions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) Filter IP ranges by services. Valid items are `amazon`
    """
    services: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    The publication time of the IP ranges, in Unix epoch time format
    """
    sync_token: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Custom URL for source JSON file. Syntax must match [AWS IP Address Ranges documentation][
    1]. Defaults to `https://ip-ranges.amazonaws.com/ip-ranges.json`.
    """
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
