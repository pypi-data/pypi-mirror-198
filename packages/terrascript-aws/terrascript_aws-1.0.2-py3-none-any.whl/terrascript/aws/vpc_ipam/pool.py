import terrascript.core as core


@core.resource(type="aws_vpc_ipam_pool", namespace="aws_vpc_ipam")
class Pool(core.Resource):

    address_family: str | core.StringOut = core.attr(str)

    allocation_default_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    allocation_max_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    allocation_min_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_import: bool | core.BoolOut | None = core.attr(bool, default=None)

    aws_service: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    ipam_scope_id: str | core.StringOut = core.attr(str)

    ipam_scope_type: str | core.StringOut = core.attr(str, computed=True)

    locale: str | core.StringOut | None = core.attr(str, default=None)

    pool_depth: int | core.IntOut = core.attr(int, computed=True)

    publicly_advertisable: bool | core.BoolOut | None = core.attr(bool, default=None)

    source_ipam_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    state: str | core.StringOut = core.attr(str, computed=True)

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
        address_family: str | core.StringOut,
        ipam_scope_id: str | core.StringOut,
        allocation_default_netmask_length: int | core.IntOut | None = None,
        allocation_max_netmask_length: int | core.IntOut | None = None,
        allocation_min_netmask_length: int | core.IntOut | None = None,
        allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        auto_import: bool | core.BoolOut | None = None,
        aws_service: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        locale: str | core.StringOut | None = None,
        publicly_advertisable: bool | core.BoolOut | None = None,
        source_ipam_pool_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Pool.Args(
                address_family=address_family,
                ipam_scope_id=ipam_scope_id,
                allocation_default_netmask_length=allocation_default_netmask_length,
                allocation_max_netmask_length=allocation_max_netmask_length,
                allocation_min_netmask_length=allocation_min_netmask_length,
                allocation_resource_tags=allocation_resource_tags,
                auto_import=auto_import,
                aws_service=aws_service,
                description=description,
                locale=locale,
                publicly_advertisable=publicly_advertisable,
                source_ipam_pool_id=source_ipam_pool_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address_family: str | core.StringOut = core.arg()

        allocation_default_netmask_length: int | core.IntOut | None = core.arg(default=None)

        allocation_max_netmask_length: int | core.IntOut | None = core.arg(default=None)

        allocation_min_netmask_length: int | core.IntOut | None = core.arg(default=None)

        allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        auto_import: bool | core.BoolOut | None = core.arg(default=None)

        aws_service: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        ipam_scope_id: str | core.StringOut = core.arg()

        locale: str | core.StringOut | None = core.arg(default=None)

        publicly_advertisable: bool | core.BoolOut | None = core.arg(default=None)

        source_ipam_pool_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
