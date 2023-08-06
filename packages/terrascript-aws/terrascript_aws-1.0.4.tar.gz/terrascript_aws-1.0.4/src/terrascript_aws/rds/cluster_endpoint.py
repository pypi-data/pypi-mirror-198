import terrascript.core as core


@core.resource(type="aws_rds_cluster_endpoint", namespace="rds")
class ClusterEndpoint(core.Resource):
    """
    Amazon Resource Name (ARN) of cluster
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resources) The identifier to use for the new endpoint. This parameter is store
    d as a lowercase string.
    """
    cluster_endpoint_identifier: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resources) The cluster identifier.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    (Required) The type of the endpoint. One of: READER , ANY .
    """
    custom_endpoint_type: str | core.StringOut = core.attr(str)

    """
    A custom endpoint for the Aurora cluster
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of DB instance identifiers that aren't part of the custom endpoint group. All other
    eligible instances are reachable through the custom endpoint. Only relevant if the list of static me
    mbers is empty. Conflicts with `static_members`.
    """
    excluded_members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The RDS Cluster Endpoint Identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of DB instance identifiers that are part of the custom endpoint group. Conflicts wit
    h `excluded_members`.
    """
    static_members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        cluster_endpoint_identifier: str | core.StringOut,
        cluster_identifier: str | core.StringOut,
        custom_endpoint_type: str | core.StringOut,
        excluded_members: list[str] | core.ArrayOut[core.StringOut] | None = None,
        static_members: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterEndpoint.Args(
                cluster_endpoint_identifier=cluster_endpoint_identifier,
                cluster_identifier=cluster_identifier,
                custom_endpoint_type=custom_endpoint_type,
                excluded_members=excluded_members,
                static_members=static_members,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_endpoint_identifier: str | core.StringOut = core.arg()

        cluster_identifier: str | core.StringOut = core.arg()

        custom_endpoint_type: str | core.StringOut = core.arg()

        excluded_members: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        static_members: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
