import terrascript.core as core


@core.resource(type="aws_apigatewayv2_route_response", namespace="aws_apigatewayv2")
class RouteResponse(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    model_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    response_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    route_id: str | core.StringOut = core.attr(str)

    route_response_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        route_id: str | core.StringOut,
        route_response_key: str | core.StringOut,
        model_selection_expression: str | core.StringOut | None = None,
        response_models: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RouteResponse.Args(
                api_id=api_id,
                route_id=route_id,
                route_response_key=route_response_key,
                model_selection_expression=model_selection_expression,
                response_models=response_models,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        model_selection_expression: str | core.StringOut | None = core.arg(default=None)

        response_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        route_id: str | core.StringOut = core.arg()

        route_response_key: str | core.StringOut = core.arg()
