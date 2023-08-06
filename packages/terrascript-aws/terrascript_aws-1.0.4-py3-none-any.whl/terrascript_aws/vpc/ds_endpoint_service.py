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


@core.data(type="aws_vpc_endpoint_service", namespace="vpc")
class DsEndpointService(core.Data):
    """
    Whether or not VPC endpoint connection requests to the service must be accepted by the service owner
    true` or `false`.
    """

    acceptance_required: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The Amazon Resource Name (ARN) of the VPC endpoint service.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Availability Zones in which the service is available.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The DNS names for the service.
    """
    base_endpoint_dns_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether or not the service manages its VPC endpoints - `true` or `false`.
    """
    manages_vpc_endpoints: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The AWS account ID of the service owner or `amazon`.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    The private DNS name for the service.
    """
    private_dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The common name of an AWS service (e.g., `s3`).
    """
    service: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the endpoint service.
    """
    service_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The service name that is specified when creating a VPC endpoint. For AWS services the ser
    vice name is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service
    is an exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
    """
    service_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The service type, `Gateway` or `Interface`.
    """
    service_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The supported IP address types.
    """
    supported_ip_address_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A map of tags, each pair of which must exactly match a pair on the desired VPC Endpoint S
    ervice.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Whether or not the service supports endpoint policies - `true` or `false`.
    """
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
