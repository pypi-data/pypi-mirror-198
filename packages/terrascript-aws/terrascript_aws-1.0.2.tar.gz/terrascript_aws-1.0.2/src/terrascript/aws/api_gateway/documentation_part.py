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


@core.resource(type="aws_api_gateway_documentation_part", namespace="aws_api_gateway")
class DocumentationPart(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    location: Location = core.attr(Location)

    properties: str | core.StringOut = core.attr(str)

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
