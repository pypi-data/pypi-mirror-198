import terrascript.core as core


@core.resource(type="aws_api_gateway_resource", namespace="api_gateway")
class Resource(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    parent_id: str | core.StringOut = core.attr(str)

    path: str | core.StringOut = core.attr(str, computed=True)

    path_part: str | core.StringOut = core.attr(str)

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
