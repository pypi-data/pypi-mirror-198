import terrascript.core as core


@core.data(type="aws_ecrpublic_authorization_token", namespace="ecrpublic")
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
    User name decoded from the authorization token.
    """
    user_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsAuthorizationToken.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
