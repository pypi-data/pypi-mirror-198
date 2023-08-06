import terrascript.core as core


@core.schema
class SourceS3(core.Schema):

    bucket: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str, computed=True)

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
        version: str | core.StringOut,
    ):
        super().__init__(
            args=SourceS3.Args(
                bucket=bucket,
                key=key,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        version: str | core.StringOut = core.arg()


@core.schema
class Source(core.Schema):

    s3: list[SourceS3] | core.ArrayOut[SourceS3] = core.attr(
        SourceS3, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        s3: list[SourceS3] | core.ArrayOut[SourceS3],
    ):
        super().__init__(
            args=Source.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: list[SourceS3] | core.ArrayOut[SourceS3] = core.arg()


@core.schema
class SignedObjectS3(core.Schema):

    bucket: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=SignedObjectS3.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()


@core.schema
class SignedObject(core.Schema):

    s3: list[SignedObjectS3] | core.ArrayOut[SignedObjectS3] = core.attr(
        SignedObjectS3, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        s3: list[SignedObjectS3] | core.ArrayOut[SignedObjectS3],
    ):
        super().__init__(
            args=SignedObject.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: list[SignedObjectS3] | core.ArrayOut[SignedObjectS3] = core.arg()


@core.schema
class RevocationRecord(core.Schema):

    reason: str | core.StringOut = core.attr(str, computed=True)

    revoked_at: str | core.StringOut = core.attr(str, computed=True)

    revoked_by: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        reason: str | core.StringOut,
        revoked_at: str | core.StringOut,
        revoked_by: str | core.StringOut,
    ):
        super().__init__(
            args=RevocationRecord.Args(
                reason=reason,
                revoked_at=revoked_at,
                revoked_by=revoked_by,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        reason: str | core.StringOut = core.arg()

        revoked_at: str | core.StringOut = core.arg()

        revoked_by: str | core.StringOut = core.arg()


@core.data(type="aws_signer_signing_job", namespace="aws_signer")
class DsSigningJob(core.Data):

    completed_at: str | core.StringOut = core.attr(str, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    job_id: str | core.StringOut = core.attr(str)

    job_invoker: str | core.StringOut = core.attr(str, computed=True)

    job_owner: str | core.StringOut = core.attr(str, computed=True)

    platform_display_name: str | core.StringOut = core.attr(str, computed=True)

    platform_id: str | core.StringOut = core.attr(str, computed=True)

    profile_name: str | core.StringOut = core.attr(str, computed=True)

    profile_version: str | core.StringOut = core.attr(str, computed=True)

    requested_by: str | core.StringOut = core.attr(str, computed=True)

    revocation_record: list[RevocationRecord] | core.ArrayOut[RevocationRecord] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    signature_expires_at: str | core.StringOut = core.attr(str, computed=True)

    signed_object: list[SignedObject] | core.ArrayOut[SignedObject] = core.attr(
        SignedObject, computed=True, kind=core.Kind.array
    )

    source: list[Source] | core.ArrayOut[Source] = core.attr(
        Source, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    status_reason: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        job_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsSigningJob.Args(
                job_id=job_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        job_id: str | core.StringOut = core.arg()
