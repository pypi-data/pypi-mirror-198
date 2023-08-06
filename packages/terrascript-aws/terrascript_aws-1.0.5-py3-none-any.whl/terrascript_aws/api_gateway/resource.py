import terrascript.core as core


@core.resource(type="aws_api_gateway_resource", namespace="api_gateway")
class Resource(core.Resource):
    """
    The resource's identifier.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the parent API resource
    """
    parent_id: str | core.StringOut = core.attr(str)

    """
    The complete path for this API resource, including all parent paths.
    """
    path: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The last path segment of this API resource.
    """
    path_part: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the associated REST API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        parent_id: str | core.StringOut,
        path_part: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resource.Args(
                parent_id=parent_id,
                path_part=path_part,
                rest_api_id=rest_api_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        parent_id: str | core.StringOut = core.arg()

        path_part: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()
