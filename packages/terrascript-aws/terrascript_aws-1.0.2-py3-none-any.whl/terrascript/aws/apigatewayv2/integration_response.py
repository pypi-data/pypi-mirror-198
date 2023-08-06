import terrascript.core as core


@core.resource(type="aws_apigatewayv2_integration_response", namespace="aws_apigatewayv2")
class IntegrationResponse(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    content_handling_strategy: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    integration_id: str | core.StringOut = core.attr(str)

    integration_response_key: str | core.StringOut = core.attr(str)

    response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    template_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        integration_id: str | core.StringOut,
        integration_response_key: str | core.StringOut,
        content_handling_strategy: str | core.StringOut | None = None,
        response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        template_selection_expression: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IntegrationResponse.Args(
                api_id=api_id,
                integration_id=integration_id,
                integration_response_key=integration_response_key,
                content_handling_strategy=content_handling_strategy,
                response_templates=response_templates,
                template_selection_expression=template_selection_expression,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        content_handling_strategy: str | core.StringOut | None = core.arg(default=None)

        integration_id: str | core.StringOut = core.arg()

        integration_response_key: str | core.StringOut = core.arg()

        response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        template_selection_expression: str | core.StringOut | None = core.arg(default=None)
