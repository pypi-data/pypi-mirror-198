import terrascript.core as core


@core.schema
class PrivateDnsNameConfiguration(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        state: str | core.StringOut,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=PrivateDnsNameConfiguration.Args(
                name=name,
                state=state,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        state: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_vpc_endpoint_service", namespace="aws_vpc")
class EndpointService(core.Resource):

    acceptance_required: bool | core.BoolOut = core.attr(bool)

    allowed_principals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    base_endpoint_dns_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    gateway_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    manages_vpc_endpoints: bool | core.BoolOut = core.attr(bool, computed=True)

    network_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    private_dns_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    private_dns_name_configuration: list[PrivateDnsNameConfiguration] | core.ArrayOut[
        PrivateDnsNameConfiguration
    ] = core.attr(PrivateDnsNameConfiguration, computed=True, kind=core.Kind.array)

    service_name: str | core.StringOut = core.attr(str, computed=True)

    service_type: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    supported_ip_address_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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
        acceptance_required: bool | core.BoolOut,
        allowed_principals: list[str] | core.ArrayOut[core.StringOut] | None = None,
        gateway_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        network_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        private_dns_name: str | core.StringOut | None = None,
        supported_ip_address_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointService.Args(
                acceptance_required=acceptance_required,
                allowed_principals=allowed_principals,
                gateway_load_balancer_arns=gateway_load_balancer_arns,
                network_load_balancer_arns=network_load_balancer_arns,
                private_dns_name=private_dns_name,
                supported_ip_address_types=supported_ip_address_types,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acceptance_required: bool | core.BoolOut = core.arg()

        allowed_principals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        gateway_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        network_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        private_dns_name: str | core.StringOut | None = core.arg(default=None)

        supported_ip_address_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
