import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_vpc_ipam_pool", namespace="aws_vpc_ipam")
class DsPool(core.Data):

    address_family: str | core.StringOut = core.attr(str, computed=True)

    allocation_default_netmask_length: int | core.IntOut = core.attr(int, computed=True)

    allocation_max_netmask_length: int | core.IntOut = core.attr(int, computed=True)

    allocation_min_netmask_length: int | core.IntOut = core.attr(int, computed=True)

    allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_import: bool | core.BoolOut = core.attr(bool, computed=True)

    aws_service: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None)

    ipam_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    ipam_scope_id: str | core.StringOut = core.attr(str, computed=True)

    ipam_scope_type: str | core.StringOut = core.attr(str, computed=True)

    locale: str | core.StringOut = core.attr(str, computed=True)

    pool_depth: int | core.IntOut = core.attr(int, computed=True)

    publicly_advertisable: bool | core.BoolOut = core.attr(bool, computed=True)

    source_ipam_pool_id: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        ipam_pool_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPool.Args(
                allocation_resource_tags=allocation_resource_tags,
                filter=filter,
                id=id,
                ipam_pool_id=ipam_pool_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        ipam_pool_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
