import terrascript.core as core


@core.resource(type="aws_vpc_ipam_scope", namespace="vpc_ipam")
class Scope(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description for the scope you're creating.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the IPAM Scope.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the IPAM for which you're creating this scope.
    """
    ipam_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the IPAM for which you're creating this scope.
    """
    ipam_id: str | core.StringOut = core.attr(str)

    ipam_scope_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Defines if the scope is the default scope or not.
    """
    is_default: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Count of pools under this scope
    """
    pool_count: int | core.IntOut = core.attr(int, computed=True)

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
        ipam_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Scope.Args(
                ipam_id=ipam_id,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        ipam_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
