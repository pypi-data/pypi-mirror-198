import terrascript.core as core


@core.schema
class EncryptionAtRest(core.Schema):

    catalog_encryption_mode: str | core.StringOut = core.attr(str, computed=True)

    sse_aws_kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        catalog_encryption_mode: str | core.StringOut,
        sse_aws_kms_key_id: str | core.StringOut,
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

        sse_aws_kms_key_id: str | core.StringOut = core.arg()


@core.schema
class ConnectionPasswordEncryption(core.Schema):

    aws_kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    return_connection_password_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        aws_kms_key_id: str | core.StringOut,
        return_connection_password_encrypted: bool | core.BoolOut,
    ):
        super().__init__(
            args=ConnectionPasswordEncryption.Args(
                aws_kms_key_id=aws_kms_key_id,
                return_connection_password_encrypted=return_connection_password_encrypted,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_kms_key_id: str | core.StringOut = core.arg()

        return_connection_password_encrypted: bool | core.BoolOut = core.arg()


@core.schema
class DataCatalogEncryptionSettingsBlk(core.Schema):

    connection_password_encryption: list[ConnectionPasswordEncryption] | core.ArrayOut[
        ConnectionPasswordEncryption
    ] = core.attr(ConnectionPasswordEncryption, computed=True, kind=core.Kind.array)

    encryption_at_rest: list[EncryptionAtRest] | core.ArrayOut[EncryptionAtRest] = core.attr(
        EncryptionAtRest, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        connection_password_encryption: list[ConnectionPasswordEncryption]
        | core.ArrayOut[ConnectionPasswordEncryption],
        encryption_at_rest: list[EncryptionAtRest] | core.ArrayOut[EncryptionAtRest],
    ):
        super().__init__(
            args=DataCatalogEncryptionSettingsBlk.Args(
                connection_password_encryption=connection_password_encryption,
                encryption_at_rest=encryption_at_rest,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_password_encryption: list[ConnectionPasswordEncryption] | core.ArrayOut[
            ConnectionPasswordEncryption
        ] = core.arg()

        encryption_at_rest: list[EncryptionAtRest] | core.ArrayOut[EncryptionAtRest] = core.arg()


@core.data(type="aws_glue_data_catalog_encryption_settings", namespace="glue")
class DsDataCatalogEncryptionSettings(core.Data):
    """
    (Required) The ID of the Data Catalog. This is typically the AWS account ID.
    """

    catalog_id: str | core.StringOut = core.attr(str)

    data_catalog_encryption_settings: list[DataCatalogEncryptionSettingsBlk] | core.ArrayOut[
        DataCatalogEncryptionSettingsBlk
    ] = core.attr(DataCatalogEncryptionSettingsBlk, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        catalog_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDataCatalogEncryptionSettings.Args(
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut = core.arg()
