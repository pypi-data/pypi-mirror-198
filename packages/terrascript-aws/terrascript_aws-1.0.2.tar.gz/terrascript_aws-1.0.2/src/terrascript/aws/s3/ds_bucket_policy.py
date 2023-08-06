import terrascript.core as core


@core.data(type="aws_s3_bucket_policy", namespace="aws_s3")
class DsBucketPolicy(core.Data):

    bucket: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsBucketPolicy.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()
