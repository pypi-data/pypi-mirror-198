import terrascript.core as core


@core.schema
class Filter(core.Schema):

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_s3_bucket_metric", namespace="s3")
class BucketMetric(core.Resource):
    """
    (Required) The name of the bucket to put metric configuration.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) [Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.
    html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags
    (documented below).
    """
    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique identifier of the metrics configuration for the bucket. Must be less than or equal
    to 64 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        name: str | core.StringOut,
        filter: Filter | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketMetric.Args(
                bucket=bucket,
                name=name,
                filter=filter,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        filter: Filter | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
