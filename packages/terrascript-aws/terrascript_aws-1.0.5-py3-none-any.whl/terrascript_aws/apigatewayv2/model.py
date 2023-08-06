import terrascript.core as core


@core.resource(type="aws_apigatewayv2_model", namespace="apigatewayv2")
class Model(core.Resource):
    """
    (Required) The API identifier.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    (Required)  The content-type for the model, for example, `application/json`. Must be between 1 and 2
    56 characters in length.
    """
    content_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The description of the model. Must be between 1 and 128 characters in length.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The model identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the model. Must be alphanumeric. Must be between 1 and 128 characters in leng
    th.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The schema for the model. This should be a [JSON schema draft 4](https://tools.ietf.org/h
    tml/draft-zyp-json-schema-04) model. Must be less than or equal to 32768 characters in length.
    """
    schema: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        content_type: str | core.StringOut,
        name: str | core.StringOut,
        schema: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Model.Args(
                api_id=api_id,
                content_type=content_type,
                name=name,
                schema=schema,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        content_type: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        schema: str | core.StringOut = core.arg()
