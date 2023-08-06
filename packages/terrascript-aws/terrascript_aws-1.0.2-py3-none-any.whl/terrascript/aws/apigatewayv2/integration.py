import terrascript.core as core


@core.schema
class ResponseParameters(core.Schema):

    mappings: dict[str, str] | core.MapOut[core.StringOut] = core.attr(str, kind=core.Kind.map)

    status_code: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        mappings: dict[str, str] | core.MapOut[core.StringOut],
        status_code: str | core.StringOut,
    ):
        super().__init__(
            args=ResponseParameters.Args(
                mappings=mappings,
                status_code=status_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mappings: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        status_code: str | core.StringOut = core.arg()


@core.schema
class TlsConfig(core.Schema):

    server_name_to_verify: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        server_name_to_verify: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TlsConfig.Args(
                server_name_to_verify=server_name_to_verify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        server_name_to_verify: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_integration", namespace="aws_apigatewayv2")
class Integration(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    connection_id: str | core.StringOut | None = core.attr(str, default=None)

    connection_type: str | core.StringOut | None = core.attr(str, default=None)

    content_handling_strategy: str | core.StringOut | None = core.attr(str, default=None)

    credentials_arn: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    integration_method: str | core.StringOut | None = core.attr(str, default=None)

    integration_response_selection_expression: str | core.StringOut = core.attr(str, computed=True)

    integration_subtype: str | core.StringOut | None = core.attr(str, default=None)

    integration_type: str | core.StringOut = core.attr(str)

    integration_uri: str | core.StringOut | None = core.attr(str, default=None)

    passthrough_behavior: str | core.StringOut | None = core.attr(str, default=None)

    payload_format_version: str | core.StringOut | None = core.attr(str, default=None)

    request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    response_parameters: list[ResponseParameters] | core.ArrayOut[
        ResponseParameters
    ] | None = core.attr(ResponseParameters, default=None, kind=core.Kind.array)

    template_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    timeout_milliseconds: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    tls_config: TlsConfig | None = core.attr(TlsConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        integration_type: str | core.StringOut,
        connection_id: str | core.StringOut | None = None,
        connection_type: str | core.StringOut | None = None,
        content_handling_strategy: str | core.StringOut | None = None,
        credentials_arn: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        integration_method: str | core.StringOut | None = None,
        integration_subtype: str | core.StringOut | None = None,
        integration_uri: str | core.StringOut | None = None,
        passthrough_behavior: str | core.StringOut | None = None,
        payload_format_version: str | core.StringOut | None = None,
        request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        response_parameters: list[ResponseParameters]
        | core.ArrayOut[ResponseParameters]
        | None = None,
        template_selection_expression: str | core.StringOut | None = None,
        timeout_milliseconds: int | core.IntOut | None = None,
        tls_config: TlsConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Integration.Args(
                api_id=api_id,
                integration_type=integration_type,
                connection_id=connection_id,
                connection_type=connection_type,
                content_handling_strategy=content_handling_strategy,
                credentials_arn=credentials_arn,
                description=description,
                integration_method=integration_method,
                integration_subtype=integration_subtype,
                integration_uri=integration_uri,
                passthrough_behavior=passthrough_behavior,
                payload_format_version=payload_format_version,
                request_parameters=request_parameters,
                request_templates=request_templates,
                response_parameters=response_parameters,
                template_selection_expression=template_selection_expression,
                timeout_milliseconds=timeout_milliseconds,
                tls_config=tls_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        connection_id: str | core.StringOut | None = core.arg(default=None)

        connection_type: str | core.StringOut | None = core.arg(default=None)

        content_handling_strategy: str | core.StringOut | None = core.arg(default=None)

        credentials_arn: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        integration_method: str | core.StringOut | None = core.arg(default=None)

        integration_subtype: str | core.StringOut | None = core.arg(default=None)

        integration_type: str | core.StringOut = core.arg()

        integration_uri: str | core.StringOut | None = core.arg(default=None)

        passthrough_behavior: str | core.StringOut | None = core.arg(default=None)

        payload_format_version: str | core.StringOut | None = core.arg(default=None)

        request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        response_parameters: list[ResponseParameters] | core.ArrayOut[
            ResponseParameters
        ] | None = core.arg(default=None)

        template_selection_expression: str | core.StringOut | None = core.arg(default=None)

        timeout_milliseconds: int | core.IntOut | None = core.arg(default=None)

        tls_config: TlsConfig | None = core.arg(default=None)
