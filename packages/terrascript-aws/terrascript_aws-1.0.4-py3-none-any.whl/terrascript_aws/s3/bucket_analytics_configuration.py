import terrascript.core as core


@core.schema
class S3BucketDestination(core.Schema):

    bucket_account_id: str | core.StringOut | None = core.attr(str, default=None)

    bucket_arn: str | core.StringOut = core.attr(str)

    format: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        bucket_account_id: str | core.StringOut | None = None,
        format: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3BucketDestination.Args(
                bucket_arn=bucket_arn,
                bucket_account_id=bucket_account_id,
                format=format,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_account_id: str | core.StringOut | None = core.arg(default=None)

        bucket_arn: str | core.StringOut = core.arg()

        format: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    s3_bucket_destination: S3BucketDestination = core.attr(S3BucketDestination)

    def __init__(
        self,
        *,
        s3_bucket_destination: S3BucketDestination,
    ):
        super().__init__(
            args=Destination.Args(
                s3_bucket_destination=s3_bucket_destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_bucket_destination: S3BucketDestination = core.arg()


@core.schema
class DataExport(core.Schema):

    destination: Destination = core.attr(Destination)

    output_schema_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        destination: Destination,
        output_schema_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DataExport.Args(
                destination=destination,
                output_schema_version=output_schema_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Destination = core.arg()

        output_schema_version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class StorageClassAnalysis(core.Schema):

    data_export: DataExport = core.attr(DataExport)

    def __init__(
        self,
        *,
        data_export: DataExport,
    ):
        super().__init__(
            args=StorageClassAnalysis.Args(
                data_export=data_export,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_export: DataExport = core.arg()


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


@core.resource(type="aws_s3_bucket_analytics_configuration", namespace="s3")
class BucketAnalyticsConfiguration(core.Resource):
    """
    (Required) The name of the bucket this analytics configuration is associated with.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (docume
    nted below).
    """
    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique identifier of the analytics configuration for the bucket.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration for the analytics data export (documented below).
    """
    storage_class_analysis: StorageClassAnalysis | None = core.attr(
        StorageClassAnalysis, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        name: str | core.StringOut,
        filter: Filter | None = None,
        storage_class_analysis: StorageClassAnalysis | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketAnalyticsConfiguration.Args(
                bucket=bucket,
                name=name,
                filter=filter,
                storage_class_analysis=storage_class_analysis,
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

        storage_class_analysis: StorageClassAnalysis | None = core.arg(default=None)
