import terrascript.core as core


@core.schema
class VirtualNode(core.Schema):

    virtual_node_name: str | core.StringOut = core.attr(str, computed=True)

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

    virtual_router_name: str | core.StringOut = core.attr(str, computed=True)

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

    virtual_node: list[VirtualNode] | core.ArrayOut[VirtualNode] = core.attr(
        VirtualNode, computed=True, kind=core.Kind.array
    )

    virtual_router: list[VirtualRouter] | core.ArrayOut[VirtualRouter] = core.attr(
        VirtualRouter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        virtual_node: list[VirtualNode] | core.ArrayOut[VirtualNode],
        virtual_router: list[VirtualRouter] | core.ArrayOut[VirtualRouter],
    ):
        super().__init__(
            args=Provider.Args(
                virtual_node=virtual_node,
                virtual_router=virtual_router,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_node: list[VirtualNode] | core.ArrayOut[VirtualNode] = core.arg()

        virtual_router: list[VirtualRouter] | core.ArrayOut[VirtualRouter] = core.arg()


@core.schema
class Spec(core.Schema):

    provider: list[Provider] | core.ArrayOut[Provider] = core.attr(
        Provider, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        provider: list[Provider] | core.ArrayOut[Provider],
    ):
        super().__init__(
            args=Spec.Args(
                provider=provider,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provider: list[Provider] | core.ArrayOut[Provider] = core.arg()


@core.data(type="aws_appmesh_virtual_service", namespace="appmesh")
class DsVirtualService(core.Data):
    """
    The ARN of the virtual service.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the virtual service.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last update date of the virtual service.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the service mesh in which the virtual service exists.
    """
    mesh_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The AWS account ID of the service mesh's owner.
    """
    mesh_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of the virtual service.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The resource owner's AWS account ID.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    The virtual service specification
    """
    spec: list[Spec] | core.ArrayOut[Spec] = core.attr(Spec, computed=True, kind=core.Kind.array)

    """
    A map of tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        mesh_name: str | core.StringOut,
        name: str | core.StringOut,
        mesh_owner: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsVirtualService.Args(
                mesh_name=mesh_name,
                name=name,
                mesh_owner=mesh_owner,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mesh_name: str | core.StringOut = core.arg()

        mesh_owner: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
