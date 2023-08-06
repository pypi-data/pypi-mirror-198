import terrascript.core as core


@core.schema
class JmxExporter(core.Schema):

    enabled_in_broker: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled_in_broker: bool | core.BoolOut,
    ):
        super().__init__(
            args=JmxExporter.Args(
                enabled_in_broker=enabled_in_broker,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled_in_broker: bool | core.BoolOut = core.arg()


@core.schema
class NodeExporter(core.Schema):

    enabled_in_broker: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled_in_broker: bool | core.BoolOut,
    ):
        super().__init__(
            args=NodeExporter.Args(
                enabled_in_broker=enabled_in_broker,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled_in_broker: bool | core.BoolOut = core.arg()


@core.schema
class Prometheus(core.Schema):

    jmx_exporter: JmxExporter | None = core.attr(JmxExporter, default=None)

    node_exporter: NodeExporter | None = core.attr(NodeExporter, default=None)

    def __init__(
        self,
        *,
        jmx_exporter: JmxExporter | None = None,
        node_exporter: NodeExporter | None = None,
    ):
        super().__init__(
            args=Prometheus.Args(
                jmx_exporter=jmx_exporter,
                node_exporter=node_exporter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        jmx_exporter: JmxExporter | None = core.arg(default=None)

        node_exporter: NodeExporter | None = core.arg(default=None)


@core.schema
class OpenMonitoring(core.Schema):

    prometheus: Prometheus = core.attr(Prometheus)

    def __init__(
        self,
        *,
        prometheus: Prometheus,
    ):
        super().__init__(
            args=OpenMonitoring.Args(
                prometheus=prometheus,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prometheus: Prometheus = core.arg()


@core.schema
class CloudwatchLogs(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    log_group: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        log_group: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CloudwatchLogs.Args(
                enabled=enabled,
                log_group=log_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        log_group: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Firehose(core.Schema):

    delivery_stream: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        delivery_stream: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Firehose.Args(
                enabled=enabled,
                delivery_stream=delivery_stream,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delivery_stream: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut = core.arg()


@core.schema
class S3(core.Schema):

    bucket: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut = core.attr(bool)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        bucket: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3.Args(
                enabled=enabled,
                bucket=bucket,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut = core.arg()

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class BrokerLogs(core.Schema):

    cloudwatch_logs: CloudwatchLogs | None = core.attr(CloudwatchLogs, default=None)

    firehose: Firehose | None = core.attr(Firehose, default=None)

    s3: S3 | None = core.attr(S3, default=None)

    def __init__(
        self,
        *,
        cloudwatch_logs: CloudwatchLogs | None = None,
        firehose: Firehose | None = None,
        s3: S3 | None = None,
    ):
        super().__init__(
            args=BrokerLogs.Args(
                cloudwatch_logs=cloudwatch_logs,
                firehose=firehose,
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logs: CloudwatchLogs | None = core.arg(default=None)

        firehose: Firehose | None = core.arg(default=None)

        s3: S3 | None = core.arg(default=None)


@core.schema
class LoggingInfo(core.Schema):

    broker_logs: BrokerLogs = core.attr(BrokerLogs)

    def __init__(
        self,
        *,
        broker_logs: BrokerLogs,
    ):
        super().__init__(
            args=LoggingInfo.Args(
                broker_logs=broker_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        broker_logs: BrokerLogs = core.arg()


@core.schema
class ConfigurationInfo(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    revision: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        revision: int | core.IntOut,
    ):
        super().__init__(
            args=ConfigurationInfo.Args(
                arn=arn,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        revision: int | core.IntOut = core.arg()


@core.schema
class EncryptionInTransit(core.Schema):

    client_broker: str | core.StringOut | None = core.attr(str, default=None)

    in_cluster: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        client_broker: str | core.StringOut | None = None,
        in_cluster: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=EncryptionInTransit.Args(
                client_broker=client_broker,
                in_cluster=in_cluster,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_broker: str | core.StringOut | None = core.arg(default=None)

        in_cluster: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class EncryptionInfo(core.Schema):

    encryption_at_rest_kms_key_arn: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    encryption_in_transit: EncryptionInTransit | None = core.attr(EncryptionInTransit, default=None)

    def __init__(
        self,
        *,
        encryption_at_rest_kms_key_arn: str | core.StringOut | None = None,
        encryption_in_transit: EncryptionInTransit | None = None,
    ):
        super().__init__(
            args=EncryptionInfo.Args(
                encryption_at_rest_kms_key_arn=encryption_at_rest_kms_key_arn,
                encryption_in_transit=encryption_in_transit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_at_rest_kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        encryption_in_transit: EncryptionInTransit | None = core.arg(default=None)


@core.schema
class ProvisionedThroughput(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    volume_throughput: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        volume_throughput: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ProvisionedThroughput.Args(
                enabled=enabled,
                volume_throughput=volume_throughput,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        volume_throughput: int | core.IntOut | None = core.arg(default=None)


@core.schema
class EbsStorageInfo(core.Schema):

    provisioned_throughput: ProvisionedThroughput | None = core.attr(
        ProvisionedThroughput, default=None
    )

    volume_size: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        provisioned_throughput: ProvisionedThroughput | None = None,
        volume_size: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EbsStorageInfo.Args(
                provisioned_throughput=provisioned_throughput,
                volume_size=volume_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provisioned_throughput: ProvisionedThroughput | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)


@core.schema
class StorageInfo(core.Schema):

    ebs_storage_info: EbsStorageInfo | None = core.attr(EbsStorageInfo, default=None)

    def __init__(
        self,
        *,
        ebs_storage_info: EbsStorageInfo | None = None,
    ):
        super().__init__(
            args=StorageInfo.Args(
                ebs_storage_info=ebs_storage_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ebs_storage_info: EbsStorageInfo | None = core.arg(default=None)


@core.schema
class PublicAccess(core.Schema):

    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PublicAccess.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ConnectivityInfo(core.Schema):

    public_access: PublicAccess | None = core.attr(PublicAccess, default=None, computed=True)

    def __init__(
        self,
        *,
        public_access: PublicAccess | None = None,
    ):
        super().__init__(
            args=ConnectivityInfo.Args(
                public_access=public_access,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        public_access: PublicAccess | None = core.arg(default=None)


@core.schema
class BrokerNodeGroupInfo(core.Schema):

    az_distribution: str | core.StringOut | None = core.attr(str, default=None)

    client_subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    connectivity_info: ConnectivityInfo | None = core.attr(
        ConnectivityInfo, default=None, computed=True
    )

    ebs_volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    instance_type: str | core.StringOut = core.attr(str)

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    storage_info: StorageInfo | None = core.attr(StorageInfo, default=None, computed=True)

    def __init__(
        self,
        *,
        client_subnets: list[str] | core.ArrayOut[core.StringOut],
        instance_type: str | core.StringOut,
        security_groups: list[str] | core.ArrayOut[core.StringOut],
        az_distribution: str | core.StringOut | None = None,
        connectivity_info: ConnectivityInfo | None = None,
        ebs_volume_size: int | core.IntOut | None = None,
        storage_info: StorageInfo | None = None,
    ):
        super().__init__(
            args=BrokerNodeGroupInfo.Args(
                client_subnets=client_subnets,
                instance_type=instance_type,
                security_groups=security_groups,
                az_distribution=az_distribution,
                connectivity_info=connectivity_info,
                ebs_volume_size=ebs_volume_size,
                storage_info=storage_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        az_distribution: str | core.StringOut | None = core.arg(default=None)

        client_subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        connectivity_info: ConnectivityInfo | None = core.arg(default=None)

        ebs_volume_size: int | core.IntOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        security_groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        storage_info: StorageInfo | None = core.arg(default=None)


@core.schema
class Sasl(core.Schema):

    iam: bool | core.BoolOut | None = core.attr(bool, default=None)

    scram: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        iam: bool | core.BoolOut | None = None,
        scram: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Sasl.Args(
                iam=iam,
                scram=scram,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam: bool | core.BoolOut | None = core.arg(default=None)

        scram: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Tls(core.Schema):

    certificate_authority_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        certificate_authority_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Tls.Args(
                certificate_authority_arns=certificate_authority_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_authority_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class ClientAuthentication(core.Schema):

    sasl: Sasl | None = core.attr(Sasl, default=None)

    tls: Tls | None = core.attr(Tls, default=None)

    unauthenticated: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        sasl: Sasl | None = None,
        tls: Tls | None = None,
        unauthenticated: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ClientAuthentication.Args(
                sasl=sasl,
                tls=tls,
                unauthenticated=unauthenticated,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sasl: Sasl | None = core.arg(default=None)

        tls: Tls | None = core.arg(default=None)

        unauthenticated: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_msk_cluster", namespace="managed_streaming_for_kafka")
class MskCluster(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
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
    (Required) Configuration block for the broker nodes of the Kafka cluster.
    """
    broker_node_group_info: BrokerNodeGroupInfo = core.attr(BrokerNodeGroupInfo)

    """
    (Optional) Configuration block for specifying a client authentication. See below.
    """
    client_authentication: ClientAuthentication | None = core.attr(
        ClientAuthentication, default=None
    )

    """
    (Required) Name of the MSK cluster.
    """
    cluster_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See be
    low.
    """
    configuration_info: ConfigurationInfo | None = core.attr(ConfigurationInfo, default=None)

    """
    Current version of the MSK Cluster used for updates, e.g., `K13V1IB3VIYZZH`
    """
    current_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for specifying encryption. See below.
    """
    encryption_info: EncryptionInfo | None = core.attr(EncryptionInfo, default=None)

    """
    (Optional) Specify the desired enhanced MSK CloudWatch monitoring level. See [Monitoring Amazon MSK
    with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
    """
    enhanced_monitoring: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specify the desired Kafka software version.
    """
    kafka_version: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for streaming broker logs to Cloudwatch/S3/Kinesis Firehose. See belo
    w.
    """
    logging_info: LoggingInfo | None = core.attr(LoggingInfo, default=None)

    """
    (Required) The desired total number of broker nodes in the kafka cluster.  It must be a multiple of
    the number of specified client subnets.
    """
    number_of_broker_nodes: int | core.IntOut = core.attr(int)

    """
    (Optional) Configuration block for JMX and Node monitoring for the MSK cluster. See below.
    """
    open_monitoring: OpenMonitoring | None = core.attr(OpenMonitoring, default=None)

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
    A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper
    cluster. The returned values are sorted alphabetically. The AWS API may not return all endpoints, so
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
        resource_name: str,
        *,
        broker_node_group_info: BrokerNodeGroupInfo,
        cluster_name: str | core.StringOut,
        kafka_version: str | core.StringOut,
        number_of_broker_nodes: int | core.IntOut,
        client_authentication: ClientAuthentication | None = None,
        configuration_info: ConfigurationInfo | None = None,
        encryption_info: EncryptionInfo | None = None,
        enhanced_monitoring: str | core.StringOut | None = None,
        logging_info: LoggingInfo | None = None,
        open_monitoring: OpenMonitoring | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskCluster.Args(
                broker_node_group_info=broker_node_group_info,
                cluster_name=cluster_name,
                kafka_version=kafka_version,
                number_of_broker_nodes=number_of_broker_nodes,
                client_authentication=client_authentication,
                configuration_info=configuration_info,
                encryption_info=encryption_info,
                enhanced_monitoring=enhanced_monitoring,
                logging_info=logging_info,
                open_monitoring=open_monitoring,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        broker_node_group_info: BrokerNodeGroupInfo = core.arg()

        client_authentication: ClientAuthentication | None = core.arg(default=None)

        cluster_name: str | core.StringOut = core.arg()

        configuration_info: ConfigurationInfo | None = core.arg(default=None)

        encryption_info: EncryptionInfo | None = core.arg(default=None)

        enhanced_monitoring: str | core.StringOut | None = core.arg(default=None)

        kafka_version: str | core.StringOut = core.arg()

        logging_info: LoggingInfo | None = core.arg(default=None)

        number_of_broker_nodes: int | core.IntOut = core.arg()

        open_monitoring: OpenMonitoring | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
