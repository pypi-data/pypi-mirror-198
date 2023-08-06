import terrascript.core as core


@core.resource(type="aws_acmpca_certificate_authority_certificate", namespace="acmpca")
class CertificateAuthorityCertificate(core.Resource):

    certificate: str | core.StringOut = core.attr(str)

    certificate_authority_arn: str | core.StringOut = core.attr(str)

    certificate_chain: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate: str | core.StringOut,
        certificate_authority_arn: str | core.StringOut,
        certificate_chain: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CertificateAuthorityCertificate.Args(
                certificate=certificate,
                certificate_authority_arn=certificate_authority_arn,
                certificate_chain=certificate_chain,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate: str | core.StringOut = core.arg()

        certificate_authority_arn: str | core.StringOut = core.arg()

        certificate_chain: str | core.StringOut | None = core.arg(default=None)
