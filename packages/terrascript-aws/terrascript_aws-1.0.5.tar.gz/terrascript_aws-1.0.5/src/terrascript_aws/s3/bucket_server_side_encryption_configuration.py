import terrascript.core as core


@core.schema
class ApplyServerSideEncryptionByDefault(core.Schema):

    kms_master_key_id: str | core.StringOut | None = core.attr(str, default=None)

    sse_algorithm: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        sse_algorithm: str | core.StringOut,
        kms_master_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ApplyServerSideEncryptionByDefault.Args(
                sse_algorithm=sse_algorithm,
                kms_master_key_id=kms_master_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_master_key_id: str | core.StringOut | None = core.arg(default=None)

        sse_algorithm: str | core.StringOut = core.arg()


@core.schema
class Rule(core.Schema):

    apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault | None = core.attr(
        ApplyServerSideEncryptionByDefault, default=None
    )

    bucket_key_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault | None = None,
        bucket_key_enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                apply_server_side_encryption_by_default=apply_server_side_encryption_by_default,
                bucket_key_enabled=bucket_key_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault | None = (
            core.arg(default=None)
        )

        bucket_key_enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_s3_bucket_server_side_encryption_configuration", namespace="s3")
class BucketServerSideEncryptionConfiguration(core.Resource):
    """
    (Required, Forces new resource) The name of the bucket.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The account ID of the expected bucket owner.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    The `bucket` or `bucket` and `expected_bucket_owner` separated by a comma (`,`) if the latter is pro
    vided.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Set of server-side encryption configuration rules. [documented below](#rule). Currently,
    only a single rule is supported.
    """
    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        rule: list[Rule] | core.ArrayOut[Rule],
        expected_bucket_owner: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketServerSideEncryptionConfiguration.Args(
                bucket=bucket,
                rule=rule,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        rule: list[Rule] | core.ArrayOut[Rule] = core.arg()
