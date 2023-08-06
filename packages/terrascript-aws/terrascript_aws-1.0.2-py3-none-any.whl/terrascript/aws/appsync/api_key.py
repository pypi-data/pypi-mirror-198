import terrascript.core as core


@core.resource(type="aws_appsync_api_key", namespace="aws_appsync")
class ApiKey(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    expires: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

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
