import terrascript.core as core


@core.data(type="aws_iam_openid_connect_provider", namespace="iam")
class DsOpenidConnectProvider(core.Data):
    """
    (Optional) The Amazon Resource Name (ARN) specifying the OpenID Connect provider.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Co
    nnect provider, they establish a value that identifies the application. (This is the value that's se
    nt as the client_id parameter on OAuth requests.)
    """
    client_id_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Map of resource tags for the IAM OIDC provider.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server ce
    rtificate(s).
    """
    thumbprint_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The URL of the OpenID Connect provider.
    """
    url: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        url: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOpenidConnectProvider.Args(
                arn=arn,
                tags=tags,
                url=url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        url: str | core.StringOut | None = core.arg(default=None)
