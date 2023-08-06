import terrascript.core as core


@core.schema
class CorsConfiguration(core.Schema):

    allow_credentials: bool | core.BoolOut = core.attr(bool, computed=True)

    allow_headers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    allow_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    allow_origins: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    expose_headers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    max_age: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        allow_credentials: bool | core.BoolOut,
        allow_headers: list[str] | core.ArrayOut[core.StringOut],
        allow_methods: list[str] | core.ArrayOut[core.StringOut],
        allow_origins: list[str] | core.ArrayOut[core.StringOut],
        expose_headers: list[str] | core.ArrayOut[core.StringOut],
        max_age: int | core.IntOut,
    ):
        super().__init__(
            args=CorsConfiguration.Args(
                allow_credentials=allow_credentials,
                allow_headers=allow_headers,
                allow_methods=allow_methods,
                allow_origins=allow_origins,
                expose_headers=expose_headers,
                max_age=max_age,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_credentials: bool | core.BoolOut = core.arg()

        allow_headers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        allow_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        allow_origins: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        expose_headers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        max_age: int | core.IntOut = core.arg()


@core.data(type="aws_apigatewayv2_api", namespace="apigatewayv2")
class DsApi(core.Data):
    """
    The URI of the API, of the form `https://{api-id}.execute-api.{region}.amazonaws.com` for HTTP APIs
    and `wss://{api-id}.execute-api.{region}.amazonaws.com` for WebSocket APIs.
    """

    api_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The API identifier.
    """
    api_id: str | core.StringOut = core.attr(str)

    """
    An [API key selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apiga
    teway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions
    ).
    """
    api_key_selection_expression: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the API.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The cross-origin resource sharing (CORS) [configuration](https://docs.aws.amazon.com/apigateway/late
    st/developerguide/http-api-cors.html).
    """
    cors_configuration: list[CorsConfiguration] | core.ArrayOut[CorsConfiguration] = core.attr(
        CorsConfiguration, computed=True, kind=core.Kind.array
    )

    """
    The description of the API.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether clients can invoke the API by using the default `execute-api` endpoint.
    """
    disable_execute_api_endpoint: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The ARN prefix to be used in an [`aws_lambda_permission`](/docs/providers/aws/r/lambda_permission.ht
    ml)'s `source_arn` attribute
    """
    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the API.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    The API protocol.
    """
    protocol_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The [route selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigat
    eway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions)
    for the API.
    """
    route_selection_expression: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    A version identifier for the API.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        api_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApi.Args(
                api_id=api_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
