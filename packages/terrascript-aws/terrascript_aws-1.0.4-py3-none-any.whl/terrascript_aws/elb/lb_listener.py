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

    scope: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    session_cookie_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    session_timeout: int | core.IntOut | None = core.attr(int, default=None, computed=True)

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
class AuthenticateCognito(core.Schema):

    authentication_request_extra_params: dict[str, str] | core.MapOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.map)

    on_unauthenticated_request: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    scope: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    session_cookie_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    session_timeout: int | core.IntOut | None = core.attr(int, default=None, computed=True)

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
class DefaultAction(core.Schema):

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
            args=DefaultAction.Args(
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


@core.resource(type="aws_lb_listener", namespace="elb")
class LbListener(core.Resource):
    """
    (Optional)  Name of the Application-Layer Protocol Negotiation (ALPN) policy. Can be set if `protoco
    l` is `TLS`. Valid values are `HTTP1Only`, `HTTP2Only`, `HTTP2Optional`, `HTTP2Preferred`, and `None
    .
    """

    alpn_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) ARN of the target group.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN of the default SSL server certificate. Exactly one certificate is required if the pro
    tocol is HTTPS. For adding additional SSL certificates, see the [`aws_lb_listener_certificate` resou
    rce](/docs/providers/aws/r/lb_listener_certificate.html).
    """
    certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Configuration block for default actions. Detailed below.
    """
    default_action: list[DefaultAction] | core.ArrayOut[DefaultAction] = core.attr(
        DefaultAction, kind=core.Kind.array
    )

    """
    ARN of the listener (matches `arn`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces New Resource) ARN of the load balancer.
    """
    load_balancer_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Port on which the load balancer is listening. Not valid for Gateway Load Balancers.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Protocol for connections from clients to the load balancer. For Application Load Balancer
    s, valid values are `HTTP` and `HTTPS`, with a default of `HTTP`. For Network Load Balancers, valid
    values are `TCP`, `TLS`, `UDP`, and `TCP_UDP`. Not valid to use `UDP` or `TCP_UDP` if dual-stack mod
    e is enabled. Not valid for Gateway Load Balancers.
    """
    protocol: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the SSL Policy for the listener. Required if `protocol` is `HTTPS` or `TLS`.
    """
    ssl_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
        default_action: list[DefaultAction] | core.ArrayOut[DefaultAction],
        load_balancer_arn: str | core.StringOut,
        alpn_policy: str | core.StringOut | None = None,
        certificate_arn: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        protocol: str | core.StringOut | None = None,
        ssl_policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbListener.Args(
                default_action=default_action,
                load_balancer_arn=load_balancer_arn,
                alpn_policy=alpn_policy,
                certificate_arn=certificate_arn,
                port=port,
                protocol=protocol,
                ssl_policy=ssl_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alpn_policy: str | core.StringOut | None = core.arg(default=None)

        certificate_arn: str | core.StringOut | None = core.arg(default=None)

        default_action: list[DefaultAction] | core.ArrayOut[DefaultAction] = core.arg()

        load_balancer_arn: str | core.StringOut = core.arg()

        port: int | core.IntOut | None = core.arg(default=None)

        protocol: str | core.StringOut | None = core.arg(default=None)

        ssl_policy: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
