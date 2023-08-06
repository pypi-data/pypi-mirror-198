import terrascript.core as core


@core.schema
class Attachment(core.Schema):

    attachment_id: str | core.StringOut = core.attr(str, computed=True)

    device_index: int | core.IntOut = core.attr(int)

    instance: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        attachment_id: str | core.StringOut,
        device_index: int | core.IntOut,
        instance: str | core.StringOut,
    ):
        super().__init__(
            args=Attachment.Args(
                attachment_id=attachment_id,
                device_index=device_index,
                instance=instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_id: str | core.StringOut = core.arg()

        device_index: int | core.IntOut = core.arg()

        instance: str | core.StringOut = core.arg()


@core.resource(type="aws_network_interface", namespace="vpc")
class NetworkInterface(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    attachment: list[Attachment] | core.ArrayOut[Attachment] | None = core.attr(
        Attachment, default=None, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    interface_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ipv4_prefix_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    ipv6_address_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    ipv6_address_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    ipv6_address_list_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    ipv6_prefix_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    mac_address: str | core.StringOut = core.attr(str, computed=True)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    private_dns_name: str | core.StringOut = core.attr(str, computed=True)

    private_ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    private_ip_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    private_ip_list_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    private_ips: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    private_ips_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    source_dest_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    subnet_id: str | core.StringOut = core.attr(str)

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
        subnet_id: str | core.StringOut,
        attachment: list[Attachment] | core.ArrayOut[Attachment] | None = None,
        description: str | core.StringOut | None = None,
        interface_type: str | core.StringOut | None = None,
        ipv4_prefix_count: int | core.IntOut | None = None,
        ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ipv6_address_count: int | core.IntOut | None = None,
        ipv6_address_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ipv6_address_list_enabled: bool | core.BoolOut | None = None,
        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ipv6_prefix_count: int | core.IntOut | None = None,
        ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        private_ip: str | core.StringOut | None = None,
        private_ip_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        private_ip_list_enabled: bool | core.BoolOut | None = None,
        private_ips: list[str] | core.ArrayOut[core.StringOut] | None = None,
        private_ips_count: int | core.IntOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        source_dest_check: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkInterface.Args(
                subnet_id=subnet_id,
                attachment=attachment,
                description=description,
                interface_type=interface_type,
                ipv4_prefix_count=ipv4_prefix_count,
                ipv4_prefixes=ipv4_prefixes,
                ipv6_address_count=ipv6_address_count,
                ipv6_address_list=ipv6_address_list,
                ipv6_address_list_enabled=ipv6_address_list_enabled,
                ipv6_addresses=ipv6_addresses,
                ipv6_prefix_count=ipv6_prefix_count,
                ipv6_prefixes=ipv6_prefixes,
                private_ip=private_ip,
                private_ip_list=private_ip_list,
                private_ip_list_enabled=private_ip_list_enabled,
                private_ips=private_ips,
                private_ips_count=private_ips_count,
                security_groups=security_groups,
                source_dest_check=source_dest_check,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attachment: list[Attachment] | core.ArrayOut[Attachment] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        interface_type: str | core.StringOut | None = core.arg(default=None)

        ipv4_prefix_count: int | core.IntOut | None = core.arg(default=None)

        ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipv6_address_count: int | core.IntOut | None = core.arg(default=None)

        ipv6_address_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipv6_address_list_enabled: bool | core.BoolOut | None = core.arg(default=None)

        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipv6_prefix_count: int | core.IntOut | None = core.arg(default=None)

        ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        private_ip: str | core.StringOut | None = core.arg(default=None)

        private_ip_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        private_ip_list_enabled: bool | core.BoolOut | None = core.arg(default=None)

        private_ips: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        private_ips_count: int | core.IntOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        source_dest_check: bool | core.BoolOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
