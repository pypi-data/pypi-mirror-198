import terrascript.core as core


@core.resource(type="aws_vpc_ipv6_cidr_block_association", namespace="vpc")
class Ipv6CidrBlockAssociation(core.Resource):
    """
    The ID of the VPC CIDR association
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The IPv6 CIDR block for the VPC. CIDR can be explicitly set or it can be derived from IPA
    M using `ipv6_netmask_length`. This parameter is required if `ipv6_netmask_length` is not set and he
    IPAM pool does not have `allocation_default_netmask` set.
    """
    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The ID of an IPv6 IPAM pool you want to use for allocating this VPC's CIDR. IPAM is a VPC
    feature that you can use to automate your IP address management workflows including assigning, trac
    king, troubleshooting, and auditing IP addresses across AWS Regions and accounts.
    """
    ipv6_ipam_pool_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The netmask length of the IPv6 CIDR you want to allocate to this VPC. Requires specifying
    a `ipv6_ipam_pool_id`. This parameter is optional if the IPAM pool has `allocation_default_netmask`
    set, otherwise it or `cidr_block` are required
    """
    ipv6_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The ID of the VPC to make the association with.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ipv6_ipam_pool_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        ipv6_cidr_block: str | core.StringOut | None = None,
        ipv6_netmask_length: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipv6CidrBlockAssociation.Args(
                ipv6_ipam_pool_id=ipv6_ipam_pool_id,
                vpc_id=vpc_id,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_netmask_length=ipv6_netmask_length,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        ipv6_ipam_pool_id: str | core.StringOut = core.arg()

        ipv6_netmask_length: int | core.IntOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
