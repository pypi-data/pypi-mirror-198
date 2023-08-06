import terrascript.core as core


@core.data(type="aws_eks_addon", namespace="aws_eks")
class DsAddon(core.Data):

    addon_name: str | core.StringOut = core.attr(str)

    addon_version: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    modified_at: str | core.StringOut = core.attr(str, computed=True)

    service_account_role_arn: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        addon_name: str | core.StringOut,
        cluster_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAddon.Args(
                addon_name=addon_name,
                cluster_name=cluster_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        addon_name: str | core.StringOut = core.arg()

        cluster_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
