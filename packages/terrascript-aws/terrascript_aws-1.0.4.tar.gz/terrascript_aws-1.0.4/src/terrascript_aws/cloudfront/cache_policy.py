import terrascript.core as core


@core.schema
class Headers(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Headers.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class HeadersConfig(core.Schema):

    header_behavior: str | core.StringOut | None = core.attr(str, default=None)

    headers: Headers | None = core.attr(Headers, default=None)

    def __init__(
        self,
        *,
        header_behavior: str | core.StringOut | None = None,
        headers: Headers | None = None,
    ):
        super().__init__(
            args=HeadersConfig.Args(
                header_behavior=header_behavior,
                headers=headers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_behavior: str | core.StringOut | None = core.arg(default=None)

        headers: Headers | None = core.arg(default=None)


@core.schema
class QueryStrings(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=QueryStrings.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class QueryStringsConfig(core.Schema):

    query_string_behavior: str | core.StringOut = core.attr(str)

    query_strings: QueryStrings | None = core.attr(QueryStrings, default=None)

    def __init__(
        self,
        *,
        query_string_behavior: str | core.StringOut,
        query_strings: QueryStrings | None = None,
    ):
        super().__init__(
            args=QueryStringsConfig.Args(
                query_string_behavior=query_string_behavior,
                query_strings=query_strings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        query_string_behavior: str | core.StringOut = core.arg()

        query_strings: QueryStrings | None = core.arg(default=None)


@core.schema
class Cookies(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Cookies.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class CookiesConfig(core.Schema):

    cookie_behavior: str | core.StringOut = core.attr(str)

    cookies: Cookies | None = core.attr(Cookies, default=None)

    def __init__(
        self,
        *,
        cookie_behavior: str | core.StringOut,
        cookies: Cookies | None = None,
    ):
        super().__init__(
            args=CookiesConfig.Args(
                cookie_behavior=cookie_behavior,
                cookies=cookies,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookie_behavior: str | core.StringOut = core.arg()

        cookies: Cookies | None = core.arg(default=None)


@core.schema
class ParametersInCacheKeyAndForwardedToOrigin(core.Schema):

    cookies_config: CookiesConfig = core.attr(CookiesConfig)

    enable_accept_encoding_brotli: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_accept_encoding_gzip: bool | core.BoolOut | None = core.attr(bool, default=None)

    headers_config: HeadersConfig = core.attr(HeadersConfig)

    query_strings_config: QueryStringsConfig = core.attr(QueryStringsConfig)

    def __init__(
        self,
        *,
        cookies_config: CookiesConfig,
        headers_config: HeadersConfig,
        query_strings_config: QueryStringsConfig,
        enable_accept_encoding_brotli: bool | core.BoolOut | None = None,
        enable_accept_encoding_gzip: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ParametersInCacheKeyAndForwardedToOrigin.Args(
                cookies_config=cookies_config,
                headers_config=headers_config,
                query_strings_config=query_strings_config,
                enable_accept_encoding_brotli=enable_accept_encoding_brotli,
                enable_accept_encoding_gzip=enable_accept_encoding_gzip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies_config: CookiesConfig = core.arg()

        enable_accept_encoding_brotli: bool | core.BoolOut | None = core.arg(default=None)

        enable_accept_encoding_gzip: bool | core.BoolOut | None = core.arg(default=None)

        headers_config: HeadersConfig = core.arg()

        query_strings_config: QueryStringsConfig = core.arg()


@core.resource(type="aws_cloudfront_cache_policy", namespace="cloudfront")
class CachePolicy(core.Resource):
    """
    (Optional) A comment to describe the cache policy.
    """

    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The default amount of time, in seconds, that you want objects to stay in the CloudFront c
    ache before CloudFront sends another request to the origin to see if the object has been updated.
    """
    default_ttl: int | core.IntOut | None = core.attr(int, default=None)

    """
    The current version of the cache policy.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier for the cache policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The maximum amount of time, in seconds, that objects stay in the CloudFront cache before
    CloudFront sends another request to the origin to see if the object has been updated.
    """
    max_ttl: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The minimum amount of time, in seconds, that you want objects to stay in the CloudFront c
    ache before CloudFront sends another request to the origin to see if the object has been updated.
    """
    min_ttl: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) A unique name to identify the cache policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The HTTP headers, cookies, and URL query strings to include in the cache key. See [Parame
    ters In Cache Key And Forwarded To Origin](#parameters-in-cache-key-and-forwarded-to-origin) for mor
    e information.
    """
    parameters_in_cache_key_and_forwarded_to_origin: ParametersInCacheKeyAndForwardedToOrigin = (
        core.attr(ParametersInCacheKeyAndForwardedToOrigin)
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        parameters_in_cache_key_and_forwarded_to_origin: ParametersInCacheKeyAndForwardedToOrigin,
        comment: str | core.StringOut | None = None,
        default_ttl: int | core.IntOut | None = None,
        max_ttl: int | core.IntOut | None = None,
        min_ttl: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CachePolicy.Args(
                name=name,
                parameters_in_cache_key_and_forwarded_to_origin=parameters_in_cache_key_and_forwarded_to_origin,
                comment=comment,
                default_ttl=default_ttl,
                max_ttl=max_ttl,
                min_ttl=min_ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        default_ttl: int | core.IntOut | None = core.arg(default=None)

        max_ttl: int | core.IntOut | None = core.arg(default=None)

        min_ttl: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameters_in_cache_key_and_forwarded_to_origin: ParametersInCacheKeyAndForwardedToOrigin = (
            core.arg()
        )
