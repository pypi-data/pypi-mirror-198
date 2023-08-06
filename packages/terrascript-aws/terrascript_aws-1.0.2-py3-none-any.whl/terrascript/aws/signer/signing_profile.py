import terrascript.core as core


@core.schema
class SignatureValidityPeriod(core.Schema):

    type: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

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


@core.resource(type="aws_signer_signing_profile", namespace="aws_signer")
class SigningProfile(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    platform_display_name: str | core.StringOut = core.attr(str, computed=True)

    platform_id: str | core.StringOut = core.attr(str)

    revocation_record: list[RevocationRecord] | core.ArrayOut[RevocationRecord] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    signature_validity_period: SignatureValidityPeriod | None = core.attr(
        SignatureValidityPeriod, default=None, computed=True
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: str | core.StringOut = core.attr(str, computed=True)

    version_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        platform_id: str | core.StringOut,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        signature_validity_period: SignatureValidityPeriod | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningProfile.Args(
                platform_id=platform_id,
                name=name,
                name_prefix=name_prefix,
                signature_validity_period=signature_validity_period,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        platform_id: str | core.StringOut = core.arg()

        signature_validity_period: SignatureValidityPeriod | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
