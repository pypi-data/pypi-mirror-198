import terrascript.core as core


@core.schema
class SourceAccessConfiguration(core.Schema):

    type: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        uri: str | core.StringOut,
    ):
        super().__init__(
            args=SourceAccessConfiguration.Args(
                type=type,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        uri: str | core.StringOut = core.arg()


@core.schema
class SelfManagedEventSource(core.Schema):

    endpoints: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    def __init__(
        self,
        *,
        endpoints: dict[str, str] | core.MapOut[core.StringOut],
    ):
        super().__init__(
            args=SelfManagedEventSource.Args(
                endpoints=endpoints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoints: dict[str, str] | core.MapOut[core.StringOut] = core.arg()


@core.schema
class OnFailure(core.Schema):

    destination_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination_arn: str | core.StringOut,
    ):
        super().__init__(
            args=OnFailure.Args(
                destination_arn=destination_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_arn: str | core.StringOut = core.arg()


@core.schema
class DestinationConfig(core.Schema):

    on_failure: OnFailure | None = core.attr(OnFailure, default=None)

    def __init__(
        self,
        *,
        on_failure: OnFailure | None = None,
    ):
        super().__init__(
            args=DestinationConfig.Args(
                on_failure=on_failure,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_failure: OnFailure | None = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    pattern: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        pattern: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                pattern=pattern,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pattern: str | core.StringOut | None = core.arg(default=None)


@core.schema
class FilterCriteria(core.Schema):

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
    ):
        super().__init__(
            args=FilterCriteria.Args(
                filter=filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)


@core.resource(type="aws_lambda_event_source_mapping", namespace="lambda_")
class EventSourceMapping(core.Resource):
    """
    (Optional) The largest number of records that Lambda will retrieve from your event source at the tim
    e of invocation. Defaults to `100` for DynamoDB, Kinesis, MQ and MSK, `10` for SQS.
    """

    batch_size: int | core.IntOut | None = core.attr(int, default=None)

    bisect_batch_on_function_error: bool | core.BoolOut | None = core.attr(bool, default=None)

    destination_config: DestinationConfig | None = core.attr(DestinationConfig, default=None)

    """
    (Optional) Determines if the mapping will be enabled on creation. Defaults to `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The event source ARN - this is required for Kinesis stream, DynamoDB stream, SQS queue, M
    Q broker or MSK cluster.  It is incompatible with a Self Managed Kafka source.
    """
    event_source_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The criteria to use for [event filtering](https://docs.aws.amazon.com/lambda/latest/dg/in
    vocation-eventfiltering.html) Kinesis stream, DynamoDB stream, SQS queue event sources. Detailed bel
    ow.
    """
    filter_criteria: FilterCriteria | None = core.attr(FilterCriteria, default=None)

    """
    The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a c
    omputed value that differs from `function_name` above.)
    """
    function_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or the ARN of the Lambda function that will be subscribing to events.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of current response type enums applied to the event source mapping for [AWS Lambda
    checkpointing](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-batchfailure
    reporting). Only available for SQS and stream sources (DynamoDB and Kinesis). Valid values: `ReportB
    atchItemFailures`.
    """
    function_response_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date this resource was last modified.
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    """
    The result of the last AWS Lambda invocation of your Lambda function.
    """
    last_processing_result: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The maximum amount of time to gather records before invoking the function, in seconds (be
    tween 0 and 300). Records will continue to buffer (or accumulate in the case of an SQS queue event s
    ource) until either `maximum_batching_window_in_seconds` expires or `batch_size` has been met. For s
    treaming event sources, defaults to as soon as records are available in the stream. If the batch it
    reads from the stream/queue only has one record in it, Lambda only sends one record to the function.
    Only available for stream sources (DynamoDB and Kinesis) and SQS standard queues.
    """
    maximum_batching_window_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    maximum_record_age_in_seconds: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    maximum_retry_attempts: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    parallelization_factor: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The name of the Amazon MQ broker destination queue to consume. Only available for MQ sour
    ces. A single queue name must be specified.
    """
    queues: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_managed_event_source: SelfManagedEventSource | None = core.attr(
        SelfManagedEventSource, default=None
    )

    source_access_configuration: list[SourceAccessConfiguration] | core.ArrayOut[
        SourceAccessConfiguration
    ] | None = core.attr(SourceAccessConfiguration, default=None, kind=core.Kind.array)

    """
    (Optional) The position in the stream where AWS Lambda should start reading. Must be one of `AT_TIME
    STAMP` (Kinesis only), `LATEST` or `TRIM_HORIZON` if getting events from Kinesis, DynamoDB or MSK. M
    ust not be provided if getting events from SQS. More information about these positions can be found
    in the [AWS DynamoDB Streams API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIRef
    erence/API_streams_GetShardIterator.html) and [AWS Kinesis API Reference](https://docs.aws.amazon.co
    m/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIterat
    orType).
    """
    starting_position: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of the d
    ata record which to start reading when using `starting_position` set to `AT_TIMESTAMP`. If a record
    with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older
    than the current trim horizon, the oldest available record is chosen.
    """
    starting_position_timestamp: str | core.StringOut | None = core.attr(str, default=None)

    """
    The state of the event source mapping.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    The reason the event source mapping is in its current state.
    """
    state_transition_reason: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the Kafka topics. Only available for MSK sources. A single topic name must be
    specified.
    """
    topics: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The duration in seconds of a processing window for [AWS Lambda streaming analytics](https
    ://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-windows). The range is be
    tween 1 second up to 900 seconds. Only available for stream sources (DynamoDB and Kinesis).
    """
    tumbling_window_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    The UUID of the created event source mapping.
    """
    uuid: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: str | core.StringOut,
        batch_size: int | core.IntOut | None = None,
        bisect_batch_on_function_error: bool | core.BoolOut | None = None,
        destination_config: DestinationConfig | None = None,
        enabled: bool | core.BoolOut | None = None,
        event_source_arn: str | core.StringOut | None = None,
        filter_criteria: FilterCriteria | None = None,
        function_response_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        maximum_batching_window_in_seconds: int | core.IntOut | None = None,
        maximum_record_age_in_seconds: int | core.IntOut | None = None,
        maximum_retry_attempts: int | core.IntOut | None = None,
        parallelization_factor: int | core.IntOut | None = None,
        queues: list[str] | core.ArrayOut[core.StringOut] | None = None,
        self_managed_event_source: SelfManagedEventSource | None = None,
        source_access_configuration: list[SourceAccessConfiguration]
        | core.ArrayOut[SourceAccessConfiguration]
        | None = None,
        starting_position: str | core.StringOut | None = None,
        starting_position_timestamp: str | core.StringOut | None = None,
        topics: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tumbling_window_in_seconds: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventSourceMapping.Args(
                function_name=function_name,
                batch_size=batch_size,
                bisect_batch_on_function_error=bisect_batch_on_function_error,
                destination_config=destination_config,
                enabled=enabled,
                event_source_arn=event_source_arn,
                filter_criteria=filter_criteria,
                function_response_types=function_response_types,
                maximum_batching_window_in_seconds=maximum_batching_window_in_seconds,
                maximum_record_age_in_seconds=maximum_record_age_in_seconds,
                maximum_retry_attempts=maximum_retry_attempts,
                parallelization_factor=parallelization_factor,
                queues=queues,
                self_managed_event_source=self_managed_event_source,
                source_access_configuration=source_access_configuration,
                starting_position=starting_position,
                starting_position_timestamp=starting_position_timestamp,
                topics=topics,
                tumbling_window_in_seconds=tumbling_window_in_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        batch_size: int | core.IntOut | None = core.arg(default=None)

        bisect_batch_on_function_error: bool | core.BoolOut | None = core.arg(default=None)

        destination_config: DestinationConfig | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        event_source_arn: str | core.StringOut | None = core.arg(default=None)

        filter_criteria: FilterCriteria | None = core.arg(default=None)

        function_name: str | core.StringOut = core.arg()

        function_response_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        maximum_batching_window_in_seconds: int | core.IntOut | None = core.arg(default=None)

        maximum_record_age_in_seconds: int | core.IntOut | None = core.arg(default=None)

        maximum_retry_attempts: int | core.IntOut | None = core.arg(default=None)

        parallelization_factor: int | core.IntOut | None = core.arg(default=None)

        queues: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        self_managed_event_source: SelfManagedEventSource | None = core.arg(default=None)

        source_access_configuration: list[SourceAccessConfiguration] | core.ArrayOut[
            SourceAccessConfiguration
        ] | None = core.arg(default=None)

        starting_position: str | core.StringOut | None = core.arg(default=None)

        starting_position_timestamp: str | core.StringOut | None = core.arg(default=None)

        topics: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tumbling_window_in_seconds: int | core.IntOut | None = core.arg(default=None)
