import terrascript.core as core


@core.data(type="aws_ecr_authorization_token", namespace="ecr")
class DsAuthorizationToken(core.Data):
    """
    Temporary IAM authentication credentials to access the ECR repository encoded in base64 in the form
    of `user_name:password`.
    """

    authorization_token: str | core.StringOut = core.attr(str, computed=True)

    """
    The time in UTC RFC3339 format when the authorization token expires.
    """
    expires_at: str | core.StringOut = core.attr(str, computed=True)

    """
    Region of the authorization token.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Password decoded from the authorization token.
    """
    password: str | core.StringOut = core.attr(str, computed=True)

    """
    The registry URL to use in the docker login command.
    """
    proxy_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) AWS account ID of the ECR Repository. If not specified the default account is assumed.
    """
    registry_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    User name decoded from the authorization token.
    """
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
