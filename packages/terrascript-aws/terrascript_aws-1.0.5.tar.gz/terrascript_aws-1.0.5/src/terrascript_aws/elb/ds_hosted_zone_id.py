import terrascript.core as core


@core.data(type="aws_elb_hosted_zone_id", namespace="elb")
class DsHostedZoneId(core.Data):
    """
    The ID of the AWS ELB HostedZoneId in the selected region.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Name of the region whose AWS ELB HostedZoneId is desired.
    """
    region: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsHostedZoneId.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: str | core.StringOut | None = core.arg(default=None)
