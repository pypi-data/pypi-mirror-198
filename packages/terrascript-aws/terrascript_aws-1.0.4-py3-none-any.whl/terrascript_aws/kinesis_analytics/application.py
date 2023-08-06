import terrascript.core as core


@core.schema
class S3(core.Schema):

    bucket_arn: str | core.StringOut = core.attr(str)

    file_key: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        file_key: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=S3.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: str | core.StringOut = core.arg()

        file_key: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class Csv(core.Schema):

    record_column_delimiter: str | core.StringOut = core.attr(str)

    record_row_delimiter: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        record_column_delimiter: str | core.StringOut,
        record_row_delimiter: str | core.StringOut,
    ):
        super().__init__(
            args=Csv.Args(
                record_column_delimiter=record_column_delimiter,
                record_row_delimiter=record_row_delimiter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column_delimiter: str | core.StringOut = core.arg()

        record_row_delimiter: str | core.StringOut = core.arg()


@core.schema
class Json(core.Schema):

    record_row_path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        record_row_path: str | core.StringOut,
    ):
        super().__init__(
            args=Json.Args(
                record_row_path=record_row_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_row_path: str | core.StringOut = core.arg()


@core.schema
class MappingParameters(core.Schema):

    csv: Csv | None = core.attr(Csv, default=None)

    json: Json | None = core.attr(Json, default=None)

    def __init__(
        self,
        *,
        csv: Csv | None = None,
        json: Json | None = None,
    ):
        super().__init__(
            args=MappingParameters.Args(
                csv=csv,
                json=json,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        csv: Csv | None = core.arg(default=None)

        json: Json | None = core.arg(default=None)


@core.schema
class RecordFormat(core.Schema):

    mapping_parameters: MappingParameters | None = core.attr(MappingParameters, default=None)

    record_format_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        record_format_type: str | core.StringOut,
        mapping_parameters: MappingParameters | None = None,
    ):
        super().__init__(
            args=RecordFormat.Args(
                record_format_type=record_format_type,
                mapping_parameters=mapping_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mapping_parameters: MappingParameters | None = core.arg(default=None)

        record_format_type: str | core.StringOut = core.arg()


@core.schema
class RecordColumns(core.Schema):

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
            args=RecordColumns.Args(
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
class ReferenceDataSourcesSchema(core.Schema):

    record_columns: list[RecordColumns] | core.ArrayOut[RecordColumns] = core.attr(
        RecordColumns, kind=core.Kind.array
    )

    record_encoding: str | core.StringOut | None = core.attr(str, default=None)

    record_format: RecordFormat = core.attr(RecordFormat)

    def __init__(
        self,
        *,
        record_columns: list[RecordColumns] | core.ArrayOut[RecordColumns],
        record_format: RecordFormat,
        record_encoding: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ReferenceDataSourcesSchema.Args(
                record_columns=record_columns,
                record_format=record_format,
                record_encoding=record_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_columns: list[RecordColumns] | core.ArrayOut[RecordColumns] = core.arg()

        record_encoding: str | core.StringOut | None = core.arg(default=None)

        record_format: RecordFormat = core.arg()


@core.schema
class ReferenceDataSources(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    s3: S3 = core.attr(S3)

    schema: ReferenceDataSourcesSchema = core.attr(ReferenceDataSourcesSchema)

    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        s3: S3,
        schema: ReferenceDataSourcesSchema,
        table_name: str | core.StringOut,
    ):
        super().__init__(
            args=ReferenceDataSources.Args(
                id=id,
                s3=s3,
                schema=schema,
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        s3: S3 = core.arg()

        schema: ReferenceDataSourcesSchema = core.arg()

        table_name: str | core.StringOut = core.arg()


@core.schema
class CloudwatchLoggingOptions(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    log_stream_arn: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        log_stream_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=CloudwatchLoggingOptions.Args(
                id=id,
                log_stream_arn=log_stream_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        log_stream_arn: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class KinesisFirehose(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisFirehose.Args(
                resource_arn=resource_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class KinesisStream(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisStream.Args(
                resource_arn=resource_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class Lambda(core.Schema):

    resource_arn: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=Lambda.Args(
                resource_arn=resource_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class OutputsSchema(core.Schema):

    record_format_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        record_format_type: str | core.StringOut,
    ):
        super().__init__(
            args=OutputsSchema.Args(
                record_format_type=record_format_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_format_type: str | core.StringOut = core.arg()


@core.schema
class Outputs(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    kinesis_firehose: KinesisFirehose | None = core.attr(KinesisFirehose, default=None)

    kinesis_stream: KinesisStream | None = core.attr(KinesisStream, default=None)

    lambda_: Lambda | None = core.attr(Lambda, default=None, alias="lambda")

    name: str | core.StringOut = core.attr(str)

    schema: OutputsSchema = core.attr(OutputsSchema)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        name: str | core.StringOut,
        schema: OutputsSchema,
        kinesis_firehose: KinesisFirehose | None = None,
        kinesis_stream: KinesisStream | None = None,
        lambda_: Lambda | None = None,
    ):
        super().__init__(
            args=Outputs.Args(
                id=id,
                name=name,
                schema=schema,
                kinesis_firehose=kinesis_firehose,
                kinesis_stream=kinesis_stream,
                lambda_=lambda_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        kinesis_firehose: KinesisFirehose | None = core.arg(default=None)

        kinesis_stream: KinesisStream | None = core.arg(default=None)

        lambda_: Lambda | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        schema: OutputsSchema = core.arg()


@core.schema
class StartingPositionConfiguration(core.Schema):

    starting_position: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        starting_position: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StartingPositionConfiguration.Args(
                starting_position=starting_position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        starting_position: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Parallelism(core.Schema):

    count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Parallelism.Args(
                count=count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut | None = core.arg(default=None)


@core.schema
class ProcessingConfiguration(core.Schema):

    lambda_: Lambda = core.attr(Lambda, alias="lambda")

    def __init__(
        self,
        *,
        lambda_: Lambda,
    ):
        super().__init__(
            args=ProcessingConfiguration.Args(
                lambda_=lambda_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_: Lambda = core.arg()


@core.schema
class Inputs(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    kinesis_firehose: KinesisFirehose | None = core.attr(KinesisFirehose, default=None)

    kinesis_stream: KinesisStream | None = core.attr(KinesisStream, default=None)

    name_prefix: str | core.StringOut = core.attr(str)

    parallelism: Parallelism | None = core.attr(Parallelism, default=None, computed=True)

    processing_configuration: ProcessingConfiguration | None = core.attr(
        ProcessingConfiguration, default=None
    )

    schema: ReferenceDataSourcesSchema = core.attr(ReferenceDataSourcesSchema)

    starting_position_configuration: list[StartingPositionConfiguration] | core.ArrayOut[
        StartingPositionConfiguration
    ] | None = core.attr(
        StartingPositionConfiguration, default=None, computed=True, kind=core.Kind.array
    )

    stream_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        name_prefix: str | core.StringOut,
        schema: ReferenceDataSourcesSchema,
        stream_names: list[str] | core.ArrayOut[core.StringOut],
        kinesis_firehose: KinesisFirehose | None = None,
        kinesis_stream: KinesisStream | None = None,
        parallelism: Parallelism | None = None,
        processing_configuration: ProcessingConfiguration | None = None,
        starting_position_configuration: list[StartingPositionConfiguration]
        | core.ArrayOut[StartingPositionConfiguration]
        | None = None,
    ):
        super().__init__(
            args=Inputs.Args(
                id=id,
                name_prefix=name_prefix,
                schema=schema,
                stream_names=stream_names,
                kinesis_firehose=kinesis_firehose,
                kinesis_stream=kinesis_stream,
                parallelism=parallelism,
                processing_configuration=processing_configuration,
                starting_position_configuration=starting_position_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        kinesis_firehose: KinesisFirehose | None = core.arg(default=None)

        kinesis_stream: KinesisStream | None = core.arg(default=None)

        name_prefix: str | core.StringOut = core.arg()

        parallelism: Parallelism | None = core.arg(default=None)

        processing_configuration: ProcessingConfiguration | None = core.arg(default=None)

        schema: ReferenceDataSourcesSchema = core.arg()

        starting_position_configuration: list[StartingPositionConfiguration] | core.ArrayOut[
            StartingPositionConfiguration
        ] | None = core.arg(default=None)

        stream_names: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_kinesis_analytics_application", namespace="kinesis_analytics")
class Application(core.Resource):
    """
    The ARN of the Kinesis Analytics Appliation.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The CloudWatch log stream options to monitor application errors.
    """
    cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.attr(
        CloudwatchLoggingOptions, default=None
    )

    """
    (Optional) SQL Code to transform input data, and generate output.
    """
    code: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Timestamp when the application version was created.
    """
    create_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the application.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN of the Kinesis Analytics Application.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Input configuration of the application. See [Inputs](#inputs) below for more details.
    """
    inputs: Inputs | None = core.attr(Inputs, default=None)

    """
    The Timestamp when the application was last updated.
    """
    last_update_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the Kinesis Analytics Application.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Output destination configuration of the application. See [Outputs](#outputs) below for mo
    re details.
    """
    outputs: list[Outputs] | core.ArrayOut[Outputs] | None = core.attr(
        Outputs, default=None, kind=core.Kind.array
    )

    """
    (Optional) An S3 Reference Data Source for the application.
    """
    reference_data_sources: ReferenceDataSources | None = core.attr(
        ReferenceDataSources, default=None
    )

    """
    (Optional) Whether to start or stop the Kinesis Analytics Application. To start an application, an i
    nput with a defined `starting_position` must be configured.
    """
    start_application: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Status of the application.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of tags for the Kinesis Analytics Application. If configured with a provider [`default
    _tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#defaul
    t_tags-configuration-block) present, tags with matching keys will overwrite those defined at the pro
    vider-level.
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
    The Version of the application.
    """
    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = None,
        code: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        inputs: Inputs | None = None,
        outputs: list[Outputs] | core.ArrayOut[Outputs] | None = None,
        reference_data_sources: ReferenceDataSources | None = None,
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
                cloudwatch_logging_options=cloudwatch_logging_options,
                code=code,
                description=description,
                inputs=inputs,
                outputs=outputs,
                reference_data_sources=reference_data_sources,
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
        cloudwatch_logging_options: CloudwatchLoggingOptions | None = core.arg(default=None)

        code: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        inputs: Inputs | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        outputs: list[Outputs] | core.ArrayOut[Outputs] | None = core.arg(default=None)

        reference_data_sources: ReferenceDataSources | None = core.arg(default=None)

        start_application: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
