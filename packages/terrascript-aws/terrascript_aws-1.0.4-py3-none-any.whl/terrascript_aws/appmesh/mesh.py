import terrascript.core as core


@core.schema
class EgressFilter(core.Schema):

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EgressFilter.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    egress_filter: EgressFilter | None = core.attr(EgressFilter, default=None)

    def __init__(
        self,
        *,
        egress_filter: EgressFilter | None = None,
    ):
        super().__init__(
            args=Spec.Args(
                egress_filter=egress_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_filter: EgressFilter | None = core.arg(default=None)


@core.resource(type="aws_appmesh_mesh", namespace="appmesh")
class Mesh(core.Resource):
    """
    The ARN of the service mesh.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the service mesh.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the service mesh.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last update date of the service mesh.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account ID of the service mesh's owner.
    """
    mesh_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name to use for the service mesh. Must be between 1 and 255 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The resource owner's AWS account ID.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The service mesh specification to apply.
    """
    spec: Spec | None = core.attr(Spec, default=None)

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
        name: str | core.StringOut,
        spec: Spec | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Mesh.Args(
                name=name,
                spec=spec,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        spec: Spec | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
