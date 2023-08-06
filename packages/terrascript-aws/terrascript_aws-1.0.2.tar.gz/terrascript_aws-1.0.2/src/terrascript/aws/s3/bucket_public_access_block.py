import terrascript.core as core


@core.resource(type="aws_s3_bucket_public_access_block", namespace="aws_s3")
class BucketPublicAccessBlock(core.Resource):

    block_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    block_public_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    bucket: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    ignore_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    restrict_public_buckets: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        block_public_acls: bool | core.BoolOut | None = None,
        block_public_policy: bool | core.BoolOut | None = None,
        ignore_public_acls: bool | core.BoolOut | None = None,
        restrict_public_buckets: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketPublicAccessBlock.Args(
                bucket=bucket,
                block_public_acls=block_public_acls,
                block_public_policy=block_public_policy,
                ignore_public_acls=ignore_public_acls,
                restrict_public_buckets=restrict_public_buckets,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_public_acls: bool | core.BoolOut | None = core.arg(default=None)

        block_public_policy: bool | core.BoolOut | None = core.arg(default=None)

        bucket: str | core.StringOut = core.arg()

        ignore_public_acls: bool | core.BoolOut | None = core.arg(default=None)

        restrict_public_buckets: bool | core.BoolOut | None = core.arg(default=None)
