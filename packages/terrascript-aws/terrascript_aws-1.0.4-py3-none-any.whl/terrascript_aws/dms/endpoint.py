import terrascript.core as core


@core.schema
class RedshiftSettings(core.Schema):

    bucket_folder: str | core.StringOut | None = core.attr(str, default=None)

    bucket_name: str | core.StringOut | None = core.attr(str, default=None)

    encryption_mode: str | core.StringOut | None = core.attr(str, default=None)

    server_side_encryption_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    service_access_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_folder: str | core.StringOut | None = None,
        bucket_name: str | core.StringOut | None = None,
        encryption_mode: str | core.StringOut | None = None,
        server_side_encryption_kms_key_id: str | core.StringOut | None = None,
        service_access_role_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RedshiftSettings.Args(
                bucket_folder=bucket_folder,
                bucket_name=bucket_name,
                encryption_mode=encryption_mode,
                server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
                service_access_role_arn=service_access_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_folder: str | core.StringOut | None = core.arg(default=None)

        bucket_name: str | core.StringOut | None = core.arg(default=None)

        encryption_mode: str | core.StringOut | None = core.arg(default=None)

        server_side_encryption_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        service_access_role_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ElasticsearchSettings(core.Schema):

    endpoint_uri: str | core.StringOut = core.attr(str)

    error_retry_duration: int | core.IntOut | None = core.attr(int, default=None)

    full_load_error_percentage: int | core.IntOut | None = core.attr(int, default=None)

    service_access_role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        endpoint_uri: str | core.StringOut,
        service_access_role_arn: str | core.StringOut,
        error_retry_duration: int | core.IntOut | None = None,
        full_load_error_percentage: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ElasticsearchSettings.Args(
                endpoint_uri=endpoint_uri,
                service_access_role_arn=service_access_role_arn,
                error_retry_duration=error_retry_duration,
                full_load_error_percentage=full_load_error_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_uri: str | core.StringOut = core.arg()

        error_retry_duration: int | core.IntOut | None = core.arg(default=None)

        full_load_error_percentage: int | core.IntOut | None = core.arg(default=None)

        service_access_role_arn: str | core.StringOut = core.arg()


@core.schema
class MongodbSettings(core.Schema):

    auth_mechanism: str | core.StringOut | None = core.attr(str, default=None)

    auth_source: str | core.StringOut | None = core.attr(str, default=None)

    auth_type: str | core.StringOut | None = core.attr(str, default=None)

    docs_to_investigate: str | core.StringOut | None = core.attr(str, default=None)

    extract_doc_id: str | core.StringOut | None = core.attr(str, default=None)

    nesting_level: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auth_mechanism: str | core.StringOut | None = None,
        auth_source: str | core.StringOut | None = None,
        auth_type: str | core.StringOut | None = None,
        docs_to_investigate: str | core.StringOut | None = None,
        extract_doc_id: str | core.StringOut | None = None,
        nesting_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MongodbSettings.Args(
                auth_mechanism=auth_mechanism,
                auth_source=auth_source,
                auth_type=auth_type,
                docs_to_investigate=docs_to_investigate,
                extract_doc_id=extract_doc_id,
                nesting_level=nesting_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_mechanism: str | core.StringOut | None = core.arg(default=None)

        auth_source: str | core.StringOut | None = core.arg(default=None)

        auth_type: str | core.StringOut | None = core.arg(default=None)

        docs_to_investigate: str | core.StringOut | None = core.arg(default=None)

        extract_doc_id: str | core.StringOut | None = core.arg(default=None)

        nesting_level: str | core.StringOut | None = core.arg(default=None)


@core.schema
class S3Settings(core.Schema):

    add_column_name: bool | core.BoolOut | None = core.attr(bool, default=None)

    bucket_folder: str | core.StringOut | None = core.attr(str, default=None)

    bucket_name: str | core.StringOut | None = core.attr(str, default=None)

    canned_acl_for_objects: str | core.StringOut | None = core.attr(str, default=None)

    cdc_inserts_and_updates: bool | core.BoolOut | None = core.attr(bool, default=None)

    cdc_inserts_only: bool | core.BoolOut | None = core.attr(bool, default=None)

    cdc_max_batch_interval: int | core.IntOut | None = core.attr(int, default=None)

    cdc_min_file_size: int | core.IntOut | None = core.attr(int, default=None)

    cdc_path: str | core.StringOut | None = core.attr(str, default=None)

    compression_type: str | core.StringOut | None = core.attr(str, default=None)

    csv_delimiter: str | core.StringOut | None = core.attr(str, default=None)

    csv_no_sup_value: str | core.StringOut | None = core.attr(str, default=None)

    csv_null_value: str | core.StringOut | None = core.attr(str, default=None)

    csv_row_delimiter: str | core.StringOut | None = core.attr(str, default=None)

    data_format: str | core.StringOut | None = core.attr(str, default=None)

    data_page_size: int | core.IntOut | None = core.attr(int, default=None)

    date_partition_delimiter: str | core.StringOut | None = core.attr(str, default=None)

    date_partition_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    date_partition_sequence: str | core.StringOut | None = core.attr(str, default=None)

    dict_page_size_limit: int | core.IntOut | None = core.attr(int, default=None)

    enable_statistics: bool | core.BoolOut | None = core.attr(bool, default=None)

    encoding_type: str | core.StringOut | None = core.attr(str, default=None)

    encryption_mode: str | core.StringOut | None = core.attr(str, default=None)

    external_table_definition: str | core.StringOut | None = core.attr(str, default=None)

    ignore_headers_row: int | core.IntOut | None = core.attr(int, default=None)

    include_op_for_full_load: bool | core.BoolOut | None = core.attr(bool, default=None)

    max_file_size: int | core.IntOut | None = core.attr(int, default=None)

    parquet_timestamp_in_millisecond: bool | core.BoolOut | None = core.attr(bool, default=None)

    parquet_version: str | core.StringOut | None = core.attr(str, default=None)

    preserve_transactions: bool | core.BoolOut | None = core.attr(bool, default=None)

    rfc_4180: bool | core.BoolOut | None = core.attr(bool, default=None)

    row_group_length: int | core.IntOut | None = core.attr(int, default=None)

    server_side_encryption_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    service_access_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    timestamp_column_name: str | core.StringOut | None = core.attr(str, default=None)

    use_csv_no_sup_value: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        add_column_name: bool | core.BoolOut | None = None,
        bucket_folder: str | core.StringOut | None = None,
        bucket_name: str | core.StringOut | None = None,
        canned_acl_for_objects: str | core.StringOut | None = None,
        cdc_inserts_and_updates: bool | core.BoolOut | None = None,
        cdc_inserts_only: bool | core.BoolOut | None = None,
        cdc_max_batch_interval: int | core.IntOut | None = None,
        cdc_min_file_size: int | core.IntOut | None = None,
        cdc_path: str | core.StringOut | None = None,
        compression_type: str | core.StringOut | None = None,
        csv_delimiter: str | core.StringOut | None = None,
        csv_no_sup_value: str | core.StringOut | None = None,
        csv_null_value: str | core.StringOut | None = None,
        csv_row_delimiter: str | core.StringOut | None = None,
        data_format: str | core.StringOut | None = None,
        data_page_size: int | core.IntOut | None = None,
        date_partition_delimiter: str | core.StringOut | None = None,
        date_partition_enabled: bool | core.BoolOut | None = None,
        date_partition_sequence: str | core.StringOut | None = None,
        dict_page_size_limit: int | core.IntOut | None = None,
        enable_statistics: bool | core.BoolOut | None = None,
        encoding_type: str | core.StringOut | None = None,
        encryption_mode: str | core.StringOut | None = None,
        external_table_definition: str | core.StringOut | None = None,
        ignore_headers_row: int | core.IntOut | None = None,
        include_op_for_full_load: bool | core.BoolOut | None = None,
        max_file_size: int | core.IntOut | None = None,
        parquet_timestamp_in_millisecond: bool | core.BoolOut | None = None,
        parquet_version: str | core.StringOut | None = None,
        preserve_transactions: bool | core.BoolOut | None = None,
        rfc_4180: bool | core.BoolOut | None = None,
        row_group_length: int | core.IntOut | None = None,
        server_side_encryption_kms_key_id: str | core.StringOut | None = None,
        service_access_role_arn: str | core.StringOut | None = None,
        timestamp_column_name: str | core.StringOut | None = None,
        use_csv_no_sup_value: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=S3Settings.Args(
                add_column_name=add_column_name,
                bucket_folder=bucket_folder,
                bucket_name=bucket_name,
                canned_acl_for_objects=canned_acl_for_objects,
                cdc_inserts_and_updates=cdc_inserts_and_updates,
                cdc_inserts_only=cdc_inserts_only,
                cdc_max_batch_interval=cdc_max_batch_interval,
                cdc_min_file_size=cdc_min_file_size,
                cdc_path=cdc_path,
                compression_type=compression_type,
                csv_delimiter=csv_delimiter,
                csv_no_sup_value=csv_no_sup_value,
                csv_null_value=csv_null_value,
                csv_row_delimiter=csv_row_delimiter,
                data_format=data_format,
                data_page_size=data_page_size,
                date_partition_delimiter=date_partition_delimiter,
                date_partition_enabled=date_partition_enabled,
                date_partition_sequence=date_partition_sequence,
                dict_page_size_limit=dict_page_size_limit,
                enable_statistics=enable_statistics,
                encoding_type=encoding_type,
                encryption_mode=encryption_mode,
                external_table_definition=external_table_definition,
                ignore_headers_row=ignore_headers_row,
                include_op_for_full_load=include_op_for_full_load,
                max_file_size=max_file_size,
                parquet_timestamp_in_millisecond=parquet_timestamp_in_millisecond,
                parquet_version=parquet_version,
                preserve_transactions=preserve_transactions,
                rfc_4180=rfc_4180,
                row_group_length=row_group_length,
                server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
                service_access_role_arn=service_access_role_arn,
                timestamp_column_name=timestamp_column_name,
                use_csv_no_sup_value=use_csv_no_sup_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        add_column_name: bool | core.BoolOut | None = core.arg(default=None)

        bucket_folder: str | core.StringOut | None = core.arg(default=None)

        bucket_name: str | core.StringOut | None = core.arg(default=None)

        canned_acl_for_objects: str | core.StringOut | None = core.arg(default=None)

        cdc_inserts_and_updates: bool | core.BoolOut | None = core.arg(default=None)

        cdc_inserts_only: bool | core.BoolOut | None = core.arg(default=None)

        cdc_max_batch_interval: int | core.IntOut | None = core.arg(default=None)

        cdc_min_file_size: int | core.IntOut | None = core.arg(default=None)

        cdc_path: str | core.StringOut | None = core.arg(default=None)

        compression_type: str | core.StringOut | None = core.arg(default=None)

        csv_delimiter: str | core.StringOut | None = core.arg(default=None)

        csv_no_sup_value: str | core.StringOut | None = core.arg(default=None)

        csv_null_value: str | core.StringOut | None = core.arg(default=None)

        csv_row_delimiter: str | core.StringOut | None = core.arg(default=None)

        data_format: str | core.StringOut | None = core.arg(default=None)

        data_page_size: int | core.IntOut | None = core.arg(default=None)

        date_partition_delimiter: str | core.StringOut | None = core.arg(default=None)

        date_partition_enabled: bool | core.BoolOut | None = core.arg(default=None)

        date_partition_sequence: str | core.StringOut | None = core.arg(default=None)

        dict_page_size_limit: int | core.IntOut | None = core.arg(default=None)

        enable_statistics: bool | core.BoolOut | None = core.arg(default=None)

        encoding_type: str | core.StringOut | None = core.arg(default=None)

        encryption_mode: str | core.StringOut | None = core.arg(default=None)

        external_table_definition: str | core.StringOut | None = core.arg(default=None)

        ignore_headers_row: int | core.IntOut | None = core.arg(default=None)

        include_op_for_full_load: bool | core.BoolOut | None = core.arg(default=None)

        max_file_size: int | core.IntOut | None = core.arg(default=None)

        parquet_timestamp_in_millisecond: bool | core.BoolOut | None = core.arg(default=None)

        parquet_version: str | core.StringOut | None = core.arg(default=None)

        preserve_transactions: bool | core.BoolOut | None = core.arg(default=None)

        rfc_4180: bool | core.BoolOut | None = core.arg(default=None)

        row_group_length: int | core.IntOut | None = core.arg(default=None)

        server_side_encryption_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        service_access_role_arn: str | core.StringOut | None = core.arg(default=None)

        timestamp_column_name: str | core.StringOut | None = core.arg(default=None)

        use_csv_no_sup_value: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class KafkaSettings(core.Schema):

    broker: str | core.StringOut = core.attr(str)

    include_control_details: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_null_and_empty: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_partition_value: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_table_alter_operations: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_transaction_details: bool | core.BoolOut | None = core.attr(bool, default=None)

    message_format: str | core.StringOut | None = core.attr(str, default=None)

    message_max_bytes: int | core.IntOut | None = core.attr(int, default=None)

    no_hex_prefix: bool | core.BoolOut | None = core.attr(bool, default=None)

    partition_include_schema_table: bool | core.BoolOut | None = core.attr(bool, default=None)

    sasl_password: str | core.StringOut | None = core.attr(str, default=None)

    sasl_username: str | core.StringOut | None = core.attr(str, default=None)

    security_protocol: str | core.StringOut | None = core.attr(str, default=None)

    ssl_ca_certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    ssl_client_certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    ssl_client_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    ssl_client_key_password: str | core.StringOut | None = core.attr(str, default=None)

    topic: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        broker: str | core.StringOut,
        include_control_details: bool | core.BoolOut | None = None,
        include_null_and_empty: bool | core.BoolOut | None = None,
        include_partition_value: bool | core.BoolOut | None = None,
        include_table_alter_operations: bool | core.BoolOut | None = None,
        include_transaction_details: bool | core.BoolOut | None = None,
        message_format: str | core.StringOut | None = None,
        message_max_bytes: int | core.IntOut | None = None,
        no_hex_prefix: bool | core.BoolOut | None = None,
        partition_include_schema_table: bool | core.BoolOut | None = None,
        sasl_password: str | core.StringOut | None = None,
        sasl_username: str | core.StringOut | None = None,
        security_protocol: str | core.StringOut | None = None,
        ssl_ca_certificate_arn: str | core.StringOut | None = None,
        ssl_client_certificate_arn: str | core.StringOut | None = None,
        ssl_client_key_arn: str | core.StringOut | None = None,
        ssl_client_key_password: str | core.StringOut | None = None,
        topic: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KafkaSettings.Args(
                broker=broker,
                include_control_details=include_control_details,
                include_null_and_empty=include_null_and_empty,
                include_partition_value=include_partition_value,
                include_table_alter_operations=include_table_alter_operations,
                include_transaction_details=include_transaction_details,
                message_format=message_format,
                message_max_bytes=message_max_bytes,
                no_hex_prefix=no_hex_prefix,
                partition_include_schema_table=partition_include_schema_table,
                sasl_password=sasl_password,
                sasl_username=sasl_username,
                security_protocol=security_protocol,
                ssl_ca_certificate_arn=ssl_ca_certificate_arn,
                ssl_client_certificate_arn=ssl_client_certificate_arn,
                ssl_client_key_arn=ssl_client_key_arn,
                ssl_client_key_password=ssl_client_key_password,
                topic=topic,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        broker: str | core.StringOut = core.arg()

        include_control_details: bool | core.BoolOut | None = core.arg(default=None)

        include_null_and_empty: bool | core.BoolOut | None = core.arg(default=None)

        include_partition_value: bool | core.BoolOut | None = core.arg(default=None)

        include_table_alter_operations: bool | core.BoolOut | None = core.arg(default=None)

        include_transaction_details: bool | core.BoolOut | None = core.arg(default=None)

        message_format: str | core.StringOut | None = core.arg(default=None)

        message_max_bytes: int | core.IntOut | None = core.arg(default=None)

        no_hex_prefix: bool | core.BoolOut | None = core.arg(default=None)

        partition_include_schema_table: bool | core.BoolOut | None = core.arg(default=None)

        sasl_password: str | core.StringOut | None = core.arg(default=None)

        sasl_username: str | core.StringOut | None = core.arg(default=None)

        security_protocol: str | core.StringOut | None = core.arg(default=None)

        ssl_ca_certificate_arn: str | core.StringOut | None = core.arg(default=None)

        ssl_client_certificate_arn: str | core.StringOut | None = core.arg(default=None)

        ssl_client_key_arn: str | core.StringOut | None = core.arg(default=None)

        ssl_client_key_password: str | core.StringOut | None = core.arg(default=None)

        topic: str | core.StringOut | None = core.arg(default=None)


@core.schema
class KinesisSettings(core.Schema):

    include_control_details: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_null_and_empty: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_partition_value: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_table_alter_operations: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_transaction_details: bool | core.BoolOut | None = core.attr(bool, default=None)

    message_format: str | core.StringOut | None = core.attr(str, default=None)

    partition_include_schema_table: bool | core.BoolOut | None = core.attr(bool, default=None)

    service_access_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    stream_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        include_control_details: bool | core.BoolOut | None = None,
        include_null_and_empty: bool | core.BoolOut | None = None,
        include_partition_value: bool | core.BoolOut | None = None,
        include_table_alter_operations: bool | core.BoolOut | None = None,
        include_transaction_details: bool | core.BoolOut | None = None,
        message_format: str | core.StringOut | None = None,
        partition_include_schema_table: bool | core.BoolOut | None = None,
        service_access_role_arn: str | core.StringOut | None = None,
        stream_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KinesisSettings.Args(
                include_control_details=include_control_details,
                include_null_and_empty=include_null_and_empty,
                include_partition_value=include_partition_value,
                include_table_alter_operations=include_table_alter_operations,
                include_transaction_details=include_transaction_details,
                message_format=message_format,
                partition_include_schema_table=partition_include_schema_table,
                service_access_role_arn=service_access_role_arn,
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        include_control_details: bool | core.BoolOut | None = core.arg(default=None)

        include_null_and_empty: bool | core.BoolOut | None = core.arg(default=None)

        include_partition_value: bool | core.BoolOut | None = core.arg(default=None)

        include_table_alter_operations: bool | core.BoolOut | None = core.arg(default=None)

        include_transaction_details: bool | core.BoolOut | None = core.arg(default=None)

        message_format: str | core.StringOut | None = core.arg(default=None)

        partition_include_schema_table: bool | core.BoolOut | None = core.arg(default=None)

        service_access_role_arn: str | core.StringOut | None = core.arg(default=None)

        stream_arn: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_dms_endpoint", namespace="dms")
class Endpoint(core.Resource):
    """
    (Optional, Default: empty string) ARN for the certificate.
    """

    certificate_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the endpoint database.
    """
    database_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block for OpenSearch settings. See below.
    """
    elasticsearch_settings: ElasticsearchSettings | None = core.attr(
        ElasticsearchSettings, default=None
    )

    """
    ARN for the endpoint.
    """
    endpoint_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Database endpoint identifier. Identifiers must contain from 1 to 255 alphanumeric charact
    ers or hyphens, begin with a letter, contain only ASCII letters, digits, and hyphens, not end with a
    hyphen, and not contain two consecutive hyphens.
    """
    endpoint_id: str | core.StringOut = core.attr(str)

    """
    (Required) Type of endpoint. Valid values are `source`, `target`.
    """
    endpoint_type: str | core.StringOut = core.attr(str)

    """
    (Required) Type of engine for the endpoint. Valid values are `aurora`, `aurora-postgresql`, `azuredb
    , `db2`, `docdb`, `dynamodb`, `elasticsearch`, `kafka`, `kinesis`, `mariadb`, `mongodb`, `mysql`, `
    opensearch`, `oracle`, `postgres`, `redshift`, `s3`, `sqlserver`, `sybase`. Please note that some of
    engine names are available only for `target` endpoint type (e.g. `redshift`).
    """
    engine_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Additional attributes associated with the connection. For available attributes see [Using
    Extra Connection Attributes with AWS Database Migration Service](https://docs.aws.amazon.com/dms/la
    test/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib).
    """
    extra_connection_attributes: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for Kafka settings. See below.
    """
    kafka_settings: KafkaSettings | None = core.attr(KafkaSettings, default=None)

    """
    (Optional) Configuration block for Kinesis settings. See below.
    """
    kinesis_settings: KinesisSettings | None = core.attr(KinesisSettings, default=None)

    """
    (Required when `engine_name` is `mongodb`, optional otherwise) ARN for the KMS key that will be used
    to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS
    will use your default encryption key. AWS KMS creates the default encryption key for your AWS accou
    nt. Your AWS account has a different default encryption key for each AWS region.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for MongoDB settings. See below.
    """
    mongodb_settings: MongodbSettings | None = core.attr(MongodbSettings, default=None)

    """
    (Optional) Password to be used to login to the endpoint database.
    """
    password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Port used by the endpoint database.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Configuration block for Redshift settings. See below.
    """
    redshift_settings: RedshiftSettings | None = core.attr(
        RedshiftSettings, default=None, computed=True
    )

    """
    (Optional) Configuration block for S3 settings. See below.
    """
    s3_settings: S3Settings | None = core.attr(S3Settings, default=None)

    """
    (Optional) ARN of the IAM role that specifies AWS DMS as the trusted entity and has the required per
    missions to access the value in SecretsManagerSecret.
    """
    secrets_manager_access_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Full ARN, partial ARN, or friendly name of the SecretsManagerSecret that contains the end
    point connection details. Supported only for `engine_name` as `aurora`, `aurora-postgresql`, `mariad
    b`, `mongodb`, `mysql`, `oracle`, `postgres`, `redshift` or `sqlserver`.
    """
    secrets_manager_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Host name of the server.
    """
    server_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) ARN used by the service access IAM role for dynamodb endpoints.
    """
    service_access_role: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Default: none) SSL mode to use for the connection. Valid values are `none`, `require`, `v
    erify-ca`, `verify-full`
    """
    ssl_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) User name to be used to login to the endpoint database.
    """
    username: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        endpoint_id: str | core.StringOut,
        endpoint_type: str | core.StringOut,
        engine_name: str | core.StringOut,
        certificate_arn: str | core.StringOut | None = None,
        database_name: str | core.StringOut | None = None,
        elasticsearch_settings: ElasticsearchSettings | None = None,
        extra_connection_attributes: str | core.StringOut | None = None,
        kafka_settings: KafkaSettings | None = None,
        kinesis_settings: KinesisSettings | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        mongodb_settings: MongodbSettings | None = None,
        password: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        redshift_settings: RedshiftSettings | None = None,
        s3_settings: S3Settings | None = None,
        secrets_manager_access_role_arn: str | core.StringOut | None = None,
        secrets_manager_arn: str | core.StringOut | None = None,
        server_name: str | core.StringOut | None = None,
        service_access_role: str | core.StringOut | None = None,
        ssl_mode: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        username: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                endpoint_id=endpoint_id,
                endpoint_type=endpoint_type,
                engine_name=engine_name,
                certificate_arn=certificate_arn,
                database_name=database_name,
                elasticsearch_settings=elasticsearch_settings,
                extra_connection_attributes=extra_connection_attributes,
                kafka_settings=kafka_settings,
                kinesis_settings=kinesis_settings,
                kms_key_arn=kms_key_arn,
                mongodb_settings=mongodb_settings,
                password=password,
                port=port,
                redshift_settings=redshift_settings,
                s3_settings=s3_settings,
                secrets_manager_access_role_arn=secrets_manager_access_role_arn,
                secrets_manager_arn=secrets_manager_arn,
                server_name=server_name,
                service_access_role=service_access_role,
                ssl_mode=ssl_mode,
                tags=tags,
                tags_all=tags_all,
                username=username,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut | None = core.arg(default=None)

        elasticsearch_settings: ElasticsearchSettings | None = core.arg(default=None)

        endpoint_id: str | core.StringOut = core.arg()

        endpoint_type: str | core.StringOut = core.arg()

        engine_name: str | core.StringOut = core.arg()

        extra_connection_attributes: str | core.StringOut | None = core.arg(default=None)

        kafka_settings: KafkaSettings | None = core.arg(default=None)

        kinesis_settings: KinesisSettings | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        mongodb_settings: MongodbSettings | None = core.arg(default=None)

        password: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        redshift_settings: RedshiftSettings | None = core.arg(default=None)

        s3_settings: S3Settings | None = core.arg(default=None)

        secrets_manager_access_role_arn: str | core.StringOut | None = core.arg(default=None)

        secrets_manager_arn: str | core.StringOut | None = core.arg(default=None)

        server_name: str | core.StringOut | None = core.arg(default=None)

        service_access_role: str | core.StringOut | None = core.arg(default=None)

        ssl_mode: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        username: str | core.StringOut | None = core.arg(default=None)
