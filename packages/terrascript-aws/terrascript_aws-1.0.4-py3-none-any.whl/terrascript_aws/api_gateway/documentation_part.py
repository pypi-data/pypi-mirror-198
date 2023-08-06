import terrascript.core as core


@core.schema
class Location(core.Schema):

    method: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    status_code: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        method: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
        status_code: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Location.Args(
                type=type,
                method=method,
                name=name,
                path=path,
                status_code=status_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        method: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        status_code: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_api_gateway_documentation_part", namespace="api_gateway")
class DocumentationPart(core.Resource):
    """
    The unique ID of the Documentation Part
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The location of the targeted API entity of the to-be-created documentation part. See belo
    w.
    """
    location: Location = core.attr(Location)

    """
    (Required) A content map of API-specific key-value pairs describing the targeted API entity. The map
    must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-c
    ompliant key-value pairs can be exported and, hence, published.
    """
    properties: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the associated Rest API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        location: Location,
        properties: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DocumentationPart.Args(
                location=location,
                properties=properties,
                rest_api_id=rest_api_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        location: Location = core.arg()

        properties: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()
