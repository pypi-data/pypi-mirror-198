import terrascript.core as core


@core.data(type="aws_redshift_orderable_cluster", namespace="redshift")
class DsOrderableCluster(core.Data):
    """
    List of Availability Zone names where the Redshit Cluster is available.
    """

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Reshift Cluster typeE.g., `multi-node` or `single-node`
    """
    cluster_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Redshift Cluster versionE.g., `1.0`
    """
    cluster_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Redshift Cluster node typeE.g., `dc2.8xlarge`
    """
    node_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Ordered list of preferred Redshift Cluster node types. The first match in this list will
    be returned. If no preferred matches are found and the original search returned more than one result
    , an error is returned.
    """
    preferred_node_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_type: str | core.StringOut | None = None,
        cluster_version: str | core.StringOut | None = None,
        node_type: str | core.StringOut | None = None,
        preferred_node_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOrderableCluster.Args(
                cluster_type=cluster_type,
                cluster_version=cluster_version,
                node_type=node_type,
                preferred_node_types=preferred_node_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_type: str | core.StringOut | None = core.arg(default=None)

        cluster_version: str | core.StringOut | None = core.arg(default=None)

        node_type: str | core.StringOut | None = core.arg(default=None)

        preferred_node_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
