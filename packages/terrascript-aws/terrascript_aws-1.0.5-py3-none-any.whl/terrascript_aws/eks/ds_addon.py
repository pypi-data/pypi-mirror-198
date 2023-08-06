import terrascript.core as core


@core.data(type="aws_eks_addon", namespace="eks")
class DsAddon(core.Data):

    addon_name: str | core.StringOut = core.attr(str)

    """
    The version of EKS add-on.
    """
    addon_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the EKS add-on.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-
    on was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    EKS Cluster name and EKS add-on name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-
    on was updated.
    """
    modified_at: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of IAM role used for EKS add-on. If value is empty -
    """
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
