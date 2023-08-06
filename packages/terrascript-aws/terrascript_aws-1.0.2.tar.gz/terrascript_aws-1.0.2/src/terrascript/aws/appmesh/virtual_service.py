import terrascript.core as core


@core.schema
class VirtualNode(core.Schema):

    virtual_node_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        virtual_node_name: str | core.StringOut,
    ):
        super().__init__(
            args=VirtualNode.Args(
                virtual_node_name=virtual_node_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node_name: str | core.StringOut = core.arg()


@core.schema
class VirtualRouter(core.Schema):

    virtual_router_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        virtual_router_name: str | core.StringOut,
    ):
        super().__init__(
            args=VirtualRouter.Args(
                virtual_router_name=virtual_router_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_router_name: str | core.StringOut = core.arg()


@core.schema
class Provider(core.Schema):

    virtual_node: VirtualNode | None = core.attr(VirtualNode, default=None)

    virtual_router: VirtualRouter | None = core.attr(VirtualRouter, default=None)

    def __init__(
        self,
        *,
        virtual_node: VirtualNode | None = None,
        virtual_router: VirtualRouter | None = None,
    ):
        super().__init__(
            args=Provider.Args(
                virtual_node=virtual_node,
                virtual_router=virtual_router,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node: VirtualNode | None = core.arg(default=None)

        virtual_router: VirtualRouter | None = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    provider: Provider | None = core.attr(Provider, default=None)

    def __init__(
        self,
        *,
        provider: Provider | None = None,
    ):
        super().__init__(
            args=Spec.Args(
                provider=provider,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provider: Provider | None = core.arg(default=None)


@core.resource(type="aws_appmesh_virtual_service", namespace="aws_appmesh")
class VirtualService(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    mesh_name: str | core.StringOut = core.attr(str)

    mesh_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    spec: Spec = core.attr(Spec)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        mesh_name: str | core.StringOut,
        name: str | core.StringOut,
        spec: Spec,
        mesh_owner: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VirtualService.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
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
