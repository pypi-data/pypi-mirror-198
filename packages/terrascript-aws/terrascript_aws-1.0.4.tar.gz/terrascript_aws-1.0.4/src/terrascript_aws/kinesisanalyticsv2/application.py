import terrascript.core as core


@core.schema
class CloudwatchLoggingOptions(core.Schema):

    cloudwatch_logging_option_id: str | core.StringOut = core.attr(str, computed=True)

    log_stream_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cloudwatch_logging_option_id: str | core.StringOut,
        log_stream_arn: str | core.StringOut,
    ):
        super().__init__(
            args=CloudwatchLoggingOptions.Args(
                cloudwatch_logging_option_id=cloudwatch_logging_option_id,
                log_stream_arn=log_stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logging_option_id: str | core.StringOut = core.arg()

        log_stream_arn: str | core.StringOut = core.arg()


@core.schema
class ApplicationRestoreConfiguration(core.Schema):

    application_restore_type: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        application_restore_type: str | core.StringOut | None = None,
        snapshot_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ApplicationRestoreConfiguration.Args(
                application_restore_type=application_restore_type,
                snapshot_name=snapshot_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_restore_type: str | core.StringOut | None = core.arg(default=None)

        snapshot_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class FlinkRunConfiguration(core.Schema):

    allow_non_restored_state: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    def __init__(
        self,
        *,
        allow_non_restored_state: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=FlinkRunConfiguration.Args(
                allow_non_restored_state=allow_non_restored_state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_non_restored_state: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class RunConfiguration(core.Schema):

    application_restore_configuration: ApplicationRestoreConfiguration | None = core.attr(
        ApplicationRestoreConfiguration, default=None, computed=True
    )

    flink_run_configuration: FlinkRunConfiguration | None = core.attr(
        FlinkRunConfiguration, default=None, computed=True
    )

    def __init__(
        self,
        *,
        application_restore_configuration: ApplicationRestoreConfiguration | None = None,
        flink_run_configuration: FlinkRunConfiguration | None = None,
    ):
        super().__init__(
            args=RunConfiguration.Args(
                application_restore_configuration=application_restore_configuration,
                flink_run_configuration=flink_run_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_restore_configuration: ApplicationRestoreConfiguration | None = core.arg(
            default=None
        )

        flink_run_configuration: FlinkRunConfiguration | None = core.arg(default=None)


@core.schema
class InputParallelism(core.Schema):

    count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=InputParallelism.Args(
                count=count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut | None = core.arg(default=None)


@core.schema
class KinesisFirehoseInput(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisFirehoseInput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()


@core.schema
class KinesisStreamsInput(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisStreamsInput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()


@core.schema
class InputLambdaProcessor(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=InputLambdaProcessor.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()


@core.schema
class InputProcessingConfiguration(core.Schema):

    input_lambda_processor: InputLambdaProcessor = core.attr(InputLambdaProcessor)

    def __init__(
        self,
        *,
        input_lambda_processor: InputLambdaProcessor,
    ):
        super().__init__(
            args=InputProcessingConfiguration.Args(
                input_lambda_processor=input_lambda_processor,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_lambda_processor: InputLambdaProcessor = core.arg()


@core.schema
class RecordColumn(core.Schema):

    mapping: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    sql_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        sql_type: str | core.StringOut,
        mapping: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RecordColumn.Args(
                name=name,
                sql_type=sql_type,
                mapping=mapping,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mapping: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        sql_type: str | core.StringOut = core.arg()


@core.schema
class CsvMappingParameters(core.Schema):

    record_column_delimiter: str | core.StringOut = core.attr(str)

    record_row_delimiter: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        record_column_delimiter: str | core.StringOut,
        record_row_delimiter: str | core.StringOut,
    ):
        super().__init__(
            args=CsvMappingParameters.Args(
                record_column_delimiter=record_column_delimiter,
                record_row_delimiter=record_row_delimiter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column_delimiter: str | core.StringOut = core.arg()

        record_row_delimiter: str | core.StringOut = core.arg()


@core.schema
class JsonMappingParameters(core.Schema):

    record_row_path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        record_row_path: str | core.StringOut,
    ):
        super().__init__(
            args=JsonMappingParameters.Args(
                record_row_path=record_row_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_row_path: str | core.StringOut = core.arg()


@core.schema
class MappingParameters(core.Schema):

    csv_mapping_parameters: CsvMappingParameters | None = core.attr(
        CsvMappingParameters, default=None
    )

    json_mapping_parameters: JsonMappingParameters | None = core.attr(
        JsonMappingParameters, default=None
    )

    def __init__(
        self,
        *,
        csv_mapping_parameters: CsvMappingParameters | None = None,
        json_mapping_parameters: JsonMappingParameters | None = None,
    ):
        super().__init__(
            args=MappingParameters.Args(
                csv_mapping_parameters=csv_mapping_parameters,
                json_mapping_parameters=json_mapping_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        csv_mapping_parameters: CsvMappingParameters | None = core.arg(default=None)

        json_mapping_parameters: JsonMappingParameters | None = core.arg(default=None)


@core.schema
class RecordFormat(core.Schema):

    mapping_parameters: MappingParameters = core.attr(MappingParameters)

    record_format_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        mapping_parameters: MappingParameters,
        record_format_type: str | core.StringOut,
    ):
        super().__init__(
            args=RecordFormat.Args(
                mapping_parameters=mapping_parameters,
                record_format_type=record_format_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mapping_parameters: MappingParameters = core.arg()

        record_format_type: str | core.StringOut = core.arg()


@core.schema
class InputSchema(core.Schema):

    record_column: list[RecordColumn] | core.ArrayOut[RecordColumn] = core.attr(
        RecordColumn, kind=core.Kind.array
    )

    record_encoding: str | core.StringOut | None = core.attr(str, default=None)

    record_format: RecordFormat = core.attr(RecordFormat)

    def __init__(
        self,
        *,
        record_column: list[RecordColumn] | core.ArrayOut[RecordColumn],
        record_format: RecordFormat,
        record_encoding: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InputSchema.Args(
                record_column=record_column,
                record_format=record_format,
                record_encoding=record_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column: list[RecordColumn] | core.ArrayOut[RecordColumn] = core.arg()

        record_encoding: str | core.StringOut | None = core.arg(default=None)

        record_format: RecordFormat = core.arg()


@core.schema
class InputStartingPositionConfiguration(core.Schema):

    input_starting_position: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        input_starting_position: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InputStartingPositionConfiguration.Args(
                input_starting_position=input_starting_position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_starting_position: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Input(core.Schema):

    in_app_stream_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    input_id: str | core.StringOut = core.attr(str, computed=True)

    input_parallelism: InputParallelism | None = core.attr(
        InputParallelism, default=None, computed=True
    )

    input_processing_configuration: InputProcessingConfiguration | None = core.attr(
        InputProcessingConfiguration, default=None
    )

    input_schema: InputSchema = core.attr(InputSchema)

    input_starting_position_configuration: list[InputStartingPositionConfiguration] | core.ArrayOut[
        InputStartingPositionConfiguration
    ] | None = core.attr(
        InputStartingPositionConfiguration, default=None, computed=True, kind=core.Kind.array
    )

    kinesis_firehose_input: KinesisFirehoseInput | None = core.attr(
        KinesisFirehoseInput, default=None
    )

    kinesis_streams_input: KinesisStreamsInput | None = core.attr(KinesisStreamsInput, default=None)

    name_prefix: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        in_app_stream_names: list[str] | core.ArrayOut[core.StringOut],
        input_id: str | core.StringOut,
        input_schema: InputSchema,
        name_prefix: str | core.StringOut,
        input_parallelism: InputParallelism | None = None,
        input_processing_configuration: InputProcessingConfiguration | None = None,
        input_starting_position_configuration: list[InputStartingPositionConfiguration]
        | core.ArrayOut[InputStartingPositionConfiguration]
        | None = None,
        kinesis_firehose_input: KinesisFirehoseInput | None = None,
        kinesis_streams_input: KinesisStreamsInput | None = None,
    ):
        super().__init__(
            args=Input.Args(
                in_app_stream_names=in_app_stream_names,
                input_id=input_id,
                input_schema=input_schema,
                name_prefix=name_prefix,
                input_parallelism=input_parallelism,
                input_processing_configuration=input_processing_configuration,
                input_starting_position_configuration=input_starting_position_configuration,
                kinesis_firehose_input=kinesis_firehose_input,
                kinesis_streams_input=kinesis_streams_input,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        in_app_stream_names: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        input_id: str | core.StringOut = core.arg()

        input_parallelism: InputParallelism | None = core.arg(default=None)

        input_processing_configuration: InputProcessingConfiguration | None = core.arg(default=None)

        input_schema: InputSchema = core.arg()

        input_starting_position_configuration: list[
            InputStartingPositionConfiguration
        ] | core.ArrayOut[InputStartingPositionConfiguration] | None = core.arg(default=None)

        kinesis_firehose_input: KinesisFirehoseInput | None = core.arg(default=None)

        kinesis_streams_input: KinesisStreamsInput | None = core.arg(default=None)

        name_prefix: str | core.StringOut = core.arg()


@core.schema
class LambdaOutput(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=LambdaOutput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()


@core.schema
class DestinationSchema(core.Schema):

    record_format_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        record_format_type: str | core.StringOut,
    ):
        super().__init__(
            args=DestinationSchema.Args(
                record_format_type=record_format_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_format_type: str | core.StringOut = core.arg()


@core.schema
class KinesisFirehoseOutput(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisFirehoseOutput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()


@core.schema
class KinesisStreamsOutput(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisStreamsOutput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()


@core.schema
class Output(core.Schema):

    destination_schema: DestinationSchema = core.attr(DestinationSchema)

    kinesis_firehose_output: KinesisFirehoseOutput | None = core.attr(
        KinesisFirehoseOutput, default=None
    )

    kinesis_streams_output: KinesisStreamsOutput | None = core.attr(
        KinesisStreamsOutput, default=None
    )

    lambda_output: LambdaOutput | None = core.attr(LambdaOutput, default=None)

    name: str | core.StringOut = core.attr(str)

    output_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination_schema: DestinationSchema,
        name: str | core.StringOut,
        output_id: str | core.StringOut,
        kinesis_firehose_output: KinesisFirehoseOutput | None = None,
        kinesis_streams_output: KinesisStreamsOutput | None = None,
        lambda_output: LambdaOutput | None = None,
    ):
        super().__init__(
            args=Output.Args(
                destination_schema=destination_schema,
                name=name,
                output_id=output_id,
                kinesis_firehose_output=kinesis_firehose_output,
                kinesis_streams_output=kinesis_streams_output,
                lambda_output=lambda_output,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_schema: DestinationSchema = core.arg()

        kinesis_firehose_output: KinesisFirehoseOutput | None = core.arg(default=None)

        kinesis_streams_output: KinesisStreamsOutput | None = core.arg(default=None)

        lambda_output: LambdaOutput | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        output_id: str | core.StringOut = core.arg()


@core.schema
class ReferenceSchema(core.Schema):

    record_column: list[RecordColumn] | core.ArrayOut[RecordColumn] = core.attr(
        RecordColumn, kind=core.Kind.array
    )

    record_encoding: str | core.StringOut | None = core.attr(str, default=None)

    record_format: RecordFormat = core.attr(RecordFormat)

    def __init__(
        self,
        *,
        record_column: list[RecordColumn] | core.ArrayOut[RecordColumn],
        record_format: RecordFormat,
        record_encoding: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ReferenceSchema.Args(
                record_column=record_column,
                record_format=record_format,
                record_encoding=record_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column: list[RecordColumn] | core.ArrayOut[RecordColumn] = core.arg()

        record_encoding: str | core.StringOut | None = core.arg(default=None)

        record_format: RecordFormat = core.arg()


@core.schema
class S3ReferenceDataSource(core.Schema):

    bucket_arn: str | core.StringOut = core.attr(str)

    file_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        file_key: str | core.StringOut,
    ):
        super().__init__(
            args=S3ReferenceDataSource.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: str | core.StringOut = core.arg()

        file_key: str | core.StringOut = core.arg()


@core.schema
class ReferenceDataSource(core.Schema):

    reference_id: str | core.StringOut = core.attr(str, computed=True)

    reference_schema: ReferenceSchema = core.attr(ReferenceSchema)

    s3_reference_data_source: S3ReferenceDataSource = core.attr(S3ReferenceDataSource)

    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        reference_id: str | core.StringOut,
        reference_schema: ReferenceSchema,
        s3_reference_data_source: S3ReferenceDataSource,
        table_name: str | core.StringOut,
    ):
        super().__init__(
            args=ReferenceDataSource.Args(
                reference_id=reference_id,
                reference_schema=reference_schema,
                s3_reference_data_source=s3_reference_data_source,
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        reference_id: str | core.StringOut = core.arg()

        reference_schema: ReferenceSchema = core.arg()

        s3_reference_data_source: S3ReferenceDataSource = core.arg()

        table_name: str | core.StringOut = core.arg()


@core.schema
class SqlApplicationConfiguration(core.Schema):

    input: Input | None = core.attr(Input, default=None)

    output: list[Output] | core.ArrayOut[Output] | None = core.attr(
        Output, default=None, kind=core.Kind.array
    )

    reference_data_source: ReferenceDataSource | None = core.attr(ReferenceDataSource, default=None)

    def __init__(
        self,
        *,
        input: Input | None = None,
        output: list[Output] | core.ArrayOut[Output] | None = None,
        reference_data_source: ReferenceDataSource | None = None,
    ):
        super().__init__(
            args=SqlApplicationConfiguration.Args(
                input=input,
                output=output,
                reference_data_source=reference_data_source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input: Input | None = core.arg(default=None)

        output: list[Output] | core.ArrayOut[Output] | None = core.arg(default=None)

        reference_data_source: ReferenceDataSource | None = core.arg(default=None)


@core.schema
class VpcConfiguration(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_configuration_id: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_configuration_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcConfiguration.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_configuration_id=vpc_configuration_id,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_configuration_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class S3ContentLocation(core.Schema):

    bucket_arn: str | core.StringOut = core.attr(str)

    file_key: str | core.StringOut = core.attr(str)

    object_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        file_key: str | core.StringOut,
        object_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3ContentLocation.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
                object_version=object_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: str | core.StringOut = core.arg()

        file_key: str | core.StringOut = core.arg()

        object_version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CodeContent(core.Schema):

    s3_content_location: S3ContentLocation | None = core.attr(S3ContentLocation, default=None)

    text_content: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_content_location: S3ContentLocation | None = None,
        text_content: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CodeContent.Args(
                s3_content_location=s3_content_location,
                text_content=text_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_content_location: S3ContentLocation | None = core.arg(default=None)

        text_content: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ApplicationCodeConfiguration(core.Schema):

    code_content: CodeContent | None = core.attr(CodeContent, default=None)

    code_content_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        code_content_type: str | core.StringOut,
        code_content: CodeContent | None = None,
    ):
        super().__init__(
            args=ApplicationCodeConfiguration.Args(
                code_content_type=code_content_type,
                code_content=code_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_content: CodeContent | None = core.arg(default=None)

        code_content_type: str | core.StringOut = core.arg()


@core.schema
class ApplicationSnapshotConfiguration(core.Schema):

    snapshots_enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        snapshots_enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=ApplicationSnapshotConfiguration.Args(
                snapshots_enabled=snapshots_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        snapshots_enabled: bool | core.BoolOut = core.arg()


@core.schema
class PropertyGroup(core.Schema):

    property_group_id: str | core.StringOut = core.attr(str)

    property_map: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    def __init__(
        self,
        *,
        property_group_id: str | core.StringOut,
        property_map: dict[str, str] | core.MapOut[core.StringOut],
    ):
        super().__init__(
            args=PropertyGroup.Args(
                property_group_id=property_group_id,
                property_map=property_map,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        property_group_id: str | core.StringOut = core.arg()

        property_map: dict[str, str] | core.MapOut[core.StringOut] = core.arg()


@core.schema
class EnvironmentProperties(core.Schema):

    property_group: list[PropertyGroup] | core.ArrayOut[PropertyGroup] = core.attr(
        PropertyGroup, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        property_group: list[PropertyGroup] | core.ArrayOut[PropertyGroup],
    ):
        super().__init__(
            args=EnvironmentProperties.Args(
                property_group=property_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        property_group: list[PropertyGroup] | core.ArrayOut[PropertyGroup] = core.arg()


@core.schema
class CheckpointConfiguration(core.Schema):

    checkpoint_interval: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    checkpointing_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    configuration_type: str | core.StringOut = core.attr(str)

    min_pause_between_checkpoints: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        configuration_type: str | core.StringOut,
        checkpoint_interval: int | core.IntOut | None = None,
        checkpointing_enabled: bool | core.BoolOut | None = None,
        min_pause_between_checkpoints: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CheckpointConfiguration.Args(
                configuration_type=configuration_type,
                checkpoint_interval=checkpoint_interval,
                checkpointing_enabled=checkpointing_enabled,
                min_pause_between_checkpoints=min_pause_between_checkpoints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        checkpoint_interval: int | core.IntOut | None = core.arg(default=None)

        checkpointing_enabled: bool | core.BoolOut | None = core.arg(default=None)

        configuration_type: str | core.StringOut = core.arg()

        min_pause_between_checkpoints: int | core.IntOut | None = core.arg(default=None)


@core.schema
class MonitoringConfiguration(core.Schema):

    configuration_type: str | core.StringOut = core.attr(str)

    log_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    metrics_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        configuration_type: str | core.StringOut,
        log_level: str | core.StringOut | None = None,
        metrics_level: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MonitoringConfiguration.Args(
                configuration_type=configuration_type,
                log_level=log_level,
                metrics_level=metrics_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configuration_type: str | core.StringOut = core.arg()

        log_level: str | core.StringOut | None = core.arg(default=None)

        metrics_level: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ParallelismConfiguration(core.Schema):

    auto_scaling_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    configuration_type: str | core.StringOut = core.attr(str)

    parallelism: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    parallelism_per_kpu: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        configuration_type: str | core.StringOut,
        auto_scaling_enabled: bool | core.BoolOut | None = None,
        parallelism: int | core.IntOut | None = None,
        parallelism_per_kpu: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ParallelismConfiguration.Args(
                configuration_type=configuration_type,
                auto_scaling_enabled=auto_scaling_enabled,
                parallelism=parallelism,
                parallelism_per_kpu=parallelism_per_kpu,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_scaling_enabled: bool | core.BoolOut | None = core.arg(default=None)

        configuration_type: str | core.StringOut = core.arg()

        parallelism: int | core.IntOut | None = core.arg(default=None)

        parallelism_per_kpu: int | core.IntOut | None = core.arg(default=None)


@core.schema
class FlinkApplicationConfiguration(core.Schema):

    checkpoint_configuration: CheckpointConfiguration | None = core.attr(
        CheckpointConfiguration, default=None, computed=True
    )

    monitoring_configuration: MonitoringConfiguration | None = core.attr(
        MonitoringConfiguration, default=None, computed=True
    )

    parallelism_configuration: ParallelismConfiguration | None = core.attr(
        ParallelismConfiguration, default=None, computed=True
    )

    def __init__(
        self,
        *,
        checkpoint_configuration: CheckpointConfiguration | None = None,
        monitoring_configuration: MonitoringConfiguration | None = None,
        parallelism_configuration: ParallelismConfiguration | None = None,
    ):
        super().__init__(
            args=FlinkApplicationConfiguration.Args(
                checkpoint_configuration=checkpoint_configuration,
                monitoring_configuration=monitoring_configuration,
                parallelism_configuration=parallelism_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        checkpoint_configuration: CheckpointConfiguration | None = core.arg(default=None)

        monitoring_configuration: MonitoringConfiguration | None = core.arg(default=None)

        parallelism_configuration: ParallelismConfiguration | None = core.arg(default=None)


@core.schema
class ApplicationConfiguration(core.Schema):

    application_code_configuration: ApplicationCodeConfiguration = core.attr(
        ApplicationCodeConfiguration
    )

    application_snapshot_configuration: ApplicationSnapshotConfiguration | None = core.attr(
        ApplicationSnapshotConfiguration, default=None, computed=True
    )

    environment_properties: EnvironmentProperties | None = core.attr(
        EnvironmentProperties, default=None
    )

    flink_application_configuration: FlinkApplicationConfiguration | None = core.attr(
        FlinkApplicationConfiguration, default=None, computed=True
    )

    run_configuration: RunConfiguration | None = core.attr(
        RunConfiguration, default=None, computed=True
    )

    sql_application_configuration: SqlApplicationConfiguration | None = core.attr(
        SqlApplicationConfiguration, default=None
    )

    vpc_configuration: VpcConfiguration | None = core.attr(VpcConfiguration, default=None)

    def __init__(
        self,
        *,
        application_code_configuration: ApplicationCodeConfiguration,
        application_snapshot_configuration: ApplicationSnapshotConfiguration | None = None,
        environment_properties: EnvironmentProperties | None = None,
        flink_application_configuration: FlinkApplicationConfiguration | None = None,
        run_configuration: RunConfiguration | None = None,
        sql_application_configuration: SqlApplicationConfiguration | None = None,
        vpc_configuration: VpcConfiguration | None = None,
    ):
        super().__init__(
            args=ApplicationConfiguration.Args(
                application_code_configuration=application_code_configuration,
                application_snapshot_configuration=application_snapshot_configuration,
                environment_properties=environment_properties,
                flink_application_configuration=flink_application_configuration,
                run_configuration=run_configuration,
                sql_application_configuration=sql_application_configuration,
                vpc_configuration=vpc_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_code_configuration: ApplicationCodeConfiguration = core.arg()

        application_snapshot_configuration: ApplicationSnapshotConfiguration | None = core.arg(
            default=None
        )

        environment_properties: EnvironmentProperties | None = core.arg(default=None)

        flink_application_configuration: FlinkApplicationConfiguration | None = core.arg(
            default=None
        )

        run_configuration: RunConfiguration | None = core.arg(default=None)

        sql_application_configuration: SqlApplicationConfiguration | None = core.arg(default=None)

        vpc_configuration: VpcConfiguration | None = core.arg(default=None)


@core.resource(type="aws_kinesisanalyticsv2_application", namespace="kinesisanalyticsv2")
class Application(core.Resource):
    """
    (Optional) The application's configuration
    """

    application_configuration: ApplicationConfiguration | None = core.attr(
        ApplicationConfiguration, default=None, computed=True
    )

    """
    The ARN of the application.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A [CloudWatch log stream](/docs/providers/aws/r/cloudwatch_log_stream.html) to monitor ap
    plication configuration errors.
    """
    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None
    )

    """
    The current timestamp when the application was created.
    """
    create_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A summary description of the application.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether to force stop an unresponsive Flink-based application.
    """
    force_stop: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The application identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The current timestamp when the application was last updated.
    """
    last_update_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the application.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The runtime environment for the application. Valid values: `SQL-1_0`, `FLINK-1_6`, `FLINK
    1_8`, `FLINK-1_11`, `FLINK-1_13`.
    """
    runtime_environment: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of the [IAM role](/docs/providers/aws/r/iam_role.html) used by the application to
    access Kinesis data streams, Kinesis Data Firehose delivery streams, Amazon S3 objects, and other e
    xternal resources.
    """
    service_execution_role: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to start or stop the application.
    """
    start_application: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The status of the application.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the application. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level.
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
    The current application version. Kinesis Data Analytics updates the `version_id` each time the appli
    cation is updated.
    """
    version_id: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        runtime_environment: str | core.StringOut,
        service_execution_role: str | core.StringOut,
        application_configuration: ApplicationConfiguration | None = None,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        description: str | core.StringOut | None = None,
        force_stop: bool | core.BoolOut | None = None,
        start_application: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                runtime_environment=runtime_environment,
                service_execution_role=service_execution_role,
                application_configuration=application_configuration,
                cloudwatch_logging_options=cloudwatch_logging_options,
                description=description,
                force_stop=force_stop,
                start_application=start_application,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_configuration: ApplicationConfiguration | None = core.arg(default=None)

        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        force_stop: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        runtime_environment: str | core.StringOut = core.arg()

        service_execution_role: str | core.StringOut = core.arg()

        start_application: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
