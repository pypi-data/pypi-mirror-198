import terrascript.core as core


@core.resource(type="aws_default_subnet", namespace="vpc")
class DefaultSubnet(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    assign_ipv6_address_on_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    availability_zone: str | core.StringOut = core.attr(str)

    """
    The AZ ID of the subnet
    """
    availability_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IPv4 CIDR block assigned to the subnet
    """
    cidr_block: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None)

    enable_dns64: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    existing_default_subnet: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Whether destroying the resource deletes the default subnet. Default: `false`
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ipv6_cidr_block_association_id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_native: bool | core.BoolOut | None = core.attr(bool, default=None)

    map_customer_owned_ip_on_launch: bool | core.BoolOut | None = core.attr(bool, default=None)

    map_public_ip_on_launch: bool | core.BoolOut | None = core.attr(bool, default=None)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    private_dns_hostname_type_on_launch: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The ID of the VPC the subnet is in
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: str | core.StringOut,
        assign_ipv6_address_on_creation: bool | core.BoolOut | None = None,
        customer_owned_ipv4_pool: str | core.StringOut | None = None,
        enable_dns64: bool | core.BoolOut | None = None,
        enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut | None = None,
        enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        ipv6_native: bool | core.BoolOut | None = None,
        map_customer_owned_ip_on_launch: bool | core.BoolOut | None = None,
        map_public_ip_on_launch: bool | core.BoolOut | None = None,
        private_dns_hostname_type_on_launch: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultSubnet.Args(
                availability_zone=availability_zone,
                assign_ipv6_address_on_creation=assign_ipv6_address_on_creation,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                enable_dns64=enable_dns64,
                enable_resource_name_dns_a_record_on_launch=enable_resource_name_dns_a_record_on_launch,
                enable_resource_name_dns_aaaa_record_on_launch=enable_resource_name_dns_aaaa_record_on_launch,
                force_destroy=force_destroy,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_native=ipv6_native,
                map_customer_owned_ip_on_launch=map_customer_owned_ip_on_launch,
                map_public_ip_on_launch=map_public_ip_on_launch,
                private_dns_hostname_type_on_launch=private_dns_hostname_type_on_launch,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        assign_ipv6_address_on_creation: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut = core.arg()

        customer_owned_ipv4_pool: str | core.StringOut | None = core.arg(default=None)

        enable_dns64: bool | core.BoolOut | None = core.arg(default=None)

        enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut | None = core.arg(
            default=None
        )

        enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut | None = core.arg(
            default=None
        )

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        ipv6_native: bool | core.BoolOut | None = core.arg(default=None)

        map_customer_owned_ip_on_launch: bool | core.BoolOut | None = core.arg(default=None)

        map_public_ip_on_launch: bool | core.BoolOut | None = core.arg(default=None)

        private_dns_hostname_type_on_launch: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
