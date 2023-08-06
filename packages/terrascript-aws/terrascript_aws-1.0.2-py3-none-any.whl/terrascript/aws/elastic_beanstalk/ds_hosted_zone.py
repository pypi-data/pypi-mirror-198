import terrascript.core as core


@core.data(type="aws_elastic_beanstalk_hosted_zone", namespace="aws_elastic_beanstalk")
class DsHostedZone(core.Data):

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
            args=DsHostedZone.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: str | core.StringOut | None = core.arg(default=None)
