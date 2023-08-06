import terrascript.core as core


@core.data(type="aws_elastic_beanstalk_hosted_zone", namespace="elastic_beanstalk")
class DsHostedZone(core.Data):
    """
    The ID of the hosted zone.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The region you'd like the zone for. By default, fetches the current region.
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
            args=DsHostedZone.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: str | core.StringOut | None = core.arg(default=None)
