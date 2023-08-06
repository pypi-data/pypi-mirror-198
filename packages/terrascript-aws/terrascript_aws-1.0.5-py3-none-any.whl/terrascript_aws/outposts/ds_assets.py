import terrascript.core as core


@core.data(type="aws_outposts_assets", namespace="outposts")
class DsAssets(core.Data):
    """
    (Required) Outpost ARN.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    A list of all the subnet ids found. This data source will fail if none are found.
    """
    asset_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsAssets.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()
