import terrascript.core as core


@core.resource(type="aws_appsync_api_key", namespace="appsync")
class ApiKey(core.Resource):
    """
    (Required) The ID of the associated AppSync API
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The API key description. Defaults to "Managed by Terraform".
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) RFC3339 string representation of the expiry date. Rounded down to nearest hour. By defaul
    t, it is 7 days from the date of creation.
    """
    expires: str | core.StringOut | None = core.attr(str, default=None)

    """
    API Key ID (Formatted as ApiId:Key)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The API key
    """
    key: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        expires: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApiKey.Args(
                api_id=api_id,
                description=description,
                expires=expires,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        expires: str | core.StringOut | None = core.arg(default=None)
