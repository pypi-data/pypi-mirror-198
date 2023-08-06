import terrascript.core as core


@core.schema
class Cookies(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Cookies.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class CookiesConfig(core.Schema):

    cookie_behavior: str | core.StringOut = core.attr(str, computed=True)

    cookies: list[Cookies] | core.ArrayOut[Cookies] = core.attr(
        Cookies, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cookie_behavior: str | core.StringOut,
        cookies: list[Cookies] | core.ArrayOut[Cookies],
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

        cookies: list[Cookies] | core.ArrayOut[Cookies] = core.arg()


@core.schema
class Headers(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Headers.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class HeadersConfig(core.Schema):

    header_behavior: str | core.StringOut = core.attr(str, computed=True)

    headers: list[Headers] | core.ArrayOut[Headers] = core.attr(
        Headers, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        header_behavior: str | core.StringOut,
        headers: list[Headers] | core.ArrayOut[Headers],
    ):
        super().__init__(
            args=HeadersConfig.Args(
                header_behavior=header_behavior,
                headers=headers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_behavior: str | core.StringOut = core.arg()

        headers: list[Headers] | core.ArrayOut[Headers] = core.arg()


@core.schema
class QueryStrings(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=QueryStrings.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class QueryStringsConfig(core.Schema):

    query_string_behavior: str | core.StringOut = core.attr(str, computed=True)

    query_strings: list[QueryStrings] | core.ArrayOut[QueryStrings] = core.attr(
        QueryStrings, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        query_string_behavior: str | core.StringOut,
        query_strings: list[QueryStrings] | core.ArrayOut[QueryStrings],
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

        query_strings: list[QueryStrings] | core.ArrayOut[QueryStrings] = core.arg()


@core.schema
class ParametersInCacheKeyAndForwardedToOrigin(core.Schema):

    cookies_config: list[CookiesConfig] | core.ArrayOut[CookiesConfig] = core.attr(
        CookiesConfig, computed=True, kind=core.Kind.array
    )

    enable_accept_encoding_brotli: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_accept_encoding_gzip: bool | core.BoolOut = core.attr(bool, computed=True)

    headers_config: list[HeadersConfig] | core.ArrayOut[HeadersConfig] = core.attr(
        HeadersConfig, computed=True, kind=core.Kind.array
    )

    query_strings_config: list[QueryStringsConfig] | core.ArrayOut[QueryStringsConfig] = core.attr(
        QueryStringsConfig, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cookies_config: list[CookiesConfig] | core.ArrayOut[CookiesConfig],
        enable_accept_encoding_brotli: bool | core.BoolOut,
        enable_accept_encoding_gzip: bool | core.BoolOut,
        headers_config: list[HeadersConfig] | core.ArrayOut[HeadersConfig],
        query_strings_config: list[QueryStringsConfig] | core.ArrayOut[QueryStringsConfig],
    ):
        super().__init__(
            args=ParametersInCacheKeyAndForwardedToOrigin.Args(
                cookies_config=cookies_config,
                enable_accept_encoding_brotli=enable_accept_encoding_brotli,
                enable_accept_encoding_gzip=enable_accept_encoding_gzip,
                headers_config=headers_config,
                query_strings_config=query_strings_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies_config: list[CookiesConfig] | core.ArrayOut[CookiesConfig] = core.arg()

        enable_accept_encoding_brotli: bool | core.BoolOut = core.arg()

        enable_accept_encoding_gzip: bool | core.BoolOut = core.arg()

        headers_config: list[HeadersConfig] | core.ArrayOut[HeadersConfig] = core.arg()

        query_strings_config: list[QueryStringsConfig] | core.ArrayOut[
            QueryStringsConfig
        ] = core.arg()


@core.data(type="aws_cloudfront_cache_policy", namespace="cloudfront")
class DsCachePolicy(core.Data):
    """
    A comment to describe the cache policy.
    """

    comment: str | core.StringOut = core.attr(str, computed=True)

    """
    The default amount of time, in seconds, that you want objects to stay in the CloudFront cache before
    CloudFront sends another request to the origin to see if the object has been updated.
    """
    default_ttl: int | core.IntOut = core.attr(int, computed=True)

    """
    The current version of the cache policy.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The identifier for the cache policy.
    """
    id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The maximum amount of time, in seconds, that objects stay in the CloudFront cache before CloudFront
    sends another request to the origin to see if the object has been updated.
    """
    max_ttl: int | core.IntOut = core.attr(int, computed=True)

    """
    The minimum amount of time, in seconds, that you want objects to stay in the CloudFront cache before
    CloudFront sends another request to the origin to see if the object has been updated.
    """
    min_ttl: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) A unique name to identify the cache policy.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The HTTP headers, cookies, and URL query strings to include in the cache key. See [Parameters In Cac
    he Key And Forwarded To Origin](#parameters-in-cache-key-and-forwarded-to-origin) for more informati
    on.
    """
    parameters_in_cache_key_and_forwarded_to_origin: list[
        ParametersInCacheKeyAndForwardedToOrigin
    ] | core.ArrayOut[ParametersInCacheKeyAndForwardedToOrigin] = core.attr(
        ParametersInCacheKeyAndForwardedToOrigin, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCachePolicy.Args(
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
