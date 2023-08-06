import terrascript.core as core


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


@core.data(type="aws_signer_signing_profile", namespace="aws_signer")
class DsSigningProfile(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    platform_display_name: str | core.StringOut = core.attr(str, computed=True)

    platform_id: str | core.StringOut = core.attr(str, computed=True)

    revocation_record: list[RevocationRecord] | core.ArrayOut[RevocationRecord] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    signature_validity_period: list[SignatureValidityPeriod] | core.ArrayOut[
        SignatureValidityPeriod
    ] = core.attr(SignatureValidityPeriod, computed=True, kind=core.Kind.array)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: str | core.StringOut = core.attr(str, computed=True)

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
