import terrascript.core as core


@core.resource(type="aws_appsync_api_cache", namespace="appsync")
class ApiCache(core.Resource):
    """
    (Required) Caching behavior. Valid values are `FULL_REQUEST_CACHING` and `PER_RESOLVER_CACHING`.
    """

    api_caching_behavior: str | core.StringOut = core.attr(str)

    """
    (Required) The GraphQL API ID.
    """
    api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) At-rest encryption flag for cache. You cannot update this setting after creation.
    """
    at_rest_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The AppSync API ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Transit encryption flag when connecting to cache. You cannot update this setting after cr
    eation.
    """
    transit_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) TTL in seconds for cache entries.
    """
    ttl: int | core.IntOut = core.attr(int)

    """
    (Required) The cache instance type. Valid values are `SMALL`, `MEDIUM`, `LARGE`, `XLARGE`, `LARGE_2X
    , `LARGE_4X`, `LARGE_8X`, `LARGE_12X`, `T2_SMALL`, `T2_MEDIUM`, `R4_LARGE`, `R4_XLARGE`, `R4_2XLARG
    E`, `R4_4XLARGE`, `R4_8XLARGE`.
    """
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
