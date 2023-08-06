import terrascript.core as core


@core.schema
class KafkaClusterClientAuthentication(core.Schema):

    authentication_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        authentication_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KafkaClusterClientAuthentication.Args(
                authentication_type=authentication_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ScaleInPolicy(core.Schema):

    cpu_utilization_percentage: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cpu_utilization_percentage: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ScaleInPolicy.Args(
                cpu_utilization_percentage=cpu_utilization_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_utilization_percentage: int | core.IntOut | None = core.arg(default=None)


@core.schema
class ScaleOutPolicy(core.Schema):

    cpu_utilization_percentage: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cpu_utilization_percentage: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ScaleOutPolicy.Args(
                cpu_utilization_percentage=cpu_utilization_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_utilization_percentage: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Autoscaling(core.Schema):

    max_worker_count: int | core.IntOut = core.attr(int)

    mcu_count: int | core.IntOut | None = core.attr(int, default=None)

    min_worker_count: int | core.IntOut = core.attr(int)

    scale_in_policy: ScaleInPolicy | None = core.attr(ScaleInPolicy, default=None, computed=True)

    scale_out_policy: ScaleOutPolicy | None = core.attr(ScaleOutPolicy, default=None, computed=True)

    def __init__(
        self,
        *,
        max_worker_count: int | core.IntOut,
        min_worker_count: int | core.IntOut,
        mcu_count: int | core.IntOut | None = None,
        scale_in_policy: ScaleInPolicy | None = None,
        scale_out_policy: ScaleOutPolicy | None = None,
    ):
        super().__init__(
            args=Autoscaling.Args(
                max_worker_count=max_worker_count,
                min_worker_count=min_worker_count,
                mcu_count=mcu_count,
                scale_in_policy=scale_in_policy,
                scale_out_policy=scale_out_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_worker_count: int | core.IntOut = core.arg()

        mcu_count: int | core.IntOut | None = core.arg(default=None)

        min_worker_count: int | core.IntOut = core.arg()

        scale_in_policy: ScaleInPolicy | None = core.arg(default=None)

        scale_out_policy: ScaleOutPolicy | None = core.arg(default=None)


@core.schema
class ProvisionedCapacity(core.Schema):

    mcu_count: int | core.IntOut | None = core.attr(int, default=None)

    worker_count: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        worker_count: int | core.IntOut,
        mcu_count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ProvisionedCapacity.Args(
                worker_count=worker_count,
                mcu_count=mcu_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mcu_count: int | core.IntOut | None = core.arg(default=None)

        worker_count: int | core.IntOut = core.arg()


@core.schema
class Capacity(core.Schema):

    autoscaling: Autoscaling | None = core.attr(Autoscaling, default=None)

    provisioned_capacity: ProvisionedCapacity | None = core.attr(ProvisionedCapacity, default=None)

    def __init__(
        self,
        *,
        autoscaling: Autoscaling | None = None,
        provisioned_capacity: ProvisionedCapacity | None = None,
    ):
        super().__init__(
            args=Capacity.Args(
                autoscaling=autoscaling,
                provisioned_capacity=provisioned_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoscaling: Autoscaling | None = core.arg(default=None)

        provisioned_capacity: ProvisionedCapacity | None = core.arg(default=None)


@core.schema
class WorkerConfiguration(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    revision: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        revision: int | core.IntOut,
    ):
        super().__init__(
            args=WorkerConfiguration.Args(
                arn=arn,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        revision: int | core.IntOut = core.arg()


@core.schema
class Vpc(core.Schema):

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        security_groups: list[str] | core.ArrayOut[core.StringOut],
        subnets: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Vpc.Args(
                security_groups=security_groups,
                subnets=subnets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class ApacheKafkaCluster(core.Schema):

    bootstrap_servers: str | core.StringOut = core.attr(str)

    vpc: Vpc = core.attr(Vpc)

    def __init__(
        self,
        *,
        bootstrap_servers: str | core.StringOut,
        vpc: Vpc,
    ):
        super().__init__(
            args=ApacheKafkaCluster.Args(
                bootstrap_servers=bootstrap_servers,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bootstrap_servers: str | core.StringOut = core.arg()

        vpc: Vpc = core.arg()


@core.schema
class KafkaCluster(core.Schema):

    apache_kafka_cluster: ApacheKafkaCluster = core.attr(ApacheKafkaCluster)

    def __init__(
        self,
        *,
        apache_kafka_cluster: ApacheKafkaCluster,
    ):
        super().__init__(
            args=KafkaCluster.Args(
                apache_kafka_cluster=apache_kafka_cluster,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apache_kafka_cluster: ApacheKafkaCluster = core.arg()


@core.schema
class CustomPlugin(core.Schema):

    arn: str | core.StringOut = core.attr(str)

    revision: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        revision: int | core.IntOut,
    ):
        super().__init__(
            args=CustomPlugin.Args(
                arn=arn,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        revision: int | core.IntOut = core.arg()


@core.schema
class Plugin(core.Schema):

    custom_plugin: CustomPlugin = core.attr(CustomPlugin)

    def __init__(
        self,
        *,
        custom_plugin: CustomPlugin,
    ):
        super().__init__(
            args=Plugin.Args(
                custom_plugin=custom_plugin,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_plugin: CustomPlugin = core.arg()


@core.schema
class KafkaClusterEncryptionInTransit(core.Schema):

    encryption_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KafkaClusterEncryptionInTransit.Args(
                encryption_type=encryption_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: str | core.StringOut | None = core.arg(default=None)


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
class WorkerLogDelivery(core.Schema):

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
            args=WorkerLogDelivery.Args(
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
class LogDelivery(core.Schema):

    worker_log_delivery: WorkerLogDelivery = core.attr(WorkerLogDelivery)

    def __init__(
        self,
        *,
        worker_log_delivery: WorkerLogDelivery,
    ):
        super().__init__(
            args=LogDelivery.Args(
                worker_log_delivery=worker_log_delivery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        worker_log_delivery: WorkerLogDelivery = core.arg()


@core.resource(type="aws_mskconnect_connector", namespace="managed_streaming_for_kafka_connect")
class MskconnectConnector(core.Resource):
    """
    (Required) The Amazon Resource Name (ARN) of the custom plugin.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Information about the capacity allocated to the connector. See below.
    """
    capacity: Capacity = core.attr(Capacity)

    """
    (Required) A map of keys to values that represent the configuration for the connector.
    """
    connector_configuration: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, kind=core.Kind.map
    )

    """
    (Optional) A summary description of the connector.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies which Apache Kafka cluster to connect to. See below.
    """
    kafka_cluster: KafkaCluster = core.attr(KafkaCluster)

    """
    (Required) Details of the client authentication used by the Apache Kafka cluster. See below.
    """
    kafka_cluster_client_authentication: KafkaClusterClientAuthentication = core.attr(
        KafkaClusterClientAuthentication
    )

    """
    (Required) Details of encryption in transit to the Apache Kafka cluster. See below.
    """
    kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransit = core.attr(
        KafkaClusterEncryptionInTransit
    )

    """
    (Required) The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster'
    s version and the plugins.
    """
    kafkaconnect_version: str | core.StringOut = core.attr(str)

    """
    (Optional) Details about log delivery. See below.
    """
    log_delivery: LogDelivery | None = core.attr(LogDelivery, default=None)

    """
    (Required) The name of the connector.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies which plugins to use for the connector. See below.
    """
    plugin: list[Plugin] | core.ArrayOut[Plugin] = core.attr(Plugin, kind=core.Kind.array)

    """
    (Required) The Amazon Resource Name (ARN) of the IAM role used by the connector to access the Amazon
    Web Services resources that it needs. The types of resources depends on the logic of the connector.
    For example, a connector that has Amazon S3 as a destination must have permissions that allow it to
    write to the S3 destination bucket.
    """
    service_execution_role_arn: str | core.StringOut = core.attr(str)

    """
    The current version of the connector.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies which worker configuration to use with the connector. See below.
    """
    worker_configuration: WorkerConfiguration | None = core.attr(WorkerConfiguration, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        capacity: Capacity,
        connector_configuration: dict[str, str] | core.MapOut[core.StringOut],
        kafka_cluster: KafkaCluster,
        kafka_cluster_client_authentication: KafkaClusterClientAuthentication,
        kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransit,
        kafkaconnect_version: str | core.StringOut,
        name: str | core.StringOut,
        plugin: list[Plugin] | core.ArrayOut[Plugin],
        service_execution_role_arn: str | core.StringOut,
        description: str | core.StringOut | None = None,
        log_delivery: LogDelivery | None = None,
        worker_configuration: WorkerConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskconnectConnector.Args(
                capacity=capacity,
                connector_configuration=connector_configuration,
                kafka_cluster=kafka_cluster,
                kafka_cluster_client_authentication=kafka_cluster_client_authentication,
                kafka_cluster_encryption_in_transit=kafka_cluster_encryption_in_transit,
                kafkaconnect_version=kafkaconnect_version,
                name=name,
                plugin=plugin,
                service_execution_role_arn=service_execution_role_arn,
                description=description,
                log_delivery=log_delivery,
                worker_configuration=worker_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity: Capacity = core.arg()

        connector_configuration: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        kafka_cluster: KafkaCluster = core.arg()

        kafka_cluster_client_authentication: KafkaClusterClientAuthentication = core.arg()

        kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransit = core.arg()

        kafkaconnect_version: str | core.StringOut = core.arg()

        log_delivery: LogDelivery | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        plugin: list[Plugin] | core.ArrayOut[Plugin] = core.arg()

        service_execution_role_arn: str | core.StringOut = core.arg()

        worker_configuration: WorkerConfiguration | None = core.arg(default=None)
