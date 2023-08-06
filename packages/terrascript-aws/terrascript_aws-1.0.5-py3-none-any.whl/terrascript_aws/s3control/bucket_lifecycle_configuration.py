import terrascript.core as core


@core.schema
class AbortIncompleteMultipartUpload(core.Schema):

    days_after_initiation: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        days_after_initiation: int | core.IntOut,
    ):
        super().__init__(
            args=AbortIncompleteMultipartUpload.Args(
                days_after_initiation=days_after_initiation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days_after_initiation: int | core.IntOut = core.arg()


@core.schema
class Expiration(core.Schema):

    date: str | core.StringOut | None = core.attr(str, default=None)

    days: int | core.IntOut | None = core.attr(int, default=None)

    expired_object_delete_marker: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        date: str | core.StringOut | None = None,
        days: int | core.IntOut | None = None,
        expired_object_delete_marker: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Expiration.Args(
                date=date,
                days=days,
                expired_object_delete_marker=expired_object_delete_marker,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date: str | core.StringOut | None = core.arg(default=None)

        days: int | core.IntOut | None = core.arg(default=None)

        expired_object_delete_marker: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = core.attr(
        AbortIncompleteMultipartUpload, default=None
    )

    expiration: Expiration | None = core.attr(Expiration, default=None)

    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut = core.attr(str)

    status: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = None,
        expiration: Expiration | None = None,
        filter: Filter | None = None,
        status: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                id=id,
                abort_incomplete_multipart_upload=abort_incomplete_multipart_upload,
                expiration=expiration,
                filter=filter,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = core.arg(
            default=None
        )

        expiration: Expiration | None = core.arg(default=None)

        filter: Filter | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_s3control_bucket_lifecycle_configuration", namespace="s3control")
class BucketLifecycleConfiguration(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the bucket.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Required) Unique identifier for the rule.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block(s) containing lifecycle rules for the bucket.
    """
    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        rule: list[Rule] | core.ArrayOut[Rule],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketLifecycleConfiguration.Args(
                bucket=bucket,
                rule=rule,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        rule: list[Rule] | core.ArrayOut[Rule] = core.arg()
