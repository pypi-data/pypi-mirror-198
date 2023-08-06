import terrascript.core as core


@core.resource(type="aws_s3_bucket_policy", namespace="aws_s3")
class BucketPolicy(core.Resource):

    bucket: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketPolicy.Args(
                bucket=bucket,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
