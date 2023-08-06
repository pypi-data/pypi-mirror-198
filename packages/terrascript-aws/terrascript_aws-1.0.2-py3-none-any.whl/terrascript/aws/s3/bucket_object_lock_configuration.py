import terrascript.core as core


@core.schema
class DefaultRetention(core.Schema):

    days: int | core.IntOut | None = core.attr(int, default=None)

    mode: str | core.StringOut | None = core.attr(str, default=None)

    years: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        days: int | core.IntOut | None = None,
        mode: str | core.StringOut | None = None,
        years: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DefaultRetention.Args(
                days=days,
                mode=mode,
                years=years,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: int | core.IntOut | None = core.arg(default=None)

        mode: str | core.StringOut | None = core.arg(default=None)

        years: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    default_retention: DefaultRetention = core.attr(DefaultRetention)

    def __init__(
        self,
        *,
        default_retention: DefaultRetention,
    ):
        super().__init__(
            args=Rule.Args(
                default_retention=default_retention,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_retention: DefaultRetention = core.arg()


@core.resource(type="aws_s3_bucket_object_lock_configuration", namespace="aws_s3")
class BucketObjectLockConfiguration(core.Resource):

    bucket: str | core.StringOut = core.attr(str)

    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    object_lock_enabled: str | core.StringOut | None = core.attr(str, default=None)

    rule: Rule = core.attr(Rule)

    token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        rule: Rule,
        expected_bucket_owner: str | core.StringOut | None = None,
        object_lock_enabled: str | core.StringOut | None = None,
        token: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketObjectLockConfiguration.Args(
                bucket=bucket,
                rule=rule,
                expected_bucket_owner=expected_bucket_owner,
                object_lock_enabled=object_lock_enabled,
                token=token,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        object_lock_enabled: str | core.StringOut | None = core.arg(default=None)

        rule: Rule = core.arg()

        token: str | core.StringOut | None = core.arg(default=None)
