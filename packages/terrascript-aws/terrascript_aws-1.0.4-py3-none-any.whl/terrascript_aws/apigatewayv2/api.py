import terrascript.core as core


@core.schema
class CorsConfiguration(core.Schema):

    allow_credentials: bool | core.BoolOut | None = core.attr(bool, default=None)

    allow_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_methods: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_origins: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_age: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allow_credentials: bool | core.BoolOut | None = None,
        allow_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        allow_methods: list[str] | core.ArrayOut[core.StringOut] | None = None,
        allow_origins: list[str] | core.ArrayOut[core.StringOut] | None = None,
        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        max_age: int | core.IntOut | None = None,
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
        allow_credentials: bool | core.BoolOut | None = core.arg(default=None)

        allow_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allow_methods: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allow_origins: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        max_age: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_api", namespace="apigatewayv2")
class Api(core.Resource):
    """
    The URI of the API, of the form `https://{api-id}.execute-api.{region}.amazonaws.com` for HTTP APIs
    and `wss://{api-id}.execute-api.{region}.amazonaws.com` for WebSocket APIs.
    """

    api_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An [API key selection expression](https://docs.aws.amazon.com/apigateway/latest/developer
    guide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-
    expressions).
    """
    api_key_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN of the API.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An OpenAPI specification that defines the set of routes and integrations to create as par
    t of the HTTP APIs. Supported only for HTTP APIs.
    """
    body: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The cross-origin resource sharing (CORS) [configuration](https://docs.aws.amazon.com/apig
    ateway/latest/developerguide/http-api-cors.html). Applicable for HTTP APIs.
    """
    cors_configuration: CorsConfiguration | None = core.attr(CorsConfiguration, default=None)

    """
    (Optional) Part of _quick create_. Specifies any credentials required for the integration. Applicabl
    e for HTTP APIs.
    """
    credentials_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The description of the API. Must be less than or equal to 1024 characters in length.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether clients can invoke the API by using the default `execute-api` endpoint.
    """
    disable_execute_api_endpoint: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The ARN prefix to be used in an [`aws_lambda_permission`](/docs/providers/aws/r/lambda_permission.ht
    ml)'s `source_arn` attribute
    """
    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether warnings should return an error while API Gateway is creating or updating the res
    ource using an OpenAPI specification. Defaults to `false`. Applicable for HTTP APIs.
    """
    fail_on_warnings: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The API identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the API. Must be less than or equal to 128 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The API protocol. Valid values: `HTTP`, `WEBSOCKET`.
    """
    protocol_type: str | core.StringOut = core.attr(str)

    """
    (Optional) Part of _quick create_. Specifies any [route key](https://docs.aws.amazon.com/apigateway/
    latest/developerguide/http-api-develop-routes.html). Applicable for HTTP APIs.
    """
    route_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The [route selection expression](https://docs.aws.amazon.com/apigateway/latest/developerg
    uide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-ex
    pressions) for the API.
    """
    route_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the API. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) Part of _quick create_. Quick create produces an API with an integration, a default catch
    all route, and a default stage which is configured to automatically deploy changes.
    """
    target: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A version identifier for the API. Must be between 1 and 64 characters in length.
    """
    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        protocol_type: str | core.StringOut,
        api_key_selection_expression: str | core.StringOut | None = None,
        body: str | core.StringOut | None = None,
        cors_configuration: CorsConfiguration | None = None,
        credentials_arn: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        disable_execute_api_endpoint: bool | core.BoolOut | None = None,
        fail_on_warnings: bool | core.BoolOut | None = None,
        route_key: str | core.StringOut | None = None,
        route_selection_expression: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Api.Args(
                name=name,
                protocol_type=protocol_type,
                api_key_selection_expression=api_key_selection_expression,
                body=body,
                cors_configuration=cors_configuration,
                credentials_arn=credentials_arn,
                description=description,
                disable_execute_api_endpoint=disable_execute_api_endpoint,
                fail_on_warnings=fail_on_warnings,
                route_key=route_key,
                route_selection_expression=route_selection_expression,
                tags=tags,
                tags_all=tags_all,
                target=target,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key_selection_expression: str | core.StringOut | None = core.arg(default=None)

        body: str | core.StringOut | None = core.arg(default=None)

        cors_configuration: CorsConfiguration | None = core.arg(default=None)

        credentials_arn: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        disable_execute_api_endpoint: bool | core.BoolOut | None = core.arg(default=None)

        fail_on_warnings: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        protocol_type: str | core.StringOut = core.arg()

        route_key: str | core.StringOut | None = core.arg(default=None)

        route_selection_expression: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)
