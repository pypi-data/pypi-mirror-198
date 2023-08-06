import terrascript.core as core


@core.schema
class VpcSettings(core.Schema):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str)

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


@core.schema
class ConnectSettings(core.Schema):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    connect_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    customer_dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    customer_username: str | core.StringOut = core.attr(str)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str)

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


@core.resource(type="aws_directory_service_directory", namespace="aws_ds")
class DirectoryServiceDirectory(core.Resource):

    access_url: str | core.StringOut = core.attr(str, computed=True)

    alias: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    connect_settings: ConnectSettings | None = core.attr(ConnectSettings, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    desired_number_of_domain_controllers: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    dns_ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    edition: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    enable_sso: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    password: str | core.StringOut = core.attr(str)

    security_group_id: str | core.StringOut = core.attr(str, computed=True)

    short_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    size: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    vpc_settings: VpcSettings | None = core.attr(VpcSettings, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        password: str | core.StringOut,
        alias: str | core.StringOut | None = None,
        connect_settings: ConnectSettings | None = None,
        description: str | core.StringOut | None = None,
        desired_number_of_domain_controllers: int | core.IntOut | None = None,
        edition: str | core.StringOut | None = None,
        enable_sso: bool | core.BoolOut | None = None,
        short_name: str | core.StringOut | None = None,
        size: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        vpc_settings: VpcSettings | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceDirectory.Args(
                name=name,
                password=password,
                alias=alias,
                connect_settings=connect_settings,
                description=description,
                desired_number_of_domain_controllers=desired_number_of_domain_controllers,
                edition=edition,
                enable_sso=enable_sso,
                short_name=short_name,
                size=size,
                tags=tags,
                tags_all=tags_all,
                type=type,
                vpc_settings=vpc_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alias: str | core.StringOut | None = core.arg(default=None)

        connect_settings: ConnectSettings | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        desired_number_of_domain_controllers: int | core.IntOut | None = core.arg(default=None)

        edition: str | core.StringOut | None = core.arg(default=None)

        enable_sso: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        password: str | core.StringOut = core.arg()

        short_name: str | core.StringOut | None = core.arg(default=None)

        size: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        vpc_settings: VpcSettings | None = core.arg(default=None)
