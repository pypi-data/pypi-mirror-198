import terrascript.core as core


@core.data(type="aws_region", namespace="meta_data_sources")
class DsRegion(core.Data):
    """
    The region's description in this format: "Location (Region name)".
    """

    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The EC2 endpoint of the region to select.
    """
    endpoint: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The full name of the region to select.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        endpoint: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRegion.Args(
                endpoint=endpoint,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
