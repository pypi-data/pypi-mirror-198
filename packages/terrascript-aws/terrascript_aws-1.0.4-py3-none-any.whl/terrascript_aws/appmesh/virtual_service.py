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


@core.resource(type="aws_appmesh_virtual_service", namespace="appmesh")
class VirtualService(core.Resource):
    """
    The ARN of the virtual service.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the virtual service.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the virtual service.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last update date of the virtual service.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the service mesh in which to create the virtual service. Must be between 1 an
    d 255 characters in length.
    """
    mesh_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provi
    der][1] is currently connected to.
    """
    mesh_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name to use for the virtual service. Must be between 1 and 255 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The resource owner's AWS account ID.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The virtual service specification to apply.
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
