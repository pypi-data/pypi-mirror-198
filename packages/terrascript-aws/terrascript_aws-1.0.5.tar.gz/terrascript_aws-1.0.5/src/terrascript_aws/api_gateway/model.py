import terrascript.core as core


@core.resource(type="aws_api_gateway_model", namespace="api_gateway")
class Model(core.Resource):
    """
    (Required) The content type of the model
    """

    content_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The description of the model
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the model
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the model
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the associated REST API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Required) The schema of the model in a JSON form
    """
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
