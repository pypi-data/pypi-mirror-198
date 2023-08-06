import terrascript.core as core


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


@core.resource(type="aws_athena_database", namespace="aws_athena")
class Database(core.Resource):

    acl_configuration: AclConfiguration | None = core.attr(AclConfiguration, default=None)

    bucket: str | core.StringOut | None = core.attr(str, default=None)

    comment: str | core.StringOut | None = core.attr(str, default=None)

    encryption_configuration: EncryptionConfiguration | None = core.attr(
        EncryptionConfiguration, default=None
    )

    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

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
