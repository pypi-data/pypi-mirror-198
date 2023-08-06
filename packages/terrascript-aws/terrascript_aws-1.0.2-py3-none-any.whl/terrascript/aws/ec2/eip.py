import terrascript.core as core


@core.resource(type="aws_eip", namespace="aws_ec2")
class Eip(core.Resource):

    address: str | core.StringOut | None = core.attr(str, default=None)

    allocation_id: str | core.StringOut = core.attr(str, computed=True)

    associate_with_private_ip: str | core.StringOut | None = core.attr(str, default=None)

    association_id: str | core.StringOut = core.attr(str, computed=True)

    carrier_ip: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ip: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None)

    domain: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_border_group: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interface: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    private_dns: str | core.StringOut = core.attr(str, computed=True)

    private_ip: str | core.StringOut = core.attr(str, computed=True)

    public_dns: str | core.StringOut = core.attr(str, computed=True)

    public_ip: str | core.StringOut = core.attr(str, computed=True)

    public_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
