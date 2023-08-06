import terrascript.core as core


@core.data(type="aws_eks_cluster_auth", namespace="eks")
class DsClusterAuth(core.Data):
    """
    Name of the cluster.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the cluster
    """
    name: str | core.StringOut = core.attr(str)

    """
    The token to use to authenticate with the cluster.
    """
    token: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsClusterAuth.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
