import terrascript.core as core


@core.data(type="aws_api_gateway_export", namespace="api_gateway")
class DsExport(core.Data):
    """
    (Optional) The content-type of the export. Valid values are `application/json` and `application/yaml
    are supported for `export_type` `ofoas30` and `swagger`.
    """

    accepts: str | core.StringOut | None = core.attr(str, default=None)

    """
    The API Spec.
    """
    body: str | core.StringOut = core.attr(str, computed=True)

    """
    The content-disposition header value in the HTTP response.
    """
    content_disposition: str | core.StringOut = core.attr(str, computed=True)

    """
    The content-type header value in the HTTP response.
    """
    content_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of export. Acceptable values are `oas30` for OpenAPI 3.0.x and `swagger` for Swa
    gger/OpenAPI 2.0.
    """
    export_type: str | core.StringOut = core.attr(str)

    """
    The `REST-API-ID:STAGE-NAME`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A key-value map of query string parameters that specify properties of the export. the fol
    lowing parameters are supported: `extensions='integrations'` or `extensions='apigateway'` will expor
    t the API with x-amazon-apigateway-integration extensions. `extensions='authorizers'` will export th
    e API with x-amazon-apigateway-authorizer extensions.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Required) The identifier of the associated REST API.
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the Stage that will be exported.
    """
    stage_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        export_type: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        stage_name: str | core.StringOut,
        accepts: str | core.StringOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsExport.Args(
                export_type=export_type,
                rest_api_id=rest_api_id,
                stage_name=stage_name,
                accepts=accepts,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accepts: str | core.StringOut | None = core.arg(default=None)

        export_type: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        stage_name: str | core.StringOut = core.arg()
