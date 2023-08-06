import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_regions", namespace="meta_data_sources")
class DsRegions(core.Data):
    """
    (Optional) If true the source will query all regions regardless of availability.
    """

    all_regions: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configuration block(s) to use as filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    Identifier of the current partition (e.g., `aws` in AWS Commercial, `aws-cn` in AWS China).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Names of regions that meets the criteria.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        all_regions: bool | core.BoolOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRegions.Args(
                all_regions=all_regions,
                filter=filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_regions: bool | core.BoolOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)
