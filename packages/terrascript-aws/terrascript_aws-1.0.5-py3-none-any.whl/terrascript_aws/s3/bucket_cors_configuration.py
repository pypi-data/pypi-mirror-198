import terrascript.core as core


@core.schema
class CorsRule(core.Schema):

    allowed_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    allowed_origins: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None)

    max_age_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allowed_methods: list[str] | core.ArrayOut[core.StringOut],
        allowed_origins: list[str] | core.ArrayOut[core.StringOut],
        allowed_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        id: str | core.StringOut | None = None,
        max_age_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CorsRule.Args(
                allowed_methods=allowed_methods,
                allowed_origins=allowed_origins,
                allowed_headers=allowed_headers,
                expose_headers=expose_headers,
                id=id,
                max_age_seconds=max_age_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        allowed_origins: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        max_age_seconds: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_s3_bucket_cors_configuration", namespace="s3")
class BucketCorsConfiguration(core.Resource):
    """
    (Required, Forces new resource) The name of the bucket.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Required) Set of origins and methods (cross-origin access that you want to allow) [documented below
    ](#cors_rule). You can configure up to 100 rules.
    """
    cors_rule: list[CorsRule] | core.ArrayOut[CorsRule] = core.attr(CorsRule, kind=core.Kind.array)

    """
    (Optional, Forces new resource) The account ID of the expected bucket owner.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Unique identifier for the rule. The value cannot be longer than 255 characters.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        cors_rule: list[CorsRule] | core.ArrayOut[CorsRule],
        expected_bucket_owner: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketCorsConfiguration.Args(
                bucket=bucket,
                cors_rule=cors_rule,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        cors_rule: list[CorsRule] | core.ArrayOut[CorsRule] = core.arg()

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)
