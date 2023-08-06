import terrascript.core as core


@core.schema
class PutItem(core.Schema):

    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        table_name: str | core.StringOut,
    ):
        super().__init__(
            args=PutItem.Args(
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        table_name: str | core.StringOut = core.arg()


@core.schema
class Dynamodbv2(core.Schema):

    put_item: PutItem | None = core.attr(PutItem, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        put_item: PutItem | None = None,
    ):
        super().__init__(
            args=Dynamodbv2.Args(
                role_arn=role_arn,
                put_item=put_item,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        put_item: PutItem | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()


@core.schema
class CloudwatchAlarm(core.Schema):

    alarm_name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    state_reason: str | core.StringOut = core.attr(str)

    state_value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        alarm_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        state_reason: str | core.StringOut,
        state_value: str | core.StringOut,
    ):
        super().__init__(
            args=CloudwatchAlarm.Args(
                alarm_name=alarm_name,
                role_arn=role_arn,
                state_reason=state_reason,
                state_value=state_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarm_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        state_reason: str | core.StringOut = core.arg()

        state_value: str | core.StringOut = core.arg()


@core.schema
class IotEvents(core.Schema):

    input_name: str | core.StringOut = core.attr(str)

    message_id: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        input_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        message_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=IotEvents.Args(
                input_name=input_name,
                role_arn=role_arn,
                message_id=message_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_name: str | core.StringOut = core.arg()

        message_id: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()


@core.schema
class Firehose(core.Schema):

    delivery_stream_name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    separator: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delivery_stream_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        separator: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Firehose.Args(
                delivery_stream_name=delivery_stream_name,
                role_arn=role_arn,
                separator=separator,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delivery_stream_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        separator: str | core.StringOut | None = core.arg(default=None)


@core.schema
class StepFunctions(core.Schema):

    execution_name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    state_machine_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        state_machine_name: str | core.StringOut,
        execution_name_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StepFunctions.Args(
                role_arn=role_arn,
                state_machine_name=state_machine_name,
                execution_name_prefix=execution_name_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execution_name_prefix: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        state_machine_name: str | core.StringOut = core.arg()


@core.schema
class HttpHeader(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=HttpHeader.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Http(core.Schema):

    confirmation_url: str | core.StringOut | None = core.attr(str, default=None)

    http_header: list[HttpHeader] | core.ArrayOut[HttpHeader] | None = core.attr(
        HttpHeader, default=None, kind=core.Kind.array
    )

    url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        url: str | core.StringOut,
        confirmation_url: str | core.StringOut | None = None,
        http_header: list[HttpHeader] | core.ArrayOut[HttpHeader] | None = None,
    ):
        super().__init__(
            args=Http.Args(
                url=url,
                confirmation_url=confirmation_url,
                http_header=http_header,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        confirmation_url: str | core.StringOut | None = core.arg(default=None)

        http_header: list[HttpHeader] | core.ArrayOut[HttpHeader] | None = core.arg(default=None)

        url: str | core.StringOut = core.arg()


@core.schema
class Kinesis(core.Schema):

    partition_key: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    stream_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        stream_name: str | core.StringOut,
        partition_key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Kinesis.Args(
                role_arn=role_arn,
                stream_name=stream_name,
                partition_key=partition_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        partition_key: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        stream_name: str | core.StringOut = core.arg()


@core.schema
class Republish(core.Schema):

    qos: int | core.IntOut | None = core.attr(int, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    topic: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        topic: str | core.StringOut,
        qos: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Republish.Args(
                role_arn=role_arn,
                topic=topic,
                qos=qos,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        qos: int | core.IntOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        topic: str | core.StringOut = core.arg()


@core.schema
class Dimension(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Dimension.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Timestamp(core.Schema):

    unit: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        unit: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Timestamp.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Timestream(core.Schema):

    database_name: str | core.StringOut = core.attr(str)

    dimension: list[Dimension] | core.ArrayOut[Dimension] = core.attr(
        Dimension, kind=core.Kind.array
    )

    role_arn: str | core.StringOut = core.attr(str)

    table_name: str | core.StringOut = core.attr(str)

    timestamp: Timestamp | None = core.attr(Timestamp, default=None)

    def __init__(
        self,
        *,
        database_name: str | core.StringOut,
        dimension: list[Dimension] | core.ArrayOut[Dimension],
        role_arn: str | core.StringOut,
        table_name: str | core.StringOut,
        timestamp: Timestamp | None = None,
    ):
        super().__init__(
            args=Timestream.Args(
                database_name=database_name,
                dimension=dimension,
                role_arn=role_arn,
                table_name=table_name,
                timestamp=timestamp,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database_name: str | core.StringOut = core.arg()

        dimension: list[Dimension] | core.ArrayOut[Dimension] = core.arg()

        role_arn: str | core.StringOut = core.arg()

        table_name: str | core.StringOut = core.arg()

        timestamp: Timestamp | None = core.arg(default=None)


@core.schema
class CloudwatchLogs(core.Schema):

    log_group_name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        log_group_name: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=CloudwatchLogs.Args(
                log_group_name=log_group_name,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_group_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class Sns(core.Schema):

    message_format: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    target_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        target_arn: str | core.StringOut,
        message_format: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Sns.Args(
                role_arn=role_arn,
                target_arn=target_arn,
                message_format=message_format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_format: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        target_arn: str | core.StringOut = core.arg()


@core.schema
class Dynamodb(core.Schema):

    hash_key_field: str | core.StringOut = core.attr(str)

    hash_key_type: str | core.StringOut | None = core.attr(str, default=None)

    hash_key_value: str | core.StringOut = core.attr(str)

    operation: str | core.StringOut | None = core.attr(str, default=None)

    payload_field: str | core.StringOut | None = core.attr(str, default=None)

    range_key_field: str | core.StringOut | None = core.attr(str, default=None)

    range_key_type: str | core.StringOut | None = core.attr(str, default=None)

    range_key_value: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        hash_key_field: str | core.StringOut,
        hash_key_value: str | core.StringOut,
        role_arn: str | core.StringOut,
        table_name: str | core.StringOut,
        hash_key_type: str | core.StringOut | None = None,
        operation: str | core.StringOut | None = None,
        payload_field: str | core.StringOut | None = None,
        range_key_field: str | core.StringOut | None = None,
        range_key_type: str | core.StringOut | None = None,
        range_key_value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Dynamodb.Args(
                hash_key_field=hash_key_field,
                hash_key_value=hash_key_value,
                role_arn=role_arn,
                table_name=table_name,
                hash_key_type=hash_key_type,
                operation=operation,
                payload_field=payload_field,
                range_key_field=range_key_field,
                range_key_type=range_key_type,
                range_key_value=range_key_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hash_key_field: str | core.StringOut = core.arg()

        hash_key_type: str | core.StringOut | None = core.arg(default=None)

        hash_key_value: str | core.StringOut = core.arg()

        operation: str | core.StringOut | None = core.arg(default=None)

        payload_field: str | core.StringOut | None = core.arg(default=None)

        range_key_field: str | core.StringOut | None = core.arg(default=None)

        range_key_type: str | core.StringOut | None = core.arg(default=None)

        range_key_value: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        table_name: str | core.StringOut = core.arg()


@core.schema
class IotAnalytics(core.Schema):

    channel_name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        channel_name: str | core.StringOut,
        role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=IotAnalytics.Args(
                channel_name=channel_name,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        channel_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class Kafka(core.Schema):

    client_properties: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, kind=core.Kind.map
    )

    destination_arn: str | core.StringOut = core.attr(str)

    key: str | core.StringOut | None = core.attr(str, default=None)

    partition: str | core.StringOut | None = core.attr(str, default=None)

    topic: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        client_properties: dict[str, str] | core.MapOut[core.StringOut],
        destination_arn: str | core.StringOut,
        topic: str | core.StringOut,
        key: str | core.StringOut | None = None,
        partition: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Kafka.Args(
                client_properties=client_properties,
                destination_arn=destination_arn,
                topic=topic,
                key=key,
                partition=partition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_properties: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        destination_arn: str | core.StringOut = core.arg()

        key: str | core.StringOut | None = core.arg(default=None)

        partition: str | core.StringOut | None = core.arg(default=None)

        topic: str | core.StringOut = core.arg()


@core.schema
class Lambda(core.Schema):

    function_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        function_arn: str | core.StringOut,
    ):
        super().__init__(
            args=Lambda.Args(
                function_arn=function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: str | core.StringOut = core.arg()


@core.schema
class Sqs(core.Schema):

    queue_url: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    use_base64: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        queue_url: str | core.StringOut,
        role_arn: str | core.StringOut,
        use_base64: bool | core.BoolOut,
    ):
        super().__init__(
            args=Sqs.Args(
                queue_url=queue_url,
                role_arn=role_arn,
                use_base64=use_base64,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        queue_url: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        use_base64: bool | core.BoolOut = core.arg()


@core.schema
class CloudwatchMetric(core.Schema):

    metric_name: str | core.StringOut = core.attr(str)

    metric_namespace: str | core.StringOut = core.attr(str)

    metric_timestamp: str | core.StringOut | None = core.attr(str, default=None)

    metric_unit: str | core.StringOut = core.attr(str)

    metric_value: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        metric_name: str | core.StringOut,
        metric_namespace: str | core.StringOut,
        metric_unit: str | core.StringOut,
        metric_value: str | core.StringOut,
        role_arn: str | core.StringOut,
        metric_timestamp: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CloudwatchMetric.Args(
                metric_name=metric_name,
                metric_namespace=metric_namespace,
                metric_unit=metric_unit,
                metric_value=metric_value,
                role_arn=role_arn,
                metric_timestamp=metric_timestamp,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_name: str | core.StringOut = core.arg()

        metric_namespace: str | core.StringOut = core.arg()

        metric_timestamp: str | core.StringOut | None = core.arg(default=None)

        metric_unit: str | core.StringOut = core.arg()

        metric_value: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class S3(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    canned_acl: str | core.StringOut | None = core.attr(str, default=None)

    key: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        key: str | core.StringOut,
        role_arn: str | core.StringOut,
        canned_acl: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3.Args(
                bucket_name=bucket_name,
                key=key,
                role_arn=role_arn,
                canned_acl=canned_acl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        canned_acl: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()


@core.schema
class Elasticsearch(core.Schema):

    endpoint: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str)

    index: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        endpoint: str | core.StringOut,
        id: str | core.StringOut,
        index: str | core.StringOut,
        role_arn: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Elasticsearch.Args(
                endpoint=endpoint,
                id=id,
                index=index,
                role_arn=role_arn,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        index: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class ErrorAction(core.Schema):

    cloudwatch_alarm: CloudwatchAlarm | None = core.attr(CloudwatchAlarm, default=None)

    cloudwatch_logs: CloudwatchLogs | None = core.attr(CloudwatchLogs, default=None)

    cloudwatch_metric: CloudwatchMetric | None = core.attr(CloudwatchMetric, default=None)

    dynamodb: Dynamodb | None = core.attr(Dynamodb, default=None)

    dynamodbv2: Dynamodbv2 | None = core.attr(Dynamodbv2, default=None)

    elasticsearch: Elasticsearch | None = core.attr(Elasticsearch, default=None)

    firehose: Firehose | None = core.attr(Firehose, default=None)

    http: Http | None = core.attr(Http, default=None)

    iot_analytics: IotAnalytics | None = core.attr(IotAnalytics, default=None)

    iot_events: IotEvents | None = core.attr(IotEvents, default=None)

    kafka: Kafka | None = core.attr(Kafka, default=None)

    kinesis: Kinesis | None = core.attr(Kinesis, default=None)

    lambda_: Lambda | None = core.attr(Lambda, default=None, alias="lambda")

    republish: Republish | None = core.attr(Republish, default=None)

    s3: S3 | None = core.attr(S3, default=None)

    sns: Sns | None = core.attr(Sns, default=None)

    sqs: Sqs | None = core.attr(Sqs, default=None)

    step_functions: StepFunctions | None = core.attr(StepFunctions, default=None)

    timestream: Timestream | None = core.attr(Timestream, default=None)

    def __init__(
        self,
        *,
        cloudwatch_alarm: CloudwatchAlarm | None = None,
        cloudwatch_logs: CloudwatchLogs | None = None,
        cloudwatch_metric: CloudwatchMetric | None = None,
        dynamodb: Dynamodb | None = None,
        dynamodbv2: Dynamodbv2 | None = None,
        elasticsearch: Elasticsearch | None = None,
        firehose: Firehose | None = None,
        http: Http | None = None,
        iot_analytics: IotAnalytics | None = None,
        iot_events: IotEvents | None = None,
        kafka: Kafka | None = None,
        kinesis: Kinesis | None = None,
        lambda_: Lambda | None = None,
        republish: Republish | None = None,
        s3: S3 | None = None,
        sns: Sns | None = None,
        sqs: Sqs | None = None,
        step_functions: StepFunctions | None = None,
        timestream: Timestream | None = None,
    ):
        super().__init__(
            args=ErrorAction.Args(
                cloudwatch_alarm=cloudwatch_alarm,
                cloudwatch_logs=cloudwatch_logs,
                cloudwatch_metric=cloudwatch_metric,
                dynamodb=dynamodb,
                dynamodbv2=dynamodbv2,
                elasticsearch=elasticsearch,
                firehose=firehose,
                http=http,
                iot_analytics=iot_analytics,
                iot_events=iot_events,
                kafka=kafka,
                kinesis=kinesis,
                lambda_=lambda_,
                republish=republish,
                s3=s3,
                sns=sns,
                sqs=sqs,
                step_functions=step_functions,
                timestream=timestream,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_alarm: CloudwatchAlarm | None = core.arg(default=None)

        cloudwatch_logs: CloudwatchLogs | None = core.arg(default=None)

        cloudwatch_metric: CloudwatchMetric | None = core.arg(default=None)

        dynamodb: Dynamodb | None = core.arg(default=None)

        dynamodbv2: Dynamodbv2 | None = core.arg(default=None)

        elasticsearch: Elasticsearch | None = core.arg(default=None)

        firehose: Firehose | None = core.arg(default=None)

        http: Http | None = core.arg(default=None)

        iot_analytics: IotAnalytics | None = core.arg(default=None)

        iot_events: IotEvents | None = core.arg(default=None)

        kafka: Kafka | None = core.arg(default=None)

        kinesis: Kinesis | None = core.arg(default=None)

        lambda_: Lambda | None = core.arg(default=None)

        republish: Republish | None = core.arg(default=None)

        s3: S3 | None = core.arg(default=None)

        sns: Sns | None = core.arg(default=None)

        sqs: Sqs | None = core.arg(default=None)

        step_functions: StepFunctions | None = core.arg(default=None)

        timestream: Timestream | None = core.arg(default=None)


@core.resource(type="aws_iot_topic_rule", namespace="iot")
class TopicRule(core.Resource):
    """
    The ARN of the topic rule
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    cloudwatch_alarm: list[CloudwatchAlarm] | core.ArrayOut[CloudwatchAlarm] | None = core.attr(
        CloudwatchAlarm, default=None, kind=core.Kind.array
    )

    cloudwatch_logs: list[CloudwatchLogs] | core.ArrayOut[CloudwatchLogs] | None = core.attr(
        CloudwatchLogs, default=None, kind=core.Kind.array
    )

    cloudwatch_metric: list[CloudwatchMetric] | core.ArrayOut[CloudwatchMetric] | None = core.attr(
        CloudwatchMetric, default=None, kind=core.Kind.array
    )

    """
    (Optional) The description of the rule.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    dynamodb: list[Dynamodb] | core.ArrayOut[Dynamodb] | None = core.attr(
        Dynamodb, default=None, kind=core.Kind.array
    )

    dynamodbv2: list[Dynamodbv2] | core.ArrayOut[Dynamodbv2] | None = core.attr(
        Dynamodbv2, default=None, kind=core.Kind.array
    )

    elasticsearch: list[Elasticsearch] | core.ArrayOut[Elasticsearch] | None = core.attr(
        Elasticsearch, default=None, kind=core.Kind.array
    )

    """
    (Required) Specifies whether the rule is enabled.
    """
    enabled: bool | core.BoolOut = core.attr(bool)

    """
    (Optional) Configuration block with error action to be associated with the rule. See the documentati
    on for `cloudwatch_alarm`, `cloudwatch_logs`, `cloudwatch_metric`, `dynamodb`, `dynamodbv2`, `elasti
    csearch`, `firehose`, `http`, `iot_analytics`, `iot_events`, `kafka`, `kinesis`, `lambda`, `republis
    h`, `s3`, `sns`, `sqs`, `step_functions`, `timestream` configuration blocks for further configuratio
    n details.
    """
    error_action: ErrorAction | None = core.attr(ErrorAction, default=None)

    firehose: list[Firehose] | core.ArrayOut[Firehose] | None = core.attr(
        Firehose, default=None, kind=core.Kind.array
    )

    http: list[Http] | core.ArrayOut[Http] | None = core.attr(
        Http, default=None, kind=core.Kind.array
    )

    """
    (Required) The unique identifier for the document you are storing.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    iot_analytics: list[IotAnalytics] | core.ArrayOut[IotAnalytics] | None = core.attr(
        IotAnalytics, default=None, kind=core.Kind.array
    )

    iot_events: list[IotEvents] | core.ArrayOut[IotEvents] | None = core.attr(
        IotEvents, default=None, kind=core.Kind.array
    )

    kafka: list[Kafka] | core.ArrayOut[Kafka] | None = core.attr(
        Kafka, default=None, kind=core.Kind.array
    )

    kinesis: list[Kinesis] | core.ArrayOut[Kinesis] | None = core.attr(
        Kinesis, default=None, kind=core.Kind.array
    )

    lambda_: list[Lambda] | core.ArrayOut[Lambda] | None = core.attr(
        Lambda, default=None, kind=core.Kind.array, alias="lambda"
    )

    """
    (Required) The name of the rule.
    """
    name: str | core.StringOut = core.attr(str)

    republish: list[Republish] | core.ArrayOut[Republish] | None = core.attr(
        Republish, default=None, kind=core.Kind.array
    )

    s3: list[S3] | core.ArrayOut[S3] | None = core.attr(S3, default=None, kind=core.Kind.array)

    sns: list[Sns] | core.ArrayOut[Sns] | None = core.attr(Sns, default=None, kind=core.Kind.array)

    """
    (Required) The SQL statement used to query the topic. For more information, see AWS IoT SQL Referenc
    e (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the
    AWS IoT Developer Guide.
    """
    sql: str | core.StringOut = core.attr(str)

    """
    (Required) The version of the SQL rules engine to use when evaluating the rule.
    """
    sql_version: str | core.StringOut = core.attr(str)

    sqs: list[Sqs] | core.ArrayOut[Sqs] | None = core.attr(Sqs, default=None, kind=core.Kind.array)

    step_functions: list[StepFunctions] | core.ArrayOut[StepFunctions] | None = core.attr(
        StepFunctions, default=None, kind=core.Kind.array
    )

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    timestream: list[Timestream] | core.ArrayOut[Timestream] | None = core.attr(
        Timestream, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        enabled: bool | core.BoolOut,
        name: str | core.StringOut,
        sql: str | core.StringOut,
        sql_version: str | core.StringOut,
        cloudwatch_alarm: list[CloudwatchAlarm] | core.ArrayOut[CloudwatchAlarm] | None = None,
        cloudwatch_logs: list[CloudwatchLogs] | core.ArrayOut[CloudwatchLogs] | None = None,
        cloudwatch_metric: list[CloudwatchMetric] | core.ArrayOut[CloudwatchMetric] | None = None,
        description: str | core.StringOut | None = None,
        dynamodb: list[Dynamodb] | core.ArrayOut[Dynamodb] | None = None,
        dynamodbv2: list[Dynamodbv2] | core.ArrayOut[Dynamodbv2] | None = None,
        elasticsearch: list[Elasticsearch] | core.ArrayOut[Elasticsearch] | None = None,
        error_action: ErrorAction | None = None,
        firehose: list[Firehose] | core.ArrayOut[Firehose] | None = None,
        http: list[Http] | core.ArrayOut[Http] | None = None,
        iot_analytics: list[IotAnalytics] | core.ArrayOut[IotAnalytics] | None = None,
        iot_events: list[IotEvents] | core.ArrayOut[IotEvents] | None = None,
        kafka: list[Kafka] | core.ArrayOut[Kafka] | None = None,
        kinesis: list[Kinesis] | core.ArrayOut[Kinesis] | None = None,
        lambda_: list[Lambda] | core.ArrayOut[Lambda] | None = None,
        republish: list[Republish] | core.ArrayOut[Republish] | None = None,
        s3: list[S3] | core.ArrayOut[S3] | None = None,
        sns: list[Sns] | core.ArrayOut[Sns] | None = None,
        sqs: list[Sqs] | core.ArrayOut[Sqs] | None = None,
        step_functions: list[StepFunctions] | core.ArrayOut[StepFunctions] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timestream: list[Timestream] | core.ArrayOut[Timestream] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TopicRule.Args(
                enabled=enabled,
                name=name,
                sql=sql,
                sql_version=sql_version,
                cloudwatch_alarm=cloudwatch_alarm,
                cloudwatch_logs=cloudwatch_logs,
                cloudwatch_metric=cloudwatch_metric,
                description=description,
                dynamodb=dynamodb,
                dynamodbv2=dynamodbv2,
                elasticsearch=elasticsearch,
                error_action=error_action,
                firehose=firehose,
                http=http,
                iot_analytics=iot_analytics,
                iot_events=iot_events,
                kafka=kafka,
                kinesis=kinesis,
                lambda_=lambda_,
                republish=republish,
                s3=s3,
                sns=sns,
                sqs=sqs,
                step_functions=step_functions,
                tags=tags,
                tags_all=tags_all,
                timestream=timestream,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_alarm: list[CloudwatchAlarm] | core.ArrayOut[CloudwatchAlarm] | None = core.arg(
            default=None
        )

        cloudwatch_logs: list[CloudwatchLogs] | core.ArrayOut[CloudwatchLogs] | None = core.arg(
            default=None
        )

        cloudwatch_metric: list[CloudwatchMetric] | core.ArrayOut[
            CloudwatchMetric
        ] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        dynamodb: list[Dynamodb] | core.ArrayOut[Dynamodb] | None = core.arg(default=None)

        dynamodbv2: list[Dynamodbv2] | core.ArrayOut[Dynamodbv2] | None = core.arg(default=None)

        elasticsearch: list[Elasticsearch] | core.ArrayOut[Elasticsearch] | None = core.arg(
            default=None
        )

        enabled: bool | core.BoolOut = core.arg()

        error_action: ErrorAction | None = core.arg(default=None)

        firehose: list[Firehose] | core.ArrayOut[Firehose] | None = core.arg(default=None)

        http: list[Http] | core.ArrayOut[Http] | None = core.arg(default=None)

        iot_analytics: list[IotAnalytics] | core.ArrayOut[IotAnalytics] | None = core.arg(
            default=None
        )

        iot_events: list[IotEvents] | core.ArrayOut[IotEvents] | None = core.arg(default=None)

        kafka: list[Kafka] | core.ArrayOut[Kafka] | None = core.arg(default=None)

        kinesis: list[Kinesis] | core.ArrayOut[Kinesis] | None = core.arg(default=None)

        lambda_: list[Lambda] | core.ArrayOut[Lambda] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        republish: list[Republish] | core.ArrayOut[Republish] | None = core.arg(default=None)

        s3: list[S3] | core.ArrayOut[S3] | None = core.arg(default=None)

        sns: list[Sns] | core.ArrayOut[Sns] | None = core.arg(default=None)

        sql: str | core.StringOut = core.arg()

        sql_version: str | core.StringOut = core.arg()

        sqs: list[Sqs] | core.ArrayOut[Sqs] | None = core.arg(default=None)

        step_functions: list[StepFunctions] | core.ArrayOut[StepFunctions] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        timestream: list[Timestream] | core.ArrayOut[Timestream] | None = core.arg(default=None)
