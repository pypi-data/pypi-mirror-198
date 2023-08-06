import terrascript.core as core


@core.resource(type="aws_api_gateway_client_certificate", namespace="api_gateway")
class ClientCertificate(core.Resource):
    """
    Amazon Resource Name (ARN)
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the client certificate was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the client certificate.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The date when the client certificate will expire.
    """
    expiration_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the client certificate.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The PEM-encoded public key of the client certificate.
    """
    pem_encoded_certificate: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClientCertificate.Args(
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
