import terrascript.core as core


@core.data(type="aws_api_gateway_resource", namespace="aws_api_gateway")
class DsResource(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    parent_id: str | core.StringOut = core.attr(str, computed=True)

    path: str | core.StringOut = core.attr(str)

    path_part: str | core.StringOut = core.attr(str, computed=True)

    rest_api_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        path: str | core.StringOut,
        rest_api_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsResource.Args(
                path=path,
                rest_api_id=rest_api_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()
