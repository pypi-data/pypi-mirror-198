import terrascript.core as core


@core.schema
class S3Destination(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        kms_key_arn: str | core.StringOut,
        key_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Destination.Args(
                bucket_name=bucket_name,
                kms_key_arn=kms_key_arn,
                key_prefix=key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        key_prefix: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_macie2_classification_export_configuration", namespace="macie2")
class ClassificationExportConfiguration(core.Resource):
    """
    The unique identifier (ID) of the configuration.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block for a S3 Destination. Defined below
    """
    s3_destination: S3Destination | None = core.attr(S3Destination, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        s3_destination: S3Destination | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClassificationExportConfiguration.Args(
                s3_destination=s3_destination,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        s3_destination: S3Destination | None = core.arg(default=None)
