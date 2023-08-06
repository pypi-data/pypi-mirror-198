import terrascript.core as core


@core.resource(type="aws_api_gateway_documentation_version", namespace="api_gateway")
class DocumentationVersion(core.Resource):
    """
    (Optional) The description of the API documentation version.
    """

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the associated Rest API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Required) The version identifier of the API documentation snapshot.
    """
    version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        rest_api_id: str | core.StringOut,
        version: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DocumentationVersion.Args(
                rest_api_id=rest_api_id,
                version=version,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        version: str | core.StringOut = core.arg()
