import terrascript.core as core


@core.resource(type="aws_iam_openid_connect_provider", namespace="iam")
class OpenidConnectProvider(core.Resource):
    """
    The ARN assigned by AWS for this provider.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A list of client IDs (also known as audiences). When a mobile or web app registers with a
    n OpenID Connect provider, they establish a value that identifies the application. (This is the valu
    e that's sent as the client_id parameter on OAuth requests.)
    """
    client_id_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Map of resource tags for the IAM OIDC provider. If configured with a provider [`default_t
    ags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_
    tags-configuration-block) present, tags with matching keys will overwrite those defined at the provi
    der-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider'
    s server certificate(s).
    """
    thumbprint_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) The URL of the identity provider. Corresponds to the _iss_ claim.
    """
    url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        client_id_list: list[str] | core.ArrayOut[core.StringOut],
        thumbprint_list: list[str] | core.ArrayOut[core.StringOut],
        url: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OpenidConnectProvider.Args(
                client_id_list=client_id_list,
                thumbprint_list=thumbprint_list,
                url=url,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_id_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        thumbprint_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        url: str | core.StringOut = core.arg()
