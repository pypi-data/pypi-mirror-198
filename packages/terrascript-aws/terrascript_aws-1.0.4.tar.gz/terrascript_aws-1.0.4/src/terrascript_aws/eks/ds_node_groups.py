import terrascript.core as core


@core.data(type="aws_eks_node_groups", namespace="eks")
class DsNodeGroups(core.Data):
    """
    (Required) The name of the cluster.
    """

    cluster_name: str | core.StringOut = core.attr(str)

    """
    Cluster name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A set of all node group names in an EKS Cluster.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsNodeGroups.Args(
                cluster_name=cluster_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: str | core.StringOut = core.arg()
