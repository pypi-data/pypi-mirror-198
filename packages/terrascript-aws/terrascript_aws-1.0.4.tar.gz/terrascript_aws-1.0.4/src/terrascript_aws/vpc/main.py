import terrascript.core as core


@core.resource(type="aws_vpc", namespace="vpc")
class Main(core.Resource):
    """
    Amazon Resource Name (ARN) of VPC
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You can
    not specify the range of IP addresses, or the size of the CIDR block. Default is `false`. Conflicts
    with `ipv6_ipam_pool_id`
    """
    assign_generated_ipv6_cidr_block: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The IPv4 CIDR block for the VPC. CIDR can be explicitly set or it can be derived from IPA
    M using `ipv4_netmask_length`.
    """
    cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the network ACL created by default on VPC creation
    """
    default_network_acl_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the route table created by default on VPC creation
    """
    default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the security group created by default on VPC creation
    """
    default_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    dhcp_options_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A boolean flag to enable/disable ClassicLink
    """
    enable_classiclink: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
    """
    enable_classiclink_dns_support: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
    """
    enable_dns_hostnames: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) A boolean flag to enable/disable DNS support in the VPC. Defaults true.
    """
    enable_dns_support: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The ID of the VPC
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A tenancy option for instances launched into the VPC. Default is `default`, which ensures
    that EC2 instances launched in this VPC use the EC2 instance tenancy attribute specified when the E
    C2 instance is launched. The only other option is `dedicated`, which ensures that EC2 instances laun
    ched in this VPC are run on dedicated tenancy instances regardless of the tenancy attribute specifie
    d at launch. This has a dedicated per region fee of $2 per hour, plus an hourly per instance usage f
    ee.
    """
    instance_tenancy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. IPAM is a VPC
    feature that you can use to automate your IP address management workflows including assigning, trac
    king, troubleshooting, and auditing IP addresses across AWS Regions and accounts. Using IPAM you can
    monitor IP address usage throughout your AWS Organization.
    """
    ipv4_ipam_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The netmask length of the IPv4 CIDR you want to allocate to this VPC. Requires specifying
    a `ipv4_ipam_pool_id`.
    """
    ipv4_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    The association ID for the IPv6 CIDR block.
    """
    ipv6_association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) IPv6 CIDR block to request from an IPAM Pool. Can be set explicitly or derived from IPAM
    using `ipv6_netmask_length`.
    """
    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) By default when an IPv6 CIDR is assigned to a VPC a default ipv6_cidr_block_network_borde
    r_group will be set to the region of the VPC. This can be changed to restrict advertisement of publi
    c addresses to specific Network Border Groups such as LocalZones.
    """
    ipv6_cidr_block_network_border_group: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) IPAM Pool ID for a IPv6 pool. Conflicts with `assign_generated_ipv6_cidr_block`.
    """
    ipv6_ipam_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Netmask length to request from IPAM Pool. Conflicts with `ipv6_cidr_block`. This can be o
    mitted if IPAM pool as a `allocation_default_netmask_length` set. Valid values: `56`.
    """
    ipv6_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    The ID of the main route table associated with
    """
    main_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the VPC.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

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
        assign_generated_ipv6_cidr_block: bool | core.BoolOut | None = None,
        cidr_block: str | core.StringOut | None = None,
        enable_classiclink: bool | core.BoolOut | None = None,
        enable_classiclink_dns_support: bool | core.BoolOut | None = None,
        enable_dns_hostnames: bool | core.BoolOut | None = None,
        enable_dns_support: bool | core.BoolOut | None = None,
        instance_tenancy: str | core.StringOut | None = None,
        ipv4_ipam_pool_id: str | core.StringOut | None = None,
        ipv4_netmask_length: int | core.IntOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        ipv6_cidr_block_network_border_group: str | core.StringOut | None = None,
        ipv6_ipam_pool_id: str | core.StringOut | None = None,
        ipv6_netmask_length: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                assign_generated_ipv6_cidr_block=assign_generated_ipv6_cidr_block,
                cidr_block=cidr_block,
                enable_classiclink=enable_classiclink,
                enable_classiclink_dns_support=enable_classiclink_dns_support,
                enable_dns_hostnames=enable_dns_hostnames,
                enable_dns_support=enable_dns_support,
                instance_tenancy=instance_tenancy,
                ipv4_ipam_pool_id=ipv4_ipam_pool_id,
                ipv4_netmask_length=ipv4_netmask_length,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_cidr_block_network_border_group=ipv6_cidr_block_network_border_group,
                ipv6_ipam_pool_id=ipv6_ipam_pool_id,
                ipv6_netmask_length=ipv6_netmask_length,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        assign_generated_ipv6_cidr_block: bool | core.BoolOut | None = core.arg(default=None)

        cidr_block: str | core.StringOut | None = core.arg(default=None)

        enable_classiclink: bool | core.BoolOut | None = core.arg(default=None)

        enable_classiclink_dns_support: bool | core.BoolOut | None = core.arg(default=None)

        enable_dns_hostnames: bool | core.BoolOut | None = core.arg(default=None)

        enable_dns_support: bool | core.BoolOut | None = core.arg(default=None)

        instance_tenancy: str | core.StringOut | None = core.arg(default=None)

        ipv4_ipam_pool_id: str | core.StringOut | None = core.arg(default=None)

        ipv4_netmask_length: int | core.IntOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        ipv6_cidr_block_network_border_group: str | core.StringOut | None = core.arg(default=None)

        ipv6_ipam_pool_id: str | core.StringOut | None = core.arg(default=None)

        ipv6_netmask_length: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
