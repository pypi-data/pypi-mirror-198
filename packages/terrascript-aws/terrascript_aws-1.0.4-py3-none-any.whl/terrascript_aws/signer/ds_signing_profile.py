import terrascript.core as core


@core.schema
class SignatureValidityPeriod(core.Schema):

    type: str | core.StringOut = core.attr(str, computed=True)

    value: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=SignatureValidityPeriod.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class RevocationRecord(core.Schema):

    revocation_effective_from: str | core.StringOut = core.attr(str, computed=True)

    revoked_at: str | core.StringOut = core.attr(str, computed=True)

    revoked_by: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        revocation_effective_from: str | core.StringOut,
        revoked_at: str | core.StringOut,
        revoked_by: str | core.StringOut,
    ):
        super().__init__(
            args=RevocationRecord.Args(
                revocation_effective_from=revocation_effective_from,
                revoked_at=revoked_at,
                revoked_by=revoked_by,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        revocation_effective_from: str | core.StringOut = core.arg()

        revoked_at: str | core.StringOut = core.arg()

        revoked_by: str | core.StringOut = core.arg()


@core.data(type="aws_signer_signing_profile", namespace="signer")
class DsSigningProfile(core.Data):
    """
    The Amazon Resource Name (ARN) for the signing profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the target signing profile.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A human-readable name for the signing platform associated with the signing profile.
    """
    platform_display_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the platform that is used by the target signing profile.
    """
    platform_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Revocation information for a signing profile.
    """
    revocation_record: list[RevocationRecord] | core.ArrayOut[RevocationRecord] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    """
    The validity period for a signing job.
    """
    signature_validity_period: list[SignatureValidityPeriod] | core.ArrayOut[
        SignatureValidityPeriod
    ] = core.attr(SignatureValidityPeriod, computed=True, kind=core.Kind.array)

    """
    The status of the target signing profile.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of tags associated with the signing profile.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The current version of the signing profile.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    The signing profile ARN, including the profile version.
    """
    version_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSigningProfile.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
