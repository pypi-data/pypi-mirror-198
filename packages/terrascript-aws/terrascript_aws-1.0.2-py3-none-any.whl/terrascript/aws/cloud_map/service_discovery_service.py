import terrascript.core as core


@core.schema
class HealthCheckCustomConfig(core.Schema):

    failure_threshold: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        failure_threshold: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=HealthCheckCustomConfig.Args(
                failure_threshold=failure_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_threshold: int | core.IntOut | None = core.arg(default=None)


@core.schema
class HealthCheckConfig(core.Schema):

    failure_threshold: int | core.IntOut | None = core.attr(int, default=None)

    resource_path: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        failure_threshold: int | core.IntOut | None = None,
        resource_path: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
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
        failure_threshold: int | core.IntOut | None = core.arg(default=None)

        resource_path: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DnsRecords(core.Schema):

    ttl: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

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
        DnsRecords, kind=core.Kind.array
    )

    namespace_id: str | core.StringOut = core.attr(str)

    routing_policy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        dns_records: list[DnsRecords] | core.ArrayOut[DnsRecords],
        namespace_id: str | core.StringOut,
        routing_policy: str | core.StringOut | None = None,
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

        routing_policy: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_service_discovery_service", namespace="aws_cloud_map")
class ServiceDiscoveryService(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    dns_config: DnsConfig | None = core.attr(DnsConfig, default=None)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    health_check_config: HealthCheckConfig | None = core.attr(HealthCheckConfig, default=None)

    health_check_custom_config: HealthCheckCustomConfig | None = core.attr(
        HealthCheckCustomConfig, default=None
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    namespace_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        dns_config: DnsConfig | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        health_check_config: HealthCheckConfig | None = None,
        health_check_custom_config: HealthCheckCustomConfig | None = None,
        namespace_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceDiscoveryService.Args(
                name=name,
                description=description,
                dns_config=dns_config,
                force_destroy=force_destroy,
                health_check_config=health_check_config,
                health_check_custom_config=health_check_custom_config,
                namespace_id=namespace_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        dns_config: DnsConfig | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        health_check_config: HealthCheckConfig | None = core.arg(default=None)

        health_check_custom_config: HealthCheckCustomConfig | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        namespace_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
