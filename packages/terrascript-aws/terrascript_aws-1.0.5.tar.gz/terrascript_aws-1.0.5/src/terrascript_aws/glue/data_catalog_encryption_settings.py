import terrascript.core as core


@core.schema
class ConnectionPasswordEncryption(core.Schema):

    aws_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    return_connection_password_encrypted: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        return_connection_password_encrypted: bool | core.BoolOut,
        aws_kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectionPasswordEncryption.Args(
                return_connection_password_encrypted=return_connection_password_encrypted,
                aws_kms_key_id=aws_kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        return_connection_password_encrypted: bool | core.BoolOut = core.arg()


@core.schema
class EncryptionAtRest(core.Schema):

    catalog_encryption_mode: str | core.StringOut = core.attr(str)

    sse_aws_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        catalog_encryption_mode: str | core.StringOut,
        sse_aws_kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EncryptionAtRest.Args(
                catalog_encryption_mode=catalog_encryption_mode,
                sse_aws_kms_key_id=sse_aws_kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_encryption_mode: str | core.StringOut = core.arg()

        sse_aws_kms_key_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DataCatalogEncryptionSettingsBlk(core.Schema):

    connection_password_encryption: ConnectionPasswordEncryption = core.attr(
        ConnectionPasswordEncryption
    )

    encryption_at_rest: EncryptionAtRest = core.attr(EncryptionAtRest)

    def __init__(
        self,
        *,
        connection_password_encryption: ConnectionPasswordEncryption,
        encryption_at_rest: EncryptionAtRest,
    ):
        super().__init__(
            args=DataCatalogEncryptionSettingsBlk.Args(
                connection_password_encryption=connection_password_encryption,
                encryption_at_rest=encryption_at_rest,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_password_encryption: ConnectionPasswordEncryption = core.arg()

        encryption_at_rest: EncryptionAtRest = core.arg()


@core.resource(type="aws_glue_data_catalog_encryption_settings", namespace="glue")
class DataCatalogEncryptionSettings(core.Resource):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    data_catalog_encryption_settings: DataCatalogEncryptionSettingsBlk = core.attr(
        DataCatalogEncryptionSettingsBlk
    )

    """
    The ID of the Data Catalog to set the security configuration for.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        data_catalog_encryption_settings: DataCatalogEncryptionSettingsBlk,
        catalog_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataCatalogEncryptionSettings.Args(
                data_catalog_encryption_settings=data_catalog_encryption_settings,
                catalog_id=catalog_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        data_catalog_encryption_settings: DataCatalogEncryptionSettingsBlk = core.arg()
