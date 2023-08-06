import terrascript.core as core


@core.schema
class AuthenticateCognito(core.Schema):

    authentication_request_extra_params: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    on_unauthenticated_request: str | core.StringOut = core.attr(str, computed=True)

    scope: str | core.StringOut = core.attr(str, computed=True)

    session_cookie_name: str | core.StringOut = core.attr(str, computed=True)

    session_timeout: int | core.IntOut = core.attr(int, computed=True)

    user_pool_arn: str | core.StringOut = core.attr(str, computed=True)

    user_pool_client_id: str | core.StringOut = core.attr(str, computed=True)

    user_pool_domain: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        authentication_request_extra_params: dict[str, str] | core.MapOut[core.StringOut],
        on_unauthenticated_request: str | core.StringOut,
        scope: str | core.StringOut,
        session_cookie_name: str | core.StringOut,
        session_timeout: int | core.IntOut,
        user_pool_arn: str | core.StringOut,
        user_pool_client_id: str | core.StringOut,
        user_pool_domain: str | core.StringOut,
    ):
        super().__init__(
            args=AuthenticateCognito.Args(
                authentication_request_extra_params=authentication_request_extra_params,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
                user_pool_arn=user_pool_arn,
                user_pool_client_id=user_pool_client_id,
                user_pool_domain=user_pool_domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: dict[str, str] | core.MapOut[
            core.StringOut
        ] = core.arg()

        on_unauthenticated_request: str | core.StringOut = core.arg()

        scope: str | core.StringOut = core.arg()

        session_cookie_name: str | core.StringOut = core.arg()

        session_timeout: int | core.IntOut = core.arg()

        user_pool_arn: str | core.StringOut = core.arg()

        user_pool_client_id: str | core.StringOut = core.arg()

        user_pool_domain: str | core.StringOut = core.arg()


@core.schema
class AuthenticateOidc(core.Schema):

    authentication_request_extra_params: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    authorization_endpoint: str | core.StringOut = core.attr(str, computed=True)

    client_id: str | core.StringOut = core.attr(str, computed=True)

    client_secret: str | core.StringOut = core.attr(str, computed=True)

    issuer: str | core.StringOut = core.attr(str, computed=True)

    on_unauthenticated_request: str | core.StringOut = core.attr(str, computed=True)

    scope: str | core.StringOut = core.attr(str, computed=True)

    session_cookie_name: str | core.StringOut = core.attr(str, computed=True)

    session_timeout: int | core.IntOut = core.attr(int, computed=True)

    token_endpoint: str | core.StringOut = core.attr(str, computed=True)

    user_info_endpoint: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        authentication_request_extra_params: dict[str, str] | core.MapOut[core.StringOut],
        authorization_endpoint: str | core.StringOut,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        issuer: str | core.StringOut,
        on_unauthenticated_request: str | core.StringOut,
        scope: str | core.StringOut,
        session_cookie_name: str | core.StringOut,
        session_timeout: int | core.IntOut,
        token_endpoint: str | core.StringOut,
        user_info_endpoint: str | core.StringOut,
    ):
        super().__init__(
            args=AuthenticateOidc.Args(
                authentication_request_extra_params=authentication_request_extra_params,
                authorization_endpoint=authorization_endpoint,
                client_id=client_id,
                client_secret=client_secret,
                issuer=issuer,
                on_unauthenticated_request=on_unauthenticated_request,
                scope=scope,
                session_cookie_name=session_cookie_name,
                session_timeout=session_timeout,
                token_endpoint=token_endpoint,
                user_info_endpoint=user_info_endpoint,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_request_extra_params: dict[str, str] | core.MapOut[
            core.StringOut
        ] = core.arg()

        authorization_endpoint: str | core.StringOut = core.arg()

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        issuer: str | core.StringOut = core.arg()

        on_unauthenticated_request: str | core.StringOut = core.arg()

        scope: str | core.StringOut = core.arg()

        session_cookie_name: str | core.StringOut = core.arg()

        session_timeout: int | core.IntOut = core.arg()

        token_endpoint: str | core.StringOut = core.arg()

        user_info_endpoint: str | core.StringOut = core.arg()


@core.schema
class FixedResponse(core.Schema):

    content_type: str | core.StringOut = core.attr(str, computed=True)

    message_body: str | core.StringOut = core.attr(str, computed=True)

    status_code: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        content_type: str | core.StringOut,
        message_body: str | core.StringOut,
        status_code: str | core.StringOut,
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

        message_body: str | core.StringOut = core.arg()

        status_code: str | core.StringOut = core.arg()


@core.schema
class TargetGroup(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    weight: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        weight: int | core.IntOut,
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

        weight: int | core.IntOut = core.arg()


@core.schema
class Stickiness(core.Schema):

    duration: int | core.IntOut = core.attr(int, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        duration: int | core.IntOut,
        enabled: bool | core.BoolOut,
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

        enabled: bool | core.BoolOut = core.arg()


@core.schema
class Forward(core.Schema):

    stickiness: list[Stickiness] | core.ArrayOut[Stickiness] = core.attr(
        Stickiness, computed=True, kind=core.Kind.array
    )

    target_group: list[TargetGroup] | core.ArrayOut[TargetGroup] = core.attr(
        TargetGroup, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        stickiness: list[Stickiness] | core.ArrayOut[Stickiness],
        target_group: list[TargetGroup] | core.ArrayOut[TargetGroup],
    ):
        super().__init__(
            args=Forward.Args(
                stickiness=stickiness,
                target_group=target_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stickiness: list[Stickiness] | core.ArrayOut[Stickiness] = core.arg()

        target_group: list[TargetGroup] | core.ArrayOut[TargetGroup] = core.arg()


@core.schema
class Redirect(core.Schema):

    host: str | core.StringOut = core.attr(str, computed=True)

    path: str | core.StringOut = core.attr(str, computed=True)

    port: str | core.StringOut = core.attr(str, computed=True)

    protocol: str | core.StringOut = core.attr(str, computed=True)

    query: str | core.StringOut = core.attr(str, computed=True)

    status_code: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        host: str | core.StringOut,
        path: str | core.StringOut,
        port: str | core.StringOut,
        protocol: str | core.StringOut,
        query: str | core.StringOut,
        status_code: str | core.StringOut,
    ):
        super().__init__(
            args=Redirect.Args(
                host=host,
                path=path,
                port=port,
                protocol=protocol,
                query=query,
                status_code=status_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: str | core.StringOut = core.arg()

        path: str | core.StringOut = core.arg()

        port: str | core.StringOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        query: str | core.StringOut = core.arg()

        status_code: str | core.StringOut = core.arg()


@core.schema
class DefaultAction(core.Schema):

    authenticate_cognito: list[AuthenticateCognito] | core.ArrayOut[
        AuthenticateCognito
    ] = core.attr(AuthenticateCognito, computed=True, kind=core.Kind.array)

    authenticate_oidc: list[AuthenticateOidc] | core.ArrayOut[AuthenticateOidc] = core.attr(
        AuthenticateOidc, computed=True, kind=core.Kind.array
    )

    fixed_response: list[FixedResponse] | core.ArrayOut[FixedResponse] = core.attr(
        FixedResponse, computed=True, kind=core.Kind.array
    )

    forward: list[Forward] | core.ArrayOut[Forward] = core.attr(
        Forward, computed=True, kind=core.Kind.array
    )

    order: int | core.IntOut = core.attr(int, computed=True)

    redirect: list[Redirect] | core.ArrayOut[Redirect] = core.attr(
        Redirect, computed=True, kind=core.Kind.array
    )

    target_group_arn: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        authenticate_cognito: list[AuthenticateCognito] | core.ArrayOut[AuthenticateCognito],
        authenticate_oidc: list[AuthenticateOidc] | core.ArrayOut[AuthenticateOidc],
        fixed_response: list[FixedResponse] | core.ArrayOut[FixedResponse],
        forward: list[Forward] | core.ArrayOut[Forward],
        order: int | core.IntOut,
        redirect: list[Redirect] | core.ArrayOut[Redirect],
        target_group_arn: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=DefaultAction.Args(
                authenticate_cognito=authenticate_cognito,
                authenticate_oidc=authenticate_oidc,
                fixed_response=fixed_response,
                forward=forward,
                order=order,
                redirect=redirect,
                target_group_arn=target_group_arn,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authenticate_cognito: list[AuthenticateCognito] | core.ArrayOut[
            AuthenticateCognito
        ] = core.arg()

        authenticate_oidc: list[AuthenticateOidc] | core.ArrayOut[AuthenticateOidc] = core.arg()

        fixed_response: list[FixedResponse] | core.ArrayOut[FixedResponse] = core.arg()

        forward: list[Forward] | core.ArrayOut[Forward] = core.arg()

        order: int | core.IntOut = core.arg()

        redirect: list[Redirect] | core.ArrayOut[Redirect] = core.arg()

        target_group_arn: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.data(type="aws_lb_listener", namespace="elb")
class DsLbListener(core.Data):

    alpn_policy: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN of the listener. Required if `load_balancer_arn` and `port` is not set.
    """
    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    default_action: list[DefaultAction] | core.ArrayOut[DefaultAction] = core.attr(
        DefaultAction, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN of the load balancer. Required if `arn` is not set.
    """
    load_balancer_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Port of the listener. Required if `arn` is not set.
    """
    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    protocol: str | core.StringOut = core.attr(str, computed=True)

    ssl_policy: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        load_balancer_arn: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLbListener.Args(
                arn=arn,
                load_balancer_arn=load_balancer_arn,
                port=port,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        load_balancer_arn: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
