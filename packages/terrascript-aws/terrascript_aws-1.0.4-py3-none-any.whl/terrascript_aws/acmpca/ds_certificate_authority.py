import terrascript.core as core


@core.schema
class CrlConfiguration(core.Schema):

    custom_cname: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    expiration_in_days: int | core.IntOut = core.attr(int, computed=True)

    s3_bucket_name: str | core.StringOut = core.attr(str, computed=True)

    s3_object_acl: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        custom_cname: str | core.StringOut,
        enabled: bool | core.BoolOut,
        expiration_in_days: int | core.IntOut,
        s3_bucket_name: str | core.StringOut,
        s3_object_acl: str | core.StringOut,
    ):
        super().__init__(
            args=CrlConfiguration.Args(
                custom_cname=custom_cname,
                enabled=enabled,
                expiration_in_days=expiration_in_days,
                s3_bucket_name=s3_bucket_name,
                s3_object_acl=s3_object_acl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_cname: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut = core.arg()

        expiration_in_days: int | core.IntOut = core.arg()

        s3_bucket_name: str | core.StringOut = core.arg()

        s3_object_acl: str | core.StringOut = core.arg()


@core.schema
class OcspConfiguration(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    ocsp_custom_cname: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        ocsp_custom_cname: str | core.StringOut,
    ):
        super().__init__(
            args=OcspConfiguration.Args(
                enabled=enabled,
                ocsp_custom_cname=ocsp_custom_cname,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        ocsp_custom_cname: str | core.StringOut = core.arg()


@core.schema
class RevocationConfiguration(core.Schema):

    crl_configuration: list[CrlConfiguration] | core.ArrayOut[CrlConfiguration] | None = core.attr(
        CrlConfiguration, default=None, computed=True, kind=core.Kind.array
    )

    ocsp_configuration: list[OcspConfiguration] | core.ArrayOut[
        OcspConfiguration
    ] | None = core.attr(OcspConfiguration, default=None, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        crl_configuration: list[CrlConfiguration] | core.ArrayOut[CrlConfiguration] | None = None,
        ocsp_configuration: list[OcspConfiguration]
        | core.ArrayOut[OcspConfiguration]
        | None = None,
    ):
        super().__init__(
            args=RevocationConfiguration.Args(
                crl_configuration=crl_configuration,
                ocsp_configuration=ocsp_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crl_configuration: list[CrlConfiguration] | core.ArrayOut[
            CrlConfiguration
        ] | None = core.arg(default=None)

        ocsp_configuration: list[OcspConfiguration] | core.ArrayOut[
            OcspConfiguration
        ] | None = core.arg(default=None)


@core.data(type="aws_acmpca_certificate_authority", namespace="acmpca")
class DsCertificateAuthority(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the certificate authority.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Base64-encoded certificate authority (CA) certificate. Only available after the certificate authorit
    y certificate has been imported.
    """
    certificate: str | core.StringOut = core.attr(str, computed=True)

    """
    Base64-encoded certificate chain that includes any intermediate certificates and chains up to root o
    n-premises certificate that you used to sign your private CA certificate. The chain does not include
    your private CA certificate. Only available after the certificate authority certificate has been im
    ported.
    """
    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    """
    The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
    """
    certificate_signing_request: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the certificate authority.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time after which the certificate authority is not valid. Only available after the certifica
    te authority certificate has been imported.
    """
    not_after: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time before which the certificate authority is not valid. Only available after the certific
    ate authority certificate has been imported.
    """
    not_before: str | core.StringOut = core.attr(str, computed=True)

    """
    Nested attribute containing revocation configuration.
    """
    revocation_configuration: list[RevocationConfiguration] | core.ArrayOut[
        RevocationConfiguration
    ] | None = core.attr(RevocationConfiguration, default=None, computed=True, kind=core.Kind.array)

    """
    Serial number of the certificate authority. Only available after the certificate authority certifica
    te has been imported.
    """
    serial: str | core.StringOut = core.attr(str, computed=True)

    """
    Status of the certificate authority.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies a key-value map of user-defined tags that are attached to the certificate authority.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The type of the certificate authority.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        revocation_configuration: list[RevocationConfiguration]
        | core.ArrayOut[RevocationConfiguration]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificateAuthority.Args(
                arn=arn,
                revocation_configuration=revocation_configuration,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        revocation_configuration: list[RevocationConfiguration] | core.ArrayOut[
            RevocationConfiguration
        ] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
