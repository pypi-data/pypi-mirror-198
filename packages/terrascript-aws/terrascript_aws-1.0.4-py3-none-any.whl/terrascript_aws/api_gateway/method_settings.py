import terrascript.core as core


@core.schema
class Settings(core.Schema):

    cache_data_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    cache_ttl_in_seconds: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    caching_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    data_trace_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    logging_level: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    metrics_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    require_authorization_for_cache_control: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    throttling_burst_limit: int | core.IntOut | None = core.attr(int, default=None)

    throttling_rate_limit: float | core.FloatOut | None = core.attr(float, default=None)

    unauthorized_cache_control_header_strategy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cache_data_encrypted: bool | core.BoolOut | None = None,
        cache_ttl_in_seconds: int | core.IntOut | None = None,
        caching_enabled: bool | core.BoolOut | None = None,
        data_trace_enabled: bool | core.BoolOut | None = None,
        logging_level: str | core.StringOut | None = None,
        metrics_enabled: bool | core.BoolOut | None = None,
        require_authorization_for_cache_control: bool | core.BoolOut | None = None,
        throttling_burst_limit: int | core.IntOut | None = None,
        throttling_rate_limit: float | core.FloatOut | None = None,
        unauthorized_cache_control_header_strategy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Settings.Args(
                cache_data_encrypted=cache_data_encrypted,
                cache_ttl_in_seconds=cache_ttl_in_seconds,
                caching_enabled=caching_enabled,
                data_trace_enabled=data_trace_enabled,
                logging_level=logging_level,
                metrics_enabled=metrics_enabled,
                require_authorization_for_cache_control=require_authorization_for_cache_control,
                throttling_burst_limit=throttling_burst_limit,
                throttling_rate_limit=throttling_rate_limit,
                unauthorized_cache_control_header_strategy=unauthorized_cache_control_header_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cache_data_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        cache_ttl_in_seconds: int | core.IntOut | None = core.arg(default=None)

        caching_enabled: bool | core.BoolOut | None = core.arg(default=None)

        data_trace_enabled: bool | core.BoolOut | None = core.arg(default=None)

        logging_level: str | core.StringOut | None = core.arg(default=None)

        metrics_enabled: bool | core.BoolOut | None = core.arg(default=None)

        require_authorization_for_cache_control: bool | core.BoolOut | None = core.arg(default=None)

        throttling_burst_limit: int | core.IntOut | None = core.arg(default=None)

        throttling_rate_limit: float | core.FloatOut | None = core.arg(default=None)

        unauthorized_cache_control_header_strategy: str | core.StringOut | None = core.arg(
            default=None
        )


@core.resource(type="aws_api_gateway_method_settings", namespace="api_gateway")
class MethodSettings(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Method path defined as `{resource_path}/{http_method}` for an individual method override,
    or `**` for overriding all methods in the stage. Ensure to trim any leading forward slashes in the
    path (e.g., `trimprefix(aws_api_gateway_resource.example.path, "/")`).
    """
    method_path: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the REST API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Required) The settings block, see below.
    """
    settings: Settings = core.attr(Settings)

    """
    (Required) The name of the stage
    """
    stage_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        method_path: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        settings: Settings,
        stage_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MethodSettings.Args(
                method_path=method_path,
                rest_api_id=rest_api_id,
                settings=settings,
                stage_name=stage_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        method_path: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()

        settings: Settings = core.arg()

        stage_name: str | core.StringOut = core.arg()
