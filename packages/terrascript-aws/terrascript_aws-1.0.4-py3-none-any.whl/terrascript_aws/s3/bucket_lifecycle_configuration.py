import terrascript.core as core


@core.schema
class NoncurrentVersionTransition(core.Schema):

    newer_noncurrent_versions: str | core.StringOut | None = core.attr(str, default=None)

    noncurrent_days: int | core.IntOut | None = core.attr(int, default=None)

    storage_class: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        storage_class: str | core.StringOut,
        newer_noncurrent_versions: str | core.StringOut | None = None,
        noncurrent_days: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NoncurrentVersionTransition.Args(
                storage_class=storage_class,
                newer_noncurrent_versions=newer_noncurrent_versions,
                noncurrent_days=noncurrent_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        newer_noncurrent_versions: str | core.StringOut | None = core.arg(default=None)

        noncurrent_days: int | core.IntOut | None = core.arg(default=None)

        storage_class: str | core.StringOut = core.arg()


@core.schema
class Tag(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Tag.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class And(core.Schema):

    object_size_greater_than: int | core.IntOut | None = core.attr(int, default=None)

    object_size_less_than: int | core.IntOut | None = core.attr(int, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        object_size_greater_than: int | core.IntOut | None = None,
        object_size_less_than: int | core.IntOut | None = None,
        prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=And.Args(
                object_size_greater_than=object_size_greater_than,
                object_size_less_than=object_size_less_than,
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object_size_greater_than: int | core.IntOut | None = core.arg(default=None)

        object_size_less_than: int | core.IntOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    and_: And | None = core.attr(And, default=None, alias="and")

    object_size_greater_than: str | core.StringOut | None = core.attr(str, default=None)

    object_size_less_than: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    tag: Tag | None = core.attr(Tag, default=None)

    def __init__(
        self,
        *,
        and_: And | None = None,
        object_size_greater_than: str | core.StringOut | None = None,
        object_size_less_than: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        tag: Tag | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                and_=and_,
                object_size_greater_than=object_size_greater_than,
                object_size_less_than=object_size_less_than,
                prefix=prefix,
                tag=tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: And | None = core.arg(default=None)

        object_size_greater_than: str | core.StringOut | None = core.arg(default=None)

        object_size_less_than: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        tag: Tag | None = core.arg(default=None)


@core.schema
class NoncurrentVersionExpiration(core.Schema):

    newer_noncurrent_versions: str | core.StringOut | None = core.attr(str, default=None)

    noncurrent_days: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        newer_noncurrent_versions: str | core.StringOut | None = None,
        noncurrent_days: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NoncurrentVersionExpiration.Args(
                newer_noncurrent_versions=newer_noncurrent_versions,
                noncurrent_days=noncurrent_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        newer_noncurrent_versions: str | core.StringOut | None = core.arg(default=None)

        noncurrent_days: int | core.IntOut | None = core.arg(default=None)


@core.schema
class AbortIncompleteMultipartUpload(core.Schema):

    days_after_initiation: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        days_after_initiation: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AbortIncompleteMultipartUpload.Args(
                days_after_initiation=days_after_initiation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days_after_initiation: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Expiration(core.Schema):

    date: str | core.StringOut | None = core.attr(str, default=None)

    days: int | core.IntOut | None = core.attr(int, default=None)

    expired_object_delete_marker: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

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
class Transition(core.Schema):

    date: str | core.StringOut | None = core.attr(str, default=None)

    days: int | core.IntOut | None = core.attr(int, default=None)

    storage_class: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        storage_class: str | core.StringOut,
        date: str | core.StringOut | None = None,
        days: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Transition.Args(
                storage_class=storage_class,
                date=date,
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date: str | core.StringOut | None = core.arg(default=None)

        days: int | core.IntOut | None = core.arg(default=None)

        storage_class: str | core.StringOut = core.arg()


@core.schema
class Rule(core.Schema):

    abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = core.attr(
        AbortIncompleteMultipartUpload, default=None
    )

    expiration: Expiration | None = core.attr(Expiration, default=None)

    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut = core.attr(str)

    noncurrent_version_expiration: NoncurrentVersionExpiration | None = core.attr(
        NoncurrentVersionExpiration, default=None
    )

    noncurrent_version_transition: list[NoncurrentVersionTransition] | core.ArrayOut[
        NoncurrentVersionTransition
    ] | None = core.attr(NoncurrentVersionTransition, default=None, kind=core.Kind.array)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str)

    transition: list[Transition] | core.ArrayOut[Transition] | None = core.attr(
        Transition, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        status: str | core.StringOut,
        abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = None,
        expiration: Expiration | None = None,
        filter: Filter | None = None,
        noncurrent_version_expiration: NoncurrentVersionExpiration | None = None,
        noncurrent_version_transition: list[NoncurrentVersionTransition]
        | core.ArrayOut[NoncurrentVersionTransition]
        | None = None,
        prefix: str | core.StringOut | None = None,
        transition: list[Transition] | core.ArrayOut[Transition] | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                id=id,
                status=status,
                abort_incomplete_multipart_upload=abort_incomplete_multipart_upload,
                expiration=expiration,
                filter=filter,
                noncurrent_version_expiration=noncurrent_version_expiration,
                noncurrent_version_transition=noncurrent_version_transition,
                prefix=prefix,
                transition=transition,
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

        noncurrent_version_expiration: NoncurrentVersionExpiration | None = core.arg(default=None)

        noncurrent_version_transition: list[NoncurrentVersionTransition] | core.ArrayOut[
            NoncurrentVersionTransition
        ] | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut = core.arg()

        transition: list[Transition] | core.ArrayOut[Transition] | None = core.arg(default=None)


@core.resource(type="aws_s3_bucket_lifecycle_configuration", namespace="s3")
class BucketLifecycleConfiguration(core.Resource):
    """
    (Required) The name of the source S3 bucket you want Amazon S3 to monitor.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) The account ID of the expected bucket owner. If the bucket is owned by a different accoun
    t, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Unique identifier for the rule. The value cannot be longer than 255 characters.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) List of configuration blocks describing the rules managing the replication [documented be
    low](#rule).
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
            args=BucketLifecycleConfiguration.Args(
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
