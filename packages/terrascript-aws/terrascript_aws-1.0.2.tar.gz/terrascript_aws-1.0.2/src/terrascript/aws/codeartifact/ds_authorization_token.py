import terrascript.core as core


@core.data(type="aws_codeartifact_authorization_token", namespace="aws_codeartifact")
class DsAuthorizationToken(core.Data):

    authorization_token: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut = core.attr(str)

    domain_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    duration_seconds: int | core.IntOut | None = core.attr(int, default=None)

    expiration: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        domain: str | core.StringOut,
        domain_owner: str | core.StringOut | None = None,
        duration_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAuthorizationToken.Args(
                domain=domain,
                domain_owner=domain_owner,
                duration_seconds=duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: str | core.StringOut = core.arg()

        domain_owner: str | core.StringOut | None = core.arg(default=None)

        duration_seconds: int | core.IntOut | None = core.arg(default=None)
