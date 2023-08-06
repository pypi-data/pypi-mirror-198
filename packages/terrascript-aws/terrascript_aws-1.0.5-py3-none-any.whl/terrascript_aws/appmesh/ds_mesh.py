import terrascript.core as core


@core.schema
class EgressFilter(core.Schema):

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=EgressFilter.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class Spec(core.Schema):

    egress_filter: list[EgressFilter] | core.ArrayOut[EgressFilter] = core.attr(
        EgressFilter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        egress_filter: list[EgressFilter] | core.ArrayOut[EgressFilter],
    ):
        super().__init__(
            args=Spec.Args(
                egress_filter=egress_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_filter: list[EgressFilter] | core.ArrayOut[EgressFilter] = core.arg()


@core.data(type="aws_appmesh_mesh", namespace="appmesh")
class DsMesh(core.Data):
    """
    The ARN of the service mesh.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the service mesh.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last update date of the service mesh.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The AWS account ID of the service mesh's owner.
    """
    mesh_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of the service mesh.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The resource owner's AWS account ID.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    The service mesh specification.
    """
    spec: list[Spec] | core.ArrayOut[Spec] = core.attr(Spec, computed=True, kind=core.Kind.array)

    """
    A map of tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        mesh_owner: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMesh.Args(
                name=name,
                mesh_owner=mesh_owner,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mesh_owner: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
