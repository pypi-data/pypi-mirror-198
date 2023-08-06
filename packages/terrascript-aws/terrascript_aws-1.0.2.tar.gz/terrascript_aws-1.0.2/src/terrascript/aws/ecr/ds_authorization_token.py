import terrascript.core as core


@core.data(type="aws_ecr_authorization_token", namespace="aws_ecr")
class DsAuthorizationToken(core.Data):

    authorization_token: str | core.StringOut = core.attr(str, computed=True)

    expires_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    password: str | core.StringOut = core.attr(str, computed=True)

    proxy_endpoint: str | core.StringOut = core.attr(str, computed=True)

    registry_id: str | core.StringOut | None = core.attr(str, default=None)

    user_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        registry_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAuthorizationToken.Args(
                registry_id=registry_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        registry_id: str | core.StringOut | None = core.arg(default=None)
