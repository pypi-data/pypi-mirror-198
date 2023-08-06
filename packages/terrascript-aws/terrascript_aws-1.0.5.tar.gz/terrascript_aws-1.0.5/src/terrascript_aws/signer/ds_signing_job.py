import terrascript.core as core


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


@core.data(type="aws_signer_signing_job", namespace="signer")
class DsSigningJob(core.Data):
    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the signing
    job was completed.
    """

    completed_at: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the signing
    job was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the signing job on output.
    """
    job_id: str | core.StringOut = core.attr(str)

    """
    The IAM entity that initiated the signing job.
    """
    job_invoker: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account ID of the job owner.
    """
    job_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    A human-readable name for the signing platform associated with the signing job.
    """
    platform_display_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The platform to which your signed code image will be distributed.
    """
    platform_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the profile that initiated the signing operation.
    """
    profile_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The version of the signing profile used to initiate the signing job.
    """
    profile_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The IAM principal that requested the signing job.
    """
    requested_by: str | core.StringOut = core.attr(str, computed=True)

    """
    A revocation record if the signature generated by the signing job has been revoked. Contains a times
    tamp and the ID of the IAM entity that revoked the signature.
    """
    revocation_record: list[RevocationRecord] | core.ArrayOut[RevocationRecord] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    """
    The time when the signature of a signing job expires.
    """
    signature_expires_at: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the S3 bucket where the signed code image is saved by code signing.
    """
    signed_object: list[SignedObject] | core.ArrayOut[SignedObject] = core.attr(
        SignedObject, computed=True, kind=core.Kind.array
    )

    """
    The object that contains the name of your S3 bucket or your raw code.
    """
    source: list[Source] | core.ArrayOut[Source] = core.attr(
        Source, computed=True, kind=core.Kind.array
    )

    """
    Status of the signing job.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    String value that contains the status reason.
    """
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
