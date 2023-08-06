import terrascript.core as core


@core.resource(type="aws_dms_certificate", namespace="dms")
class Certificate(core.Resource):
    """
    The Amazon Resource Name (ARN) for the certificate.
    """

    certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The certificate identifier.
    """
    certificate_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The contents of the .pem X.509 certificate file for the certificate. Either `certificate_
    pem` or `certificate_wallet` must be set.
    """
    certificate_pem: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The contents of the Oracle Wallet certificate for use with SSL, provided as a base64-enco
    ded String. Either `certificate_pem` or `certificate_wallet` must be set.
    """
    certificate_wallet: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
        certificate_id: str | core.StringOut,
        certificate_pem: str | core.StringOut | None = None,
        certificate_wallet: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                certificate_id=certificate_id,
                certificate_pem=certificate_pem,
                certificate_wallet=certificate_wallet,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_id: str | core.StringOut = core.arg()

        certificate_pem: str | core.StringOut | None = core.arg(default=None)

        certificate_wallet: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
