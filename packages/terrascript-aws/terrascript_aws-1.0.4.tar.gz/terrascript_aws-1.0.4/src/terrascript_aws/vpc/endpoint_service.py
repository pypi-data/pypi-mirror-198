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


@core.resource(type="aws_vpc_endpoint_service", namespace="vpc")
class EndpointService(core.Resource):
    """
    (Required) Whether or not VPC endpoint connection requests to the service must be accepted by the se
    rvice owner - `true` or `false`.
    """

    acceptance_required: bool | core.BoolOut = core.attr(bool)

    """
    (Optional) The ARNs of one or more principals allowed to discover the endpoint service.
    """
    allowed_principals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The Amazon Resource Name (ARN) of the VPC endpoint service.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A set of Availability Zones in which the service is available.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A set of DNS names for the service.
    """
    base_endpoint_dns_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Amazon Resource Names (ARNs) of one or more Gateway Load Balancers for the endpoint servi
    ce.
    """
    gateway_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ID of the VPC endpoint service.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether or not the service manages its VPC endpoints - `true` or `false`.
    """
    manages_vpc_endpoints: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Amazon Resource Names (ARNs) of one or more Network Load Balancers for the endpoint servi
    ce.
    """
    network_load_balancer_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The private DNS name for the service.
    """
    private_dns_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    List of objects containing information about the endpoint service private DNS name configuration.
    """
    private_dns_name_configuration: list[PrivateDnsNameConfiguration] | core.ArrayOut[
        PrivateDnsNameConfiguration
    ] = core.attr(PrivateDnsNameConfiguration, computed=True, kind=core.Kind.array)

    """
    The service name.
    """
    service_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The service type, `Gateway` or `Interface`.
    """
    service_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the VPC endpoint service.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The supported IP address types. The possible values are `ipv4` and `ipv6`.
    """
    supported_ip_address_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
