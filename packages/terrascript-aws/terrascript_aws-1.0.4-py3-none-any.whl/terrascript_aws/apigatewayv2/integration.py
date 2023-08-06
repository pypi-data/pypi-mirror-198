import terrascript.core as core


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


@core.resource(type="aws_apigatewayv2_integration", namespace="apigatewayv2")
class Integration(core.Resource):
    """
    (Required) The API identifier.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The ID of the [VPC link](apigatewayv2_vpc_link.html) for a private integration. Supported
    only for HTTP APIs. Must be between 1 and 1024 characters in length.
    """
    connection_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The type of the network connection to the integration endpoint. Valid values: `INTERNET`,
    VPC_LINK`. Default is `INTERNET`.
    """
    connection_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY
    , `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.
    """
    content_handling_strategy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The credentials required for the integration, if any.
    """
    credentials_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The description of the integration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The integration identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.
    """
    integration_method: str | core.StringOut | None = core.attr(str, default=None)

    """
    The [integration response selection expression](https://docs.aws.amazon.com/apigateway/latest/develo
    perguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-re
    sponse-selection-expressions) for the integration.
    """
    integration_response_selection_expression: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the AWS service action to invoke. Supported only for HTTP APIs when `integratio
    n_type` is `AWS_PROXY`. See the [AWS service integration reference](https://docs.aws.amazon.com/apig
    ateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html) documentatio
    n for supported values. Must be between 1 and 128 characters in length.
    """
    integration_subtype: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The integration type of an integration.
    """
    integration_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is
    AWS_PROXY`.
    """
    integration_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The pass-through behavior for incoming requests based on the Content-Type header in the r
    equest, and the available mapping templates specified as the `request_templates` attribute.
    """
    passthrough_behavior: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/
    http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to
    an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.
    """
    payload_format_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) For WebSocket APIs, a key-value map specifying request parameters that are passed from th
    e method request to the backend.
    """
    request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) A map of [Velocity](https://velocity.apache.org/) templates that are applied on the reque
    st payload based on the value of the Content-Type header sent by the client. Supported only for WebS
    ocket APIs.
    """
    request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Mappings to transform the HTTP response from a backend integration before returning the r
    esponse to clients. Supported only for HTTP APIs.
    """
    response_parameters: list[ResponseParameters] | core.ArrayOut[
        ResponseParameters
    ] | None = core.attr(ResponseParameters, default=None, kind=core.Kind.array)

    """
    (Optional) The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/develop
    erguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-select
    ion-expressions) for the integration.
    """
    template_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 3
    0,000 milliseconds for HTTP APIs.
    """
    timeout_milliseconds: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The TLS configuration for a private integration. Supported only for HTTP APIs.
    """
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
