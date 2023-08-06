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


@core.data(type="aws_eip", namespace="ec2")
class DsEip(core.Data):
    """
    The ID representing the association of the address with an instance in a VPC.
    """

    association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The carrier IP address.
    """
    carrier_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    Customer Owned IP.
    """
    customer_owned_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of a Customer Owned IP Pool. For more on customer owned IP addressed check out [Customer-owne
    d IP addresses guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-networking-comp
    onents.html#ip-addressing)
    """
    customer_owned_ipv4_pool: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).
    """
    domain: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more name/value pairs to use as filters. There are several valid keys, for a full
    reference, check out the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
    API_DescribeAddresses.html).
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do N
    OT set `id`, only set `public_ip`
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the instance that the address is associated with (if any).
    """
    instance_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the network interface.
    """
    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the network interface.
    """
    network_interface_owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Private DNS associated with the Elastic IP address.
    """
    private_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    The private IP address associated with the Elastic IP address.
    """
    private_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    Public DNS associated with the Elastic IP address.
    """
    public_dns: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The public IP of the specific EIP to retrieve.
    """
    public_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of an address pool.
    """
    public_ipv4_pool: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags, each pair of which must exactly match a pair on the desired Elastic IP
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        public_ip: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEip.Args(
                filter=filter,
                id=id,
                public_ip=public_ip,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        public_ip: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
