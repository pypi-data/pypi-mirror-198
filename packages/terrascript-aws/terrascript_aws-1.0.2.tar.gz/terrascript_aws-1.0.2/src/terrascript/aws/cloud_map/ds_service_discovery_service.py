import terrascript.core as core


@core.schema
class DnsRecords(core.Schema):

    ttl: int | core.IntOut = core.attr(int, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ttl: int | core.IntOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=DnsRecords.Args(
                ttl=ttl,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ttl: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class DnsConfig(core.Schema):

    dns_records: list[DnsRecords] | core.ArrayOut[DnsRecords] = core.attr(
        DnsRecords, computed=True, kind=core.Kind.array
    )

    namespace_id: str | core.StringOut = core.attr(str, computed=True)

    routing_policy: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_records: list[DnsRecords] | core.ArrayOut[DnsRecords],
        namespace_id: str | core.StringOut,
        routing_policy: str | core.StringOut,
    ):
        super().__init__(
            args=DnsConfig.Args(
                dns_records=dns_records,
                namespace_id=namespace_id,
                routing_policy=routing_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_records: list[DnsRecords] | core.ArrayOut[DnsRecords] = core.arg()

        namespace_id: str | core.StringOut = core.arg()

        routing_policy: str | core.StringOut = core.arg()


@core.schema
class HealthCheckCustomConfig(core.Schema):

    failure_threshold: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        failure_threshold: int | core.IntOut,
    ):
        super().__init__(
            args=HealthCheckCustomConfig.Args(
                failure_threshold=failure_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_threshold: int | core.IntOut = core.arg()


@core.schema
class HealthCheckConfig(core.Schema):

    failure_threshold: int | core.IntOut = core.attr(int, computed=True)

    resource_path: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        failure_threshold: int | core.IntOut,
        resource_path: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=HealthCheckConfig.Args(
                failure_threshold=failure_threshold,
                resource_path=resource_path,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_threshold: int | core.IntOut = core.arg()

        resource_path: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.data(type="aws_service_discovery_service", namespace="aws_cloud_map")
class DsServiceDiscoveryService(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    dns_config: list[DnsConfig] | core.ArrayOut[DnsConfig] = core.attr(
        DnsConfig, computed=True, kind=core.Kind.array
    )

    health_check_config: list[HealthCheckConfig] | core.ArrayOut[HealthCheckConfig] = core.attr(
        HealthCheckConfig, computed=True, kind=core.Kind.array
    )

    health_check_custom_config: list[HealthCheckCustomConfig] | core.ArrayOut[
        HealthCheckCustomConfig
    ] = core.attr(HealthCheckCustomConfig, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    namespace_id: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        namespace_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServiceDiscoveryService.Args(
                name=name,
                namespace_id=namespace_id,
                tags=tags,
                tags_all=tags_all,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        namespace_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
