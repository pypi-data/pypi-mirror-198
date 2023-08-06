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


@core.data(type="aws_eip", namespace="aws_ec2")
class DsEip(core.Data):

    association_id: str | core.StringOut = core.attr(str, computed=True)

    carrier_ip: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ip: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ipv4_pool: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut = core.attr(str, computed=True)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    instance_id: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    network_interface_owner_id: str | core.StringOut = core.attr(str, computed=True)

    private_dns: str | core.StringOut = core.attr(str, computed=True)

    private_ip: str | core.StringOut = core.attr(str, computed=True)

    public_dns: str | core.StringOut = core.attr(str, computed=True)

    public_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    public_ipv4_pool: str | core.StringOut = core.attr(str, computed=True)

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
