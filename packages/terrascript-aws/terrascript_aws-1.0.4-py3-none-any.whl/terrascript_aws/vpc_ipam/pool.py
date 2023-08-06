import terrascript.core as core


@core.resource(type="aws_vpc_ipam_pool", namespace="vpc_ipam")
class Pool(core.Resource):
    """
    (Optional) The IP protocol assigned to this pool. You must choose either IPv4 or IPv6 protocol for a
    pool.
    """

    address_family: str | core.StringOut = core.attr(str)

    """
    (Optional) A default netmask length for allocations added to this pool. If, for example, the CIDR as
    signed to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16
    (unless you provide a different netmask value when you create the new allocation).
    """
    allocation_default_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The maximum netmask length that will be required for CIDR allocations in this pool.
    """
    allocation_max_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The minimum netmask length that will be required for CIDR allocations in this pool.
    """
    allocation_min_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Tags that are required for resources that use CIDRs from this IPAM pool. Resources that d
    o not have these tags will not be allowed to allocate space from the pool. If the resources have the
    ir tags changed after they have allocated space or if the allocation tagging requirements are change
    d on the pool, the resource may be marked as noncompliant.
    """
    allocation_resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Amazon Resource Name (ARN) of IPAM
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If you include this argument, IPAM automatically imports any VPCs you have in your scope
    that fall
    """
    auto_import: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Limits which AWS service the pool can be used in. Only useable on public scopes. Valid Va
    lues: `ec2`.
    """
    aws_service: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A description for the IPAM pool.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the IPAM
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the scope in which you would like to create the IPAM pool.
    """
    ipam_scope_id: str | core.StringOut = core.attr(str)

    ipam_scope_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The locale in which you would like to create the IPAM pool. Locale is the Region where yo
    u want to make an IPAM pool available for allocations. You can only create pools with locales that m
    atch the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches th
    e VPC's Region. Possible values: Any AWS region, such as `us-east-1`.
    """
    locale: str | core.StringOut | None = core.attr(str, default=None)

    pool_depth: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Defines whether or not IPv6 pool space is publicly advertisable over the internet. This o
    ption is not available for IPv4 pool space.
    """
    publicly_advertisable: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The ID of the source IPAM pool. Use this argument to create a child pool within an existi
    ng pool.
    """
    source_ipam_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the IPAM
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
