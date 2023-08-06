import terrascript.core as core


@core.schema
class RequestParameter(core.Schema):

    request_parameter_key: str | core.StringOut = core.attr(str)

    required: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        request_parameter_key: str | core.StringOut,
        required: bool | core.BoolOut,
    ):
        super().__init__(
            args=RequestParameter.Args(
                request_parameter_key=request_parameter_key,
                required=required,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        request_parameter_key: str | core.StringOut = core.arg()

        required: bool | core.BoolOut = core.arg()


@core.resource(type="aws_apigatewayv2_route", namespace="apigatewayv2")
class Route(core.Resource):
    """
    (Required) The API identifier.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Boolean whether an API key is required for the route. Defaults to `false`. Supported only
    for WebSocket APIs.
    """
    api_key_required: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The authorization scopes supported by this route. The scopes are used with a JWT authoriz
    er to authorize the method invocation.
    """
    authorization_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The authorization type for the route.
    """
    authorization_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The identifier of the [`aws_apigatewayv2_authorizer`](apigatewayv2_authorizer.html) resou
    rce to be associated with this route.
    """
    authorizer_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The route identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The [model selection expression](https://docs.aws.amazon.com/apigateway/latest/developerg
    uide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-ex
    pressions) for the route. Supported only for WebSocket APIs.
    """
    model_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The operation name for the route. Must be between 1 and 64 characters in length.
    """
    operation_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The request models for the route. Supported only for WebSocket APIs.
    """
    request_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) The request parameters for the route. Supported only for WebSocket APIs.
    """
    request_parameter: list[RequestParameter] | core.ArrayOut[RequestParameter] | None = core.attr(
        RequestParameter, default=None, kind=core.Kind.array
    )

    """
    (Required) The route key for the route. For HTTP APIs, the route key can be either `$default`, or a
    combination of an HTTP method and resource path, for example, `GET /pets`.
    """
    route_key: str | core.StringOut = core.attr(str)

    """
    (Optional) The [route response selection expression](https://docs.aws.amazon.com/apigateway/latest/d
    eveloperguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-res
    ponse-selection-expressions) for the route. Supported only for WebSocket APIs.
    """
    route_response_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The target for the route, of the form `integrations/`*`IntegrationID`*, where *`Integrati
    onID`* is the identifier of an [`aws_apigatewayv2_integration`](apigatewayv2_integration.html) resou
    rce.
    """
    target: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        route_key: str | core.StringOut,
        api_key_required: bool | core.BoolOut | None = None,
        authorization_scopes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        authorization_type: str | core.StringOut | None = None,
        authorizer_id: str | core.StringOut | None = None,
        model_selection_expression: str | core.StringOut | None = None,
        operation_name: str | core.StringOut | None = None,
        request_models: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        request_parameter: list[RequestParameter] | core.ArrayOut[RequestParameter] | None = None,
        route_response_selection_expression: str | core.StringOut | None = None,
        target: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Route.Args(
                api_id=api_id,
                route_key=route_key,
                api_key_required=api_key_required,
                authorization_scopes=authorization_scopes,
                authorization_type=authorization_type,
                authorizer_id=authorizer_id,
                model_selection_expression=model_selection_expression,
                operation_name=operation_name,
                request_models=request_models,
                request_parameter=request_parameter,
                route_response_selection_expression=route_response_selection_expression,
                target=target,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        api_key_required: bool | core.BoolOut | None = core.arg(default=None)

        authorization_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        authorization_type: str | core.StringOut | None = core.arg(default=None)

        authorizer_id: str | core.StringOut | None = core.arg(default=None)

        model_selection_expression: str | core.StringOut | None = core.arg(default=None)

        operation_name: str | core.StringOut | None = core.arg(default=None)

        request_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        request_parameter: list[RequestParameter] | core.ArrayOut[
            RequestParameter
        ] | None = core.arg(default=None)

        route_key: str | core.StringOut = core.arg()

        route_response_selection_expression: str | core.StringOut | None = core.arg(default=None)

        target: str | core.StringOut | None = core.arg(default=None)
