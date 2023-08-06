import terrascript.core as core


@core.schema
class AuthenticateOidc(core.Schema):

    authentication_request_extra_params: dict[str, str] | core.MapOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.map)

    authorization_endpoint: str | core.StringOut = core.attr(str)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    issuer: str | core.StringOut = core.attr(str)

    on_unauthenticated_request: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    scope: str | core.StringOut | None = core.attr(str, default=None)

    session_cookie_name: str | core.StringOut | None = core.attr(str, default=None)

    session_timeout: int | core.IntOut | None = core.attr(int, default=None)

    token_endpoint: str | core.StringOut = core.attr(str)

    user_info_endpoint: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        authorization_endpoint: str | core.StringOut,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        issuer: str | core.StringOut,
        token_endpoint: str | core.StringOut,
        user_info_endpoint: str | core.StringOut,
        authentication_request_extra_params: dict[str, str]
        | core.MapOut[core.StringOut]
        | None = None,
        on_unauthenticated_request: str | core.StringOut | None = None,
        scope: str | core.StringOut | None = None,
        session_cookie_name: str | core.StringOut | None = None,
        session_timeout: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AuthenticateOidc.Args(
                authorization_endpoint=authorization_endpoint,
                client_id=client_id,
                client_secret=client_secret,
                issuer=issuer,
                token_endpoint=token_endpoint,
                user_info_endpoint=user_info_endpoint,
                authentication_request_extra_params=authentication_request_extra_params,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: dict[str, str] | core.MapOut[
            core.StringOut
        ] | None = core.arg(default=None)

        authorization_endpoint: str | core.StringOut = core.arg()

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        issuer: str | core.StringOut = core.arg()

        on_unauthenticated_request: str | core.StringOut | None = core.arg(default=None)

        scope: str | core.StringOut | None = core.arg(default=None)

        session_cookie_name: str | core.StringOut | None = core.arg(default=None)

        session_timeout: int | core.IntOut | None = core.arg(default=None)

        token_endpoint: str | core.StringOut = core.arg()

        user_info_endpoint: str | core.StringOut = core.arg()


@core.schema
class TargetGroup(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    weight: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        weight: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TargetGroup.Args(
                arn=arn,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        weight: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Stickiness(core.Schema):

    duration: int | core.IntOut = core.attr(int)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        duration: int | core.IntOut,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Stickiness.Args(
                duration=duration,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: int | core.IntOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Forward(core.Schema):

    stickiness: Stickiness | None = core.attr(Stickiness, default=None)

    target_group: list[TargetGroup] | core.ArrayOut[TargetGroup] = core.attr(
        TargetGroup, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        target_group: list[TargetGroup] | core.ArrayOut[TargetGroup],
        stickiness: Stickiness | None = None,
    ):
        super().__init__(
            args=Forward.Args(
                target_group=target_group,
                stickiness=stickiness,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stickiness: Stickiness | None = core.arg(default=None)

        target_group: list[TargetGroup] | core.ArrayOut[TargetGroup] = core.arg()


@core.schema
class Redirect(core.Schema):

    host: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    port: str | core.StringOut | None = core.attr(str, default=None)

    protocol: str | core.StringOut | None = core.attr(str, default=None)

    query: str | core.StringOut | None = core.attr(str, default=None)

    status_code: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status_code: str | core.StringOut,
        host: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
        port: str | core.StringOut | None = None,
        protocol: str | core.StringOut | None = None,
        query: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Redirect.Args(
                status_code=status_code,
                host=host,
                path=path,
                port=port,
                protocol=protocol,
                query=query,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        port: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut | None = core.arg(default=None)

        query: str | core.StringOut | None = core.arg(default=None)

        status_code: str | core.StringOut = core.arg()


@core.schema
class FixedResponse(core.Schema):

    content_type: str | core.StringOut = core.attr(str)

    message_body: str | core.StringOut | None = core.attr(str, default=None)

    status_code: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        content_type: str | core.StringOut,
        message_body: str | core.StringOut | None = None,
        status_code: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FixedResponse.Args(
                content_type=content_type,
                message_body=message_body,
                status_code=status_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_type: str | core.StringOut = core.arg()

        message_body: str | core.StringOut | None = core.arg(default=None)

        status_code: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AuthenticateCognito(core.Schema):

    authentication_request_extra_params: dict[str, str] | core.MapOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.map)

    on_unauthenticated_request: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    scope: str | core.StringOut | None = core.attr(str, default=None)

    session_cookie_name: str | core.StringOut | None = core.attr(str, default=None)

    session_timeout: int | core.IntOut | None = core.attr(int, default=None)

    user_pool_arn: str | core.StringOut = core.attr(str)

    user_pool_client_id: str | core.StringOut = core.attr(str)

    user_pool_domain: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        user_pool_arn: str | core.StringOut,
        user_pool_client_id: str | core.StringOut,
        user_pool_domain: str | core.StringOut,
        authentication_request_extra_params: dict[str, str]
        | core.MapOut[core.StringOut]
        | None = None,
        on_unauthenticated_request: str | core.StringOut | None = None,
        scope: str | core.StringOut | None = None,
        session_cookie_name: str | core.StringOut | None = None,
        session_timeout: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AuthenticateCognito.Args(
                user_pool_arn=user_pool_arn,
                user_pool_client_id=user_pool_client_id,
                user_pool_domain=user_pool_domain,
                authentication_request_extra_params=authentication_request_extra_params,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: dict[str, str] | core.MapOut[
            core.StringOut
        ] | None = core.arg(default=None)

        on_unauthenticated_request: str | core.StringOut | None = core.arg(default=None)

        scope: str | core.StringOut | None = core.arg(default=None)

        session_cookie_name: str | core.StringOut | None = core.arg(default=None)

        session_timeout: int | core.IntOut | None = core.arg(default=None)

        user_pool_arn: str | core.StringOut = core.arg()

        user_pool_client_id: str | core.StringOut = core.arg()

        user_pool_domain: str | core.StringOut = core.arg()


@core.schema
class Action(core.Schema):

    authenticate_cognito: AuthenticateCognito | None = core.attr(AuthenticateCognito, default=None)

    authenticate_oidc: AuthenticateOidc | None = core.attr(AuthenticateOidc, default=None)

    fixed_response: FixedResponse | None = core.attr(FixedResponse, default=None)

    forward: Forward | None = core.attr(Forward, default=None)

    order: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    redirect: Redirect | None = core.attr(Redirect, default=None)

    target_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        authenticate_cognito: AuthenticateCognito | None = None,
        authenticate_oidc: AuthenticateOidc | None = None,
        fixed_response: FixedResponse | None = None,
        forward: Forward | None = None,
        order: int | core.IntOut | None = None,
        redirect: Redirect | None = None,
        target_group_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Action.Args(
                type=type,
                authenticate_cognito=authenticate_cognito,
                authenticate_oidc=authenticate_oidc,
                fixed_response=fixed_response,
                forward=forward,
                order=order,
                redirect=redirect,
                target_group_arn=target_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authenticate_cognito: AuthenticateCognito | None = core.arg(default=None)

        authenticate_oidc: AuthenticateOidc | None = core.arg(default=None)

        fixed_response: FixedResponse | None = core.arg(default=None)

        forward: Forward | None = core.arg(default=None)

        order: int | core.IntOut | None = core.arg(default=None)

        redirect: Redirect | None = core.arg(default=None)

        target_group_arn: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class QueryString(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        value: str | core.StringOut,
        key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=QueryString.Args(
                value=value,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.schema
class SourceIp(core.Schema):

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=SourceIp.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class HostHeader(core.Schema):

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=HostHeader.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class HttpHeader(core.Schema):

    http_header_name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        http_header_name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=HttpHeader.Args(
                http_header_name=http_header_name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_header_name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class HttpRequestMethod(core.Schema):

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=HttpRequestMethod.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class PathPattern(core.Schema):

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=PathPattern.Args(
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Condition(core.Schema):

    host_header: HostHeader | None = core.attr(HostHeader, default=None)

    http_header: HttpHeader | None = core.attr(HttpHeader, default=None)

    http_request_method: HttpRequestMethod | None = core.attr(HttpRequestMethod, default=None)

    path_pattern: PathPattern | None = core.attr(PathPattern, default=None)

    query_string: list[QueryString] | core.ArrayOut[QueryString] | None = core.attr(
        QueryString, default=None, kind=core.Kind.array
    )

    source_ip: SourceIp | None = core.attr(SourceIp, default=None)

    def __init__(
        self,
        *,
        host_header: HostHeader | None = None,
        http_header: HttpHeader | None = None,
        http_request_method: HttpRequestMethod | None = None,
        path_pattern: PathPattern | None = None,
        query_string: list[QueryString] | core.ArrayOut[QueryString] | None = None,
        source_ip: SourceIp | None = None,
    ):
        super().__init__(
            args=Condition.Args(
                host_header=host_header,
                http_header=http_header,
                http_request_method=http_request_method,
                path_pattern=path_pattern,
                query_string=query_string,
                source_ip=source_ip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host_header: HostHeader | None = core.arg(default=None)

        http_header: HttpHeader | None = core.arg(default=None)

        http_request_method: HttpRequestMethod | None = core.arg(default=None)

        path_pattern: PathPattern | None = core.arg(default=None)

        query_string: list[QueryString] | core.ArrayOut[QueryString] | None = core.arg(default=None)

        source_ip: SourceIp | None = core.arg(default=None)


@core.resource(type="aws_lb_listener_rule", namespace="elb")
class LbListenerRule(core.Resource):
    """
    (Required) An Action block. Action blocks are documented below.
    """

    action: list[Action] | core.ArrayOut[Action] = core.attr(Action, kind=core.Kind.array)

    """
    (Required) The Amazon Resource Name (ARN) of the target group.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A Condition block. Multiple condition blocks of different types can be set and all must b
    e satisfied for the rule to match. Condition blocks are documented below.
    """
    condition: list[Condition] | core.ArrayOut[Condition] = core.attr(
        Condition, kind=core.Kind.array
    )

    """
    The ARN of the rule (matches `arn`)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces New Resource) The ARN of the listener to which to attach the rule.
    """
    listener_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) The priority for the rule between `1` and `50000`. Leaving it unset will automatically se
    t the rule with next available priority after currently existing highest rule. A listener can't have
    multiple rules with the same priority.
    """
    priority: int | core.IntOut | None = core.attr(int, default=None, computed=True)

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

    def __init__(
        self,
        resource_name: str,
        *,
        action: list[Action] | core.ArrayOut[Action],
        condition: list[Condition] | core.ArrayOut[Condition],
        listener_arn: str | core.StringOut,
        priority: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbListenerRule.Args(
                action=action,
                condition=condition,
                listener_arn=listener_arn,
                priority=priority,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: list[Action] | core.ArrayOut[Action] = core.arg()

        condition: list[Condition] | core.ArrayOut[Condition] = core.arg()

        listener_arn: str | core.StringOut = core.arg()

        priority: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
