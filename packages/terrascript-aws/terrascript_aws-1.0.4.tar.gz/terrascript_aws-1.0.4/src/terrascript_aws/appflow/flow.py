import terrascript.core as core


@core.schema
class ErrorHandlingConfig(core.Schema):

    bucket_name: str | core.StringOut | None = core.attr(str, default=None)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    fail_on_first_destination_error: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut | None = None,
        bucket_prefix: str | core.StringOut | None = None,
        fail_on_first_destination_error: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ErrorHandlingConfig.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                fail_on_first_destination_error=fail_on_first_destination_error,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut | None = core.arg(default=None)

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        fail_on_first_destination_error: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesSalesforce(core.Schema):

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    object: str | core.StringOut = core.attr(str)

    write_operation_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
        error_handling_config: ErrorHandlingConfig | None = None,
        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        write_operation_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesSalesforce.Args(
                object=object,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        object: str | core.StringOut = core.arg()

        write_operation_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class UpsolverS3OutputFormatConfigPrefixConfig(core.Schema):

    prefix_format: str | core.StringOut | None = core.attr(str, default=None)

    prefix_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        prefix_type: str | core.StringOut,
        prefix_format: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=UpsolverS3OutputFormatConfigPrefixConfig.Args(
                prefix_type=prefix_type,
                prefix_format=prefix_format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix_format: str | core.StringOut | None = core.arg(default=None)

        prefix_type: str | core.StringOut = core.arg()


@core.schema
class AggregationConfig(core.Schema):

    aggregation_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aggregation_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AggregationConfig.Args(
                aggregation_type=aggregation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class UpsolverS3OutputFormatConfig(core.Schema):

    aggregation_config: AggregationConfig | None = core.attr(AggregationConfig, default=None)

    file_type: str | core.StringOut | None = core.attr(str, default=None)

    prefix_config: UpsolverS3OutputFormatConfigPrefixConfig = core.attr(
        UpsolverS3OutputFormatConfigPrefixConfig
    )

    def __init__(
        self,
        *,
        prefix_config: UpsolverS3OutputFormatConfigPrefixConfig,
        aggregation_config: AggregationConfig | None = None,
        file_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=UpsolverS3OutputFormatConfig.Args(
                prefix_config=prefix_config,
                aggregation_config=aggregation_config,
                file_type=file_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_config: AggregationConfig | None = core.arg(default=None)

        file_type: str | core.StringOut | None = core.arg(default=None)

        prefix_config: UpsolverS3OutputFormatConfigPrefixConfig = core.arg()


@core.schema
class Upsolver(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    s3_output_format_config: UpsolverS3OutputFormatConfig = core.attr(UpsolverS3OutputFormatConfig)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        s3_output_format_config: UpsolverS3OutputFormatConfig,
        bucket_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Upsolver.Args(
                bucket_name=bucket_name,
                s3_output_format_config=s3_output_format_config,
                bucket_prefix=bucket_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        s3_output_format_config: UpsolverS3OutputFormatConfig = core.arg()


@core.schema
class Redshift(core.Schema):

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    intermediate_bucket_name: str | core.StringOut = core.attr(str)

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        intermediate_bucket_name: str | core.StringOut,
        object: str | core.StringOut,
        bucket_prefix: str | core.StringOut | None = None,
        error_handling_config: ErrorHandlingConfig | None = None,
    ):
        super().__init__(
            args=Redshift.Args(
                intermediate_bucket_name=intermediate_bucket_name,
                object=object,
                bucket_prefix=bucket_prefix,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        intermediate_bucket_name: str | core.StringOut = core.arg()

        object: str | core.StringOut = core.arg()


@core.schema
class SuccessResponseHandlingConfig(core.Schema):

    bucket_name: str | core.StringOut | None = core.attr(str, default=None)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut | None = None,
        bucket_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SuccessResponseHandlingConfig.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut | None = core.arg(default=None)

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesSapoData(core.Schema):

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    object_path: str | core.StringOut = core.attr(str)

    success_response_handling_config: SuccessResponseHandlingConfig | None = core.attr(
        SuccessResponseHandlingConfig, default=None
    )

    write_operation_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        object_path: str | core.StringOut,
        error_handling_config: ErrorHandlingConfig | None = None,
        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        success_response_handling_config: SuccessResponseHandlingConfig | None = None,
        write_operation_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesSapoData.Args(
                object_path=object_path,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                success_response_handling_config=success_response_handling_config,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        object_path: str | core.StringOut = core.arg()

        success_response_handling_config: SuccessResponseHandlingConfig | None = core.arg(
            default=None
        )

        write_operation_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesCustomConnector(core.Schema):

    custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    entity_name: str | core.StringOut = core.attr(str)

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    write_operation_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        entity_name: str | core.StringOut,
        custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        error_handling_config: ErrorHandlingConfig | None = None,
        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        write_operation_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesCustomConnector.Args(
                entity_name=entity_name,
                custom_properties=custom_properties,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        entity_name: str | core.StringOut = core.arg()

        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        write_operation_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Snowflake(core.Schema):

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    intermediate_bucket_name: str | core.StringOut = core.attr(str)

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        intermediate_bucket_name: str | core.StringOut,
        object: str | core.StringOut,
        bucket_prefix: str | core.StringOut | None = None,
        error_handling_config: ErrorHandlingConfig | None = None,
    ):
        super().__init__(
            args=Snowflake.Args(
                intermediate_bucket_name=intermediate_bucket_name,
                object=object,
                bucket_prefix=bucket_prefix,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        intermediate_bucket_name: str | core.StringOut = core.arg()

        object: str | core.StringOut = core.arg()


@core.schema
class DestinationConnectorPropertiesZendesk(core.Schema):

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    object: str | core.StringOut = core.attr(str)

    write_operation_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
        error_handling_config: ErrorHandlingConfig | None = None,
        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        write_operation_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesZendesk.Args(
                object=object,
                error_handling_config=error_handling_config,
                id_field_names=id_field_names,
                write_operation_type=write_operation_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        id_field_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        object: str | core.StringOut = core.arg()

        write_operation_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CustomerProfiles(core.Schema):

    domain_name: str | core.StringOut = core.attr(str)

    object_type_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        domain_name: str | core.StringOut,
        object_type_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomerProfiles.Args(
                domain_name=domain_name,
                object_type_name=object_type_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut = core.arg()

        object_type_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EventBridge(core.Schema):

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
        error_handling_config: ErrorHandlingConfig | None = None,
    ):
        super().__init__(
            args=EventBridge.Args(
                object=object,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        object: str | core.StringOut = core.arg()


@core.schema
class DestinationConnectorPropertiesMarketo(core.Schema):

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
        error_handling_config: ErrorHandlingConfig | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesMarketo.Args(
                object=object,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        object: str | core.StringOut = core.arg()


@core.schema
class DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(core.Schema):

    prefix_format: str | core.StringOut | None = core.attr(str, default=None)

    prefix_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        prefix_format: str | core.StringOut | None = None,
        prefix_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig.Args(
                prefix_format=prefix_format,
                prefix_type=prefix_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix_format: str | core.StringOut | None = core.arg(default=None)

        prefix_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DestinationConnectorPropertiesS3S3OutputFormatConfig(core.Schema):

    aggregation_config: AggregationConfig | None = core.attr(AggregationConfig, default=None)

    file_type: str | core.StringOut | None = core.attr(str, default=None)

    prefix_config: DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig | None = (
        core.attr(DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig, default=None)
    )

    def __init__(
        self,
        *,
        aggregation_config: AggregationConfig | None = None,
        file_type: str | core.StringOut | None = None,
        prefix_config: DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig
        | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesS3S3OutputFormatConfig.Args(
                aggregation_config=aggregation_config,
                file_type=file_type,
                prefix_config=prefix_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_config: AggregationConfig | None = core.arg(default=None)

        file_type: str | core.StringOut | None = core.arg(default=None)

        prefix_config: DestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig | None = (
            core.arg(default=None)
        )


@core.schema
class DestinationConnectorPropertiesS3(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    s3_output_format_config: DestinationConnectorPropertiesS3S3OutputFormatConfig | None = (
        core.attr(DestinationConnectorPropertiesS3S3OutputFormatConfig, default=None)
    )

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        bucket_prefix: str | core.StringOut | None = None,
        s3_output_format_config: DestinationConnectorPropertiesS3S3OutputFormatConfig | None = None,
    ):
        super().__init__(
            args=DestinationConnectorPropertiesS3.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                s3_output_format_config=s3_output_format_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        s3_output_format_config: DestinationConnectorPropertiesS3S3OutputFormatConfig | None = (
            core.arg(default=None)
        )


@core.schema
class Honeycode(core.Schema):

    error_handling_config: ErrorHandlingConfig | None = core.attr(ErrorHandlingConfig, default=None)

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
        error_handling_config: ErrorHandlingConfig | None = None,
    ):
        super().__init__(
            args=Honeycode.Args(
                object=object,
                error_handling_config=error_handling_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_handling_config: ErrorHandlingConfig | None = core.arg(default=None)

        object: str | core.StringOut = core.arg()


@core.schema
class LookoutMetrics(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class DestinationConnectorProperties(core.Schema):

    custom_connector: DestinationConnectorPropertiesCustomConnector | None = core.attr(
        DestinationConnectorPropertiesCustomConnector, default=None
    )

    customer_profiles: CustomerProfiles | None = core.attr(CustomerProfiles, default=None)

    event_bridge: EventBridge | None = core.attr(EventBridge, default=None)

    honeycode: Honeycode | None = core.attr(Honeycode, default=None)

    lookout_metrics: LookoutMetrics | None = core.attr(LookoutMetrics, default=None)

    marketo: DestinationConnectorPropertiesMarketo | None = core.attr(
        DestinationConnectorPropertiesMarketo, default=None
    )

    redshift: Redshift | None = core.attr(Redshift, default=None)

    s3: DestinationConnectorPropertiesS3 | None = core.attr(
        DestinationConnectorPropertiesS3, default=None
    )

    salesforce: DestinationConnectorPropertiesSalesforce | None = core.attr(
        DestinationConnectorPropertiesSalesforce, default=None
    )

    sapo_data: DestinationConnectorPropertiesSapoData | None = core.attr(
        DestinationConnectorPropertiesSapoData, default=None
    )

    snowflake: Snowflake | None = core.attr(Snowflake, default=None)

    upsolver: Upsolver | None = core.attr(Upsolver, default=None)

    zendesk: DestinationConnectorPropertiesZendesk | None = core.attr(
        DestinationConnectorPropertiesZendesk, default=None
    )

    def __init__(
        self,
        *,
        custom_connector: DestinationConnectorPropertiesCustomConnector | None = None,
        customer_profiles: CustomerProfiles | None = None,
        event_bridge: EventBridge | None = None,
        honeycode: Honeycode | None = None,
        lookout_metrics: LookoutMetrics | None = None,
        marketo: DestinationConnectorPropertiesMarketo | None = None,
        redshift: Redshift | None = None,
        s3: DestinationConnectorPropertiesS3 | None = None,
        salesforce: DestinationConnectorPropertiesSalesforce | None = None,
        sapo_data: DestinationConnectorPropertiesSapoData | None = None,
        snowflake: Snowflake | None = None,
        upsolver: Upsolver | None = None,
        zendesk: DestinationConnectorPropertiesZendesk | None = None,
    ):
        super().__init__(
            args=DestinationConnectorProperties.Args(
                custom_connector=custom_connector,
                customer_profiles=customer_profiles,
                event_bridge=event_bridge,
                honeycode=honeycode,
                lookout_metrics=lookout_metrics,
                marketo=marketo,
                redshift=redshift,
                s3=s3,
                salesforce=salesforce,
                sapo_data=sapo_data,
                snowflake=snowflake,
                upsolver=upsolver,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_connector: DestinationConnectorPropertiesCustomConnector | None = core.arg(
            default=None
        )

        customer_profiles: CustomerProfiles | None = core.arg(default=None)

        event_bridge: EventBridge | None = core.arg(default=None)

        honeycode: Honeycode | None = core.arg(default=None)

        lookout_metrics: LookoutMetrics | None = core.arg(default=None)

        marketo: DestinationConnectorPropertiesMarketo | None = core.arg(default=None)

        redshift: Redshift | None = core.arg(default=None)

        s3: DestinationConnectorPropertiesS3 | None = core.arg(default=None)

        salesforce: DestinationConnectorPropertiesSalesforce | None = core.arg(default=None)

        sapo_data: DestinationConnectorPropertiesSapoData | None = core.arg(default=None)

        snowflake: Snowflake | None = core.arg(default=None)

        upsolver: Upsolver | None = core.arg(default=None)

        zendesk: DestinationConnectorPropertiesZendesk | None = core.arg(default=None)


@core.schema
class DestinationFlowConfig(core.Schema):

    api_version: str | core.StringOut | None = core.attr(str, default=None)

    connector_profile_name: str | core.StringOut | None = core.attr(str, default=None)

    connector_type: str | core.StringOut = core.attr(str)

    destination_connector_properties: DestinationConnectorProperties = core.attr(
        DestinationConnectorProperties
    )

    def __init__(
        self,
        *,
        connector_type: str | core.StringOut,
        destination_connector_properties: DestinationConnectorProperties,
        api_version: str | core.StringOut | None = None,
        connector_profile_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DestinationFlowConfig.Args(
                connector_type=connector_type,
                destination_connector_properties=destination_connector_properties,
                api_version=api_version,
                connector_profile_name=connector_profile_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_version: str | core.StringOut | None = core.arg(default=None)

        connector_profile_name: str | core.StringOut | None = core.arg(default=None)

        connector_type: str | core.StringOut = core.arg()

        destination_connector_properties: DestinationConnectorProperties = core.arg()


@core.schema
class ConnectorOperator(core.Schema):

    amplitude: str | core.StringOut | None = core.attr(str, default=None)

    custom_connector: str | core.StringOut | None = core.attr(str, default=None)

    datadog: str | core.StringOut | None = core.attr(str, default=None)

    dynatrace: str | core.StringOut | None = core.attr(str, default=None)

    google_analytics: str | core.StringOut | None = core.attr(str, default=None)

    infor_nexus: str | core.StringOut | None = core.attr(str, default=None)

    marketo: str | core.StringOut | None = core.attr(str, default=None)

    s3: str | core.StringOut | None = core.attr(str, default=None)

    salesforce: str | core.StringOut | None = core.attr(str, default=None)

    sapo_data: str | core.StringOut | None = core.attr(str, default=None)

    service_now: str | core.StringOut | None = core.attr(str, default=None)

    singular: str | core.StringOut | None = core.attr(str, default=None)

    slack: str | core.StringOut | None = core.attr(str, default=None)

    trendmicro: str | core.StringOut | None = core.attr(str, default=None)

    veeva: str | core.StringOut | None = core.attr(str, default=None)

    zendesk: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        amplitude: str | core.StringOut | None = None,
        custom_connector: str | core.StringOut | None = None,
        datadog: str | core.StringOut | None = None,
        dynatrace: str | core.StringOut | None = None,
        google_analytics: str | core.StringOut | None = None,
        infor_nexus: str | core.StringOut | None = None,
        marketo: str | core.StringOut | None = None,
        s3: str | core.StringOut | None = None,
        salesforce: str | core.StringOut | None = None,
        sapo_data: str | core.StringOut | None = None,
        service_now: str | core.StringOut | None = None,
        singular: str | core.StringOut | None = None,
        slack: str | core.StringOut | None = None,
        trendmicro: str | core.StringOut | None = None,
        veeva: str | core.StringOut | None = None,
        zendesk: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectorOperator.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                infor_nexus=infor_nexus,
                marketo=marketo,
                s3=s3,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: str | core.StringOut | None = core.arg(default=None)

        custom_connector: str | core.StringOut | None = core.arg(default=None)

        datadog: str | core.StringOut | None = core.arg(default=None)

        dynatrace: str | core.StringOut | None = core.arg(default=None)

        google_analytics: str | core.StringOut | None = core.arg(default=None)

        infor_nexus: str | core.StringOut | None = core.arg(default=None)

        marketo: str | core.StringOut | None = core.arg(default=None)

        s3: str | core.StringOut | None = core.arg(default=None)

        salesforce: str | core.StringOut | None = core.arg(default=None)

        sapo_data: str | core.StringOut | None = core.arg(default=None)

        service_now: str | core.StringOut | None = core.arg(default=None)

        singular: str | core.StringOut | None = core.arg(default=None)

        slack: str | core.StringOut | None = core.arg(default=None)

        trendmicro: str | core.StringOut | None = core.arg(default=None)

        veeva: str | core.StringOut | None = core.arg(default=None)

        zendesk: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Task(core.Schema):

    connector_operator: list[ConnectorOperator] | core.ArrayOut[
        ConnectorOperator
    ] | None = core.attr(ConnectorOperator, default=None, kind=core.Kind.array)

    destination_field: str | core.StringOut | None = core.attr(str, default=None)

    source_fields: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    task_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    task_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source_fields: list[str] | core.ArrayOut[core.StringOut],
        task_type: str | core.StringOut,
        connector_operator: list[ConnectorOperator]
        | core.ArrayOut[ConnectorOperator]
        | None = None,
        destination_field: str | core.StringOut | None = None,
        task_properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Task.Args(
                source_fields=source_fields,
                task_type=task_type,
                connector_operator=connector_operator,
                destination_field=destination_field,
                task_properties=task_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connector_operator: list[ConnectorOperator] | core.ArrayOut[
            ConnectorOperator
        ] | None = core.arg(default=None)

        destination_field: str | core.StringOut | None = core.arg(default=None)

        source_fields: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        task_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        task_type: str | core.StringOut = core.arg()


@core.schema
class IncrementalPullConfig(core.Schema):

    datetime_type_field_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        datetime_type_field_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=IncrementalPullConfig.Args(
                datetime_type_field_name=datetime_type_field_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        datetime_type_field_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Dynatrace(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=Dynatrace.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class SourceConnectorPropertiesSapoData(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=SourceConnectorPropertiesSapoData.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class Datadog(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=Datadog.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class Veeva(core.Schema):

    document_type: str | core.StringOut | None = core.attr(str, default=None)

    include_all_versions: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_renditions: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_source_files: bool | core.BoolOut | None = core.attr(bool, default=None)

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
        document_type: str | core.StringOut | None = None,
        include_all_versions: bool | core.BoolOut | None = None,
        include_renditions: bool | core.BoolOut | None = None,
        include_source_files: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Veeva.Args(
                object=object,
                document_type=document_type,
                include_all_versions=include_all_versions,
                include_renditions=include_renditions,
                include_source_files=include_source_files,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        document_type: str | core.StringOut | None = core.arg(default=None)

        include_all_versions: bool | core.BoolOut | None = core.arg(default=None)

        include_renditions: bool | core.BoolOut | None = core.arg(default=None)

        include_source_files: bool | core.BoolOut | None = core.arg(default=None)

        object: str | core.StringOut = core.arg()


@core.schema
class InforNexus(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=InforNexus.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class Trendmicro(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=Trendmicro.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class SourceConnectorPropertiesSalesforce(core.Schema):

    enable_dynamic_field_update: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_deleted_records: bool | core.BoolOut | None = core.attr(bool, default=None)

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
        enable_dynamic_field_update: bool | core.BoolOut | None = None,
        include_deleted_records: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=SourceConnectorPropertiesSalesforce.Args(
                object=object,
                enable_dynamic_field_update=enable_dynamic_field_update,
                include_deleted_records=include_deleted_records,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_dynamic_field_update: bool | core.BoolOut | None = core.arg(default=None)

        include_deleted_records: bool | core.BoolOut | None = core.arg(default=None)

        object: str | core.StringOut = core.arg()


@core.schema
class ServiceNow(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=ServiceNow.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class Singular(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=Singular.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class SourceConnectorPropertiesMarketo(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=SourceConnectorPropertiesMarketo.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class S3InputFormatConfig(core.Schema):

    s3_input_file_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_input_file_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3InputFormatConfig.Args(
                s3_input_file_type=s3_input_file_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_input_file_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SourceConnectorPropertiesS3(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    s3_input_format_config: S3InputFormatConfig | None = core.attr(
        S3InputFormatConfig, default=None
    )

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        bucket_prefix: str | core.StringOut | None = None,
        s3_input_format_config: S3InputFormatConfig | None = None,
    ):
        super().__init__(
            args=SourceConnectorPropertiesS3.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                s3_input_format_config=s3_input_format_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        s3_input_format_config: S3InputFormatConfig | None = core.arg(default=None)


@core.schema
class Amplitude(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=Amplitude.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class GoogleAnalytics(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=GoogleAnalytics.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class SourceConnectorPropertiesZendesk(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=SourceConnectorPropertiesZendesk.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class SourceConnectorPropertiesCustomConnector(core.Schema):

    custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    entity_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        entity_name: str | core.StringOut,
        custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=SourceConnectorPropertiesCustomConnector.Args(
                entity_name=entity_name,
                custom_properties=custom_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        entity_name: str | core.StringOut = core.arg()


@core.schema
class Slack(core.Schema):

    object: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object: str | core.StringOut,
    ):
        super().__init__(
            args=Slack.Args(
                object=object,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object: str | core.StringOut = core.arg()


@core.schema
class SourceConnectorProperties(core.Schema):

    amplitude: Amplitude | None = core.attr(Amplitude, default=None)

    custom_connector: SourceConnectorPropertiesCustomConnector | None = core.attr(
        SourceConnectorPropertiesCustomConnector, default=None
    )

    datadog: Datadog | None = core.attr(Datadog, default=None)

    dynatrace: Dynatrace | None = core.attr(Dynatrace, default=None)

    google_analytics: GoogleAnalytics | None = core.attr(GoogleAnalytics, default=None)

    infor_nexus: InforNexus | None = core.attr(InforNexus, default=None)

    marketo: SourceConnectorPropertiesMarketo | None = core.attr(
        SourceConnectorPropertiesMarketo, default=None
    )

    s3: SourceConnectorPropertiesS3 | None = core.attr(SourceConnectorPropertiesS3, default=None)

    salesforce: SourceConnectorPropertiesSalesforce | None = core.attr(
        SourceConnectorPropertiesSalesforce, default=None
    )

    sapo_data: SourceConnectorPropertiesSapoData | None = core.attr(
        SourceConnectorPropertiesSapoData, default=None
    )

    service_now: ServiceNow | None = core.attr(ServiceNow, default=None)

    singular: Singular | None = core.attr(Singular, default=None)

    slack: Slack | None = core.attr(Slack, default=None)

    trendmicro: Trendmicro | None = core.attr(Trendmicro, default=None)

    veeva: Veeva | None = core.attr(Veeva, default=None)

    zendesk: SourceConnectorPropertiesZendesk | None = core.attr(
        SourceConnectorPropertiesZendesk, default=None
    )

    def __init__(
        self,
        *,
        amplitude: Amplitude | None = None,
        custom_connector: SourceConnectorPropertiesCustomConnector | None = None,
        datadog: Datadog | None = None,
        dynatrace: Dynatrace | None = None,
        google_analytics: GoogleAnalytics | None = None,
        infor_nexus: InforNexus | None = None,
        marketo: SourceConnectorPropertiesMarketo | None = None,
        s3: SourceConnectorPropertiesS3 | None = None,
        salesforce: SourceConnectorPropertiesSalesforce | None = None,
        sapo_data: SourceConnectorPropertiesSapoData | None = None,
        service_now: ServiceNow | None = None,
        singular: Singular | None = None,
        slack: Slack | None = None,
        trendmicro: Trendmicro | None = None,
        veeva: Veeva | None = None,
        zendesk: SourceConnectorPropertiesZendesk | None = None,
    ):
        super().__init__(
            args=SourceConnectorProperties.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                infor_nexus=infor_nexus,
                marketo=marketo,
                s3=s3,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: Amplitude | None = core.arg(default=None)

        custom_connector: SourceConnectorPropertiesCustomConnector | None = core.arg(default=None)

        datadog: Datadog | None = core.arg(default=None)

        dynatrace: Dynatrace | None = core.arg(default=None)

        google_analytics: GoogleAnalytics | None = core.arg(default=None)

        infor_nexus: InforNexus | None = core.arg(default=None)

        marketo: SourceConnectorPropertiesMarketo | None = core.arg(default=None)

        s3: SourceConnectorPropertiesS3 | None = core.arg(default=None)

        salesforce: SourceConnectorPropertiesSalesforce | None = core.arg(default=None)

        sapo_data: SourceConnectorPropertiesSapoData | None = core.arg(default=None)

        service_now: ServiceNow | None = core.arg(default=None)

        singular: Singular | None = core.arg(default=None)

        slack: Slack | None = core.arg(default=None)

        trendmicro: Trendmicro | None = core.arg(default=None)

        veeva: Veeva | None = core.arg(default=None)

        zendesk: SourceConnectorPropertiesZendesk | None = core.arg(default=None)


@core.schema
class SourceFlowConfig(core.Schema):

    api_version: str | core.StringOut | None = core.attr(str, default=None)

    connector_profile_name: str | core.StringOut | None = core.attr(str, default=None)

    connector_type: str | core.StringOut = core.attr(str)

    incremental_pull_config: IncrementalPullConfig | None = core.attr(
        IncrementalPullConfig, default=None
    )

    source_connector_properties: SourceConnectorProperties = core.attr(SourceConnectorProperties)

    def __init__(
        self,
        *,
        connector_type: str | core.StringOut,
        source_connector_properties: SourceConnectorProperties,
        api_version: str | core.StringOut | None = None,
        connector_profile_name: str | core.StringOut | None = None,
        incremental_pull_config: IncrementalPullConfig | None = None,
    ):
        super().__init__(
            args=SourceFlowConfig.Args(
                connector_type=connector_type,
                source_connector_properties=source_connector_properties,
                api_version=api_version,
                connector_profile_name=connector_profile_name,
                incremental_pull_config=incremental_pull_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_version: str | core.StringOut | None = core.arg(default=None)

        connector_profile_name: str | core.StringOut | None = core.arg(default=None)

        connector_type: str | core.StringOut = core.arg()

        incremental_pull_config: IncrementalPullConfig | None = core.arg(default=None)

        source_connector_properties: SourceConnectorProperties = core.arg()


@core.schema
class Scheduled(core.Schema):

    data_pull_mode: str | core.StringOut | None = core.attr(str, default=None)

    first_execution_from: str | core.StringOut | None = core.attr(str, default=None)

    schedule_end_time: str | core.StringOut | None = core.attr(str, default=None)

    schedule_expression: str | core.StringOut = core.attr(str)

    schedule_offset: int | core.IntOut | None = core.attr(int, default=None)

    schedule_start_time: str | core.StringOut | None = core.attr(str, default=None)

    timezone: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        schedule_expression: str | core.StringOut,
        data_pull_mode: str | core.StringOut | None = None,
        first_execution_from: str | core.StringOut | None = None,
        schedule_end_time: str | core.StringOut | None = None,
        schedule_offset: int | core.IntOut | None = None,
        schedule_start_time: str | core.StringOut | None = None,
        timezone: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Scheduled.Args(
                schedule_expression=schedule_expression,
                data_pull_mode=data_pull_mode,
                first_execution_from=first_execution_from,
                schedule_end_time=schedule_end_time,
                schedule_offset=schedule_offset,
                schedule_start_time=schedule_start_time,
                timezone=timezone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_pull_mode: str | core.StringOut | None = core.arg(default=None)

        first_execution_from: str | core.StringOut | None = core.arg(default=None)

        schedule_end_time: str | core.StringOut | None = core.arg(default=None)

        schedule_expression: str | core.StringOut = core.arg()

        schedule_offset: int | core.IntOut | None = core.arg(default=None)

        schedule_start_time: str | core.StringOut | None = core.arg(default=None)

        timezone: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TriggerProperties(core.Schema):

    scheduled: Scheduled | None = core.attr(Scheduled, default=None)

    def __init__(
        self,
        *,
        scheduled: Scheduled | None = None,
    ):
        super().__init__(
            args=TriggerProperties.Args(
                scheduled=scheduled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scheduled: Scheduled | None = core.arg(default=None)


@core.schema
class TriggerConfig(core.Schema):

    trigger_properties: TriggerProperties | None = core.attr(
        TriggerProperties, default=None, computed=True
    )

    trigger_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        trigger_type: str | core.StringOut,
        trigger_properties: TriggerProperties | None = None,
    ):
        super().__init__(
            args=TriggerConfig.Args(
                trigger_type=trigger_type,
                trigger_properties=trigger_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        trigger_properties: TriggerProperties | None = core.arg(default=None)

        trigger_type: str | core.StringOut = core.arg()


@core.resource(type="aws_appflow_flow", namespace="appflow")
class Flow(core.Resource):
    """
    The flow's Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of the flow you want to create.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A [Destination Flow Config](#destination-flow-config) that controls how Amazon AppFlow pl
    aces data in the destination connector.
    """
    destination_flow_config: list[DestinationFlowConfig] | core.ArrayOut[
        DestinationFlowConfig
    ] = core.attr(DestinationFlowConfig, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for en
    cryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don'
    t provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
    """
    kms_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of the flow.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The [Source Flow Config](#source-flow-config) that controls how Amazon AppFlow retrieves
    data from the source connector.
    """
    source_flow_config: SourceFlowConfig = core.attr(SourceFlowConfig)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Required) A [Task](#task) that Amazon AppFlow performs while transferring the data in the flow run.
    """
    task: list[Task] | core.ArrayOut[Task] = core.attr(Task, kind=core.Kind.array)

    """
    (Required) A [Trigger](#trigger-config) that determine how and when the flow runs.
    """
    trigger_config: TriggerConfig = core.attr(TriggerConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_flow_config: list[DestinationFlowConfig] | core.ArrayOut[DestinationFlowConfig],
        name: str | core.StringOut,
        source_flow_config: SourceFlowConfig,
        task: list[Task] | core.ArrayOut[Task],
        trigger_config: TriggerConfig,
        description: str | core.StringOut | None = None,
        kms_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Flow.Args(
                destination_flow_config=destination_flow_config,
                name=name,
                source_flow_config=source_flow_config,
                task=task,
                trigger_config=trigger_config,
                description=description,
                kms_arn=kms_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        destination_flow_config: list[DestinationFlowConfig] | core.ArrayOut[
            DestinationFlowConfig
        ] = core.arg()

        kms_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        source_flow_config: SourceFlowConfig = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        task: list[Task] | core.ArrayOut[Task] = core.arg()

        trigger_config: TriggerConfig = core.arg()
