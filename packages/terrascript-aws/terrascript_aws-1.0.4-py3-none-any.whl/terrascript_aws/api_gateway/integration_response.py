import terrascript.core as core


@core.resource(type="aws_api_gateway_integration_response", namespace="api_gateway")
class IntegrationResponse(core.Resource):
    """
    (Optional) Specifies how to handle request payload content type conversions. Supported values are `C
    ONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will
    be passed through from the integration response to the method response without modification.
    """

    content_handling: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
    """
    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The API resource ID
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of response parameters that can be read from the backend response.
    """
    response_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) A map specifying the templates used to transform the integration response body
    """
    response_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Required) The ID of the associated REST API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the regular expression pattern used to choose
    """
    selection_pattern: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The HTTP status code
    """
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
