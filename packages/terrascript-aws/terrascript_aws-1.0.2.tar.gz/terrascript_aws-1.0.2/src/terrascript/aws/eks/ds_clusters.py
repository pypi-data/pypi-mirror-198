import terrascript.core as core


@core.data(type="aws_eks_clusters", namespace="aws_eks")
class DsClusters(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsClusters.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
