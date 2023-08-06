import terrascript.core as core


@core.schema
class S3Destination(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut = core.attr(str)

    sync_format: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        region: str | core.StringOut,
        kms_key_arn: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        sync_format: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Destination.Args(
                bucket_name=bucket_name,
                region=region,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
                sync_format=sync_format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut = core.arg()

        sync_format: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ssm_resource_data_sync", namespace="ssm")
class ResourceDataSync(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name for the configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Amazon S3 configuration details for the sync.
    """
    s3_destination: S3Destination = core.attr(S3Destination)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        s3_destination: S3Destination,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceDataSync.Args(
                name=name,
                s3_destination=s3_destination,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        s3_destination: S3Destination = core.arg()
