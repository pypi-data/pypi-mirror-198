import terrascript.core as core


@core.schema
class VirtualService(core.Schema):

    virtual_service_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        virtual_service_name: str | core.StringOut,
    ):
        super().__init__(
            args=VirtualService.Args(
                virtual_service_name=virtual_service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_service_name: str | core.StringOut = core.arg()


@core.schema
class Target(core.Schema):

    virtual_service: VirtualService = core.attr(VirtualService)

    def __init__(
        self,
        *,
        virtual_service: VirtualService,
    ):
        super().__init__(
            args=Target.Args(
                virtual_service=virtual_service,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_service: VirtualService = core.arg()


@core.schema
class RewriteHostname(core.Schema):

    default_target_hostname: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        default_target_hostname: str | core.StringOut,
    ):
        super().__init__(
            args=RewriteHostname.Args(
                default_target_hostname=default_target_hostname,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_target_hostname: str | core.StringOut = core.arg()


@core.schema
class Prefix(core.Schema):

    default_prefix: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        default_prefix: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Prefix.Args(
                default_prefix=default_prefix,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_prefix: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Rewrite(core.Schema):

    hostname: RewriteHostname | None = core.attr(RewriteHostname, default=None)

    prefix: Prefix | None = core.attr(Prefix, default=None)

    def __init__(
        self,
        *,
        hostname: RewriteHostname | None = None,
        prefix: Prefix | None = None,
    ):
        super().__init__(
            args=Rewrite.Args(
                hostname=hostname,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hostname: RewriteHostname | None = core.arg(default=None)

        prefix: Prefix | None = core.arg(default=None)


@core.schema
class Http2RouteAction(core.Schema):

    rewrite: Rewrite | None = core.attr(Rewrite, default=None)

    target: Target = core.attr(Target)

    def __init__(
        self,
        *,
        target: Target,
        rewrite: Rewrite | None = None,
    ):
        super().__init__(
            args=Http2RouteAction.Args(
                target=target,
                rewrite=rewrite,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rewrite: Rewrite | None = core.arg(default=None)

        target: Target = core.arg()


@core.schema
class Http2RouteMatchHostname(core.Schema):

    exact: str | core.StringOut | None = core.attr(str, default=None)

    suffix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        exact: str | core.StringOut | None = None,
        suffix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Http2RouteMatchHostname.Args(
                exact=exact,
                suffix=suffix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exact: str | core.StringOut | None = core.arg(default=None)

        suffix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Http2RouteMatch(core.Schema):

    hostname: Http2RouteMatchHostname | None = core.attr(Http2RouteMatchHostname, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        hostname: Http2RouteMatchHostname | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Http2RouteMatch.Args(
                hostname=hostname,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hostname: Http2RouteMatchHostname | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Http2Route(core.Schema):

    action: Http2RouteAction = core.attr(Http2RouteAction)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    def __init__(
        self,
        *,
        action: Http2RouteAction,
        match: Http2RouteMatch,
    ):
        super().__init__(
            args=Http2Route.Args(
                action=action,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Http2RouteAction = core.arg()

        match: Http2RouteMatch = core.arg()


@core.schema
class HttpRoute(core.Schema):

    action: Http2RouteAction = core.attr(Http2RouteAction)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    def __init__(
        self,
        *,
        action: Http2RouteAction,
        match: Http2RouteMatch,
    ):
        super().__init__(
            args=HttpRoute.Args(
                action=action,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Http2RouteAction = core.arg()

        match: Http2RouteMatch = core.arg()


@core.schema
class GrpcRouteMatch(core.Schema):

    service_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        service_name: str | core.StringOut,
    ):
        super().__init__(
            args=GrpcRouteMatch.Args(
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        service_name: str | core.StringOut = core.arg()


@core.schema
class GrpcRouteAction(core.Schema):

    target: Target = core.attr(Target)

    def __init__(
        self,
        *,
        target: Target,
    ):
        super().__init__(
            args=GrpcRouteAction.Args(
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target: Target = core.arg()


@core.schema
class GrpcRoute(core.Schema):

    action: GrpcRouteAction = core.attr(GrpcRouteAction)

    match: GrpcRouteMatch = core.attr(GrpcRouteMatch)

    def __init__(
        self,
        *,
        action: GrpcRouteAction,
        match: GrpcRouteMatch,
    ):
        super().__init__(
            args=GrpcRoute.Args(
                action=action,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: GrpcRouteAction = core.arg()

        match: GrpcRouteMatch = core.arg()


@core.schema
class Spec(core.Schema):

    grpc_route: GrpcRoute | None = core.attr(GrpcRoute, default=None)

    http2_route: Http2Route | None = core.attr(Http2Route, default=None)

    http_route: HttpRoute | None = core.attr(HttpRoute, default=None)

    def __init__(
        self,
        *,
        grpc_route: GrpcRoute | None = None,
        http2_route: Http2Route | None = None,
        http_route: HttpRoute | None = None,
    ):
        super().__init__(
            args=Spec.Args(
                grpc_route=grpc_route,
                http2_route=http2_route,
                http_route=http_route,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc_route: GrpcRoute | None = core.arg(default=None)

        http2_route: Http2Route | None = core.arg(default=None)

        http_route: HttpRoute | None = core.arg(default=None)


@core.resource(type="aws_appmesh_gateway_route", namespace="appmesh")
class GatewayRoute(core.Resource):
    """
    The ARN of the gateway route.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the gateway route.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the gateway route.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last update date of the gateway route.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the service mesh in which to create the gateway route. Must be between 1 and
    255 characters in length.
    """
    mesh_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provi
    der][1] is currently connected to.
    """
    mesh_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name to use for the gateway route. Must be between 1 and 255 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The resource owner's AWS account ID.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The gateway route specification to apply.
    """
    spec: Spec = core.attr(Spec)

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
    (Required) The name of the [virtual gateway](/docs/providers/aws/r/appmesh_virtual_gateway.html) to
    associate the gateway route with. Must be between 1 and 255 characters in length.
    """
    virtual_gateway_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        mesh_name: str | core.StringOut,
        name: str | core.StringOut,
        spec: Spec,
        virtual_gateway_name: str | core.StringOut,
        mesh_owner: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GatewayRoute.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
                virtual_gateway_name=virtual_gateway_name,
                mesh_owner=mesh_owner,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        mesh_name: str | core.StringOut = core.arg()

        mesh_owner: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        spec: Spec = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        virtual_gateway_name: str | core.StringOut = core.arg()
