import terrascript.core as core


@core.resource(type="aws_s3_bucket_public_access_block", namespace="s3")
class BucketPublicAccessBlock(core.Resource):
    """
    (Optional) Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling
    this setting does not affect existing policies or ACLs. When set to `true` causes the following beh
    avior:
    """

    block_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false
    . Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazo
    n S3 to:
    """
    block_public_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) S3 Bucket to which this Public Access Block configuration should be applied.
    """
    bucket: str | core.StringOut = core.attr(str)

    """
    Name of the S3 bucket the configuration is attached to
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enablin
    g this setting does not affect the persistence of any existing ACLs and doesn't prevent new public A
    CLs from being set. When set to `true` causes Amazon S3 to:
    """
    ignore_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `fa
    lse`. Enabling this setting does not affect the previously stored bucket policy, except that public
    and cross-account access within the public bucket policy, including non-public delegation to specifi
    c accounts, is blocked. When set to `true`:
    """
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
