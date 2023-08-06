import terrascript.core as core


@core.data(type="aws_codeartifact_authorization_token", namespace="codeartifact")
class DsAuthorizationToken(core.Data):
    """
    Temporary authorization token.
    """

    authorization_token: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the domain that is in scope for the generated authorization token.
    """
    domain: str | core.StringOut = core.attr(str)

    """
    (Optional) The account number of the AWS account that owns the domain.
    """
    domain_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The time, in seconds, that the generated authorization token is valid. Valid values are `
    0` and between `900` and `43200`.
    """
    duration_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    The time in UTC RFC3339 format when the authorization token expires.
    """
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
