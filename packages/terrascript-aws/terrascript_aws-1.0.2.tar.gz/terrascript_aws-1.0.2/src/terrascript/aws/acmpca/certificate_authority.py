import terrascript.core as core


@core.schema
class OcspConfiguration(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    ocsp_custom_cname: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        ocsp_custom_cname: str | core.StringOut | None = None,
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

        ocsp_custom_cname: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CrlConfiguration(core.Schema):

    custom_cname: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    expiration_in_days: int | core.IntOut = core.attr(int)

    s3_bucket_name: str | core.StringOut | None = core.attr(str, default=None)

    s3_object_acl: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        expiration_in_days: int | core.IntOut,
        custom_cname: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        s3_bucket_name: str | core.StringOut | None = None,
        s3_object_acl: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CrlConfiguration.Args(
                expiration_in_days=expiration_in_days,
                custom_cname=custom_cname,
                enabled=enabled,
                s3_bucket_name=s3_bucket_name,
                s3_object_acl=s3_object_acl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_cname: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        expiration_in_days: int | core.IntOut = core.arg()

        s3_bucket_name: str | core.StringOut | None = core.arg(default=None)

        s3_object_acl: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RevocationConfiguration(core.Schema):

    crl_configuration: CrlConfiguration | None = core.attr(CrlConfiguration, default=None)

    ocsp_configuration: OcspConfiguration | None = core.attr(OcspConfiguration, default=None)

    def __init__(
        self,
        *,
        crl_configuration: CrlConfiguration | None = None,
        ocsp_configuration: OcspConfiguration | None = None,
    ):
        super().__init__(
            args=RevocationConfiguration.Args(
                crl_configuration=crl_configuration,
                ocsp_configuration=ocsp_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crl_configuration: CrlConfiguration | None = core.arg(default=None)

        ocsp_configuration: OcspConfiguration | None = core.arg(default=None)


@core.schema
class Subject(core.Schema):

    common_name: str | core.StringOut | None = core.attr(str, default=None)

    country: str | core.StringOut | None = core.attr(str, default=None)

    distinguished_name_qualifier: str | core.StringOut | None = core.attr(str, default=None)

    generation_qualifier: str | core.StringOut | None = core.attr(str, default=None)

    given_name: str | core.StringOut | None = core.attr(str, default=None)

    initials: str | core.StringOut | None = core.attr(str, default=None)

    locality: str | core.StringOut | None = core.attr(str, default=None)

    organization: str | core.StringOut | None = core.attr(str, default=None)

    organizational_unit: str | core.StringOut | None = core.attr(str, default=None)

    pseudonym: str | core.StringOut | None = core.attr(str, default=None)

    state: str | core.StringOut | None = core.attr(str, default=None)

    surname: str | core.StringOut | None = core.attr(str, default=None)

    title: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        common_name: str | core.StringOut | None = None,
        country: str | core.StringOut | None = None,
        distinguished_name_qualifier: str | core.StringOut | None = None,
        generation_qualifier: str | core.StringOut | None = None,
        given_name: str | core.StringOut | None = None,
        initials: str | core.StringOut | None = None,
        locality: str | core.StringOut | None = None,
        organization: str | core.StringOut | None = None,
        organizational_unit: str | core.StringOut | None = None,
        pseudonym: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        surname: str | core.StringOut | None = None,
        title: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Subject.Args(
                common_name=common_name,
                country=country,
                distinguished_name_qualifier=distinguished_name_qualifier,
                generation_qualifier=generation_qualifier,
                given_name=given_name,
                initials=initials,
                locality=locality,
                organization=organization,
                organizational_unit=organizational_unit,
                pseudonym=pseudonym,
                state=state,
                surname=surname,
                title=title,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        common_name: str | core.StringOut | None = core.arg(default=None)

        country: str | core.StringOut | None = core.arg(default=None)

        distinguished_name_qualifier: str | core.StringOut | None = core.arg(default=None)

        generation_qualifier: str | core.StringOut | None = core.arg(default=None)

        given_name: str | core.StringOut | None = core.arg(default=None)

        initials: str | core.StringOut | None = core.arg(default=None)

        locality: str | core.StringOut | None = core.arg(default=None)

        organization: str | core.StringOut | None = core.arg(default=None)

        organizational_unit: str | core.StringOut | None = core.arg(default=None)

        pseudonym: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        surname: str | core.StringOut | None = core.arg(default=None)

        title: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CertificateAuthorityConfiguration(core.Schema):

    key_algorithm: str | core.StringOut = core.attr(str)

    signing_algorithm: str | core.StringOut = core.attr(str)

    subject: Subject = core.attr(Subject)

    def __init__(
        self,
        *,
        key_algorithm: str | core.StringOut,
        signing_algorithm: str | core.StringOut,
        subject: Subject,
    ):
        super().__init__(
            args=CertificateAuthorityConfiguration.Args(
                key_algorithm=key_algorithm,
                signing_algorithm=signing_algorithm,
                subject=subject,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_algorithm: str | core.StringOut = core.arg()

        signing_algorithm: str | core.StringOut = core.arg()

        subject: Subject = core.arg()


@core.resource(type="aws_acmpca_certificate_authority", namespace="aws_acmpca")
class CertificateAuthority(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate: str | core.StringOut = core.attr(str, computed=True)

    certificate_authority_configuration: CertificateAuthorityConfiguration = core.attr(
        CertificateAuthorityConfiguration
    )

    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    certificate_signing_request: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    not_after: str | core.StringOut = core.attr(str, computed=True)

    not_before: str | core.StringOut = core.attr(str, computed=True)

    permanent_deletion_time_in_days: int | core.IntOut | None = core.attr(int, default=None)

    revocation_configuration: RevocationConfiguration | None = core.attr(
        RevocationConfiguration, default=None
    )

    serial: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_authority_configuration: CertificateAuthorityConfiguration,
        enabled: bool | core.BoolOut | None = None,
        permanent_deletion_time_in_days: int | core.IntOut | None = None,
        revocation_configuration: RevocationConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CertificateAuthority.Args(
                certificate_authority_configuration=certificate_authority_configuration,
                enabled=enabled,
                permanent_deletion_time_in_days=permanent_deletion_time_in_days,
                revocation_configuration=revocation_configuration,
                tags=tags,
                tags_all=tags_all,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_authority_configuration: CertificateAuthorityConfiguration = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        permanent_deletion_time_in_days: int | core.IntOut | None = core.arg(default=None)

        revocation_configuration: RevocationConfiguration | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
