import terrascript.core as core


@core.resource(type="aws_eip", namespace="ec2")
class Eip(core.Resource):
    """
    (Optional) IP address from an EC2 BYOIP pool. This option is only available for VPC EIPs.
    """

    address: str | core.StringOut | None = core.attr(str, default=None)

    """
    ID that AWS assigns to represent the allocation of the Elastic IP address for use with instances in
    a VPC.
    """
    allocation_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) User-specified primary or secondary private IP address to associate with the Elastic IP a
    ddress. If no private IP address is specified, the Elastic IP address is associated with the primary
    private IP address.
    """
    associate_with_private_ip: str | core.StringOut | None = core.attr(str, default=None)

    """
    ID representing the association of the address with an instance in a VPC.
    """
    association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Carrier IP address.
    """
    carrier_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    Customer owned IP.
    """
    customer_owned_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ID  of a customer-owned address pool. For more on customer owned IP addressed check out [
    Customer-owned IP addresses guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-ne
    tworking-components.html#ip-addressing).
    """
    customer_owned_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None)

    """
    Indicates if this EIP is for use in VPC (`vpc`) or EC2 Classic (`standard`).
    """
    domain: str | core.StringOut = core.attr(str, computed=True)

    """
    Contains the EIP allocation ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) EC2 instance ID.
    """
    instance: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Location from which the IP address is advertised. Use this parameter to limit the address
    to this location.
    """
    network_border_group: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Network interface ID to associate with.
    """
    network_interface: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The Private DNS associated with the Elastic IP address (if in VPC).
    """
    private_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    Contains the private IP address (if in VPC).
    """
    private_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    Public DNS associated with the Elastic IP address.
    """
    public_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    Contains the public IP address.
    """
    public_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) EC2 IPv4 address pool identifier or `amazon`. This option is only available for VPC EIPs.
    """
    public_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags to assign to the resource. Tags can only be applied to EIPs in a VPC. If conf
    igured with a provider [`default_tags` configuration block](https://registry.terraform.io/providers/
    hashicorp/aws/latest/docs#default_tags-configuration-block) present, tags with matching keys will ov
    erwrite those defined at the provider-level.
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
    (Optional) Boolean if the EIP is in a VPC or not.
    """
    vpc: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        address: str | core.StringOut | None = None,
        associate_with_private_ip: str | core.StringOut | None = None,
        customer_owned_ipv4_pool: str | core.StringOut | None = None,
        instance: str | core.StringOut | None = None,
        network_border_group: str | core.StringOut | None = None,
        network_interface: str | core.StringOut | None = None,
        public_ipv4_pool: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Eip.Args(
                address=address,
                associate_with_private_ip=associate_with_private_ip,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                instance=instance,
                network_border_group=network_border_group,
                network_interface=network_interface,
                public_ipv4_pool=public_ipv4_pool,
                tags=tags,
                tags_all=tags_all,
                vpc=vpc,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address: str | core.StringOut | None = core.arg(default=None)

        associate_with_private_ip: str | core.StringOut | None = core.arg(default=None)

        customer_owned_ipv4_pool: str | core.StringOut | None = core.arg(default=None)

        instance: str | core.StringOut | None = core.arg(default=None)

        network_border_group: str | core.StringOut | None = core.arg(default=None)

        network_interface: str | core.StringOut | None = core.arg(default=None)

        public_ipv4_pool: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc: bool | core.BoolOut | None = core.arg(default=None)
