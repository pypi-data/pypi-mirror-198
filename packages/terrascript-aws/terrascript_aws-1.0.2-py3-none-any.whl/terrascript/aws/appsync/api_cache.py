import terrascript.core as core


@core.resource(type="aws_appsync_api_cache", namespace="aws_appsync")
class ApiCache(core.Resource):

    api_caching_behavior: str | core.StringOut = core.attr(str)

    api_id: str | core.StringOut = core.attr(str)

    at_rest_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    transit_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    ttl: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_caching_behavior: str | core.StringOut,
        api_id: str | core.StringOut,
        ttl: int | core.IntOut,
        type: str | core.StringOut,
        at_rest_encryption_enabled: bool | core.BoolOut | None = None,
        transit_encryption_enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApiCache.Args(
                api_caching_behavior=api_caching_behavior,
                api_id=api_id,
                ttl=ttl,
                type=type,
                at_rest_encryption_enabled=at_rest_encryption_enabled,
                transit_encryption_enabled=transit_encryption_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_caching_behavior: str | core.StringOut = core.arg()

        api_id: str | core.StringOut = core.arg()

        at_rest_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        transit_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        ttl: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()
