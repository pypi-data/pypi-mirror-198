import terrascript.core as core


@core.data(type="aws_api_gateway_resource", namespace="api_gateway")
class DsResource(core.Data):
    """
    Set to the ID of the found Resource.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the ID of the parent Resource.
    """
    parent_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The full path of the resource.  If no path is found, an error will be returned.
    """
    path: str | core.StringOut = core.attr(str)

    """
    Set to the path relative to the parent Resource.
    """
    path_part: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The REST API id that owns the resource. If no REST API is found, an error will be returne
    d.
    """
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
