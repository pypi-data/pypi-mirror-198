import terrascript.core as core


@core.resource(type="aws_api_gateway_method_response", namespace="api_gateway")
class MethodResponse(core.Resource):

    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    resource_id: str | core.StringOut = core.attr(str)

    response_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    response_parameters: dict[str, bool] | core.MapOut[core.BoolOut] | None = core.attr(
        bool, default=None, kind=core.Kind.map
    )

    rest_api_id: str | core.StringOut = core.attr(str)

    status_code: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        http_method: str | core.StringOut,
        resource_id: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        status_code: str | core.StringOut,
        response_models: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        response_parameters: dict[str, bool] | core.MapOut[core.BoolOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MethodResponse.Args(
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                status_code=status_code,
                response_models=response_models,
                response_parameters=response_parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        http_method: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()

        response_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        response_parameters: dict[str, bool] | core.MapOut[core.BoolOut] | None = core.arg(
            default=None
        )

        rest_api_id: str | core.StringOut = core.arg()

        status_code: str | core.StringOut = core.arg()
