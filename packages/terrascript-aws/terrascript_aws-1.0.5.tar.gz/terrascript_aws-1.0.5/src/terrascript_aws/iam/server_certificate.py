import terrascript.core as core


@core.resource(type="aws_iam_server_certificate", namespace="iam")
class ServerCertificate(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the server certificate.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_body: str | core.StringOut = core.attr(str)

    certificate_chain: str | core.StringOut | None = core.attr(str, default=None)

    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) on which the cert
    ificate is set to expire.
    """
    expiration: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique Server Certificate name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the Server Certificate. Do not include the
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IAM path for the server certificate.  If it is not
    """
    path: str | core.StringOut | None = core.attr(str, default=None)

    private_key: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of resource tags for the server certificate. If configured with a provider [`default_
    tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default
    _tags-configuration-block) present, tags with matching keys will overwrite those defined at the prov
    ider-level.
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
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) when the server c
    ertificate was uploaded.
    """
    upload_date: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_body: str | core.StringOut,
        private_key: str | core.StringOut,
        certificate_chain: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServerCertificate.Args(
                certificate_body=certificate_body,
                private_key=private_key,
                certificate_chain=certificate_chain,
                name=name,
                name_prefix=name_prefix,
                path=path,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_body: str | core.StringOut = core.arg()

        certificate_chain: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        private_key: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
