import terrascript.core as core


@core.data(type="aws_eks_addon_version", namespace="eks")
class DsAddonVersion(core.Data):

    addon_name: str | core.StringOut = core.attr(str)

    """
    The name of the add-on
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    kubernetes_version: str | core.StringOut = core.attr(str)

    """
    (Optional) Determines if the most recent or default version of the addon should be returned.
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The version of the EKS add-on.
    """
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
