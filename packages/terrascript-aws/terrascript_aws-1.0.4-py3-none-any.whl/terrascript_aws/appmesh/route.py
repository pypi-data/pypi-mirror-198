import terrascript.core as core


@core.schema
class WeightedTarget(core.Schema):

    virtual_node: str | core.StringOut = core.attr(str)

    weight: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        virtual_node: str | core.StringOut,
        weight: int | core.IntOut,
    ):
        super().__init__(
            args=WeightedTarget.Args(
                virtual_node=virtual_node,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node: str | core.StringOut = core.arg()

        weight: int | core.IntOut = core.arg()


@core.schema
class Action(core.Schema):

    weighted_target: list[WeightedTarget] | core.ArrayOut[WeightedTarget] = core.attr(
        WeightedTarget, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        weighted_target: list[WeightedTarget] | core.ArrayOut[WeightedTarget],
    ):
        super().__init__(
            args=Action.Args(
                weighted_target=weighted_target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        weighted_target: list[WeightedTarget] | core.ArrayOut[WeightedTarget] = core.arg()


@core.schema
class Range(core.Schema):

    end: int | core.IntOut = core.attr(int)

    start: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        end: int | core.IntOut,
        start: int | core.IntOut,
    ):
        super().__init__(
            args=Range.Args(
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        end: int | core.IntOut = core.arg()

        start: int | core.IntOut = core.arg()


@core.schema
class MetadataMatch(core.Schema):

    exact: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    range: Range | None = core.attr(Range, default=None)

    regex: str | core.StringOut | None = core.attr(str, default=None)

    suffix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        exact: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        range: Range | None = None,
        regex: str | core.StringOut | None = None,
        suffix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MetadataMatch.Args(
                exact=exact,
                prefix=prefix,
                range=range,
                regex=regex,
                suffix=suffix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exact: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        range: Range | None = core.arg(default=None)

        regex: str | core.StringOut | None = core.arg(default=None)

        suffix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Metadata(core.Schema):

    invert: bool | core.BoolOut | None = core.attr(bool, default=None)

    match: MetadataMatch | None = core.attr(MetadataMatch, default=None)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        invert: bool | core.BoolOut | None = None,
        match: MetadataMatch | None = None,
    ):
        super().__init__(
            args=Metadata.Args(
                name=name,
                invert=invert,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invert: bool | core.BoolOut | None = core.arg(default=None)

        match: MetadataMatch | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()


@core.schema
class GrpcRouteMatch(core.Schema):

    metadata: list[Metadata] | core.ArrayOut[Metadata] | None = core.attr(
        Metadata, default=None, kind=core.Kind.array
    )

    method_name: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    service_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metadata: list[Metadata] | core.ArrayOut[Metadata] | None = None,
        method_name: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        service_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=GrpcRouteMatch.Args(
                metadata=metadata,
                method_name=method_name,
                prefix=prefix,
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metadata: list[Metadata] | core.ArrayOut[Metadata] | None = core.arg(default=None)

        method_name: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        service_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class PerRetryTimeout(core.Schema):

    unit: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        unit: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=PerRetryTimeout.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class GrpcRouteRetryPolicy(core.Schema):

    grpc_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    http_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_retries: int | core.IntOut = core.attr(int)

    per_retry_timeout: PerRetryTimeout = core.attr(PerRetryTimeout)

    tcp_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        max_retries: int | core.IntOut,
        per_retry_timeout: PerRetryTimeout,
        grpc_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = None,
        http_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tcp_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=GrpcRouteRetryPolicy.Args(
                max_retries=max_retries,
                per_retry_timeout=per_retry_timeout,
                grpc_retry_events=grpc_retry_events,
                http_retry_events=http_retry_events,
                tcp_retry_events=tcp_retry_events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        http_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        max_retries: int | core.IntOut = core.arg()

        per_retry_timeout: PerRetryTimeout = core.arg()

        tcp_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Idle(core.Schema):

    unit: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        unit: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=Idle.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class PerRequest(core.Schema):

    unit: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        unit: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=PerRequest.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class GrpcRouteTimeout(core.Schema):

    idle: Idle | None = core.attr(Idle, default=None)

    per_request: PerRequest | None = core.attr(PerRequest, default=None)

    def __init__(
        self,
        *,
        idle: Idle | None = None,
        per_request: PerRequest | None = None,
    ):
        super().__init__(
            args=GrpcRouteTimeout.Args(
                idle=idle,
                per_request=per_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Idle | None = core.arg(default=None)

        per_request: PerRequest | None = core.arg(default=None)


@core.schema
class GrpcRoute(core.Schema):

    action: Action = core.attr(Action)

    match: GrpcRouteMatch | None = core.attr(GrpcRouteMatch, default=None)

    retry_policy: GrpcRouteRetryPolicy | None = core.attr(GrpcRouteRetryPolicy, default=None)

    timeout: GrpcRouteTimeout | None = core.attr(GrpcRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        match: GrpcRouteMatch | None = None,
        retry_policy: GrpcRouteRetryPolicy | None = None,
        timeout: GrpcRouteTimeout | None = None,
    ):
        super().__init__(
            args=GrpcRoute.Args(
                action=action,
                match=match,
                retry_policy=retry_policy,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        match: GrpcRouteMatch | None = core.arg(default=None)

        retry_policy: GrpcRouteRetryPolicy | None = core.arg(default=None)

        timeout: GrpcRouteTimeout | None = core.arg(default=None)


@core.schema
class Header(core.Schema):

    invert: bool | core.BoolOut | None = core.attr(bool, default=None)

    match: MetadataMatch | None = core.attr(MetadataMatch, default=None)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        invert: bool | core.BoolOut | None = None,
        match: MetadataMatch | None = None,
    ):
        super().__init__(
            args=Header.Args(
                name=name,
                invert=invert,
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        invert: bool | core.BoolOut | None = core.arg(default=None)

        match: MetadataMatch | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()


@core.schema
class Http2RouteMatch(core.Schema):

    header: list[Header] | core.ArrayOut[Header] | None = core.attr(
        Header, default=None, kind=core.Kind.array
    )

    method: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut = core.attr(str)

    scheme: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        prefix: str | core.StringOut,
        header: list[Header] | core.ArrayOut[Header] | None = None,
        method: str | core.StringOut | None = None,
        scheme: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Http2RouteMatch.Args(
                prefix=prefix,
                header=header,
                method=method,
                scheme=scheme,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header: list[Header] | core.ArrayOut[Header] | None = core.arg(default=None)

        method: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut = core.arg()

        scheme: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Http2RouteRetryPolicy(core.Schema):

    http_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_retries: int | core.IntOut = core.attr(int)

    per_retry_timeout: PerRetryTimeout = core.attr(PerRetryTimeout)

    tcp_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        max_retries: int | core.IntOut,
        per_retry_timeout: PerRetryTimeout,
        http_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tcp_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Http2RouteRetryPolicy.Args(
                max_retries=max_retries,
                per_retry_timeout=per_retry_timeout,
                http_retry_events=http_retry_events,
                tcp_retry_events=tcp_retry_events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        max_retries: int | core.IntOut = core.arg()

        per_retry_timeout: PerRetryTimeout = core.arg()

        tcp_retry_events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Http2Route(core.Schema):

    action: Action = core.attr(Action)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    retry_policy: Http2RouteRetryPolicy | None = core.attr(Http2RouteRetryPolicy, default=None)

    timeout: GrpcRouteTimeout | None = core.attr(GrpcRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        match: Http2RouteMatch,
        retry_policy: Http2RouteRetryPolicy | None = None,
        timeout: GrpcRouteTimeout | None = None,
    ):
        super().__init__(
            args=Http2Route.Args(
                action=action,
                match=match,
                retry_policy=retry_policy,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        match: Http2RouteMatch = core.arg()

        retry_policy: Http2RouteRetryPolicy | None = core.arg(default=None)

        timeout: GrpcRouteTimeout | None = core.arg(default=None)


@core.schema
class HttpRoute(core.Schema):

    action: Action = core.attr(Action)

    match: Http2RouteMatch = core.attr(Http2RouteMatch)

    retry_policy: Http2RouteRetryPolicy | None = core.attr(Http2RouteRetryPolicy, default=None)

    timeout: GrpcRouteTimeout | None = core.attr(GrpcRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        match: Http2RouteMatch,
        retry_policy: Http2RouteRetryPolicy | None = None,
        timeout: GrpcRouteTimeout | None = None,
    ):
        super().__init__(
            args=HttpRoute.Args(
                action=action,
                match=match,
                retry_policy=retry_policy,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        match: Http2RouteMatch = core.arg()

        retry_policy: Http2RouteRetryPolicy | None = core.arg(default=None)

        timeout: GrpcRouteTimeout | None = core.arg(default=None)


@core.schema
class TcpRouteTimeout(core.Schema):

    idle: Idle | None = core.attr(Idle, default=None)

    def __init__(
        self,
        *,
        idle: Idle | None = None,
    ):
        super().__init__(
            args=TcpRouteTimeout.Args(
                idle=idle,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Idle | None = core.arg(default=None)


@core.schema
class TcpRoute(core.Schema):

    action: Action = core.attr(Action)

    timeout: TcpRouteTimeout | None = core.attr(TcpRouteTimeout, default=None)

    def __init__(
        self,
        *,
        action: Action,
        timeout: TcpRouteTimeout | None = None,
    ):
        super().__init__(
            args=TcpRoute.Args(
                action=action,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        timeout: TcpRouteTimeout | None = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    grpc_route: GrpcRoute | None = core.attr(GrpcRoute, default=None)

    http2_route: Http2Route | None = core.attr(Http2Route, default=None)

    http_route: HttpRoute | None = core.attr(HttpRoute, default=None)

    priority: int | core.IntOut | None = core.attr(int, default=None)

    tcp_route: TcpRoute | None = core.attr(TcpRoute, default=None)

    def __init__(
        self,
        *,
        grpc_route: GrpcRoute | None = None,
        http2_route: Http2Route | None = None,
        http_route: HttpRoute | None = None,
        priority: int | core.IntOut | None = None,
        tcp_route: TcpRoute | None = None,
    ):
        super().__init__(
            args=Spec.Args(
                grpc_route=grpc_route,
                http2_route=http2_route,
                http_route=http_route,
                priority=priority,
                tcp_route=tcp_route,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc_route: GrpcRoute | None = core.arg(default=None)

        http2_route: Http2Route | None = core.arg(default=None)

        http_route: HttpRoute | None = core.arg(default=None)

        priority: int | core.IntOut | None = core.arg(default=None)

        tcp_route: TcpRoute | None = core.arg(default=None)


@core.resource(type="aws_appmesh_route", namespace="appmesh")
class Route(core.Resource):
    """
    The ARN of the route.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the route.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the route.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last update date of the route.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the service mesh in which to create the route. Must be between 1 and 255 char
    acters in length.
    """
    mesh_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provi
    der][1] is currently connected to.
    """
    mesh_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name to use for the route. Must be between 1 and 255 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The resource owner's AWS account ID.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The route specification to apply.
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
    (Required) The name of the virtual router in which to create the route. Must be between 1 and 255 ch
    aracters in length.
    """
    virtual_router_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        mesh_name: str | core.StringOut,
        name: str | core.StringOut,
        spec: Spec,
        virtual_router_name: str | core.StringOut,
        mesh_owner: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Route.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
                virtual_router_name=virtual_router_name,
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

        virtual_router_name: str | core.StringOut = core.arg()
