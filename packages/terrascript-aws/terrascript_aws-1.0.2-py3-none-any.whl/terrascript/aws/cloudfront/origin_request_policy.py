import terrascript.core as core


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


@core.resource(type="aws_cloudfront_origin_request_policy", namespace="aws_cloudfront")
class OriginRequestPolicy(core.Resource):

    comment: str | core.StringOut | None = core.attr(str, default=None)

    cookies_config: CookiesConfig = core.attr(CookiesConfig)

    etag: str | core.StringOut = core.attr(str, computed=True)

    headers_config: HeadersConfig = core.attr(HeadersConfig)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    query_strings_config: QueryStringsConfig = core.attr(QueryStringsConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        cookies_config: CookiesConfig,
        headers_config: HeadersConfig,
        name: str | core.StringOut,
        query_strings_config: QueryStringsConfig,
        comment: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OriginRequestPolicy.Args(
                cookies_config=cookies_config,
                headers_config=headers_config,
                name=name,
                query_strings_config=query_strings_config,
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        cookies_config: CookiesConfig = core.arg()

        headers_config: HeadersConfig = core.arg()

        name: str | core.StringOut = core.arg()

        query_strings_config: QueryStringsConfig = core.arg()
