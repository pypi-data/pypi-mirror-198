import terrascript.core as core


@core.data(type="aws_ecrpublic_authorization_token", namespace="aws_ecrpublic")
class DsAuthorizationToken(core.Data):

    authorization_token: str | core.StringOut = core.attr(str, computed=True)

    expires_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    password: str | core.StringOut = core.attr(str, computed=True)

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
