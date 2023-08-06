import terrascript.core as core


@core.resource(type="aws_api_gateway_integration_response", namespace="aws_api_gateway")
class IntegrationResponse(core.Resource):

    content_handling: str | core.StringOut | None = core.attr(str, default=None)

    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    resource_id: str | core.StringOut = core.attr(str)

    response_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rest_api_id: str | core.StringOut = core.attr(str)

    selection_pattern: str | core.StringOut | None = core.attr(str, default=None)

    status_code: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        http_method: str | core.StringOut,
        resource_id: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        status_code: str | core.StringOut,
        content_handling: str | core.StringOut | None = None,
        response_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        selection_pattern: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IntegrationResponse.Args(
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                status_code=status_code,
                content_handling=content_handling,
                response_parameters=response_parameters,
                response_templates=response_templates,
                selection_pattern=selection_pattern,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_handling: str | core.StringOut | None = core.arg(default=None)

        http_method: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()

        response_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        rest_api_id: str | core.StringOut = core.arg()

        selection_pattern: str | core.StringOut | None = core.arg(default=None)

        status_code: str | core.StringOut = core.arg()
