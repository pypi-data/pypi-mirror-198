import terrascript.core as core


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


@core.resource(type="aws_lb", namespace="aws_elb")
class Lb(core.Resource):

    access_logs: AccessLogs | None = core.attr(AccessLogs, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    arn_suffix: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ipv4_pool: str | core.StringOut | None = core.attr(str, default=None)

    desync_mitigation_mode: str | core.StringOut | None = core.attr(str, default=None)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    drop_invalid_header_fields: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_cross_zone_load_balancing: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_http2: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_waf_fail_open: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_timeout: int | core.IntOut | None = core.attr(int, default=None)

    internal: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    ip_address_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    load_balancer_type: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    preserve_host_header: bool | core.BoolOut | None = core.attr(bool, default=None)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] | None = core.attr(
        SubnetMapping, default=None, computed=True, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

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
