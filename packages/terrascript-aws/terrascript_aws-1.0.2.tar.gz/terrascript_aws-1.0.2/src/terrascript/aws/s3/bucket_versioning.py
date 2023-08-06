import terrascript.core as core


@core.schema
class VersioningConfiguration(core.Schema):

    mfa_delete: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
        mfa_delete: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=VersioningConfiguration.Args(
                status=status,
                mfa_delete=mfa_delete,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mfa_delete: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut = core.arg()


@core.resource(type="aws_s3_bucket_versioning", namespace="aws_s3")
class BucketVersioning(core.Resource):

    bucket: str | core.StringOut = core.attr(str)

    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    mfa: str | core.StringOut | None = core.attr(str, default=None)

    versioning_configuration: VersioningConfiguration = core.attr(VersioningConfiguration)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        versioning_configuration: VersioningConfiguration,
        expected_bucket_owner: str | core.StringOut | None = None,
        mfa: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketVersioning.Args(
                bucket=bucket,
                versioning_configuration=versioning_configuration,
                expected_bucket_owner=expected_bucket_owner,
                mfa=mfa,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        mfa: str | core.StringOut | None = core.arg(default=None)

        versioning_configuration: VersioningConfiguration = core.arg()
