import terrascript.core as core


@core.data(type="aws_outposts_asset", namespace="aws_outposts")
class DsAsset(core.Data):

    arn: str | core.StringOut = core.attr(str)

    asset_id: str | core.StringOut = core.attr(str)

    asset_type: str | core.StringOut = core.attr(str, computed=True)

    host_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    rack_elevation: int | core.IntOut = core.attr(int, computed=True)

    rack_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        asset_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsAsset.Args(
                arn=arn,
                asset_id=asset_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        asset_id: str | core.StringOut = core.arg()
