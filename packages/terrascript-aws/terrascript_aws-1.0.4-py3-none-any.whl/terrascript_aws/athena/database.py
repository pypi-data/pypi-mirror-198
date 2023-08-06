import terrascript.core as core


@core.schema
class EncryptionConfiguration(core.Schema):

    encryption_option: str | core.StringOut = core.attr(str)

    kms_key: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_option: str | core.StringOut,
        kms_key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_option=encryption_option,
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_option: str | core.StringOut = core.arg()

        kms_key: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AclConfiguration(core.Schema):

    s3_acl_option: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_acl_option: str | core.StringOut,
    ):
        super().__init__(
            args=AclConfiguration.Args(
                s3_acl_option=s3_acl_option,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_acl_option: str | core.StringOut = core.arg()


@core.resource(type="aws_athena_database", namespace="athena")
class Database(core.Resource):
    """
    (Optional) Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query
    results. See [ACL Configuration](#acl-configuration) below.
    """

    acl_configuration: AclConfiguration | None = core.attr(AclConfiguration, default=None)

    """
    (Required) Name of S3 bucket to save the results of the query execution.
    """
    bucket: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Description of the database.
    """
    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Ma
    nagement Service (AWS KMS) key. See [Encryption Configuration](#encryption-configuration) below.
    """
    encryption_configuration: EncryptionConfiguration | None = core.attr(
        EncryptionConfiguration, default=None
    )

    """
    (Optional) The AWS account ID that you expect to be the owner of the Amazon S3 bucket.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Default: false) A boolean that indicates all tables should be deleted from the database s
    o that the database can be destroyed without error. The tables are *not* recoverable.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The database name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the database to create.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A key-value map of custom metadata properties for the database definition.
    """
    properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        acl_configuration: AclConfiguration | None = None,
        bucket: str | core.StringOut | None = None,
        comment: str | core.StringOut | None = None,
        encryption_configuration: EncryptionConfiguration | None = None,
        expected_bucket_owner: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Database.Args(
                name=name,
                acl_configuration=acl_configuration,
                bucket=bucket,
                comment=comment,
                encryption_configuration=encryption_configuration,
                expected_bucket_owner=expected_bucket_owner,
                force_destroy=force_destroy,
                properties=properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acl_configuration: AclConfiguration | None = core.arg(default=None)

        bucket: str | core.StringOut | None = core.arg(default=None)

        comment: str | core.StringOut | None = core.arg(default=None)

        encryption_configuration: EncryptionConfiguration | None = core.arg(default=None)

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
