import terrascript.core as core


@core.schema
class ConnectSettings(core.Schema):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    connect_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    customer_dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    customer_username: str | core.StringOut = core.attr(str, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: list[str] | core.ArrayOut[core.StringOut],
        connect_ips: list[str] | core.ArrayOut[core.StringOut],
        customer_dns_ips: list[str] | core.ArrayOut[core.StringOut],
        customer_username: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectSettings.Args(
                availability_zones=availability_zones,
                connect_ips=connect_ips,
                customer_dns_ips=customer_dns_ips,
                customer_username=customer_username,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        connect_ips: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        customer_dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        customer_username: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class RadiusSettings(core.Schema):

    authentication_protocol: str | core.StringOut = core.attr(str, computed=True)

    display_label: str | core.StringOut = core.attr(str, computed=True)

    radius_port: int | core.IntOut = core.attr(int, computed=True)

    radius_retries: int | core.IntOut = core.attr(int, computed=True)

    radius_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    radius_timeout: int | core.IntOut = core.attr(int, computed=True)

    use_same_username: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        authentication_protocol: str | core.StringOut,
        display_label: str | core.StringOut,
        radius_port: int | core.IntOut,
        radius_retries: int | core.IntOut,
        radius_servers: list[str] | core.ArrayOut[core.StringOut],
        radius_timeout: int | core.IntOut,
        use_same_username: bool | core.BoolOut,
    ):
        super().__init__(
            args=RadiusSettings.Args(
                authentication_protocol=authentication_protocol,
                display_label=display_label,
                radius_port=radius_port,
                radius_retries=radius_retries,
                radius_servers=radius_servers,
                radius_timeout=radius_timeout,
                use_same_username=use_same_username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_protocol: str | core.StringOut = core.arg()

        display_label: str | core.StringOut = core.arg()

        radius_port: int | core.IntOut = core.arg()

        radius_retries: int | core.IntOut = core.arg()

        radius_servers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        radius_timeout: int | core.IntOut = core.arg()

        use_same_username: bool | core.BoolOut = core.arg()


@core.schema
class VpcSettings(core.Schema):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: list[str] | core.ArrayOut[core.StringOut],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcSettings.Args(
                availability_zones=availability_zones,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.data(type="aws_directory_service_directory", namespace="aws_ds")
class DsDirectoryServiceDirectory(core.Data):

    access_url: str | core.StringOut = core.attr(str, computed=True)

    alias: str | core.StringOut = core.attr(str, computed=True)

    connect_settings: list[ConnectSettings] | core.ArrayOut[ConnectSettings] = core.attr(
        ConnectSettings, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    directory_id: str | core.StringOut = core.attr(str)

    dns_ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    edition: str | core.StringOut = core.attr(str, computed=True)

    enable_sso: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    radius_settings: list[RadiusSettings] | core.ArrayOut[RadiusSettings] = core.attr(
        RadiusSettings, computed=True, kind=core.Kind.array
    )

    security_group_id: str | core.StringOut = core.attr(str, computed=True)

    short_name: str | core.StringOut = core.attr(str, computed=True)

    size: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    vpc_settings: list[VpcSettings] | core.ArrayOut[VpcSettings] = core.attr(
        VpcSettings, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        directory_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDirectoryServiceDirectory.Args(
                directory_id=directory_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
