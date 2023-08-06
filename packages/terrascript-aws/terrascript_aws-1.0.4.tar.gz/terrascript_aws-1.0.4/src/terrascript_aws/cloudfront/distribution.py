import terrascript.core as core


@core.schema
class GeoRestriction(core.Schema):

    locations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    restriction_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        restriction_type: str | core.StringOut,
        locations: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=GeoRestriction.Args(
                restriction_type=restriction_type,
                locations=locations,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        locations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        restriction_type: str | core.StringOut = core.arg()


@core.schema
class Restrictions(core.Schema):

    geo_restriction: GeoRestriction = core.attr(GeoRestriction)

    def __init__(
        self,
        *,
        geo_restriction: GeoRestriction,
    ):
        super().__init__(
            args=Restrictions.Args(
                geo_restriction=geo_restriction,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        geo_restriction: GeoRestriction = core.arg()


@core.schema
class Member(core.Schema):

    origin_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        origin_id: str | core.StringOut,
    ):
        super().__init__(
            args=Member.Args(
                origin_id=origin_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        origin_id: str | core.StringOut = core.arg()


@core.schema
class FailoverCriteria(core.Schema):

    status_codes: list[int] | core.ArrayOut[core.IntOut] = core.attr(int, kind=core.Kind.array)

    def __init__(
        self,
        *,
        status_codes: list[int] | core.ArrayOut[core.IntOut],
    ):
        super().__init__(
            args=FailoverCriteria.Args(
                status_codes=status_codes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status_codes: list[int] | core.ArrayOut[core.IntOut] = core.arg()


@core.schema
class OriginGroup(core.Schema):

    failover_criteria: FailoverCriteria = core.attr(FailoverCriteria)

    member: list[Member] | core.ArrayOut[Member] = core.attr(Member, kind=core.Kind.array)

    origin_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        failover_criteria: FailoverCriteria,
        member: list[Member] | core.ArrayOut[Member],
        origin_id: str | core.StringOut,
    ):
        super().__init__(
            args=OriginGroup.Args(
                failover_criteria=failover_criteria,
                member=member,
                origin_id=origin_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failover_criteria: FailoverCriteria = core.arg()

        member: list[Member] | core.ArrayOut[Member] = core.arg()

        origin_id: str | core.StringOut = core.arg()


@core.schema
class CustomErrorResponse(core.Schema):

    error_caching_min_ttl: int | core.IntOut | None = core.attr(int, default=None)

    error_code: int | core.IntOut = core.attr(int)

    response_code: int | core.IntOut | None = core.attr(int, default=None)

    response_page_path: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        error_code: int | core.IntOut,
        error_caching_min_ttl: int | core.IntOut | None = None,
        response_code: int | core.IntOut | None = None,
        response_page_path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomErrorResponse.Args(
                error_code=error_code,
                error_caching_min_ttl=error_caching_min_ttl,
                response_code=response_code,
                response_page_path=response_page_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_caching_min_ttl: int | core.IntOut | None = core.arg(default=None)

        error_code: int | core.IntOut = core.arg()

        response_code: int | core.IntOut | None = core.arg(default=None)

        response_page_path: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CustomOriginConfig(core.Schema):

    http_port: int | core.IntOut = core.attr(int)

    https_port: int | core.IntOut = core.attr(int)

    origin_keepalive_timeout: int | core.IntOut | None = core.attr(int, default=None)

    origin_protocol_policy: str | core.StringOut = core.attr(str)

    origin_read_timeout: int | core.IntOut | None = core.attr(int, default=None)

    origin_ssl_protocols: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        http_port: int | core.IntOut,
        https_port: int | core.IntOut,
        origin_protocol_policy: str | core.StringOut,
        origin_ssl_protocols: list[str] | core.ArrayOut[core.StringOut],
        origin_keepalive_timeout: int | core.IntOut | None = None,
        origin_read_timeout: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CustomOriginConfig.Args(
                http_port=http_port,
                https_port=https_port,
                origin_protocol_policy=origin_protocol_policy,
                origin_ssl_protocols=origin_ssl_protocols,
                origin_keepalive_timeout=origin_keepalive_timeout,
                origin_read_timeout=origin_read_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_port: int | core.IntOut = core.arg()

        https_port: int | core.IntOut = core.arg()

        origin_keepalive_timeout: int | core.IntOut | None = core.arg(default=None)

        origin_protocol_policy: str | core.StringOut = core.arg()

        origin_read_timeout: int | core.IntOut | None = core.arg(default=None)

        origin_ssl_protocols: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class OriginShield(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    origin_shield_region: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        origin_shield_region: str | core.StringOut,
    ):
        super().__init__(
            args=OriginShield.Args(
                enabled=enabled,
                origin_shield_region=origin_shield_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        origin_shield_region: str | core.StringOut = core.arg()


@core.schema
class S3OriginConfig(core.Schema):

    origin_access_identity: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        origin_access_identity: str | core.StringOut,
    ):
        super().__init__(
            args=S3OriginConfig.Args(
                origin_access_identity=origin_access_identity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        origin_access_identity: str | core.StringOut = core.arg()


@core.schema
class CustomHeader(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=CustomHeader.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Origin(core.Schema):

    connection_attempts: int | core.IntOut | None = core.attr(int, default=None)

    connection_timeout: int | core.IntOut | None = core.attr(int, default=None)

    custom_header: list[CustomHeader] | core.ArrayOut[CustomHeader] | None = core.attr(
        CustomHeader, default=None, kind=core.Kind.array
    )

    custom_origin_config: CustomOriginConfig | None = core.attr(CustomOriginConfig, default=None)

    domain_name: str | core.StringOut = core.attr(str)

    origin_id: str | core.StringOut = core.attr(str)

    origin_path: str | core.StringOut | None = core.attr(str, default=None)

    origin_shield: OriginShield | None = core.attr(OriginShield, default=None)

    s3_origin_config: S3OriginConfig | None = core.attr(S3OriginConfig, default=None)

    def __init__(
        self,
        *,
        domain_name: str | core.StringOut,
        origin_id: str | core.StringOut,
        connection_attempts: int | core.IntOut | None = None,
        connection_timeout: int | core.IntOut | None = None,
        custom_header: list[CustomHeader] | core.ArrayOut[CustomHeader] | None = None,
        custom_origin_config: CustomOriginConfig | None = None,
        origin_path: str | core.StringOut | None = None,
        origin_shield: OriginShield | None = None,
        s3_origin_config: S3OriginConfig | None = None,
    ):
        super().__init__(
            args=Origin.Args(
                domain_name=domain_name,
                origin_id=origin_id,
                connection_attempts=connection_attempts,
                connection_timeout=connection_timeout,
                custom_header=custom_header,
                custom_origin_config=custom_origin_config,
                origin_path=origin_path,
                origin_shield=origin_shield,
                s3_origin_config=s3_origin_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_attempts: int | core.IntOut | None = core.arg(default=None)

        connection_timeout: int | core.IntOut | None = core.arg(default=None)

        custom_header: list[CustomHeader] | core.ArrayOut[CustomHeader] | None = core.arg(
            default=None
        )

        custom_origin_config: CustomOriginConfig | None = core.arg(default=None)

        domain_name: str | core.StringOut = core.arg()

        origin_id: str | core.StringOut = core.arg()

        origin_path: str | core.StringOut | None = core.arg(default=None)

        origin_shield: OriginShield | None = core.arg(default=None)

        s3_origin_config: S3OriginConfig | None = core.arg(default=None)


@core.schema
class LambdaFunctionAssociation(core.Schema):

    event_type: str | core.StringOut = core.attr(str)

    include_body: bool | core.BoolOut | None = core.attr(bool, default=None)

    lambda_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        event_type: str | core.StringOut,
        lambda_arn: str | core.StringOut,
        include_body: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=LambdaFunctionAssociation.Args(
                event_type=event_type,
                lambda_arn=lambda_arn,
                include_body=include_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_type: str | core.StringOut = core.arg()

        include_body: bool | core.BoolOut | None = core.arg(default=None)

        lambda_arn: str | core.StringOut = core.arg()


@core.schema
class FunctionAssociation(core.Schema):

    event_type: str | core.StringOut = core.attr(str)

    function_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        event_type: str | core.StringOut,
        function_arn: str | core.StringOut,
    ):
        super().__init__(
            args=FunctionAssociation.Args(
                event_type=event_type,
                function_arn=function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_type: str | core.StringOut = core.arg()

        function_arn: str | core.StringOut = core.arg()


@core.schema
class OrderedCacheBehaviorForwardedValuesCookies(core.Schema):

    forward: str | core.StringOut = core.attr(str)

    whitelisted_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        forward: str | core.StringOut,
        whitelisted_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=OrderedCacheBehaviorForwardedValuesCookies.Args(
                forward=forward,
                whitelisted_names=whitelisted_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        forward: str | core.StringOut = core.arg()

        whitelisted_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class OrderedCacheBehaviorForwardedValues(core.Schema):

    cookies: OrderedCacheBehaviorForwardedValuesCookies = core.attr(
        OrderedCacheBehaviorForwardedValuesCookies
    )

    headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    query_string: bool | core.BoolOut = core.attr(bool)

    query_string_cache_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cookies: OrderedCacheBehaviorForwardedValuesCookies,
        query_string: bool | core.BoolOut,
        headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        query_string_cache_keys: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=OrderedCacheBehaviorForwardedValues.Args(
                cookies=cookies,
                query_string=query_string,
                headers=headers,
                query_string_cache_keys=query_string_cache_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies: OrderedCacheBehaviorForwardedValuesCookies = core.arg()

        headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        query_string: bool | core.BoolOut = core.arg()

        query_string_cache_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class OrderedCacheBehavior(core.Schema):

    allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    cache_policy_id: str | core.StringOut | None = core.attr(str, default=None)

    cached_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    compress: bool | core.BoolOut | None = core.attr(bool, default=None)

    default_ttl: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    field_level_encryption_id: str | core.StringOut | None = core.attr(str, default=None)

    forwarded_values: OrderedCacheBehaviorForwardedValues | None = core.attr(
        OrderedCacheBehaviorForwardedValues, default=None
    )

    function_association: list[FunctionAssociation] | core.ArrayOut[
        FunctionAssociation
    ] | None = core.attr(FunctionAssociation, default=None, kind=core.Kind.array)

    lambda_function_association: list[LambdaFunctionAssociation] | core.ArrayOut[
        LambdaFunctionAssociation
    ] | None = core.attr(LambdaFunctionAssociation, default=None, kind=core.Kind.array)

    max_ttl: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    min_ttl: int | core.IntOut | None = core.attr(int, default=None)

    origin_request_policy_id: str | core.StringOut | None = core.attr(str, default=None)

    path_pattern: str | core.StringOut = core.attr(str)

    realtime_log_config_arn: str | core.StringOut | None = core.attr(str, default=None)

    response_headers_policy_id: str | core.StringOut | None = core.attr(str, default=None)

    smooth_streaming: bool | core.BoolOut | None = core.attr(bool, default=None)

    target_origin_id: str | core.StringOut = core.attr(str)

    trusted_key_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    trusted_signers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    viewer_protocol_policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        allowed_methods: list[str] | core.ArrayOut[core.StringOut],
        cached_methods: list[str] | core.ArrayOut[core.StringOut],
        path_pattern: str | core.StringOut,
        target_origin_id: str | core.StringOut,
        viewer_protocol_policy: str | core.StringOut,
        cache_policy_id: str | core.StringOut | None = None,
        compress: bool | core.BoolOut | None = None,
        default_ttl: int | core.IntOut | None = None,
        field_level_encryption_id: str | core.StringOut | None = None,
        forwarded_values: OrderedCacheBehaviorForwardedValues | None = None,
        function_association: list[FunctionAssociation]
        | core.ArrayOut[FunctionAssociation]
        | None = None,
        lambda_function_association: list[LambdaFunctionAssociation]
        | core.ArrayOut[LambdaFunctionAssociation]
        | None = None,
        max_ttl: int | core.IntOut | None = None,
        min_ttl: int | core.IntOut | None = None,
        origin_request_policy_id: str | core.StringOut | None = None,
        realtime_log_config_arn: str | core.StringOut | None = None,
        response_headers_policy_id: str | core.StringOut | None = None,
        smooth_streaming: bool | core.BoolOut | None = None,
        trusted_key_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        trusted_signers: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=OrderedCacheBehavior.Args(
                allowed_methods=allowed_methods,
                cached_methods=cached_methods,
                path_pattern=path_pattern,
                target_origin_id=target_origin_id,
                viewer_protocol_policy=viewer_protocol_policy,
                cache_policy_id=cache_policy_id,
                compress=compress,
                default_ttl=default_ttl,
                field_level_encryption_id=field_level_encryption_id,
                forwarded_values=forwarded_values,
                function_association=function_association,
                lambda_function_association=lambda_function_association,
                max_ttl=max_ttl,
                min_ttl=min_ttl,
                origin_request_policy_id=origin_request_policy_id,
                realtime_log_config_arn=realtime_log_config_arn,
                response_headers_policy_id=response_headers_policy_id,
                smooth_streaming=smooth_streaming,
                trusted_key_groups=trusted_key_groups,
                trusted_signers=trusted_signers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        cache_policy_id: str | core.StringOut | None = core.arg(default=None)

        cached_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        compress: bool | core.BoolOut | None = core.arg(default=None)

        default_ttl: int | core.IntOut | None = core.arg(default=None)

        field_level_encryption_id: str | core.StringOut | None = core.arg(default=None)

        forwarded_values: OrderedCacheBehaviorForwardedValues | None = core.arg(default=None)

        function_association: list[FunctionAssociation] | core.ArrayOut[
            FunctionAssociation
        ] | None = core.arg(default=None)

        lambda_function_association: list[LambdaFunctionAssociation] | core.ArrayOut[
            LambdaFunctionAssociation
        ] | None = core.arg(default=None)

        max_ttl: int | core.IntOut | None = core.arg(default=None)

        min_ttl: int | core.IntOut | None = core.arg(default=None)

        origin_request_policy_id: str | core.StringOut | None = core.arg(default=None)

        path_pattern: str | core.StringOut = core.arg()

        realtime_log_config_arn: str | core.StringOut | None = core.arg(default=None)

        response_headers_policy_id: str | core.StringOut | None = core.arg(default=None)

        smooth_streaming: bool | core.BoolOut | None = core.arg(default=None)

        target_origin_id: str | core.StringOut = core.arg()

        trusted_key_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        trusted_signers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        viewer_protocol_policy: str | core.StringOut = core.arg()


@core.schema
class DefaultCacheBehaviorForwardedValuesCookies(core.Schema):

    forward: str | core.StringOut = core.attr(str)

    whitelisted_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        forward: str | core.StringOut,
        whitelisted_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=DefaultCacheBehaviorForwardedValuesCookies.Args(
                forward=forward,
                whitelisted_names=whitelisted_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        forward: str | core.StringOut = core.arg()

        whitelisted_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class DefaultCacheBehaviorForwardedValues(core.Schema):

    cookies: DefaultCacheBehaviorForwardedValuesCookies = core.attr(
        DefaultCacheBehaviorForwardedValuesCookies
    )

    headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    query_string: bool | core.BoolOut = core.attr(bool)

    query_string_cache_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cookies: DefaultCacheBehaviorForwardedValuesCookies,
        query_string: bool | core.BoolOut,
        headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        query_string_cache_keys: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=DefaultCacheBehaviorForwardedValues.Args(
                cookies=cookies,
                query_string=query_string,
                headers=headers,
                query_string_cache_keys=query_string_cache_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies: DefaultCacheBehaviorForwardedValuesCookies = core.arg()

        headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        query_string: bool | core.BoolOut = core.arg()

        query_string_cache_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class DefaultCacheBehavior(core.Schema):

    allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    cache_policy_id: str | core.StringOut | None = core.attr(str, default=None)

    cached_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    compress: bool | core.BoolOut | None = core.attr(bool, default=None)

    default_ttl: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    field_level_encryption_id: str | core.StringOut | None = core.attr(str, default=None)

    forwarded_values: DefaultCacheBehaviorForwardedValues | None = core.attr(
        DefaultCacheBehaviorForwardedValues, default=None
    )

    function_association: list[FunctionAssociation] | core.ArrayOut[
        FunctionAssociation
    ] | None = core.attr(FunctionAssociation, default=None, kind=core.Kind.array)

    lambda_function_association: list[LambdaFunctionAssociation] | core.ArrayOut[
        LambdaFunctionAssociation
    ] | None = core.attr(LambdaFunctionAssociation, default=None, kind=core.Kind.array)

    max_ttl: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    min_ttl: int | core.IntOut | None = core.attr(int, default=None)

    origin_request_policy_id: str | core.StringOut | None = core.attr(str, default=None)

    realtime_log_config_arn: str | core.StringOut | None = core.attr(str, default=None)

    response_headers_policy_id: str | core.StringOut | None = core.attr(str, default=None)

    smooth_streaming: bool | core.BoolOut | None = core.attr(bool, default=None)

    target_origin_id: str | core.StringOut = core.attr(str)

    trusted_key_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    trusted_signers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    viewer_protocol_policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        allowed_methods: list[str] | core.ArrayOut[core.StringOut],
        cached_methods: list[str] | core.ArrayOut[core.StringOut],
        target_origin_id: str | core.StringOut,
        viewer_protocol_policy: str | core.StringOut,
        cache_policy_id: str | core.StringOut | None = None,
        compress: bool | core.BoolOut | None = None,
        default_ttl: int | core.IntOut | None = None,
        field_level_encryption_id: str | core.StringOut | None = None,
        forwarded_values: DefaultCacheBehaviorForwardedValues | None = None,
        function_association: list[FunctionAssociation]
        | core.ArrayOut[FunctionAssociation]
        | None = None,
        lambda_function_association: list[LambdaFunctionAssociation]
        | core.ArrayOut[LambdaFunctionAssociation]
        | None = None,
        max_ttl: int | core.IntOut | None = None,
        min_ttl: int | core.IntOut | None = None,
        origin_request_policy_id: str | core.StringOut | None = None,
        realtime_log_config_arn: str | core.StringOut | None = None,
        response_headers_policy_id: str | core.StringOut | None = None,
        smooth_streaming: bool | core.BoolOut | None = None,
        trusted_key_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        trusted_signers: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=DefaultCacheBehavior.Args(
                allowed_methods=allowed_methods,
                cached_methods=cached_methods,
                target_origin_id=target_origin_id,
                viewer_protocol_policy=viewer_protocol_policy,
                cache_policy_id=cache_policy_id,
                compress=compress,
                default_ttl=default_ttl,
                field_level_encryption_id=field_level_encryption_id,
                forwarded_values=forwarded_values,
                function_association=function_association,
                lambda_function_association=lambda_function_association,
                max_ttl=max_ttl,
                min_ttl=min_ttl,
                origin_request_policy_id=origin_request_policy_id,
                realtime_log_config_arn=realtime_log_config_arn,
                response_headers_policy_id=response_headers_policy_id,
                smooth_streaming=smooth_streaming,
                trusted_key_groups=trusted_key_groups,
                trusted_signers=trusted_signers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        cache_policy_id: str | core.StringOut | None = core.arg(default=None)

        cached_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        compress: bool | core.BoolOut | None = core.arg(default=None)

        default_ttl: int | core.IntOut | None = core.arg(default=None)

        field_level_encryption_id: str | core.StringOut | None = core.arg(default=None)

        forwarded_values: DefaultCacheBehaviorForwardedValues | None = core.arg(default=None)

        function_association: list[FunctionAssociation] | core.ArrayOut[
            FunctionAssociation
        ] | None = core.arg(default=None)

        lambda_function_association: list[LambdaFunctionAssociation] | core.ArrayOut[
            LambdaFunctionAssociation
        ] | None = core.arg(default=None)

        max_ttl: int | core.IntOut | None = core.arg(default=None)

        min_ttl: int | core.IntOut | None = core.arg(default=None)

        origin_request_policy_id: str | core.StringOut | None = core.arg(default=None)

        realtime_log_config_arn: str | core.StringOut | None = core.arg(default=None)

        response_headers_policy_id: str | core.StringOut | None = core.arg(default=None)

        smooth_streaming: bool | core.BoolOut | None = core.arg(default=None)

        target_origin_id: str | core.StringOut = core.arg()

        trusted_key_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        trusted_signers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        viewer_protocol_policy: str | core.StringOut = core.arg()


@core.schema
class TrustedSignersItems(core.Schema):

    aws_account_number: str | core.StringOut = core.attr(str, computed=True)

    key_pair_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        aws_account_number: str | core.StringOut,
        key_pair_ids: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=TrustedSignersItems.Args(
                aws_account_number=aws_account_number,
                key_pair_ids=key_pair_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_account_number: str | core.StringOut = core.arg()

        key_pair_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class TrustedSigners(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    items: list[TrustedSignersItems] | core.ArrayOut[TrustedSignersItems] = core.attr(
        TrustedSignersItems, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        items: list[TrustedSignersItems] | core.ArrayOut[TrustedSignersItems],
    ):
        super().__init__(
            args=TrustedSigners.Args(
                enabled=enabled,
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        items: list[TrustedSignersItems] | core.ArrayOut[TrustedSignersItems] = core.arg()


@core.schema
class ViewerCertificate(core.Schema):

    acm_certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    cloudfront_default_certificate: bool | core.BoolOut | None = core.attr(bool, default=None)

    iam_certificate_id: str | core.StringOut | None = core.attr(str, default=None)

    minimum_protocol_version: str | core.StringOut | None = core.attr(str, default=None)

    ssl_support_method: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        acm_certificate_arn: str | core.StringOut | None = None,
        cloudfront_default_certificate: bool | core.BoolOut | None = None,
        iam_certificate_id: str | core.StringOut | None = None,
        minimum_protocol_version: str | core.StringOut | None = None,
        ssl_support_method: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ViewerCertificate.Args(
                acm_certificate_arn=acm_certificate_arn,
                cloudfront_default_certificate=cloudfront_default_certificate,
                iam_certificate_id=iam_certificate_id,
                minimum_protocol_version=minimum_protocol_version,
                ssl_support_method=ssl_support_method,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm_certificate_arn: str | core.StringOut | None = core.arg(default=None)

        cloudfront_default_certificate: bool | core.BoolOut | None = core.arg(default=None)

        iam_certificate_id: str | core.StringOut | None = core.arg(default=None)

        minimum_protocol_version: str | core.StringOut | None = core.arg(default=None)

        ssl_support_method: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LoggingConfig(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    include_cookies: bool | core.BoolOut | None = core.attr(bool, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        include_cookies: bool | core.BoolOut | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LoggingConfig.Args(
                bucket=bucket,
                include_cookies=include_cookies,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        include_cookies: bool | core.BoolOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TrustedKeyGroupsItems(core.Schema):

    key_group_id: str | core.StringOut = core.attr(str, computed=True)

    key_pair_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key_group_id: str | core.StringOut,
        key_pair_ids: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=TrustedKeyGroupsItems.Args(
                key_group_id=key_group_id,
                key_pair_ids=key_pair_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_group_id: str | core.StringOut = core.arg()

        key_pair_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class TrustedKeyGroups(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    items: list[TrustedKeyGroupsItems] | core.ArrayOut[TrustedKeyGroupsItems] = core.attr(
        TrustedKeyGroupsItems, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        items: list[TrustedKeyGroupsItems] | core.ArrayOut[TrustedKeyGroupsItems],
    ):
        super().__init__(
            args=TrustedKeyGroups.Args(
                enabled=enabled,
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        items: list[TrustedKeyGroupsItems] | core.ArrayOut[TrustedKeyGroupsItems] = core.arg()


@core.resource(type="aws_cloudfront_distribution", namespace="cloudfront")
class Distribution(core.Resource):

    aliases: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:
    distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Internal value used by CloudFront to allow future
    """
    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    comment: str | core.StringOut | None = core.attr(str, default=None)

    custom_error_response: list[CustomErrorResponse] | core.ArrayOut[
        CustomErrorResponse
    ] | None = core.attr(CustomErrorResponse, default=None, kind=core.Kind.array)

    default_cache_behavior: DefaultCacheBehavior = core.attr(DefaultCacheBehavior)

    default_root_object: str | core.StringOut | None = core.attr(str, default=None)

    """
    The domain name corresponding to the distribution. For
    """
    domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    true` if any of the key groups have public keys that CloudFront can use to verify the signature
    s of signed URLs and signed cookies
    """
    enabled: bool | core.BoolOut = core.attr(bool)

    """
    The current version of the distribution's information. For example:
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    The CloudFront Route 53 zone ID that can be used to
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    http_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    The identifier for the distribution. For example: `EDFDVBD632BHDS5`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of invalidation batches
    """
    in_progress_validation_batches: int | core.IntOut = core.attr(int, computed=True)

    is_ipv6_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The date and time the distribution was last modified.
    """
    last_modified_time: str | core.StringOut = core.attr(str, computed=True)

    logging_config: LoggingConfig | None = core.attr(LoggingConfig, default=None)

    ordered_cache_behavior: list[OrderedCacheBehavior] | core.ArrayOut[
        OrderedCacheBehavior
    ] | None = core.attr(OrderedCacheBehavior, default=None, kind=core.Kind.array)

    origin: list[Origin] | core.ArrayOut[Origin] = core.attr(Origin, kind=core.Kind.array)

    origin_group: list[OriginGroup] | core.ArrayOut[OriginGroup] | None = core.attr(
        OriginGroup, default=None, kind=core.Kind.array
    )

    price_class: str | core.StringOut | None = core.attr(str, default=None)

    restrictions: Restrictions = core.attr(Restrictions)

    retain_on_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The current status of the distribution. `Deployed` if the
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    List of nested attributes for active trusted key groups, if the distribution is set up to serve priv
    ate content with signed URLs
    """
    trusted_key_groups: list[TrustedKeyGroups] | core.ArrayOut[TrustedKeyGroups] = core.attr(
        TrustedKeyGroups, computed=True, kind=core.Kind.array
    )

    """
    List of nested attributes for active trusted signers, if the distribution is set up to serve private
    content with signed URLs
    """
    trusted_signers: list[TrustedSigners] | core.ArrayOut[TrustedSigners] = core.attr(
        TrustedSigners, computed=True, kind=core.Kind.array
    )

    viewer_certificate: ViewerCertificate = core.attr(ViewerCertificate)

    wait_for_deployment: bool | core.BoolOut | None = core.attr(bool, default=None)

    web_acl_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        default_cache_behavior: DefaultCacheBehavior,
        enabled: bool | core.BoolOut,
        origin: list[Origin] | core.ArrayOut[Origin],
        restrictions: Restrictions,
        viewer_certificate: ViewerCertificate,
        aliases: list[str] | core.ArrayOut[core.StringOut] | None = None,
        comment: str | core.StringOut | None = None,
        custom_error_response: list[CustomErrorResponse]
        | core.ArrayOut[CustomErrorResponse]
        | None = None,
        default_root_object: str | core.StringOut | None = None,
        http_version: str | core.StringOut | None = None,
        is_ipv6_enabled: bool | core.BoolOut | None = None,
        logging_config: LoggingConfig | None = None,
        ordered_cache_behavior: list[OrderedCacheBehavior]
        | core.ArrayOut[OrderedCacheBehavior]
        | None = None,
        origin_group: list[OriginGroup] | core.ArrayOut[OriginGroup] | None = None,
        price_class: str | core.StringOut | None = None,
        retain_on_delete: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        wait_for_deployment: bool | core.BoolOut | None = None,
        web_acl_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Distribution.Args(
                default_cache_behavior=default_cache_behavior,
                enabled=enabled,
                origin=origin,
                restrictions=restrictions,
                viewer_certificate=viewer_certificate,
                aliases=aliases,
                comment=comment,
                custom_error_response=custom_error_response,
                default_root_object=default_root_object,
                http_version=http_version,
                is_ipv6_enabled=is_ipv6_enabled,
                logging_config=logging_config,
                ordered_cache_behavior=ordered_cache_behavior,
                origin_group=origin_group,
                price_class=price_class,
                retain_on_delete=retain_on_delete,
                tags=tags,
                tags_all=tags_all,
                wait_for_deployment=wait_for_deployment,
                web_acl_id=web_acl_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aliases: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        comment: str | core.StringOut | None = core.arg(default=None)

        custom_error_response: list[CustomErrorResponse] | core.ArrayOut[
            CustomErrorResponse
        ] | None = core.arg(default=None)

        default_cache_behavior: DefaultCacheBehavior = core.arg()

        default_root_object: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut = core.arg()

        http_version: str | core.StringOut | None = core.arg(default=None)

        is_ipv6_enabled: bool | core.BoolOut | None = core.arg(default=None)

        logging_config: LoggingConfig | None = core.arg(default=None)

        ordered_cache_behavior: list[OrderedCacheBehavior] | core.ArrayOut[
            OrderedCacheBehavior
        ] | None = core.arg(default=None)

        origin: list[Origin] | core.ArrayOut[Origin] = core.arg()

        origin_group: list[OriginGroup] | core.ArrayOut[OriginGroup] | None = core.arg(default=None)

        price_class: str | core.StringOut | None = core.arg(default=None)

        restrictions: Restrictions = core.arg()

        retain_on_delete: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        viewer_certificate: ViewerCertificate = core.arg()

        wait_for_deployment: bool | core.BoolOut | None = core.arg(default=None)

        web_acl_id: str | core.StringOut | None = core.arg(default=None)
