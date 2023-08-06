import terrascript.core as core


@core.data(type="aws_acmpca_certificate", namespace="aws_acmpca")
class DsCertificate(core.Data):

    arn: str | core.StringOut = core.attr(str)

    certificate: str | core.StringOut = core.attr(str, computed=True)

    certificate_authority_arn: str | core.StringOut = core.attr(str)

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
