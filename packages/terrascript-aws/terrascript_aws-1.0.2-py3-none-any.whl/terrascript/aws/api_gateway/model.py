import terrascript.core as core


@core.resource(type="aws_api_gateway_model", namespace="aws_api_gateway")
class Model(core.Resource):

    content_type: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    rest_api_id: str | core.StringOut = core.attr(str)

    schema: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content_type: str | core.StringOut,
        name: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        schema: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Model.Args(
                content_type=content_type,
                name=name,
                rest_api_id=rest_api_id,
                description=description,
                schema=schema,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_type: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()

        schema: str | core.StringOut | None = core.arg(default=None)
