import terrascript.core as core


@core.resource(type="aws_eks_addon", namespace="aws_eks")
class Addon(core.Resource):

    addon_name: str | core.StringOut = core.attr(str)

    addon_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    modified_at: str | core.StringOut = core.attr(str, computed=True)

    preserve: bool | core.BoolOut | None = core.attr(bool, default=None)

    resolve_conflicts: str | core.StringOut | None = core.attr(str, default=None)

    service_account_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        addon_name: str | core.StringOut,
        cluster_name: str | core.StringOut,
        addon_version: str | core.StringOut | None = None,
        preserve: bool | core.BoolOut | None = None,
        resolve_conflicts: str | core.StringOut | None = None,
        service_account_role_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Addon.Args(
                addon_name=addon_name,
                cluster_name=cluster_name,
                addon_version=addon_version,
                preserve=preserve,
                resolve_conflicts=resolve_conflicts,
                service_account_role_arn=service_account_role_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        addon_name: str | core.StringOut = core.arg()

        addon_version: str | core.StringOut | None = core.arg(default=None)

        cluster_name: str | core.StringOut = core.arg()

        preserve: bool | core.BoolOut | None = core.arg(default=None)

        resolve_conflicts: str | core.StringOut | None = core.arg(default=None)

        service_account_role_arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
