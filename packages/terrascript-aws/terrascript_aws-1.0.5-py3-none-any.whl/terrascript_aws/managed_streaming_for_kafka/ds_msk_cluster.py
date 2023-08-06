import terrascript.core as core


@core.data(type="aws_msk_cluster", namespace="managed_streaming_for_kafka")
class DsMskCluster(core.Data):
    """
    Amazon Resource Name (ARN) of the MSK cluster.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Comma separated list of one or more hostname:port pairs of kafka brokers suitable to bootstrap conne
    ctivity to the kafka cluster. Contains a value if `encryption_info.0.encryption_in_transit.0.client_
    broker` is set to `PLAINTEXT` or `TLS_PLAINTEXT`. The resource sorts values alphabetically. AWS may
    not always return all endpoints so this value is not guaranteed to be stable across applies.
    """
    bootstrap_brokers: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more DNS names (or IP addresses) and SASL IAM port pairs. For example, `b-1-public.exampleClu
    sterName.abcde.c2.kafka.us-east-1.amazonaws.com:9198,b-2-public.exampleClusterName.abcde.c2.kafka.us
    east-1.amazonaws.com:9198,b-3-public.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9198
    . This attribute will have a value if `encryption_info.0.encryption_in_transit.0.client_broker` is
    set to `TLS_PLAINTEXT` or `TLS` and `client_authentication.0.sasl.0.iam` is set to `true` and `broke
    r_node_group_info.0.connectivity_info.0.public_access.0.type` is set to `SERVICE_PROVIDED_EIPS` and
    the cluster fulfill all other requirements for public access. The resource sorts the list alphabetic
    ally. AWS may not always return all endpoints so the values may not be stable across applies.
    """
    bootstrap_brokers_public_sasl_iam: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more DNS names (or IP addresses) and SASL SCRAM port pairs. For example, `b-1-public.exampleC
    lusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9196,b-2-public.exampleClusterName.abcde.c2.kafka.
    us-east-1.amazonaws.com:9196,b-3-public.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:91
    96`. This attribute will have a value if `encryption_info.0.encryption_in_transit.0.client_broker` i
    s set to `TLS_PLAINTEXT` or `TLS` and `client_authentication.0.sasl.0.scram` is set to `true` and `b
    roker_node_group_info.0.connectivity_info.0.public_access.0.type` is set to `SERVICE_PROVIDED_EIPS`
    and the cluster fulfill all other requirements for public access. The resource sorts the list alphab
    etically. AWS may not always return all endpoints so the values may not be stable across applies.
    """
    bootstrap_brokers_public_sasl_scram: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more DNS names (or IP addresses) and TLS port pairs. For example, `b-1-public.exampleClusterN
    ame.abcde.c2.kafka.us-east-1.amazonaws.com:9194,b-2-public.exampleClusterName.abcde.c2.kafka.us-east
    1.amazonaws.com:9194,b-3-public.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9194`. Th
    is attribute will have a value if `encryption_info.0.encryption_in_transit.0.client_broker` is set t
    o `TLS_PLAINTEXT` or `TLS` and `broker_node_group_info.0.connectivity_info.0.public_access.0.type` i
    s set to `SERVICE_PROVIDED_EIPS` and the cluster fulfill all other requirements for public access. T
    he resource sorts the list alphabetically. AWS may not always return all endpoints so the values may
    not be stable across applies.
    """
    bootstrap_brokers_public_tls: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more DNS names (or IP addresses) and SASL IAM port pairs. For example, `b-1.exampleClusterNam
    e.abcde.c2.kafka.us-east-1.amazonaws.com:9098,b-2.exampleClusterName.abcde.c2.kafka.us-east-1.amazon
    aws.com:9098,b-3.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9098`. This attribute wil
    l have a value if `encryption_info.0.encryption_in_transit.0.client_broker` is set to `TLS_PLAINTEXT
    or `TLS` and `client_authentication.0.sasl.0.iam` is set to `true`. The resource sorts the list al
    phabetically. AWS may not always return all endpoints so the values may not be stable across applies
    .
    """
    bootstrap_brokers_sasl_iam: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more DNS names (or IP addresses) and SASL SCRAM port pairs. For example, `b-1.exampleClusterN
    ame.abcde.c2.kafka.us-east-1.amazonaws.com:9096,b-2.exampleClusterName.abcde.c2.kafka.us-east-1.amaz
    onaws.com:9096,b-3.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9096`. This attribute w
    ill have a value if `encryption_info.0.encryption_in_transit.0.client_broker` is set to `TLS_PLAINTE
    XT` or `TLS` and `client_authentication.0.sasl.0.scram` is set to `true`. The resource sorts the lis
    t alphabetically. AWS may not always return all endpoints so the values may not be stable across app
    lies.
    """
    bootstrap_brokers_sasl_scram: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more DNS names (or IP addresses) and TLS port pairs. For example, `b-1.exampleClusterName.abc
    de.c2.kafka.us-east-1.amazonaws.com:9094,b-2.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.c
    om:9094,b-3.exampleClusterName.abcde.c2.kafka.us-east-1.amazonaws.com:9094`. This attribute will hav
    e a value if `encryption_info.0.encryption_in_transit.0.client_broker` is set to `TLS_PLAINTEXT` or
    TLS`. The resource sorts the list alphabetically. AWS may not always return all endpoints so the va
    lues may not be stable across applies.
    """
    bootstrap_brokers_tls: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the cluster.
    """
    cluster_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Apache Kafka version.
    """
    kafka_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Number of broker nodes in the cluster.
    """
    number_of_broker_nodes: int | core.IntOut = core.attr(int, computed=True)

    """
    Map of key-value pairs assigned to the cluster.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper
    cluster. The returned values are sorted alphbetically. The AWS API may not return all endpoints, so
    this value is not guaranteed to be stable across applies.
    """
    zookeeper_connect_string: str | core.StringOut = core.attr(str, computed=True)

    """
    A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper
    cluster via TLS. The returned values are sorted alphabetically. The AWS API may not return all endpo
    ints, so this value is not guaranteed to be stable across applies.
    """
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
