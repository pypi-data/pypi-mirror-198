import terrascript.core as core


@core.schema
class Tiering(core.Schema):

    access_tier: str | core.StringOut = core.attr(str)

    days: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        access_tier: str | core.StringOut,
        days: int | core.IntOut,
    ):
        super().__init__(
            args=Tiering.Args(
                access_tier=access_tier,
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_tier: str | core.StringOut = core.arg()

        days: int | core.IntOut = core.arg()


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


@core.resource(type="aws_s3_bucket_intelligent_tiering_configuration", namespace="s3")
class BucketIntelligentTieringConfiguration(core.Resource):
    """
    (Required) The name of the bucket this intelligent tiering configuration is associated with.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) A bucket filter. The configuration only includes objects that meet the filter's criteria
    (documented below).
    """
    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The unique name used to identify the S3 Intelligent-Tiering configuration for the bucket.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the status of the configuration. Valid values: `Enabled`, `Disabled`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The S3 Intelligent-Tiering storage class tiers of the configuration (documented below).
    """
    tiering: list[Tiering] | core.ArrayOut[Tiering] = core.attr(Tiering, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        name: str | core.StringOut,
        tiering: list[Tiering] | core.ArrayOut[Tiering],
        filter: Filter | None = None,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketIntelligentTieringConfiguration.Args(
                bucket=bucket,
                name=name,
                tiering=tiering,
                filter=filter,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        filter: Filter | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)

        tiering: list[Tiering] | core.ArrayOut[Tiering] = core.arg()
