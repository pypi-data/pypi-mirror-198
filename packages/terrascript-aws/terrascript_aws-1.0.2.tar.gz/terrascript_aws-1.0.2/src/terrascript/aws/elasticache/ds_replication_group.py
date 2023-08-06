import terrascript.core as core


@core.schema
class LogDeliveryConfiguration(core.Schema):

    destination: str | core.StringOut = core.attr(str, computed=True)

    destination_type: str | core.StringOut = core.attr(str, computed=True)

    log_format: str | core.StringOut = core.attr(str, computed=True)

    log_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination: str | core.StringOut,
        destination_type: str | core.StringOut,
        log_format: str | core.StringOut,
        log_type: str | core.StringOut,
    ):
        super().__init__(
            args=LogDeliveryConfiguration.Args(
                destination=destination,
                destination_type=destination_type,
                log_format=log_format,
                log_type=log_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: str | core.StringOut = core.arg()

        destination_type: str | core.StringOut = core.arg()

        log_format: str | core.StringOut = core.arg()

        log_type: str | core.StringOut = core.arg()


@core.data(type="aws_elasticache_replication_group", namespace="aws_elasticache")
class DsReplicationGroup(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auth_token_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    automatic_failover_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    configuration_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
        LogDeliveryConfiguration
    ] = core.attr(LogDeliveryConfiguration, computed=True, kind=core.Kind.array)

    member_clusters: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    multi_az_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    node_type: str | core.StringOut = core.attr(str, computed=True)

    num_cache_clusters: int | core.IntOut = core.attr(int, computed=True)

    num_node_groups: int | core.IntOut = core.attr(int, computed=True)

    number_cache_clusters: int | core.IntOut = core.attr(int, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    primary_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    reader_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    replicas_per_node_group: int | core.IntOut = core.attr(int, computed=True)

    replication_group_description: str | core.StringOut = core.attr(str, computed=True)

    replication_group_id: str | core.StringOut = core.attr(str)

    snapshot_retention_limit: int | core.IntOut = core.attr(int, computed=True)

    snapshot_window: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        replication_group_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsReplicationGroup.Args(
                replication_group_id=replication_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replication_group_id: str | core.StringOut = core.arg()
