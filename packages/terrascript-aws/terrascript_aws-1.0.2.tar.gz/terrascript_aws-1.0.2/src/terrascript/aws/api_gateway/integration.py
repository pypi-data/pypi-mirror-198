import terrascript.core as core


@core.schema
class TlsConfig(core.Schema):

    insecure_skip_verification: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        insecure_skip_verification: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=TlsConfig.Args(
                insecure_skip_verification=insecure_skip_verification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insecure_skip_verification: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_api_gateway_integration", namespace="aws_api_gateway")
class Integration(core.Resource):

    cache_key_parameters: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cache_namespace: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    connection_id: str | core.StringOut | None = core.attr(str, default=None)

    connection_type: str | core.StringOut | None = core.attr(str, default=None)

    content_handling: str | core.StringOut | None = core.attr(str, default=None)

    credentials: str | core.StringOut | None = core.attr(str, default=None)

    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    integration_http_method: str | core.StringOut | None = core.attr(str, default=None)

    passthrough_behavior: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    resource_id: str | core.StringOut = core.attr(str)

    rest_api_id: str | core.StringOut = core.attr(str)

    timeout_milliseconds: int | core.IntOut | None = core.attr(int, default=None)

    tls_config: TlsConfig | None = core.attr(TlsConfig, default=None)

    type: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        http_method: str | core.StringOut,
        resource_id: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        type: str | core.StringOut,
        cache_key_parameters: list[str] | core.ArrayOut[core.StringOut] | None = None,
        cache_namespace: str | core.StringOut | None = None,
        connection_id: str | core.StringOut | None = None,
        connection_type: str | core.StringOut | None = None,
        content_handling: str | core.StringOut | None = None,
        credentials: str | core.StringOut | None = None,
        integration_http_method: str | core.StringOut | None = None,
        passthrough_behavior: str | core.StringOut | None = None,
        request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timeout_milliseconds: int | core.IntOut | None = None,
        tls_config: TlsConfig | None = None,
        uri: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Integration.Args(
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                type=type,
                cache_key_parameters=cache_key_parameters,
                cache_namespace=cache_namespace,
                connection_id=connection_id,
                connection_type=connection_type,
                content_handling=content_handling,
                credentials=credentials,
                integration_http_method=integration_http_method,
                passthrough_behavior=passthrough_behavior,
                request_parameters=request_parameters,
                request_templates=request_templates,
                timeout_milliseconds=timeout_milliseconds,
                tls_config=tls_config,
                uri=uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cache_key_parameters: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        cache_namespace: str | core.StringOut | None = core.arg(default=None)

        connection_id: str | core.StringOut | None = core.arg(default=None)

        connection_type: str | core.StringOut | None = core.arg(default=None)

        content_handling: str | core.StringOut | None = core.arg(default=None)

        credentials: str | core.StringOut | None = core.arg(default=None)

        http_method: str | core.StringOut = core.arg()

        integration_http_method: str | core.StringOut | None = core.arg(default=None)

        passthrough_behavior: str | core.StringOut | None = core.arg(default=None)

        request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        resource_id: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()

        timeout_milliseconds: int | core.IntOut | None = core.arg(default=None)

        tls_config: TlsConfig | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        uri: str | core.StringOut | None = core.arg(default=None)
