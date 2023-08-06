import terrascript.core as core


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


@core.data(type="aws_cloudfront_origin_request_policy", namespace="aws_cloudfront")
class DsOriginRequestPolicy(core.Data):

    comment: str | core.StringOut = core.attr(str, computed=True)

    cookies_config: list[CookiesConfig] | core.ArrayOut[CookiesConfig] = core.attr(
        CookiesConfig, computed=True, kind=core.Kind.array
    )

    etag: str | core.StringOut = core.attr(str, computed=True)

    headers_config: list[HeadersConfig] | core.ArrayOut[HeadersConfig] = core.attr(
        HeadersConfig, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    query_strings_config: list[QueryStringsConfig] | core.ArrayOut[QueryStringsConfig] = core.attr(
        QueryStringsConfig, computed=True, kind=core.Kind.array
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
            args=DsOriginRequestPolicy.Args(
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
