import terrascript.core as core


@core.schema
class AccessLogs(core.Schema):

    bucket: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    prefix: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        enabled: bool | core.BoolOut,
        prefix: str | core.StringOut,
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

        enabled: bool | core.BoolOut = core.arg()

        prefix: str | core.StringOut = core.arg()


@core.schema
class SubnetMapping(core.Schema):

    allocation_id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_address: str | core.StringOut = core.attr(str, computed=True)

    outpost_id: str | core.StringOut = core.attr(str, computed=True)

    private_ipv4_address: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        allocation_id: str | core.StringOut,
        ipv6_address: str | core.StringOut,
        outpost_id: str | core.StringOut,
        private_ipv4_address: str | core.StringOut,
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=SubnetMapping.Args(
                allocation_id=allocation_id,
                ipv6_address=ipv6_address,
                outpost_id=outpost_id,
                private_ipv4_address=private_ipv4_address,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_id: str | core.StringOut = core.arg()

        ipv6_address: str | core.StringOut = core.arg()

        outpost_id: str | core.StringOut = core.arg()

        private_ipv4_address: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.data(type="aws_lb", namespace="elb")
class DsLb(core.Data):

    access_logs: list[AccessLogs] | core.ArrayOut[AccessLogs] = core.attr(
        AccessLogs, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The full ARN of the load balancer.
    """
    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn_suffix: str | core.StringOut = core.attr(str, computed=True)

    customer_owned_ipv4_pool: str | core.StringOut = core.attr(str, computed=True)

    desync_mitigation_mode: str | core.StringOut = core.attr(str, computed=True)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    drop_invalid_header_fields: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_deletion_protection: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_http2: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_waf_fail_open: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_timeout: int | core.IntOut = core.attr(int, computed=True)

    internal: bool | core.BoolOut = core.attr(bool, computed=True)

    ip_address_type: str | core.StringOut = core.attr(str, computed=True)

    load_balancer_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The unique name of the load balancer.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    preserve_host_header: bool | core.BoolOut = core.attr(bool, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] = core.attr(
        SubnetMapping, computed=True, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A mapping of tags, each pair of which must exactly match a pair on the desired load balan
    cer.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLb.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
