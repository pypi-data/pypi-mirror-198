import terrascript.core as core


@core.resource(type="aws_api_gateway_gateway_response", namespace="api_gateway")
class GatewayResponse(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    response_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    response_type: str | core.StringOut = core.attr(str)

    rest_api_id: str | core.StringOut = core.attr(str)

    status_code: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        response_type: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        response_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        status_code: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GatewayResponse.Args(
                response_type=response_type,
                rest_api_id=rest_api_id,
                response_parameters=response_parameters,
                response_templates=response_templates,
                status_code=status_code,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        response_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        response_type: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()

        status_code: str | core.StringOut | None = core.arg(default=None)
