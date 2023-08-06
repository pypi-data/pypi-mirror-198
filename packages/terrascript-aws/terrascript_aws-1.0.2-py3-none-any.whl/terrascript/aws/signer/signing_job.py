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
class DestinationS3(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DestinationS3.Args(
                bucket=bucket,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    s3: DestinationS3 = core.attr(DestinationS3)

    def __init__(
        self,
        *,
        s3: DestinationS3,
    ):
        super().__init__(
            args=Destination.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: DestinationS3 = core.arg()


@core.schema
class SourceS3(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    version: str | core.StringOut = core.attr(str)

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

    s3: SourceS3 = core.attr(SourceS3)

    def __init__(
        self,
        *,
        s3: SourceS3,
    ):
        super().__init__(
            args=Source.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: SourceS3 = core.arg()


@core.resource(type="aws_signer_signing_job", namespace="aws_signer")
class SigningJob(core.Resource):

    completed_at: str | core.StringOut = core.attr(str, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    destination: Destination = core.attr(Destination)

    id: str | core.StringOut = core.attr(str, computed=True)

    ignore_signing_job_failure: bool | core.BoolOut | None = core.attr(bool, default=None)

    job_id: str | core.StringOut = core.attr(str, computed=True)

    job_invoker: str | core.StringOut = core.attr(str, computed=True)

    job_owner: str | core.StringOut = core.attr(str, computed=True)

    platform_display_name: str | core.StringOut = core.attr(str, computed=True)

    platform_id: str | core.StringOut = core.attr(str, computed=True)

    profile_name: str | core.StringOut = core.attr(str)

    profile_version: str | core.StringOut = core.attr(str, computed=True)

    requested_by: str | core.StringOut = core.attr(str, computed=True)

    revocation_record: list[RevocationRecord] | core.ArrayOut[RevocationRecord] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    signature_expires_at: str | core.StringOut = core.attr(str, computed=True)

    signed_object: list[SignedObject] | core.ArrayOut[SignedObject] = core.attr(
        SignedObject, computed=True, kind=core.Kind.array
    )

    source: Source = core.attr(Source)

    status: str | core.StringOut = core.attr(str, computed=True)

    status_reason: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination: Destination,
        profile_name: str | core.StringOut,
        source: Source,
        ignore_signing_job_failure: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningJob.Args(
                destination=destination,
                profile_name=profile_name,
                source=source,
                ignore_signing_job_failure=ignore_signing_job_failure,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination: Destination = core.arg()

        ignore_signing_job_failure: bool | core.BoolOut | None = core.arg(default=None)

        profile_name: str | core.StringOut = core.arg()

        source: Source = core.arg()
