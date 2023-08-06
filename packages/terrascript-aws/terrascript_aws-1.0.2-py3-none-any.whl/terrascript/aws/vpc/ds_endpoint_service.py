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


@core.data(type="aws_vpc_endpoint_service", namespace="aws_vpc")
class DsEndpointService(core.Data):

    acceptance_required: bool | core.BoolOut = core.attr(bool, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    base_endpoint_dns_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    manages_vpc_endpoints: bool | core.BoolOut = core.attr(bool, computed=True)

    owner: str | core.StringOut = core.attr(str, computed=True)

    private_dns_name: str | core.StringOut = core.attr(str, computed=True)

    service: str | core.StringOut | None = core.attr(str, default=None)

    service_id: str | core.StringOut = core.attr(str, computed=True)

    service_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    service_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    supported_ip_address_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_policy_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        service: str | core.StringOut | None = None,
        service_name: str | core.StringOut | None = None,
        service_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpointService.Args(
                filter=filter,
                service=service,
                service_name=service_name,
                service_type=service_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        service: str | core.StringOut | None = core.arg(default=None)

        service_name: str | core.StringOut | None = core.arg(default=None)

        service_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
