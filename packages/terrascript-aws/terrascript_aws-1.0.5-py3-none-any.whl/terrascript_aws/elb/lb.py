import terrascript.core as core


@core.schema
class AccessLogs(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AccessLogs.Args(
                bucket=bucket,
                enabled=enabled,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SubnetMapping(core.Schema):

    allocation_id: str | core.StringOut | None = core.attr(str, default=None)

    ipv6_address: str | core.StringOut | None = core.attr(str, default=None)

    outpost_id: str | core.StringOut = core.attr(str, computed=True)

    private_ipv4_address: str | core.StringOut | None = core.attr(str, default=None)

    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        outpost_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
        allocation_id: str | core.StringOut | None = None,
        ipv6_address: str | core.StringOut | None = None,
        private_ipv4_address: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SubnetMapping.Args(
                outpost_id=outpost_id,
                subnet_id=subnet_id,
                allocation_id=allocation_id,
                ipv6_address=ipv6_address,
                private_ipv4_address=private_ipv4_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_id: str | core.StringOut | None = core.arg(default=None)

        ipv6_address: str | core.StringOut | None = core.arg(default=None)

        outpost_id: str | core.StringOut = core.arg()

        private_ipv4_address: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut = core.arg()


@core.resource(type="aws_lb", namespace="elb")
class Lb(core.Resource):
    """
    (Optional) An Access Logs block. Access Logs documented below.
    """

    access_logs: AccessLogs | None = core.attr(AccessLogs, default=None)

    """
    The ARN of the load balancer (matches `id`).
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN suffix for use with CloudWatch Metrics.
    """
    arn_suffix: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the customer owned ipv4 pool to use for this load balancer.
    """
    customer_owned_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Determines how the load balancer handles requests that might pose a security risk to an a
    pplication due to HTTP desync. Valid values are `monitor`, `defensive` (default), `strictest`.
    """
    desync_mitigation_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    The DNS name of the load balancer.
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether HTTP headers with header fields that are not valid are removed by the l
    oad balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requi
    res that message header names contain only alphanumeric characters and hyphens. Only valid for Load
    Balancers of type `application`.
    """
    drop_invalid_header_fields: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If true, cross-zone load balancing of the load balancer will be enabled.
    """
    enable_cross_zone_load_balancing: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If true, deletion of the load balancer will be disabled via
    """
    enable_deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
    """
    enable_http2: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Indicates whether to allow a WAF-enabled load balancer to route requests to targets if it
    is unable to forward the request to AWS WAF. Defaults to `false`.
    """
    enable_waf_fail_open: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The ARN of the load balancer (matches `arn`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The time in seconds that the connection is allowed to be idle. Only valid for Load Balanc
    ers of type `application`. Default: 60.
    """
    idle_timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) If true, the LB will be internal.
    """
    internal: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) The type of IP addresses used by the subnets for your load balancer. The possible values
    are `ipv4` and `dualstack`
    """
    ip_address_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The type of load balancer to create. Possible values are `application`, `gateway`, or `ne
    twork`. The default value is `application`.
    """
    load_balancer_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the LB. This name must be unique within your AWS account, can have a maximum
    of 32 characters,
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether the Application Load Balancer should preserve the Host header in the HT
    TP request and send it to the target without any change. Defaults to `false`.
    """
    preserve_host_header: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `
    application`.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A subnet mapping block as documented below.
    """
    subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] | None = core.attr(
        SubnetMapping, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A list of subnet IDs to attach to the LB. Subnets
    """
    subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
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

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).
    """
    zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        access_logs: AccessLogs | None = None,
        customer_owned_ipv4_pool: str | core.StringOut | None = None,
        desync_mitigation_mode: str | core.StringOut | None = None,
        drop_invalid_header_fields: bool | core.BoolOut | None = None,
        enable_cross_zone_load_balancing: bool | core.BoolOut | None = None,
        enable_deletion_protection: bool | core.BoolOut | None = None,
        enable_http2: bool | core.BoolOut | None = None,
        enable_waf_fail_open: bool | core.BoolOut | None = None,
        idle_timeout: int | core.IntOut | None = None,
        internal: bool | core.BoolOut | None = None,
        ip_address_type: str | core.StringOut | None = None,
        load_balancer_type: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        preserve_host_header: bool | core.BoolOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] | None = None,
        subnets: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Lb.Args(
                access_logs=access_logs,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                desync_mitigation_mode=desync_mitigation_mode,
                drop_invalid_header_fields=drop_invalid_header_fields,
                enable_cross_zone_load_balancing=enable_cross_zone_load_balancing,
                enable_deletion_protection=enable_deletion_protection,
                enable_http2=enable_http2,
                enable_waf_fail_open=enable_waf_fail_open,
                idle_timeout=idle_timeout,
                internal=internal,
                ip_address_type=ip_address_type,
                load_balancer_type=load_balancer_type,
                name=name,
                name_prefix=name_prefix,
                preserve_host_header=preserve_host_header,
                security_groups=security_groups,
                subnet_mapping=subnet_mapping,
                subnets=subnets,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_logs: AccessLogs | None = core.arg(default=None)

        customer_owned_ipv4_pool: str | core.StringOut | None = core.arg(default=None)

        desync_mitigation_mode: str | core.StringOut | None = core.arg(default=None)

        drop_invalid_header_fields: bool | core.BoolOut | None = core.arg(default=None)

        enable_cross_zone_load_balancing: bool | core.BoolOut | None = core.arg(default=None)

        enable_deletion_protection: bool | core.BoolOut | None = core.arg(default=None)

        enable_http2: bool | core.BoolOut | None = core.arg(default=None)

        enable_waf_fail_open: bool | core.BoolOut | None = core.arg(default=None)

        idle_timeout: int | core.IntOut | None = core.arg(default=None)

        internal: bool | core.BoolOut | None = core.arg(default=None)

        ip_address_type: str | core.StringOut | None = core.arg(default=None)

        load_balancer_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        preserve_host_header: bool | core.BoolOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] | None = core.arg(
            default=None
        )

        subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
