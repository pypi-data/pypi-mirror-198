import terrascript.core as core


@core.data(type="aws_msk_cluster", namespace="aws_managed_streaming_for_kafka")
class DsMskCluster(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bootstrap_brokers: str | core.StringOut = core.attr(str, computed=True)

    bootstrap_brokers_public_sasl_iam: str | core.StringOut = core.attr(str, computed=True)

    bootstrap_brokers_public_sasl_scram: str | core.StringOut = core.attr(str, computed=True)

    bootstrap_brokers_public_tls: str | core.StringOut = core.attr(str, computed=True)

    bootstrap_brokers_sasl_iam: str | core.StringOut = core.attr(str, computed=True)

    bootstrap_brokers_sasl_scram: str | core.StringOut = core.attr(str, computed=True)

    bootstrap_brokers_tls: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    kafka_version: str | core.StringOut = core.attr(str, computed=True)

    number_of_broker_nodes: int | core.IntOut = core.attr(int, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    zookeeper_connect_string: str | core.StringOut = core.attr(str, computed=True)

    zookeeper_connect_string_tls: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMskCluster.Args(
                cluster_name=cluster_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
