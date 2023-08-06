import terrascript.core as core


@core.data(type="aws_api_gateway_sdk", namespace="aws_api_gateway")
class DsSdk(core.Data):

    body: str | core.StringOut = core.attr(str, computed=True)

    content_disposition: str | core.StringOut = core.attr(str, computed=True)

    content_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rest_api_id: str | core.StringOut = core.attr(str)

    sdk_type: str | core.StringOut = core.attr(str)

    stage_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        rest_api_id: str | core.StringOut,
        sdk_type: str | core.StringOut,
        stage_name: str | core.StringOut,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSdk.Args(
                rest_api_id=rest_api_id,
                sdk_type=sdk_type,
                stage_name=stage_name,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        sdk_type: str | core.StringOut = core.arg()

        stage_name: str | core.StringOut = core.arg()
