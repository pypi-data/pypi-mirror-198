import terrascript.core as core


@core.data(type="aws_eks_node_groups", namespace="aws_eks")
class DsNodeGroups(core.Data):

    cluster_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
