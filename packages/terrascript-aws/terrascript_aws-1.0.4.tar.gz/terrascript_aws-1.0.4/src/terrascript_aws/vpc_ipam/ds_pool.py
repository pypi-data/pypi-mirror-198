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


@core.data(type="aws_vpc_ipam_pool", namespace="vpc_ipam")
class DsPool(core.Data):
    """
    The IP protocol assigned to this pool.
    """

    address_family: str | core.StringOut = core.attr(str, computed=True)

    """
    A default netmask length for allocations added to this pool. If, for example, the CIDR assigned to t
    his pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.
    """
    allocation_default_netmask_length: int | core.IntOut = core.attr(int, computed=True)

    """
    The maximum netmask length that will be required for CIDR allocations in this pool.
    """
    allocation_max_netmask_length: int | core.IntOut = core.attr(int, computed=True)

    """
    The minimum netmask length that will be required for CIDR allocations in this pool.
    """
    allocation_min_netmask_length: int | core.IntOut = core.attr(int, computed=True)

    """
    Tags that are required to create resources in using this pool.
    """
    allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Amazon Resource Name (ARN) of the pool
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    If enabled, IPAM will continuously look for resources within the CIDR range of this pool and automat
    ically import them as allocations into your IPAM.
    """
    auto_import: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Limits which service in AWS that the pool can be used in. "ec2", for example, allows users to use sp
    ace for Elastic IP addresses and VPCs.
    """
    aws_service: str | core.StringOut = core.attr(str, computed=True)

    """
    A description for the IPAM pool.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Custom filter block as described below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    The ID of the IPAM pool.
    """
    id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the IPAM pool you would like information on.
    """
    ipam_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the scope the pool belongs to.
    """
    ipam_scope_id: str | core.StringOut = core.attr(str, computed=True)

    ipam_scope_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Locale is the Region where your pool is available for allocations. You can only create pools with lo
    cales that match the operating Regions of the IPAM. You can only create VPCs from a pool whose local
    e matches the VPC's Region.
    """
    locale: str | core.StringOut = core.attr(str, computed=True)

    pool_depth: int | core.IntOut = core.attr(int, computed=True)

    """
    Defines whether or not IPv6 pool space is publicly ∂advertisable over the internet.
    """
    publicly_advertisable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The ID of the source IPAM pool.
    """
    source_ipam_pool_id: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags to assigned to the resource.
    """
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
