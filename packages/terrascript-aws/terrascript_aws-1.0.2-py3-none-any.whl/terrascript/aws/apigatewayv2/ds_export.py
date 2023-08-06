import terrascript.core as core


@core.data(type="aws_apigatewayv2_export", namespace="aws_apigatewayv2")
class DsExport(core.Data):

    api_id: str | core.StringOut = core.attr(str)

    body: str | core.StringOut = core.attr(str, computed=True)

    export_version: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    include_extensions: bool | core.BoolOut | None = core.attr(bool, default=None)

    output_type: str | core.StringOut = core.attr(str)

    specification: str | core.StringOut = core.attr(str)

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
