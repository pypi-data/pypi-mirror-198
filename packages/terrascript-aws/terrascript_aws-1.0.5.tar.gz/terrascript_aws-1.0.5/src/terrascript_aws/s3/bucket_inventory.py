import terrascript.core as core


@core.schema
class Filter(core.Schema):

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SseKms(core.Schema):

    key_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key_id: str | core.StringOut,
    ):
        super().__init__(
            args=SseKms.Args(
                key_id=key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_id: str | core.StringOut = core.arg()


@core.schema
class SseS3(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class Encryption(core.Schema):

    sse_kms: SseKms | None = core.attr(SseKms, default=None)

    sse_s3: SseS3 | None = core.attr(SseS3, default=None)

    def __init__(
        self,
        *,
        sse_kms: SseKms | None = None,
        sse_s3: SseS3 | None = None,
    ):
        super().__init__(
            args=Encryption.Args(
                sse_kms=sse_kms,
                sse_s3=sse_s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sse_kms: SseKms | None = core.arg(default=None)

        sse_s3: SseS3 | None = core.arg(default=None)


@core.schema
class Bucket(core.Schema):

    account_id: str | core.StringOut | None = core.attr(str, default=None)

    bucket_arn: str | core.StringOut = core.attr(str)

    encryption: Encryption | None = core.attr(Encryption, default=None)

    format: str | core.StringOut = core.attr(str)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: str | core.StringOut,
        format: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        encryption: Encryption | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Bucket.Args(
                bucket_arn=bucket_arn,
                format=format,
                account_id=account_id,
                encryption=encryption,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut | None = core.arg(default=None)

        bucket_arn: str | core.StringOut = core.arg()

        encryption: Encryption | None = core.arg(default=None)

        format: str | core.StringOut = core.arg()

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    bucket: Bucket = core.attr(Bucket)

    def __init__(
        self,
        *,
        bucket: Bucket,
    ):
        super().__init__(
            args=Destination.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Bucket = core.arg()


@core.schema
class Schedule(core.Schema):

    frequency: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        frequency: str | core.StringOut,
    ):
        super().__init__(
            args=Schedule.Args(
                frequency=frequency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        frequency: str | core.StringOut = core.arg()


@core.resource(type="aws_s3_bucket_inventory", namespace="s3")
class BucketInventory(core.Resource):
    """
    (Required) The name of the source bucket that inventory lists the objects for.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Required) Contains information about where to publish the inventory results (documented below).
    """
    destination: Destination = core.attr(Destination)

    """
    (Optional, Default: `true`) Specifies whether the inventory is enabled or disabled.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies an inventory filter. The inventory only includes objects that meet the filter's
    criteria (documented below).
    """
    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Object versions to include in the inventory list. Valid values: `All`, `Current`.
    """
    included_object_versions: str | core.StringOut = core.attr(str)

    """
    (Required) Unique identifier of the inventory configuration for the bucket.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) List of optional fields that are included in the inventory results. Please refer to the S
    3 [documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryConfiguration.html#Am
    azonS3-Type-InventoryConfiguration-OptionalFields) for more details.
    """
    optional_fields: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) Specifies the schedule for generating inventory results (documented below).
    """
    schedule: Schedule = core.attr(Schedule)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        destination: Destination,
        included_object_versions: str | core.StringOut,
        name: str | core.StringOut,
        schedule: Schedule,
        enabled: bool | core.BoolOut | None = None,
        filter: Filter | None = None,
        optional_fields: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketInventory.Args(
                bucket=bucket,
                destination=destination,
                included_object_versions=included_object_versions,
                name=name,
                schedule=schedule,
                enabled=enabled,
                filter=filter,
                optional_fields=optional_fields,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        destination: Destination = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        filter: Filter | None = core.arg(default=None)

        included_object_versions: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        optional_fields: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        schedule: Schedule = core.arg()
