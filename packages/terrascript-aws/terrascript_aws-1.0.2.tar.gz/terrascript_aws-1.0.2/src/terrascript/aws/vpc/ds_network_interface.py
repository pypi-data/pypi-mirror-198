import terrascript.core as core


@core.schema
class Attachment(core.Schema):

    attachment_id: str | core.StringOut = core.attr(str, computed=True)

    device_index: int | core.IntOut = core.attr(int, computed=True)

    instance_id: str | core.StringOut = core.attr(str, computed=True)

    instance_owner_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attachment_id: str | core.StringOut,
        device_index: int | core.IntOut,
        instance_id: str | core.StringOut,
        instance_owner_id: str | core.StringOut,
    ):
        super().__init__(
            args=Attachment.Args(
                attachment_id=attachment_id,
                device_index=device_index,
                instance_id=instance_id,
                instance_owner_id=instance_owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_id: str | core.StringOut = core.arg()

        device_index: int | core.IntOut = core.arg()

        instance_id: str | core.StringOut = core.arg()

        instance_owner_id: str | core.StringOut = core.arg()


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


@core.schema
class Association(core.Schema):

    allocation_id: str | core.StringOut = core.attr(str, computed=True)

    association_id: str | core.StringOut = core.attr(str, computed=True)

    carrier_ip: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ip: str | core.StringOut = core.attr(str, computed=True)

    ip_owner_id: str | core.StringOut = core.attr(str, computed=True)

    public_dns_name: str | core.StringOut = core.attr(str, computed=True)

    public_ip: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        allocation_id: str | core.StringOut,
        association_id: str | core.StringOut,
        carrier_ip: str | core.StringOut,
        customer_owned_ip: str | core.StringOut,
        ip_owner_id: str | core.StringOut,
        public_dns_name: str | core.StringOut,
        public_ip: str | core.StringOut,
    ):
        super().__init__(
            args=Association.Args(
                allocation_id=allocation_id,
                association_id=association_id,
                carrier_ip=carrier_ip,
                customer_owned_ip=customer_owned_ip,
                ip_owner_id=ip_owner_id,
                public_dns_name=public_dns_name,
                public_ip=public_ip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_id: str | core.StringOut = core.arg()

        association_id: str | core.StringOut = core.arg()

        carrier_ip: str | core.StringOut = core.arg()

        customer_owned_ip: str | core.StringOut = core.arg()

        ip_owner_id: str | core.StringOut = core.arg()

        public_dns_name: str | core.StringOut = core.arg()

        public_ip: str | core.StringOut = core.arg()


@core.data(type="aws_network_interface", namespace="aws_vpc")
class DsNetworkInterface(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    association: list[Association] | core.ArrayOut[Association] = core.attr(
        Association, computed=True, kind=core.Kind.array
    )

    attachment: list[Attachment] | core.ArrayOut[Attachment] = core.attr(
        Attachment, computed=True, kind=core.Kind.array
    )

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    interface_type: str | core.StringOut = core.attr(str, computed=True)

    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    mac_address: str | core.StringOut = core.attr(str, computed=True)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    private_dns_name: str | core.StringOut = core.attr(str, computed=True)

    private_ip: str | core.StringOut = core.attr(str, computed=True)

    private_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    requester_id: str | core.StringOut = core.attr(str, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsNetworkInterface.Args(
                filter=filter,
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
