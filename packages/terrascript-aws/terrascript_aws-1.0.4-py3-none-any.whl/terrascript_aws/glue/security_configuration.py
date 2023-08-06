import terrascript.core as core


@core.schema
class CloudwatchEncryption(core.Schema):

    cloudwatch_encryption_mode: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cloudwatch_encryption_mode: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CloudwatchEncryption.Args(
                cloudwatch_encryption_mode=cloudwatch_encryption_mode,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_encryption_mode: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class JobBookmarksEncryption(core.Schema):

    job_bookmarks_encryption_mode: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        job_bookmarks_encryption_mode: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=JobBookmarksEncryption.Args(
                job_bookmarks_encryption_mode=job_bookmarks_encryption_mode,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        job_bookmarks_encryption_mode: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class S3Encryption(core.Schema):

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    s3_encryption_mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        kms_key_arn: str | core.StringOut | None = None,
        s3_encryption_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Encryption.Args(
                kms_key_arn=kms_key_arn,
                s3_encryption_mode=s3_encryption_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        s3_encryption_mode: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EncryptionConfiguration(core.Schema):

    cloudwatch_encryption: CloudwatchEncryption = core.attr(CloudwatchEncryption)

    job_bookmarks_encryption: JobBookmarksEncryption = core.attr(JobBookmarksEncryption)

    s3_encryption: S3Encryption = core.attr(S3Encryption)

    def __init__(
        self,
        *,
        cloudwatch_encryption: CloudwatchEncryption,
        job_bookmarks_encryption: JobBookmarksEncryption,
        s3_encryption: S3Encryption,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                cloudwatch_encryption=cloudwatch_encryption,
                job_bookmarks_encryption=job_bookmarks_encryption,
                s3_encryption=s3_encryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_encryption: CloudwatchEncryption = core.arg()

        job_bookmarks_encryption: JobBookmarksEncryption = core.arg()

        s3_encryption: S3Encryption = core.arg()


@core.resource(type="aws_glue_security_configuration", namespace="glue")
class SecurityConfiguration(core.Resource):

    encryption_configuration: EncryptionConfiguration = core.attr(EncryptionConfiguration)

    """
    Glue security configuration name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        encryption_configuration: EncryptionConfiguration,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecurityConfiguration.Args(
                encryption_configuration=encryption_configuration,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        encryption_configuration: EncryptionConfiguration = core.arg()

        name: str | core.StringOut = core.arg()
