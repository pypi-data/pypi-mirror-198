import terrascript.core as core


@core.schema
class DnsOptions(core.Schema):

    dns_record_ip_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        dns_record_ip_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DnsOptions.Args(
                dns_record_ip_type=dns_record_ip_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_record_ip_type: str | core.StringOut | None = core.arg(default=None)


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


@core.resource(type="aws_vpc_endpoint", namespace="vpc")
class Endpoint(core.Resource):
    """
    The Amazon Resource Name (ARN) of the VPC endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account)
    .
    """
    auto_accept: bool | core.BoolOut | None = core.attr(bool, default=None)

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

    """
    (Optional) The DNS options for the endpoint. See dns_options below.
    """
    dns_options: DnsOptions | None = core.attr(DnsOptions, default=None, computed=True)

    """
    The ID of the VPC endpoint.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The IP address type for the endpoint. Valid values are `ipv4`, `dualstack`, and `ipv6`.
    """
    ip_address_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
    (Optional) A policy to attach to the endpoint that controls access to the service. This is a JSON fo
    rmatted string. Defaults to full access. All `Gateway` and some `Interface` endpoints support polici
    es - see the [relevant AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpo
    ints-access.html) for more details. For more information about building AWS IAM policy documents wit
    h Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-p
    olicy).
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
    """
    prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional; AWS services and AWS Marketplace partner services only) Whether or not to associate a pri
    vate hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
    """
    private_dns_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Whether or not the VPC Endpoint is being managed by its service - `true` or `false`.
    """
    requester_managed: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) One or more route table IDs. Applicable for endpoints of type `Gateway`.
    """
    route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The ID of one or more security groups to associate with the network interface. Applicable
    for endpoints of type `Interface`.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) The service name. For AWS services the service name is usually in the form `com.amazonaws
    .<region>.<service>` (the SageMaker Notebook service is an exception to this rule, the service name
    is in the form `aws.sagemaker.<region>.notebook`).
    """
    service_name: str | core.StringOut = core.attr(str)

    """
    The state of the VPC endpoint.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of one or more subnets in which to create a network interface for the endpoint. Ap
    plicable for endpoints of type `GatewayLoadBalancer` and `Interface`.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
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

    """
    (Optional) The VPC endpoint type, `Gateway`, `GatewayLoadBalancer`, or `Interface`. Defaults to `Gat
    eway`.
    """
    vpc_endpoint_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the VPC in which the endpoint will be used.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        service_name: str | core.StringOut,
        vpc_id: str | core.StringOut,
        auto_accept: bool | core.BoolOut | None = None,
        dns_options: DnsOptions | None = None,
        ip_address_type: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        private_dns_enabled: bool | core.BoolOut | None = None,
        route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_endpoint_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                service_name=service_name,
                vpc_id=vpc_id,
                auto_accept=auto_accept,
                dns_options=dns_options,
                ip_address_type=ip_address_type,
                policy=policy,
                private_dns_enabled=private_dns_enabled,
                route_table_ids=route_table_ids,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                vpc_endpoint_type=vpc_endpoint_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_accept: bool | core.BoolOut | None = core.arg(default=None)

        dns_options: DnsOptions | None = core.arg(default=None)

        ip_address_type: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        private_dns_enabled: bool | core.BoolOut | None = core.arg(default=None)

        route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        service_name: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_endpoint_type: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
