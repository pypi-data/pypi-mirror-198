import terrascript.core as core


@core.data(type="aws_eks_addon_version", namespace="aws_eks")
class DsAddonVersion(core.Data):

    addon_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    kubernetes_version: str | core.StringOut = core.attr(str)

    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        addon_name: str | core.StringOut,
        kubernetes_version: str | core.StringOut,
        most_recent: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAddonVersion.Args(
                addon_name=addon_name,
                kubernetes_version=kubernetes_version,
                most_recent=most_recent,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        addon_name: str | core.StringOut = core.arg()

        kubernetes_version: str | core.StringOut = core.arg()

        most_recent: bool | core.BoolOut | None = core.arg(default=None)
