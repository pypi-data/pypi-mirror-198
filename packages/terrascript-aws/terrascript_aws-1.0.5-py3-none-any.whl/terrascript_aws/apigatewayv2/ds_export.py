import terrascript.core as core


@core.data(type="aws_apigatewayv2_export", namespace="apigatewayv2")
class DsExport(core.Data):
    """
    (Required) The API identifier.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    The id of the API.
    """
    body: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The version of the API Gateway export algorithm. API Gateway uses the latest version by d
    efault. Currently, the only supported version is `1.0`.
    """
    export_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    The API identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether to include API Gateway extensions in the exported API definition. API G
    ateway extensions are included by default.
    """
    include_extensions: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The output type of the exported definition file. Valid values are `JSON` and `YAML`.
    """
    output_type: str | core.StringOut = core.attr(str)

    """
    (Required) The version of the API specification to use. `OAS30`, for OpenAPI 3.0, is the only suppor
    ted value.
    """
    specification: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the API stage to export. If you don't specify this property, a representation
    of the latest API configuration is exported.
    """
    stage_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        api_id: str | core.StringOut,
        output_type: str | core.StringOut,
        specification: str | core.StringOut,
        export_version: str | core.StringOut | None = None,
        include_extensions: bool | core.BoolOut | None = None,
        stage_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsExport.Args(
                api_id=api_id,
                output_type=output_type,
                specification=specification,
                export_version=export_version,
                include_extensions=include_extensions,
                stage_name=stage_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_id: str | core.StringOut = core.arg()

        export_version: str | core.StringOut | None = core.arg(default=None)

        include_extensions: bool | core.BoolOut | None = core.arg(default=None)

        output_type: str | core.StringOut = core.arg()

        specification: str | core.StringOut = core.arg()

        stage_name: str | core.StringOut | None = core.arg(default=None)
