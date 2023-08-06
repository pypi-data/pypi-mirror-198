import terrascript.core as core


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


@core.resource(type="aws_lambda_event_source_mapping", namespace="aws_lambda_")
class EventSourceMapping(core.Resource):

    batch_size: int | core.IntOut | None = core.attr(int, default=None)

    bisect_batch_on_function_error: bool | core.BoolOut | None = core.attr(bool, default=None)

    destination_config: DestinationConfig | None = core.attr(DestinationConfig, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    event_source_arn: str | core.StringOut | None = core.attr(str, default=None)

    filter_criteria: FilterCriteria | None = core.attr(FilterCriteria, default=None)

    function_arn: str | core.StringOut = core.attr(str, computed=True)

    function_name: str | core.StringOut = core.attr(str)

    function_response_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    last_processing_result: str | core.StringOut = core.attr(str, computed=True)

    maximum_batching_window_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    maximum_record_age_in_seconds: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    maximum_retry_attempts: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    parallelization_factor: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    queues: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_managed_event_source: SelfManagedEventSource | None = core.attr(
        SelfManagedEventSource, default=None
    )

    source_access_configuration: list[SourceAccessConfiguration] | core.ArrayOut[
        SourceAccessConfiguration
    ] | None = core.attr(SourceAccessConfiguration, default=None, kind=core.Kind.array)

    starting_position: str | core.StringOut | None = core.attr(str, default=None)

    starting_position_timestamp: str | core.StringOut | None = core.attr(str, default=None)

    state: str | core.StringOut = core.attr(str, computed=True)

    state_transition_reason: str | core.StringOut = core.attr(str, computed=True)

    topics: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tumbling_window_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

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
