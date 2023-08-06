import terrascript.core as core


@core.data(type="aws_s3_bucket", namespace="aws_s3")
class DsBucket(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bucket: str | core.StringOut = core.attr(str)

    bucket_domain_name: str | core.StringOut = core.attr(str, computed=True)

    bucket_regional_domain_name: str | core.StringOut = core.attr(str, computed=True)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    website_domain: str | core.StringOut = core.attr(str, computed=True)

    website_endpoint: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsBucket.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()
