import terrascript.core as core


@core.resource(type="aws_default_vpc", namespace="vpc")
class DefaultVpc(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    assign_generated_ipv6_cidr_block: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The primary IPv4 CIDR block for the VPC
    """
    cidr_block: str | core.StringOut = core.attr(str, computed=True)

    default_network_acl_id: str | core.StringOut = core.attr(str, computed=True)

    default_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    default_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    dhcp_options_id: str | core.StringOut = core.attr(str, computed=True)

    enable_classiclink: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    enable_classiclink_dns_support: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    enable_dns_hostnames: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_dns_support: bool | core.BoolOut | None = core.attr(bool, default=None)

    existing_default_vpc: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Whether destroying the resource deletes the default VPC. Default: `false`
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The allowed tenancy of instances launched into the VPC
    """
    instance_tenancy: str | core.StringOut = core.attr(str, computed=True)

    ipv6_association_id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ipv6_cidr_block_network_border_group: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    ipv6_ipam_pool_id: str | core.StringOut | None = core.attr(str, default=None)

    ipv6_netmask_length: int | core.IntOut | None = core.attr(int, default=None)

    main_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

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
        assign_generated_ipv6_cidr_block: bool | core.BoolOut | None = None,
        enable_classiclink: bool | core.BoolOut | None = None,
        enable_classiclink_dns_support: bool | core.BoolOut | None = None,
        enable_dns_hostnames: bool | core.BoolOut | None = None,
        enable_dns_support: bool | core.BoolOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
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
            args=DefaultVpc.Args(
                assign_generated_ipv6_cidr_block=assign_generated_ipv6_cidr_block,
                enable_classiclink=enable_classiclink,
                enable_classiclink_dns_support=enable_classiclink_dns_support,
                enable_dns_hostnames=enable_dns_hostnames,
                enable_dns_support=enable_dns_support,
                force_destroy=force_destroy,
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

        enable_classiclink: bool | core.BoolOut | None = core.arg(default=None)

        enable_classiclink_dns_support: bool | core.BoolOut | None = core.arg(default=None)

        enable_dns_hostnames: bool | core.BoolOut | None = core.arg(default=None)

        enable_dns_support: bool | core.BoolOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        ipv6_cidr_block_network_border_group: str | core.StringOut | None = core.arg(default=None)

        ipv6_ipam_pool_id: str | core.StringOut | None = core.arg(default=None)

        ipv6_netmask_length: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
