import terrascript.core as core


@core.data(type="aws_api_gateway_export", namespace="aws_api_gateway")
class DsExport(core.Data):

    accepts: str | core.StringOut | None = core.attr(str, default=None)

    body: str | core.StringOut = core.attr(str, computed=True)

    content_disposition: str | core.StringOut = core.attr(str, computed=True)

    content_type: str | core.StringOut = core.attr(str, computed=True)

    export_type: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rest_api_id: str | core.StringOut = core.attr(str)

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
