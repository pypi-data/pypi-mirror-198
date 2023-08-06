import terrascript.core as core


@core.schema
class CloudwatchDestination(core.Schema):

    default_value: str | core.StringOut = core.attr(str)

    dimension_name: str | core.StringOut = core.attr(str)

    value_source: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        default_value: str | core.StringOut,
        dimension_name: str | core.StringOut,
        value_source: str | core.StringOut,
    ):
        super().__init__(
            args=CloudwatchDestination.Args(
                default_value=default_value,
                dimension_name=dimension_name,
                value_source=value_source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_value: str | core.StringOut = core.arg()

        dimension_name: str | core.StringOut = core.arg()

        value_source: str | core.StringOut = core.arg()


@core.schema
class KinesisDestination(core.Schema):

    role_arn: str | core.StringOut = core.attr(str)

    stream_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        stream_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisDestination.Args(
                role_arn=role_arn,
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_arn: str | core.StringOut = core.arg()

        stream_arn: str | core.StringOut = core.arg()


@core.schema
class SnsDestination(core.Schema):

    topic_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        topic_arn: str | core.StringOut,
    ):
        super().__init__(
            args=SnsDestination.Args(
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        topic_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_ses_event_destination", namespace="ses")
class EventDestination(core.Resource):
    """
    The SES event destination ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) CloudWatch destination for the events
    """
    cloudwatch_destination: list[CloudwatchDestination] | core.ArrayOut[
        CloudwatchDestination
    ] | None = core.attr(CloudwatchDestination, default=None, kind=core.Kind.array)

    """
    (Required) The name of the configuration set
    """
    configuration_set_name: str | core.StringOut = core.attr(str)

    """
    (Optional) If true, the event destination will be enabled
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The SES event destination name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Send the events to a kinesis firehose destination
    """
    kinesis_destination: KinesisDestination | None = core.attr(KinesisDestination, default=None)

    """
    (Required) A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`,
    "delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
    """
    matching_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Required) The name of the event destination
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Send the events to an SNS Topic destination
    """
    sns_destination: SnsDestination | None = core.attr(SnsDestination, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        configuration_set_name: str | core.StringOut,
        matching_types: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        cloudwatch_destination: list[CloudwatchDestination]
        | core.ArrayOut[CloudwatchDestination]
        | None = None,
        enabled: bool | core.BoolOut | None = None,
        kinesis_destination: KinesisDestination | None = None,
        sns_destination: SnsDestination | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventDestination.Args(
                configuration_set_name=configuration_set_name,
                matching_types=matching_types,
                name=name,
                cloudwatch_destination=cloudwatch_destination,
                enabled=enabled,
                kinesis_destination=kinesis_destination,
                sns_destination=sns_destination,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_destination: list[CloudwatchDestination] | core.ArrayOut[
            CloudwatchDestination
        ] | None = core.arg(default=None)

        configuration_set_name: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        kinesis_destination: KinesisDestination | None = core.arg(default=None)

        matching_types: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()

        sns_destination: SnsDestination | None = core.arg(default=None)
