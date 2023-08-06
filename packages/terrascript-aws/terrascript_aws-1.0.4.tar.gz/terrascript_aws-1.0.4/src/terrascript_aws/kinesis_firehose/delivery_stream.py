import terrascript.core as core


@core.schema
class VpcConfig(core.Schema):

    role_arn: str | core.StringOut = core.attr(str)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcConfig.Args(
                role_arn=role_arn,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_arn: str | core.StringOut = core.arg()

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class CloudwatchLoggingOptions(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    log_group_name: str | core.StringOut | None = core.attr(str, default=None)

    log_stream_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        log_group_name: str | core.StringOut | None = None,
        log_stream_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CloudwatchLoggingOptions.Args(
                enabled=enabled,
                log_group_name=log_group_name,
                log_stream_name=log_stream_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        log_group_name: str | core.StringOut | None = core.arg(default=None)

        log_stream_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Parameters(core.Schema):

    parameter_name: str | core.StringOut = core.attr(str)

    parameter_value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        parameter_name: str | core.StringOut,
        parameter_value: str | core.StringOut,
    ):
        super().__init__(
            args=Parameters.Args(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_name: str | core.StringOut = core.arg()

        parameter_value: str | core.StringOut = core.arg()


@core.schema
class Processors(core.Schema):

    parameters: list[Parameters] | core.ArrayOut[Parameters] | None = core.attr(
        Parameters, default=None, kind=core.Kind.array
    )

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        parameters: list[Parameters] | core.ArrayOut[Parameters] | None = None,
    ):
        super().__init__(
            args=Processors.Args(
                type=type,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameters: list[Parameters] | core.ArrayOut[Parameters] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class ProcessingConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    processors: list[Processors] | core.ArrayOut[Processors] | None = core.attr(
        Processors, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        processors: list[Processors] | core.ArrayOut[Processors] | None = None,
    ):
        super().__init__(
            args=ProcessingConfiguration.Args(
                enabled=enabled,
                processors=processors,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        processors: list[Processors] | core.ArrayOut[Processors] | None = core.arg(default=None)


@core.schema
class ElasticsearchConfiguration(core.Schema):

    buffering_interval: int | core.IntOut | None = core.attr(int, default=None)

    buffering_size: int | core.IntOut | None = core.attr(int, default=None)

    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    cluster_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    domain_arn: str | core.StringOut | None = core.attr(str, default=None)

    index_name: str | core.StringOut = core.attr(str)

    index_rotation_period: str | core.StringOut | None = core.attr(str, default=None)

    processing_configuration: ProcessingConfiguration | None = core.attr(
        ProcessingConfiguration, default=None
    )

    retry_duration: int | core.IntOut | None = core.attr(int, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    s3_backup_mode: str | core.StringOut | None = core.attr(str, default=None)

    type_name: str | core.StringOut | None = core.attr(str, default=None)

    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        *,
        index_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        buffering_interval: int | core.IntOut | None = None,
        buffering_size: int | core.IntOut | None = None,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        cluster_endpoint: str | core.StringOut | None = None,
        domain_arn: str | core.StringOut | None = None,
        index_rotation_period: str | core.StringOut | None = None,
        processing_configuration: ProcessingConfiguration | None = None,
        retry_duration: int | core.IntOut | None = None,
        s3_backup_mode: str | core.StringOut | None = None,
        type_name: str | core.StringOut | None = None,
        vpc_config: VpcConfig | None = None,
    ):
        super().__init__(
            args=ElasticsearchConfiguration.Args(
                index_name=index_name,
                role_arn=role_arn,
                buffering_interval=buffering_interval,
                buffering_size=buffering_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                cluster_endpoint=cluster_endpoint,
                domain_arn=domain_arn,
                index_rotation_period=index_rotation_period,
                processing_configuration=processing_configuration,
                retry_duration=retry_duration,
                s3_backup_mode=s3_backup_mode,
                type_name=type_name,
                vpc_config=vpc_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        buffering_interval: int | core.IntOut | None = core.arg(default=None)

        buffering_size: int | core.IntOut | None = core.arg(default=None)

        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        cluster_endpoint: str | core.StringOut | None = core.arg(default=None)

        domain_arn: str | core.StringOut | None = core.arg(default=None)

        index_name: str | core.StringOut = core.arg()

        index_rotation_period: str | core.StringOut | None = core.arg(default=None)

        processing_configuration: ProcessingConfiguration | None = core.arg(default=None)

        retry_duration: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        s3_backup_mode: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)


@core.schema
class S3Configuration(core.Schema):

    bucket_arn: str | core.StringOut = core.attr(str)

    buffer_interval: int | core.IntOut | None = core.attr(int, default=None)

    buffer_size: int | core.IntOut | None = core.attr(int, default=None)

    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    compression_format: str | core.StringOut | None = core.attr(str, default=None)

    error_output_prefix: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
        buffer_interval: int | core.IntOut | None = None,
        buffer_size: int | core.IntOut | None = None,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        compression_format: str | core.StringOut | None = None,
        error_output_prefix: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Configuration.Args(
                bucket_arn=bucket_arn,
                role_arn=role_arn,
                buffer_interval=buffer_interval,
                buffer_size=buffer_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                compression_format=compression_format,
                error_output_prefix=error_output_prefix,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: str | core.StringOut = core.arg()

        buffer_interval: int | core.IntOut | None = core.arg(default=None)

        buffer_size: int | core.IntOut | None = core.arg(default=None)

        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        compression_format: str | core.StringOut | None = core.arg(default=None)

        error_output_prefix: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()


@core.schema
class CommonAttributes(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=CommonAttributes.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class RequestConfiguration(core.Schema):

    common_attributes: list[CommonAttributes] | core.ArrayOut[CommonAttributes] | None = core.attr(
        CommonAttributes, default=None, kind=core.Kind.array
    )

    content_encoding: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        common_attributes: list[CommonAttributes] | core.ArrayOut[CommonAttributes] | None = None,
        content_encoding: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RequestConfiguration.Args(
                common_attributes=common_attributes,
                content_encoding=content_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        common_attributes: list[CommonAttributes] | core.ArrayOut[
            CommonAttributes
        ] | None = core.arg(default=None)

        content_encoding: str | core.StringOut | None = core.arg(default=None)


@core.schema
class HttpEndpointConfiguration(core.Schema):

    access_key: str | core.StringOut | None = core.attr(str, default=None)

    buffering_interval: int | core.IntOut | None = core.attr(int, default=None)

    buffering_size: int | core.IntOut | None = core.attr(int, default=None)

    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    name: str | core.StringOut | None = core.attr(str, default=None)

    processing_configuration: ProcessingConfiguration | None = core.attr(
        ProcessingConfiguration, default=None
    )

    request_configuration: RequestConfiguration | None = core.attr(
        RequestConfiguration, default=None, computed=True
    )

    retry_duration: int | core.IntOut | None = core.attr(int, default=None)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    s3_backup_mode: str | core.StringOut | None = core.attr(str, default=None)

    url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        url: str | core.StringOut,
        access_key: str | core.StringOut | None = None,
        buffering_interval: int | core.IntOut | None = None,
        buffering_size: int | core.IntOut | None = None,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        name: str | core.StringOut | None = None,
        processing_configuration: ProcessingConfiguration | None = None,
        request_configuration: RequestConfiguration | None = None,
        retry_duration: int | core.IntOut | None = None,
        role_arn: str | core.StringOut | None = None,
        s3_backup_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=HttpEndpointConfiguration.Args(
                url=url,
                access_key=access_key,
                buffering_interval=buffering_interval,
                buffering_size=buffering_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                name=name,
                processing_configuration=processing_configuration,
                request_configuration=request_configuration,
                retry_duration=retry_duration,
                role_arn=role_arn,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_key: str | core.StringOut | None = core.arg(default=None)

        buffering_interval: int | core.IntOut | None = core.arg(default=None)

        buffering_size: int | core.IntOut | None = core.arg(default=None)

        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        processing_configuration: ProcessingConfiguration | None = core.arg(default=None)

        request_configuration: RequestConfiguration | None = core.arg(default=None)

        retry_duration: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        s3_backup_mode: str | core.StringOut | None = core.arg(default=None)

        url: str | core.StringOut = core.arg()


@core.schema
class KinesisSourceConfiguration(core.Schema):

    kinesis_stream_arn: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        kinesis_stream_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisSourceConfiguration.Args(
                kinesis_stream_arn=kinesis_stream_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kinesis_stream_arn: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class S3BackupConfiguration(core.Schema):

    bucket_arn: str | core.StringOut = core.attr(str)

    buffer_interval: int | core.IntOut | None = core.attr(int, default=None)

    buffer_size: int | core.IntOut | None = core.attr(int, default=None)

    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    compression_format: str | core.StringOut | None = core.attr(str, default=None)

    error_output_prefix: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
        buffer_interval: int | core.IntOut | None = None,
        buffer_size: int | core.IntOut | None = None,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        compression_format: str | core.StringOut | None = None,
        error_output_prefix: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3BackupConfiguration.Args(
                bucket_arn=bucket_arn,
                role_arn=role_arn,
                buffer_interval=buffer_interval,
                buffer_size=buffer_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                compression_format=compression_format,
                error_output_prefix=error_output_prefix,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: str | core.StringOut = core.arg()

        buffer_interval: int | core.IntOut | None = core.arg(default=None)

        buffer_size: int | core.IntOut | None = core.arg(default=None)

        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        compression_format: str | core.StringOut | None = core.arg(default=None)

        error_output_prefix: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()


@core.schema
class DynamicPartitioningConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    retry_duration: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        retry_duration: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DynamicPartitioningConfiguration.Args(
                enabled=enabled,
                retry_duration=retry_duration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        retry_duration: int | core.IntOut | None = core.arg(default=None)


@core.schema
class SchemaConfiguration(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    database_name: str | core.StringOut = core.attr(str)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    role_arn: str | core.StringOut = core.attr(str)

    table_name: str | core.StringOut = core.attr(str)

    version_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        database_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        table_name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
        version_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SchemaConfiguration.Args(
                database_name=database_name,
                role_arn=role_arn,
                table_name=table_name,
                catalog_id=catalog_id,
                region=region,
                version_id=version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        region: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        table_name: str | core.StringOut = core.arg()

        version_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class HiveJsonSerDe(core.Schema):

    timestamp_formats: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        timestamp_formats: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=HiveJsonSerDe.Args(
                timestamp_formats=timestamp_formats,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        timestamp_formats: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class OpenXJsonSerDe(core.Schema):

    case_insensitive: bool | core.BoolOut | None = core.attr(bool, default=None)

    column_to_json_key_mappings: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    convert_dots_in_json_keys_to_underscores: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        case_insensitive: bool | core.BoolOut | None = None,
        column_to_json_key_mappings: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        convert_dots_in_json_keys_to_underscores: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=OpenXJsonSerDe.Args(
                case_insensitive=case_insensitive,
                column_to_json_key_mappings=column_to_json_key_mappings,
                convert_dots_in_json_keys_to_underscores=convert_dots_in_json_keys_to_underscores,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        case_insensitive: bool | core.BoolOut | None = core.arg(default=None)

        column_to_json_key_mappings: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        convert_dots_in_json_keys_to_underscores: bool | core.BoolOut | None = core.arg(
            default=None
        )


@core.schema
class Deserializer(core.Schema):

    hive_json_ser_de: HiveJsonSerDe | None = core.attr(HiveJsonSerDe, default=None)

    open_x_json_ser_de: OpenXJsonSerDe | None = core.attr(OpenXJsonSerDe, default=None)

    def __init__(
        self,
        *,
        hive_json_ser_de: HiveJsonSerDe | None = None,
        open_x_json_ser_de: OpenXJsonSerDe | None = None,
    ):
        super().__init__(
            args=Deserializer.Args(
                hive_json_ser_de=hive_json_ser_de,
                open_x_json_ser_de=open_x_json_ser_de,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hive_json_ser_de: HiveJsonSerDe | None = core.arg(default=None)

        open_x_json_ser_de: OpenXJsonSerDe | None = core.arg(default=None)


@core.schema
class InputFormatConfiguration(core.Schema):

    deserializer: Deserializer = core.attr(Deserializer)

    def __init__(
        self,
        *,
        deserializer: Deserializer,
    ):
        super().__init__(
            args=InputFormatConfiguration.Args(
                deserializer=deserializer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        deserializer: Deserializer = core.arg()


@core.schema
class ParquetSerDe(core.Schema):

    block_size_bytes: int | core.IntOut | None = core.attr(int, default=None)

    compression: str | core.StringOut | None = core.attr(str, default=None)

    enable_dictionary_compression: bool | core.BoolOut | None = core.attr(bool, default=None)

    max_padding_bytes: int | core.IntOut | None = core.attr(int, default=None)

    page_size_bytes: int | core.IntOut | None = core.attr(int, default=None)

    writer_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        block_size_bytes: int | core.IntOut | None = None,
        compression: str | core.StringOut | None = None,
        enable_dictionary_compression: bool | core.BoolOut | None = None,
        max_padding_bytes: int | core.IntOut | None = None,
        page_size_bytes: int | core.IntOut | None = None,
        writer_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ParquetSerDe.Args(
                block_size_bytes=block_size_bytes,
                compression=compression,
                enable_dictionary_compression=enable_dictionary_compression,
                max_padding_bytes=max_padding_bytes,
                page_size_bytes=page_size_bytes,
                writer_version=writer_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_size_bytes: int | core.IntOut | None = core.arg(default=None)

        compression: str | core.StringOut | None = core.arg(default=None)

        enable_dictionary_compression: bool | core.BoolOut | None = core.arg(default=None)

        max_padding_bytes: int | core.IntOut | None = core.arg(default=None)

        page_size_bytes: int | core.IntOut | None = core.arg(default=None)

        writer_version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class OrcSerDe(core.Schema):

    block_size_bytes: int | core.IntOut | None = core.attr(int, default=None)

    bloom_filter_columns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    bloom_filter_false_positive_probability: float | core.FloatOut | None = core.attr(
        float, default=None
    )

    compression: str | core.StringOut | None = core.attr(str, default=None)

    dictionary_key_threshold: float | core.FloatOut | None = core.attr(float, default=None)

    enable_padding: bool | core.BoolOut | None = core.attr(bool, default=None)

    format_version: str | core.StringOut | None = core.attr(str, default=None)

    padding_tolerance: float | core.FloatOut | None = core.attr(float, default=None)

    row_index_stride: int | core.IntOut | None = core.attr(int, default=None)

    stripe_size_bytes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        block_size_bytes: int | core.IntOut | None = None,
        bloom_filter_columns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        bloom_filter_false_positive_probability: float | core.FloatOut | None = None,
        compression: str | core.StringOut | None = None,
        dictionary_key_threshold: float | core.FloatOut | None = None,
        enable_padding: bool | core.BoolOut | None = None,
        format_version: str | core.StringOut | None = None,
        padding_tolerance: float | core.FloatOut | None = None,
        row_index_stride: int | core.IntOut | None = None,
        stripe_size_bytes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=OrcSerDe.Args(
                block_size_bytes=block_size_bytes,
                bloom_filter_columns=bloom_filter_columns,
                bloom_filter_false_positive_probability=bloom_filter_false_positive_probability,
                compression=compression,
                dictionary_key_threshold=dictionary_key_threshold,
                enable_padding=enable_padding,
                format_version=format_version,
                padding_tolerance=padding_tolerance,
                row_index_stride=row_index_stride,
                stripe_size_bytes=stripe_size_bytes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_size_bytes: int | core.IntOut | None = core.arg(default=None)

        bloom_filter_columns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        bloom_filter_false_positive_probability: float | core.FloatOut | None = core.arg(
            default=None
        )

        compression: str | core.StringOut | None = core.arg(default=None)

        dictionary_key_threshold: float | core.FloatOut | None = core.arg(default=None)

        enable_padding: bool | core.BoolOut | None = core.arg(default=None)

        format_version: str | core.StringOut | None = core.arg(default=None)

        padding_tolerance: float | core.FloatOut | None = core.arg(default=None)

        row_index_stride: int | core.IntOut | None = core.arg(default=None)

        stripe_size_bytes: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Serializer(core.Schema):

    orc_ser_de: OrcSerDe | None = core.attr(OrcSerDe, default=None)

    parquet_ser_de: ParquetSerDe | None = core.attr(ParquetSerDe, default=None)

    def __init__(
        self,
        *,
        orc_ser_de: OrcSerDe | None = None,
        parquet_ser_de: ParquetSerDe | None = None,
    ):
        super().__init__(
            args=Serializer.Args(
                orc_ser_de=orc_ser_de,
                parquet_ser_de=parquet_ser_de,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        orc_ser_de: OrcSerDe | None = core.arg(default=None)

        parquet_ser_de: ParquetSerDe | None = core.arg(default=None)


@core.schema
class OutputFormatConfiguration(core.Schema):

    serializer: Serializer = core.attr(Serializer)

    def __init__(
        self,
        *,
        serializer: Serializer,
    ):
        super().__init__(
            args=OutputFormatConfiguration.Args(
                serializer=serializer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        serializer: Serializer = core.arg()


@core.schema
class DataFormatConversionConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    input_format_configuration: InputFormatConfiguration = core.attr(InputFormatConfiguration)

    output_format_configuration: OutputFormatConfiguration = core.attr(OutputFormatConfiguration)

    schema_configuration: SchemaConfiguration = core.attr(SchemaConfiguration)

    def __init__(
        self,
        *,
        input_format_configuration: InputFormatConfiguration,
        output_format_configuration: OutputFormatConfiguration,
        schema_configuration: SchemaConfiguration,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=DataFormatConversionConfiguration.Args(
                input_format_configuration=input_format_configuration,
                output_format_configuration=output_format_configuration,
                schema_configuration=schema_configuration,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        input_format_configuration: InputFormatConfiguration = core.arg()

        output_format_configuration: OutputFormatConfiguration = core.arg()

        schema_configuration: SchemaConfiguration = core.arg()


@core.schema
class ExtendedS3Configuration(core.Schema):

    bucket_arn: str | core.StringOut = core.attr(str)

    buffer_interval: int | core.IntOut | None = core.attr(int, default=None)

    buffer_size: int | core.IntOut | None = core.attr(int, default=None)

    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    compression_format: str | core.StringOut | None = core.attr(str, default=None)

    data_format_conversion_configuration: DataFormatConversionConfiguration | None = core.attr(
        DataFormatConversionConfiguration, default=None
    )

    dynamic_partitioning_configuration: DynamicPartitioningConfiguration | None = core.attr(
        DynamicPartitioningConfiguration, default=None
    )

    error_output_prefix: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    processing_configuration: ProcessingConfiguration | None = core.attr(
        ProcessingConfiguration, default=None
    )

    role_arn: str | core.StringOut = core.attr(str)

    s3_backup_configuration: S3BackupConfiguration | None = core.attr(
        S3BackupConfiguration, default=None
    )

    s3_backup_mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
        buffer_interval: int | core.IntOut | None = None,
        buffer_size: int | core.IntOut | None = None,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        compression_format: str | core.StringOut | None = None,
        data_format_conversion_configuration: DataFormatConversionConfiguration | None = None,
        dynamic_partitioning_configuration: DynamicPartitioningConfiguration | None = None,
        error_output_prefix: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        processing_configuration: ProcessingConfiguration | None = None,
        s3_backup_configuration: S3BackupConfiguration | None = None,
        s3_backup_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ExtendedS3Configuration.Args(
                bucket_arn=bucket_arn,
                role_arn=role_arn,
                buffer_interval=buffer_interval,
                buffer_size=buffer_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                compression_format=compression_format,
                data_format_conversion_configuration=data_format_conversion_configuration,
                dynamic_partitioning_configuration=dynamic_partitioning_configuration,
                error_output_prefix=error_output_prefix,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
                processing_configuration=processing_configuration,
                s3_backup_configuration=s3_backup_configuration,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: str | core.StringOut = core.arg()

        buffer_interval: int | core.IntOut | None = core.arg(default=None)

        buffer_size: int | core.IntOut | None = core.arg(default=None)

        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        compression_format: str | core.StringOut | None = core.arg(default=None)

        data_format_conversion_configuration: DataFormatConversionConfiguration | None = core.arg(
            default=None
        )

        dynamic_partitioning_configuration: DynamicPartitioningConfiguration | None = core.arg(
            default=None
        )

        error_output_prefix: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        processing_configuration: ProcessingConfiguration | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        s3_backup_configuration: S3BackupConfiguration | None = core.arg(default=None)

        s3_backup_mode: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    key_arn: str | core.StringOut | None = core.attr(str, default=None)

    key_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        key_arn: str | core.StringOut | None = None,
        key_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ServerSideEncryption.Args(
                enabled=enabled,
                key_arn=key_arn,
                key_type=key_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        key_arn: str | core.StringOut | None = core.arg(default=None)

        key_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SplunkConfiguration(core.Schema):

    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    hec_acknowledgment_timeout: int | core.IntOut | None = core.attr(int, default=None)

    hec_endpoint: str | core.StringOut = core.attr(str)

    hec_endpoint_type: str | core.StringOut | None = core.attr(str, default=None)

    hec_token: str | core.StringOut = core.attr(str)

    processing_configuration: ProcessingConfiguration | None = core.attr(
        ProcessingConfiguration, default=None
    )

    retry_duration: int | core.IntOut | None = core.attr(int, default=None)

    s3_backup_mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        hec_endpoint: str | core.StringOut,
        hec_token: str | core.StringOut,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        hec_acknowledgment_timeout: int | core.IntOut | None = None,
        hec_endpoint_type: str | core.StringOut | None = None,
        processing_configuration: ProcessingConfiguration | None = None,
        retry_duration: int | core.IntOut | None = None,
        s3_backup_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SplunkConfiguration.Args(
                hec_endpoint=hec_endpoint,
                hec_token=hec_token,
                cloudwatch_logging_options=cloudwatch_logging_options,
                hec_acknowledgment_timeout=hec_acknowledgment_timeout,
                hec_endpoint_type=hec_endpoint_type,
                processing_configuration=processing_configuration,
                retry_duration=retry_duration,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        hec_acknowledgment_timeout: int | core.IntOut | None = core.arg(default=None)

        hec_endpoint: str | core.StringOut = core.arg()

        hec_endpoint_type: str | core.StringOut | None = core.arg(default=None)

        hec_token: str | core.StringOut = core.arg()

        processing_configuration: ProcessingConfiguration | None = core.arg(default=None)

        retry_duration: int | core.IntOut | None = core.arg(default=None)

        s3_backup_mode: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RedshiftConfiguration(core.Schema):

    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    cluster_jdbcurl: str | core.StringOut = core.attr(str)

    copy_options: str | core.StringOut | None = core.attr(str, default=None)

    data_table_columns: str | core.StringOut | None = core.attr(str, default=None)

    data_table_name: str | core.StringOut = core.attr(str)

    password: str | core.StringOut = core.attr(str)

    processing_configuration: ProcessingConfiguration | None = core.attr(
        ProcessingConfiguration, default=None
    )

    retry_duration: int | core.IntOut | None = core.attr(int, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    s3_backup_configuration: S3BackupConfiguration | None = core.attr(
        S3BackupConfiguration, default=None
    )

    s3_backup_mode: str | core.StringOut | None = core.attr(str, default=None)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cluster_jdbcurl: str | core.StringOut,
        data_table_name: str | core.StringOut,
        password: str | core.StringOut,
        role_arn: str | core.StringOut,
        username: str | core.StringOut,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        copy_options: str | core.StringOut | None = None,
        data_table_columns: str | core.StringOut | None = None,
        processing_configuration: ProcessingConfiguration | None = None,
        retry_duration: int | core.IntOut | None = None,
        s3_backup_configuration: S3BackupConfiguration | None = None,
        s3_backup_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RedshiftConfiguration.Args(
                cluster_jdbcurl=cluster_jdbcurl,
                data_table_name=data_table_name,
                password=password,
                role_arn=role_arn,
                username=username,
                cloudwatch_logging_options=cloudwatch_logging_options,
                copy_options=copy_options,
                data_table_columns=data_table_columns,
                processing_configuration=processing_configuration,
                retry_duration=retry_duration,
                s3_backup_configuration=s3_backup_configuration,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        cluster_jdbcurl: str | core.StringOut = core.arg()

        copy_options: str | core.StringOut | None = core.arg(default=None)

        data_table_columns: str | core.StringOut | None = core.arg(default=None)

        data_table_name: str | core.StringOut = core.arg()

        password: str | core.StringOut = core.arg()

        processing_configuration: ProcessingConfiguration | None = core.arg(default=None)

        retry_duration: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        s3_backup_configuration: S3BackupConfiguration | None = core.arg(default=None)

        s3_backup_mode: str | core.StringOut | None = core.arg(default=None)

        username: str | core.StringOut = core.arg()


@core.resource(type="aws_kinesis_firehose_delivery_stream", namespace="kinesis_firehose")
class DeliveryStream(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the Stream
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    destination: str | core.StringOut = core.attr(str)

    destination_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration options if elasticsearch is the destination. More details are given below.
    """
    elasticsearch_configuration: ElasticsearchConfiguration | None = core.attr(
        ElasticsearchConfiguration, default=None
    )

    """
    (Optional, only Required when `destination` is `extended_s3`) Enhanced configuration options for the
    s3 destination. More details are given below.
    """
    extended_s3_configuration: ExtendedS3Configuration | None = core.attr(
        ExtendedS3Configuration, default=None
    )

    """
    (Optional) Configuration options if http_endpoint is the destination. requires the user to also spec
    ify a `s3_configuration` block.  More details are given below.
    """
    http_endpoint_configuration: HttpEndpointConfiguration | None = core.attr(
        HttpEndpointConfiguration, default=None
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Allows the ability to specify the kinesis stream that is used as the source of the fireho
    se delivery stream.
    """
    kinesis_source_configuration: KinesisSourceConfiguration | None = core.attr(
        KinesisSourceConfiguration, default=None
    )

    """
    (Required) A name to identify the stream. This is unique to the
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration options if redshift is the destination.
    """
    redshift_configuration: RedshiftConfiguration | None = core.attr(
        RedshiftConfiguration, default=None
    )

    """
    (Optional) Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` ins
    tead. Configuration options for the s3 destination (or the intermediate bucket if the destination
    """
    s3_configuration: S3Configuration | None = core.attr(S3Configuration, default=None)

    """
    (Optional) Encrypt at rest options.
    """
    server_side_encryption: ServerSideEncryption | None = core.attr(
        ServerSideEncryption, default=None
    )

    """
    (Optional) Configuration options if splunk is the destination. More details are given below.
    """
    splunk_configuration: SplunkConfiguration | None = core.attr(SplunkConfiguration, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Specifies the table version for the output data schema. Defaults to `LATEST`.
    """
    version_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination: str | core.StringOut,
        name: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        destination_id: str | core.StringOut | None = None,
        elasticsearch_configuration: ElasticsearchConfiguration | None = None,
        extended_s3_configuration: ExtendedS3Configuration | None = None,
        http_endpoint_configuration: HttpEndpointConfiguration | None = None,
        kinesis_source_configuration: KinesisSourceConfiguration | None = None,
        redshift_configuration: RedshiftConfiguration | None = None,
        s3_configuration: S3Configuration | None = None,
        server_side_encryption: ServerSideEncryption | None = None,
        splunk_configuration: SplunkConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        version_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeliveryStream.Args(
                destination=destination,
                name=name,
                arn=arn,
                destination_id=destination_id,
                elasticsearch_configuration=elasticsearch_configuration,
                extended_s3_configuration=extended_s3_configuration,
                http_endpoint_configuration=http_endpoint_configuration,
                kinesis_source_configuration=kinesis_source_configuration,
                redshift_configuration=redshift_configuration,
                s3_configuration=s3_configuration,
                server_side_encryption=server_side_encryption,
                splunk_configuration=splunk_configuration,
                tags=tags,
                tags_all=tags_all,
                version_id=version_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: str | core.StringOut | None = core.arg(default=None)

        destination: str | core.StringOut = core.arg()

        destination_id: str | core.StringOut | None = core.arg(default=None)

        elasticsearch_configuration: ElasticsearchConfiguration | None = core.arg(default=None)

        extended_s3_configuration: ExtendedS3Configuration | None = core.arg(default=None)

        http_endpoint_configuration: HttpEndpointConfiguration | None = core.arg(default=None)

        kinesis_source_configuration: KinesisSourceConfiguration | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        redshift_configuration: RedshiftConfiguration | None = core.arg(default=None)

        s3_configuration: S3Configuration | None = core.arg(default=None)

        server_side_encryption: ServerSideEncryption | None = core.arg(default=None)

        splunk_configuration: SplunkConfiguration | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        version_id: str | core.StringOut | None = core.arg(default=None)
