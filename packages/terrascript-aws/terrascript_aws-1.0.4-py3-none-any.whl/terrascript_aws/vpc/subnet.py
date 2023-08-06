import terrascript.core as core


@core.resource(type="aws_subnet", namespace="vpc")
class Subnet(core.Resource):
    """
    The ARN of the subnet.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specify true to indicate
    """
    assign_ipv6_address_on_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) AZ for the subnet.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) AZ ID of the subnet. This argument is not supported in all regions or partitions. If nece
    ssary, use `availability_zone` instead.
    """
    availability_zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The IPv4 CIDR block for the subnet.
    """
    cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The customer owned IPv4 address pool. Typically used with the `map_customer_owned_ip_on_l
    aunch` argument. The `outpost_arn` argument must be specified when configured.
    """
    customer_owned_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet sho
    uld return synthetic IPv6 addresses for IPv4-only destinations. Default: `false`.
    """
    enable_dns64: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Indicates whether to respond to DNS queries for instance hostnames with DNS A records. De
    fault: `false`.
    """
    enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    (Optional) Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
    Default: `false`.
    """
    enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    The ID of the subnet
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The IPv6 network range for the subnet,
    """
    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    """
    The association ID for the IPv6 CIDR block.
    """
    ipv6_cidr_block_association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether to create an IPv6-only subnet. Default: `false`.
    """
    ipv6_native: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specify `true` to indicate that network interfaces created in the subnet should be assig
    ned a customer owned IP address. The `customer_owned_ipv4_pool` and `outpost_arn` arguments must be
    specified when set to `true`. Default is `false`.
    """
    map_customer_owned_ip_on_launch: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specify true to indicate
    """
    map_public_ip_on_launch: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) of the Outpost.
    """
    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the AWS account that owns the subnet.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subne
    ts, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you
    can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: `ip-n
    ame`, `resource-name`.
    """
    private_dns_hostname_type_on_launch: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

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

    """
    (Required) The VPC ID.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: str | core.StringOut,
        assign_ipv6_address_on_creation: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        availability_zone_id: str | core.StringOut | None = None,
        cidr_block: str | core.StringOut | None = None,
        customer_owned_ipv4_pool: str | core.StringOut | None = None,
        enable_dns64: bool | core.BoolOut | None = None,
        enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut | None = None,
        enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        ipv6_native: bool | core.BoolOut | None = None,
        map_customer_owned_ip_on_launch: bool | core.BoolOut | None = None,
        map_public_ip_on_launch: bool | core.BoolOut | None = None,
        outpost_arn: str | core.StringOut | None = None,
        private_dns_hostname_type_on_launch: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Subnet.Args(
                vpc_id=vpc_id,
                assign_ipv6_address_on_creation=assign_ipv6_address_on_creation,
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                cidr_block=cidr_block,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                enable_dns64=enable_dns64,
                enable_resource_name_dns_a_record_on_launch=enable_resource_name_dns_a_record_on_launch,
                enable_resource_name_dns_aaaa_record_on_launch=enable_resource_name_dns_aaaa_record_on_launch,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_native=ipv6_native,
                map_customer_owned_ip_on_launch=map_customer_owned_ip_on_launch,
                map_public_ip_on_launch=map_public_ip_on_launch,
                outpost_arn=outpost_arn,
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

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        availability_zone_id: str | core.StringOut | None = core.arg(default=None)

        cidr_block: str | core.StringOut | None = core.arg(default=None)

        customer_owned_ipv4_pool: str | core.StringOut | None = core.arg(default=None)

        enable_dns64: bool | core.BoolOut | None = core.arg(default=None)

        enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut | None = core.arg(
            default=None
        )

        enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut | None = core.arg(
            default=None
        )

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        ipv6_native: bool | core.BoolOut | None = core.arg(default=None)

        map_customer_owned_ip_on_launch: bool | core.BoolOut | None = core.arg(default=None)

        map_public_ip_on_launch: bool | core.BoolOut | None = core.arg(default=None)

        outpost_arn: str | core.StringOut | None = core.arg(default=None)

        private_dns_hostname_type_on_launch: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
