import terrascript.core as core


@core.data(type="aws_outposts_asset", namespace="outposts")
class DsAsset(core.Data):
    """
    (Required) Outpost ARN.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the asset.
    """
    asset_id: str | core.StringOut = core.attr(str)

    """
    The type of the asset.
    """
    asset_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The host ID of the Dedicated Hosts on the asset, if a Dedicated Host is provisioned.
    """
    host_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The position of an asset in a rack measured in rack units.
    """
    rack_elevation: int | core.IntOut = core.attr(int, computed=True)

    """
    The rack ID of the asset.
    """
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
