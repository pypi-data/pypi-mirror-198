import terrascript.core as core


@core.resource(type="aws_s3_bucket_accelerate_configuration", namespace="s3")
class BucketAccelerateConfiguration(core.Resource):
    """
    (Required, Forces new resource) The name of the bucket.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The account ID of the expected bucket owner.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    The `bucket` or `bucket` and `expected_bucket_owner` separated by a comma (`,`) if the latter is pro
    vided.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The transfer acceleration state of the bucket. Valid values: `Enabled`, `Suspended`.
    """
    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        status: str | core.StringOut,
        expected_bucket_owner: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketAccelerateConfiguration.Args(
                bucket=bucket,
                status=status,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut = core.arg()
