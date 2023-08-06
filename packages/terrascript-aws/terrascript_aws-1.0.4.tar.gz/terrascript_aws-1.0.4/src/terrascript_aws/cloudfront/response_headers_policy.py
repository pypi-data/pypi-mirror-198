import terrascript.core as core


@core.schema
class AccessControlAllowHeaders(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AccessControlAllowHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AccessControlAllowMethods(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AccessControlAllowMethods.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AccessControlAllowOrigins(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AccessControlAllowOrigins.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AccessControlExposeHeaders(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AccessControlExposeHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class CorsConfig(core.Schema):

    access_control_allow_credentials: bool | core.BoolOut = core.attr(bool)

    access_control_allow_headers: AccessControlAllowHeaders = core.attr(AccessControlAllowHeaders)

    access_control_allow_methods: AccessControlAllowMethods = core.attr(AccessControlAllowMethods)

    access_control_allow_origins: AccessControlAllowOrigins = core.attr(AccessControlAllowOrigins)

    access_control_expose_headers: AccessControlExposeHeaders | None = core.attr(
        AccessControlExposeHeaders, default=None
    )

    access_control_max_age_sec: int | core.IntOut | None = core.attr(int, default=None)

    origin_override: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        access_control_allow_credentials: bool | core.BoolOut,
        access_control_allow_headers: AccessControlAllowHeaders,
        access_control_allow_methods: AccessControlAllowMethods,
        access_control_allow_origins: AccessControlAllowOrigins,
        origin_override: bool | core.BoolOut,
        access_control_expose_headers: AccessControlExposeHeaders | None = None,
        access_control_max_age_sec: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CorsConfig.Args(
                access_control_allow_credentials=access_control_allow_credentials,
                access_control_allow_headers=access_control_allow_headers,
                access_control_allow_methods=access_control_allow_methods,
                access_control_allow_origins=access_control_allow_origins,
                origin_override=origin_override,
                access_control_expose_headers=access_control_expose_headers,
                access_control_max_age_sec=access_control_max_age_sec,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_allow_credentials: bool | core.BoolOut = core.arg()

        access_control_allow_headers: AccessControlAllowHeaders = core.arg()

        access_control_allow_methods: AccessControlAllowMethods = core.arg()

        access_control_allow_origins: AccessControlAllowOrigins = core.arg()

        access_control_expose_headers: AccessControlExposeHeaders | None = core.arg(default=None)

        access_control_max_age_sec: int | core.IntOut | None = core.arg(default=None)

        origin_override: bool | core.BoolOut = core.arg()


@core.schema
class Items(core.Schema):

    header: str | core.StringOut = core.attr(str)

    override: bool | core.BoolOut = core.attr(bool)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        header: str | core.StringOut,
        override: bool | core.BoolOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Items.Args(
                header=header,
                override=override,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header: str | core.StringOut = core.arg()

        override: bool | core.BoolOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class CustomHeadersConfig(core.Schema):

    items: list[Items] | core.ArrayOut[Items] | None = core.attr(
        Items, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[Items] | core.ArrayOut[Items] | None = None,
    ):
        super().__init__(
            args=CustomHeadersConfig.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[Items] | core.ArrayOut[Items] | None = core.arg(default=None)


@core.schema
class FrameOptions(core.Schema):

    frame_option: str | core.StringOut = core.attr(str)

    override: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        frame_option: str | core.StringOut,
        override: bool | core.BoolOut,
    ):
        super().__init__(
            args=FrameOptions.Args(
                frame_option=frame_option,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        frame_option: str | core.StringOut = core.arg()

        override: bool | core.BoolOut = core.arg()


@core.schema
class ReferrerPolicy(core.Schema):

    override: bool | core.BoolOut = core.attr(bool)

    referrer_policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        override: bool | core.BoolOut,
        referrer_policy: str | core.StringOut,
    ):
        super().__init__(
            args=ReferrerPolicy.Args(
                override=override,
                referrer_policy=referrer_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        override: bool | core.BoolOut = core.arg()

        referrer_policy: str | core.StringOut = core.arg()


@core.schema
class StrictTransportSecurity(core.Schema):

    access_control_max_age_sec: int | core.IntOut = core.attr(int)

    include_subdomains: bool | core.BoolOut | None = core.attr(bool, default=None)

    override: bool | core.BoolOut = core.attr(bool)

    preload: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        access_control_max_age_sec: int | core.IntOut,
        override: bool | core.BoolOut,
        include_subdomains: bool | core.BoolOut | None = None,
        preload: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=StrictTransportSecurity.Args(
                access_control_max_age_sec=access_control_max_age_sec,
                override=override,
                include_subdomains=include_subdomains,
                preload=preload,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_max_age_sec: int | core.IntOut = core.arg()

        include_subdomains: bool | core.BoolOut | None = core.arg(default=None)

        override: bool | core.BoolOut = core.arg()

        preload: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class XssProtection(core.Schema):

    mode_block: bool | core.BoolOut | None = core.attr(bool, default=None)

    override: bool | core.BoolOut = core.attr(bool)

    protection: bool | core.BoolOut = core.attr(bool)

    report_uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        override: bool | core.BoolOut,
        protection: bool | core.BoolOut,
        mode_block: bool | core.BoolOut | None = None,
        report_uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=XssProtection.Args(
                override=override,
                protection=protection,
                mode_block=mode_block,
                report_uri=report_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode_block: bool | core.BoolOut | None = core.arg(default=None)

        override: bool | core.BoolOut = core.arg()

        protection: bool | core.BoolOut = core.arg()

        report_uri: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ContentSecurityPolicy(core.Schema):

    content_security_policy: str | core.StringOut = core.attr(str)

    override: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        content_security_policy: str | core.StringOut,
        override: bool | core.BoolOut,
    ):
        super().__init__(
            args=ContentSecurityPolicy.Args(
                content_security_policy=content_security_policy,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_security_policy: str | core.StringOut = core.arg()

        override: bool | core.BoolOut = core.arg()


@core.schema
class ContentTypeOptions(core.Schema):

    override: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        override: bool | core.BoolOut,
    ):
        super().__init__(
            args=ContentTypeOptions.Args(
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        override: bool | core.BoolOut = core.arg()


@core.schema
class SecurityHeadersConfig(core.Schema):

    content_security_policy: ContentSecurityPolicy | None = core.attr(
        ContentSecurityPolicy, default=None
    )

    content_type_options: ContentTypeOptions | None = core.attr(ContentTypeOptions, default=None)

    frame_options: FrameOptions | None = core.attr(FrameOptions, default=None)

    referrer_policy: ReferrerPolicy | None = core.attr(ReferrerPolicy, default=None)

    strict_transport_security: StrictTransportSecurity | None = core.attr(
        StrictTransportSecurity, default=None
    )

    xss_protection: XssProtection | None = core.attr(XssProtection, default=None)

    def __init__(
        self,
        *,
        content_security_policy: ContentSecurityPolicy | None = None,
        content_type_options: ContentTypeOptions | None = None,
        frame_options: FrameOptions | None = None,
        referrer_policy: ReferrerPolicy | None = None,
        strict_transport_security: StrictTransportSecurity | None = None,
        xss_protection: XssProtection | None = None,
    ):
        super().__init__(
            args=SecurityHeadersConfig.Args(
                content_security_policy=content_security_policy,
                content_type_options=content_type_options,
                frame_options=frame_options,
                referrer_policy=referrer_policy,
                strict_transport_security=strict_transport_security,
                xss_protection=xss_protection,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_security_policy: ContentSecurityPolicy | None = core.arg(default=None)

        content_type_options: ContentTypeOptions | None = core.arg(default=None)

        frame_options: FrameOptions | None = core.arg(default=None)

        referrer_policy: ReferrerPolicy | None = core.arg(default=None)

        strict_transport_security: StrictTransportSecurity | None = core.arg(default=None)

        xss_protection: XssProtection | None = core.arg(default=None)


@core.schema
class ServerTimingHeadersConfig(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    sampling_rate: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        sampling_rate: float | core.FloatOut,
    ):
        super().__init__(
            args=ServerTimingHeadersConfig.Args(
                enabled=enabled,
                sampling_rate=sampling_rate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        sampling_rate: float | core.FloatOut = core.arg()


@core.resource(type="aws_cloudfront_response_headers_policy", namespace="cloudfront")
class ResponseHeadersPolicy(core.Resource):
    """
    (Optional) A comment to describe the response headers policy. The comment cannot be longer than 128
    characters.
    """

    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A configuration for a set of HTTP response headers that are used for Cross-Origin Resourc
    e Sharing (CORS). See [Cors Config](#cors-config) for more information.
    """
    cors_config: CorsConfig | None = core.attr(CorsConfig, default=None)

    """
    (Optional) Object that contains an attribute `items` that contains a list of custom headers. See [Cu
    stom Header](#custom-header) for more information.
    """
    custom_headers_config: CustomHeadersConfig | None = core.attr(CustomHeadersConfig, default=None)

    """
    The current version of the response headers policy.
    """
    etag: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The identifier for the response headers policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A unique name to identify the response headers policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A configuration for a set of security-related HTTP response headers. See [Security Header
    s Config](#security-headers-config) for more information.
    """
    security_headers_config: SecurityHeadersConfig | None = core.attr(
        SecurityHeadersConfig, default=None
    )

    """
    (Optional) A configuration for enabling the Server-Timing header in HTTP responses sent from CloudFr
    ont. See [Server Timing Headers Config](#server-timing-headers-config) for more information.
    """
    server_timing_headers_config: ServerTimingHeadersConfig | None = core.attr(
        ServerTimingHeadersConfig, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        cors_config: CorsConfig | None = None,
        custom_headers_config: CustomHeadersConfig | None = None,
        etag: str | core.StringOut | None = None,
        security_headers_config: SecurityHeadersConfig | None = None,
        server_timing_headers_config: ServerTimingHeadersConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResponseHeadersPolicy.Args(
                name=name,
                comment=comment,
                cors_config=cors_config,
                custom_headers_config=custom_headers_config,
                etag=etag,
                security_headers_config=security_headers_config,
                server_timing_headers_config=server_timing_headers_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        cors_config: CorsConfig | None = core.arg(default=None)

        custom_headers_config: CustomHeadersConfig | None = core.arg(default=None)

        etag: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        security_headers_config: SecurityHeadersConfig | None = core.arg(default=None)

        server_timing_headers_config: ServerTimingHeadersConfig | None = core.arg(default=None)
