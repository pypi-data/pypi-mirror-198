import terrascript.core as core


@core.schema
class ContentTypeOptions(core.Schema):

    override: bool | core.BoolOut = core.attr(bool, computed=True)

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
class FrameOptions(core.Schema):

    frame_option: str | core.StringOut = core.attr(str, computed=True)

    override: bool | core.BoolOut = core.attr(bool, computed=True)

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

    override: bool | core.BoolOut = core.attr(bool, computed=True)

    referrer_policy: str | core.StringOut = core.attr(str, computed=True)

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

    access_control_max_age_sec: int | core.IntOut = core.attr(int, computed=True)

    include_subdomains: bool | core.BoolOut = core.attr(bool, computed=True)

    override: bool | core.BoolOut = core.attr(bool, computed=True)

    preload: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        access_control_max_age_sec: int | core.IntOut,
        include_subdomains: bool | core.BoolOut,
        override: bool | core.BoolOut,
        preload: bool | core.BoolOut,
    ):
        super().__init__(
            args=StrictTransportSecurity.Args(
                access_control_max_age_sec=access_control_max_age_sec,
                include_subdomains=include_subdomains,
                override=override,
                preload=preload,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_max_age_sec: int | core.IntOut = core.arg()

        include_subdomains: bool | core.BoolOut = core.arg()

        override: bool | core.BoolOut = core.arg()

        preload: bool | core.BoolOut = core.arg()


@core.schema
class XssProtection(core.Schema):

    mode_block: bool | core.BoolOut = core.attr(bool, computed=True)

    override: bool | core.BoolOut = core.attr(bool, computed=True)

    protection: bool | core.BoolOut = core.attr(bool, computed=True)

    report_uri: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        mode_block: bool | core.BoolOut,
        override: bool | core.BoolOut,
        protection: bool | core.BoolOut,
        report_uri: str | core.StringOut,
    ):
        super().__init__(
            args=XssProtection.Args(
                mode_block=mode_block,
                override=override,
                protection=protection,
                report_uri=report_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode_block: bool | core.BoolOut = core.arg()

        override: bool | core.BoolOut = core.arg()

        protection: bool | core.BoolOut = core.arg()

        report_uri: str | core.StringOut = core.arg()


@core.schema
class ContentSecurityPolicy(core.Schema):

    content_security_policy: str | core.StringOut = core.attr(str, computed=True)

    override: bool | core.BoolOut = core.attr(bool, computed=True)

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
class SecurityHeadersConfig(core.Schema):

    content_security_policy: list[ContentSecurityPolicy] | core.ArrayOut[
        ContentSecurityPolicy
    ] = core.attr(ContentSecurityPolicy, computed=True, kind=core.Kind.array)

    content_type_options: list[ContentTypeOptions] | core.ArrayOut[ContentTypeOptions] = core.attr(
        ContentTypeOptions, computed=True, kind=core.Kind.array
    )

    frame_options: list[FrameOptions] | core.ArrayOut[FrameOptions] = core.attr(
        FrameOptions, computed=True, kind=core.Kind.array
    )

    referrer_policy: list[ReferrerPolicy] | core.ArrayOut[ReferrerPolicy] = core.attr(
        ReferrerPolicy, computed=True, kind=core.Kind.array
    )

    strict_transport_security: list[StrictTransportSecurity] | core.ArrayOut[
        StrictTransportSecurity
    ] = core.attr(StrictTransportSecurity, computed=True, kind=core.Kind.array)

    xss_protection: list[XssProtection] | core.ArrayOut[XssProtection] = core.attr(
        XssProtection, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        content_security_policy: list[ContentSecurityPolicy] | core.ArrayOut[ContentSecurityPolicy],
        content_type_options: list[ContentTypeOptions] | core.ArrayOut[ContentTypeOptions],
        frame_options: list[FrameOptions] | core.ArrayOut[FrameOptions],
        referrer_policy: list[ReferrerPolicy] | core.ArrayOut[ReferrerPolicy],
        strict_transport_security: list[StrictTransportSecurity]
        | core.ArrayOut[StrictTransportSecurity],
        xss_protection: list[XssProtection] | core.ArrayOut[XssProtection],
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
        content_security_policy: list[ContentSecurityPolicy] | core.ArrayOut[
            ContentSecurityPolicy
        ] = core.arg()

        content_type_options: list[ContentTypeOptions] | core.ArrayOut[
            ContentTypeOptions
        ] = core.arg()

        frame_options: list[FrameOptions] | core.ArrayOut[FrameOptions] = core.arg()

        referrer_policy: list[ReferrerPolicy] | core.ArrayOut[ReferrerPolicy] = core.arg()

        strict_transport_security: list[StrictTransportSecurity] | core.ArrayOut[
            StrictTransportSecurity
        ] = core.arg()

        xss_protection: list[XssProtection] | core.ArrayOut[XssProtection] = core.arg()


@core.schema
class ServerTimingHeadersConfig(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    sampling_rate: float | core.FloatOut = core.attr(float, computed=True)

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


@core.schema
class AccessControlAllowHeaders(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=AccessControlAllowHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class AccessControlAllowMethods(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=AccessControlAllowMethods.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class AccessControlAllowOrigins(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=AccessControlAllowOrigins.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class AccessControlExposeHeaders(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=AccessControlExposeHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class CorsConfig(core.Schema):

    access_control_allow_credentials: bool | core.BoolOut = core.attr(bool, computed=True)

    access_control_allow_headers: list[AccessControlAllowHeaders] | core.ArrayOut[
        AccessControlAllowHeaders
    ] = core.attr(AccessControlAllowHeaders, computed=True, kind=core.Kind.array)

    access_control_allow_methods: list[AccessControlAllowMethods] | core.ArrayOut[
        AccessControlAllowMethods
    ] = core.attr(AccessControlAllowMethods, computed=True, kind=core.Kind.array)

    access_control_allow_origins: list[AccessControlAllowOrigins] | core.ArrayOut[
        AccessControlAllowOrigins
    ] = core.attr(AccessControlAllowOrigins, computed=True, kind=core.Kind.array)

    access_control_expose_headers: list[AccessControlExposeHeaders] | core.ArrayOut[
        AccessControlExposeHeaders
    ] = core.attr(AccessControlExposeHeaders, computed=True, kind=core.Kind.array)

    access_control_max_age_sec: int | core.IntOut = core.attr(int, computed=True)

    origin_override: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        access_control_allow_credentials: bool | core.BoolOut,
        access_control_allow_headers: list[AccessControlAllowHeaders]
        | core.ArrayOut[AccessControlAllowHeaders],
        access_control_allow_methods: list[AccessControlAllowMethods]
        | core.ArrayOut[AccessControlAllowMethods],
        access_control_allow_origins: list[AccessControlAllowOrigins]
        | core.ArrayOut[AccessControlAllowOrigins],
        access_control_expose_headers: list[AccessControlExposeHeaders]
        | core.ArrayOut[AccessControlExposeHeaders],
        access_control_max_age_sec: int | core.IntOut,
        origin_override: bool | core.BoolOut,
    ):
        super().__init__(
            args=CorsConfig.Args(
                access_control_allow_credentials=access_control_allow_credentials,
                access_control_allow_headers=access_control_allow_headers,
                access_control_allow_methods=access_control_allow_methods,
                access_control_allow_origins=access_control_allow_origins,
                access_control_expose_headers=access_control_expose_headers,
                access_control_max_age_sec=access_control_max_age_sec,
                origin_override=origin_override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_allow_credentials: bool | core.BoolOut = core.arg()

        access_control_allow_headers: list[AccessControlAllowHeaders] | core.ArrayOut[
            AccessControlAllowHeaders
        ] = core.arg()

        access_control_allow_methods: list[AccessControlAllowMethods] | core.ArrayOut[
            AccessControlAllowMethods
        ] = core.arg()

        access_control_allow_origins: list[AccessControlAllowOrigins] | core.ArrayOut[
            AccessControlAllowOrigins
        ] = core.arg()

        access_control_expose_headers: list[AccessControlExposeHeaders] | core.ArrayOut[
            AccessControlExposeHeaders
        ] = core.arg()

        access_control_max_age_sec: int | core.IntOut = core.arg()

        origin_override: bool | core.BoolOut = core.arg()


@core.schema
class Items(core.Schema):

    header: str | core.StringOut = core.attr(str, computed=True)

    override: bool | core.BoolOut = core.attr(bool, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

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

    items: list[Items] | core.ArrayOut[Items] = core.attr(
        Items, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[Items] | core.ArrayOut[Items],
    ):
        super().__init__(
            args=CustomHeadersConfig.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[Items] | core.ArrayOut[Items] = core.arg()


@core.data(type="aws_cloudfront_response_headers_policy", namespace="cloudfront")
class DsResponseHeadersPolicy(core.Data):
    """
    A comment to describe the response headers policy. The comment cannot be longer than 128 characters.
    """

    comment: str | core.StringOut = core.attr(str, computed=True)

    """
    A configuration for a set of HTTP response headers that are used for Cross-Origin Resource Sharing (
    CORS). See [Cors Config](#cors-config) for more information.
    """
    cors_config: list[CorsConfig] | core.ArrayOut[CorsConfig] = core.attr(
        CorsConfig, computed=True, kind=core.Kind.array
    )

    """
    Object that contains an attribute `items` that contains a list of Custom Headers See [Custom Header]
    (#custom-header) for more information.
    """
    custom_headers_config: list[CustomHeadersConfig] | core.ArrayOut[
        CustomHeadersConfig
    ] = core.attr(CustomHeadersConfig, computed=True, kind=core.Kind.array)

    """
    The current version of the response headers policy.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The identifier for the response headers policy.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A unique name to identify the response headers policy.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A configuration for a set of security-related HTTP response headers. See [Security Headers Config](#
    security-headers-config) for more information.
    """
    security_headers_config: list[SecurityHeadersConfig] | core.ArrayOut[
        SecurityHeadersConfig
    ] = core.attr(SecurityHeadersConfig, computed=True, kind=core.Kind.array)

    """
    (Optional) A configuration for enabling the Server-Timing header in HTTP responses sent from CloudFr
    ont. See [Server Timing Headers Config](#server-timing-headers-config) for more information.
    """
    server_timing_headers_config: list[ServerTimingHeadersConfig] | core.ArrayOut[
        ServerTimingHeadersConfig
    ] = core.attr(ServerTimingHeadersConfig, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsResponseHeadersPolicy.Args(
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
