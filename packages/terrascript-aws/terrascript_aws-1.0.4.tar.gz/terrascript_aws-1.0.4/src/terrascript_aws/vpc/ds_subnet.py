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


@core.data(type="aws_subnet", namespace="vpc")
class DsSubnet(core.Data):
    """
    ARN of the subnet.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether an IPv6 address is assigned on creation.
    """
    assign_ipv6_address_on_creation: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Availability zone where the subnet must reside.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) ID of the Availability Zone for the subnet. This argument is not supported in all regions
    or partitions. If necessary, use `availability_zone` instead.
    """
    availability_zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Available IP addresses of the subnet.
    """
    available_ip_address_count: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) CIDR block of the desired subnet.
    """
    cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Identifier of customer owned IPv4 address pool.
    """
    customer_owned_ipv4_pool: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether the desired subnet must be the default subnet for its associated availability zon
    e.
    """
    default_for_az: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet return synthet
    ic IPv6 addresses for IPv4-only destinations.
    """
    enable_dns64: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
    """
    enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut = core.attr(
        bool, computed=True
    )

    """
    Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
    """
    enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut = core.attr(
        bool, computed=True
    )

    """
    (Optional) Configuration block. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) ID of the specific subnet to retrieve.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) IPv6 CIDR block of the desired subnet.
    """
    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Association ID of the IPv6 CIDR block.
    """
    ipv6_cidr_block_association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether this is an IPv6-only subnet.
    """
    ipv6_native: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether customer owned IP addresses are assigned on network interface creation.
    """
    map_customer_owned_ip_on_launch: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether public IP addresses are assigned on instance launch.
    """
    map_public_ip_on_launch: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    ARN of the Outpost.
    """
    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ID of the AWS account that owns the subnet.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of hostnames assigned to instances in the subnet at launch.
    """
    private_dns_hostname_type_on_launch: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) State that the desired subnet must have.
    """
    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags, each pair of which must exactly match a pair on the desired subnet.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) ID of the VPC that the desired subnet belongs to.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: str | core.StringOut | None = None,
        availability_zone_id: str | core.StringOut | None = None,
        cidr_block: str | core.StringOut | None = None,
        default_for_az: bool | core.BoolOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSubnet.Args(
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                cidr_block=cidr_block,
                default_for_az=default_for_az,
                filter=filter,
                id=id,
                ipv6_cidr_block=ipv6_cidr_block,
                state=state,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        availability_zone_id: str | core.StringOut | None = core.arg(default=None)

        cidr_block: str | core.StringOut | None = core.arg(default=None)

        default_for_az: bool | core.BoolOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
