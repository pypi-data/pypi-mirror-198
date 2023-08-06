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


@core.data(type="aws_acmpca_certificate_authority", namespace="aws_acmpca")
class DsCertificateAuthority(core.Data):

    arn: str | core.StringOut = core.attr(str)

    certificate: str | core.StringOut = core.attr(str, computed=True)

    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    certificate_signing_request: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    not_after: str | core.StringOut = core.attr(str, computed=True)

    not_before: str | core.StringOut = core.attr(str, computed=True)

    revocation_configuration: list[RevocationConfiguration] | core.ArrayOut[
        RevocationConfiguration
    ] | None = core.attr(RevocationConfiguration, default=None, computed=True, kind=core.Kind.array)

    serial: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
