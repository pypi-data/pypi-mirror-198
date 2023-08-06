import terrascript.core as core


@core.data(type="aws_acmpca_certificate", namespace="acmpca")
class DsCertificate(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the certificate issued by the private certificate authority
    .
    """

    arn: str | core.StringOut = core.attr(str)

    """
    The PEM-encoded certificate value.
    """
    certificate: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon Resource Name (ARN) of the certificate authority.
    """
    certificate_authority_arn: str | core.StringOut = core.attr(str)

    """
    The PEM-encoded certificate chain that includes any intermediate certificates and chains up to root
    CA.
    """
    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        certificate_authority_arn: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificate.Args(
                arn=arn,
                certificate_authority_arn=certificate_authority_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        certificate_authority_arn: str | core.StringOut = core.arg()
