import terrascript.core as core


@core.resource(type="aws_codebuild_source_credential", namespace="codebuild")
class SourceCredential(core.Resource):
    """
    The ARN of Source Credential.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket r
    epository. An OAUTH connection is not supported by the API.
    """
    auth_type: str | core.StringOut = core.attr(str)

    """
    The ARN of Source Credential.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The source provider used for this project.
    """
    server_type: str | core.StringOut = core.attr(str)

    """
    (Required) For `GitHub` or `GitHub Enterprise`, this is the personal access token. For `Bitbucket`,
    this is the app password.
    """
    token: str | core.StringOut = core.attr(str)

    """
    (Optional) The Bitbucket username when the authType is `BASIC_AUTH`. This parameter is not valid for
    other types of source providers or connections.
    """
    user_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_type: str | core.StringOut,
        server_type: str | core.StringOut,
        token: str | core.StringOut,
        user_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SourceCredential.Args(
                auth_type=auth_type,
                server_type=server_type,
                token=token,
                user_name=user_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth_type: str | core.StringOut = core.arg()

        server_type: str | core.StringOut = core.arg()

        token: str | core.StringOut = core.arg()

        user_name: str | core.StringOut | None = core.arg(default=None)
