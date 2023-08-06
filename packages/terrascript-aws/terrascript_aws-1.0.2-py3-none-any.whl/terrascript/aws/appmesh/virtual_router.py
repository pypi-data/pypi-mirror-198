import terrascript.core as core


@core.schema
class PortMapping(core.Schema):

    port: int | core.IntOut = core.attr(int)

    protocol: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        port: int | core.IntOut,
        protocol: str | core.StringOut,
    ):
        super().__init__(
            args=PortMapping.Args(
                port=port,
                protocol=protocol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port: int | core.IntOut = core.arg()

        protocol: str | core.StringOut = core.arg()


@core.schema
class Listener(core.Schema):

    port_mapping: PortMapping = core.attr(PortMapping)

    def __init__(
        self,
        *,
        port_mapping: PortMapping,
    ):
        super().__init__(
            args=Listener.Args(
                port_mapping=port_mapping,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port_mapping: PortMapping = core.arg()


@core.schema
class Spec(core.Schema):

    listener: Listener = core.attr(Listener)

    def __init__(
        self,
        *,
        listener: Listener,
    ):
        super().__init__(
            args=Spec.Args(
                listener=listener,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        listener: Listener = core.arg()


@core.resource(type="aws_appmesh_virtual_router", namespace="aws_appmesh")
class VirtualRouter(core.Resource):

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
            args=VirtualRouter.Args(
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
