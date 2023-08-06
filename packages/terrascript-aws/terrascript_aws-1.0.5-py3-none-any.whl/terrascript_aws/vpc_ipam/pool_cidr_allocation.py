import terrascript.core as core


@core.resource(type="aws_vpc_ipam_pool_cidr_allocation", namespace="vpc_ipam")
class PoolCidrAllocation(core.Resource):
    """
    (Optional) The CIDR you want to assign to the pool.
    """

    cidr: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The description for the allocation.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Exclude a particular CIDR range from being returned by the pool.
    """
    disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ID of the allocation.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    ipam_pool_allocation_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the pool to which you want to assign a CIDR.
    """
    ipam_pool_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The netmask length of the CIDR you would like to allocate to the IPAM pool. Valid Values:
    0-32`.
    """
    netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    The ID of the resource.
    """
    resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The owner of the resource.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of the resource.
    """
    resource_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        ipam_pool_id: str | core.StringOut,
        cidr: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = None,
        netmask_length: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PoolCidrAllocation.Args(
                ipam_pool_id=ipam_pool_id,
                cidr=cidr,
                description=description,
                disallowed_cidrs=disallowed_cidrs,
                netmask_length=netmask_length,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        disallowed_cidrs: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipam_pool_id: str | core.StringOut = core.arg()

        netmask_length: int | core.IntOut | None = core.arg(default=None)
