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


@core.schema
class DnsEntry(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        hosted_zone_id: str | core.StringOut,
    ):
        super().__init__(
            args=DnsEntry.Args(
                dns_name=dns_name,
                hosted_zone_id=hosted_zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        hosted_zone_id: str | core.StringOut = core.arg()


@core.schema
class DnsOptions(core.Schema):

    dns_record_ip_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_record_ip_type: str | core.StringOut,
    ):
        super().__init__(
            args=DnsOptions.Args(
                dns_record_ip_type=dns_record_ip_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_record_ip_type: str | core.StringOut = core.arg()


@core.data(type="aws_vpc_endpoint", namespace="vpc")
class DsEndpoint(core.Data):
    """
    The Amazon Resource Name (ARN) of the VPC endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.
    """
    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are d
    ocumented below.
    """
    dns_entry: list[DnsEntry] | core.ArrayOut[DnsEntry] = core.attr(
        DnsEntry, computed=True, kind=core.Kind.array
    )

    dns_options: list[DnsOptions] | core.ArrayOut[DnsOptions] = core.attr(
        DnsOptions, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Custom filter block as described below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The ID of the specific VPC Endpoint to retrieve.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ip_address_type: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.
    """
    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The ID of the AWS account that owns the VPC endpoint.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The policy document associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
    """
    policy: str | core.StringOut = core.attr(str, computed=True)

    """
    The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
    """
    prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether or not the VPC is associated with a private hosted zone - `true` or `false`. Applicable for
    endpoints of type `Interface`.
    """
    private_dns_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether or not the VPC Endpoint is being managed by its service - `true` or `false`.
    """
    requester_managed: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    One or more route tables associated with the VPC Endpoint. Applicable for endpoints of type `Gateway
    .
    """
    route_table_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    One or more security groups associated with the network interfaces. Applicable for endpoints of type
    Interface`.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The service name of the specific VPC Endpoint to retrieve. For AWS services the service n
    ame is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service is an
    exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
    """
    service_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The state of the specific VPC Endpoint to retrieve.
    """
    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    One or more subnets in which the VPC Endpoint is located. Applicable for endpoints of type `Interfac
    e`.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A map of tags, each pair of which must exactly match
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The VPC Endpoint type, `Gateway` or `Interface`.
    """
    vpc_endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the VPC in which the specific VPC Endpoint is used.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        service_name: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpoint.Args(
                filter=filter,
                id=id,
                service_name=service_name,
                state=state,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        service_name: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
