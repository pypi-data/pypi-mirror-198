import terrascript.core as core


@core.resource(type="aws_iot_certificate", namespace="iot")
class Certificate(core.Resource):
    """
    (Required)  Boolean flag to indicate if the certificate should be active
    """

    active: bool | core.BoolOut = core.attr(bool)

    """
    The ARN of the created certificate.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The CA certificate for the certificate to be registered. If this is set, the CA needs to
    be registered with AWS IoT beforehand.
    """
    ca_pem: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The certificate to be registered. If `ca_pem` is unspecified, review
    """
    certificate_pem: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The certificate signing request. Review
    """
    csr: str | core.StringOut | None = core.attr(str, default=None)

    """
    The internal ID assigned to this certificate.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    When neither CSR nor certificate is provided, the private key.
    """
    private_key: str | core.StringOut = core.attr(str, computed=True)

    """
    When neither CSR nor certificate is provided, the public key.
    """
    public_key: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        active: bool | core.BoolOut,
        ca_pem: str | core.StringOut | None = None,
        certificate_pem: str | core.StringOut | None = None,
        csr: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                active=active,
                ca_pem=ca_pem,
                certificate_pem=certificate_pem,
                csr=csr,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active: bool | core.BoolOut = core.arg()

        ca_pem: str | core.StringOut | None = core.arg(default=None)

        certificate_pem: str | core.StringOut | None = core.arg(default=None)

        csr: str | core.StringOut | None = core.arg(default=None)
