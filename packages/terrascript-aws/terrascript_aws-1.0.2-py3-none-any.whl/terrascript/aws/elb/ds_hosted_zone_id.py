import terrascript.core as core


@core.data(type="aws_elb_hosted_zone_id", namespace="aws_elb")
class DsHostedZoneId(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

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
