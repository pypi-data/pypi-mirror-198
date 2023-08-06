import terrascript.core as core


@core.schema
class LambdaFunction(core.Schema):

    events: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    filter_prefix: str | core.StringOut | None = core.attr(str, default=None)

    filter_suffix: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    lambda_function_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        events: list[str] | core.ArrayOut[core.StringOut],
        filter_prefix: str | core.StringOut | None = None,
        filter_suffix: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
        lambda_function_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LambdaFunction.Args(
                events=events,
                filter_prefix=filter_prefix,
                filter_suffix=filter_suffix,
                id=id,
                lambda_function_arn=lambda_function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        filter_prefix: str | core.StringOut | None = core.arg(default=None)

        filter_suffix: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        lambda_function_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Topic(core.Schema):

    events: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    filter_prefix: str | core.StringOut | None = core.attr(str, default=None)

    filter_suffix: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    topic_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        events: list[str] | core.ArrayOut[core.StringOut],
        topic_arn: str | core.StringOut,
        filter_prefix: str | core.StringOut | None = None,
        filter_suffix: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Topic.Args(
                events=events,
                topic_arn=topic_arn,
                filter_prefix=filter_prefix,
                filter_suffix=filter_suffix,
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        filter_prefix: str | core.StringOut | None = core.arg(default=None)

        filter_suffix: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        topic_arn: str | core.StringOut = core.arg()


@core.schema
class Queue(core.Schema):

    events: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    filter_prefix: str | core.StringOut | None = core.attr(str, default=None)

    filter_suffix: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    queue_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        events: list[str] | core.ArrayOut[core.StringOut],
        queue_arn: str | core.StringOut,
        filter_prefix: str | core.StringOut | None = None,
        filter_suffix: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Queue.Args(
                events=events,
                queue_arn=queue_arn,
                filter_prefix=filter_prefix,
                filter_suffix=filter_suffix,
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        filter_prefix: str | core.StringOut | None = core.arg(default=None)

        filter_suffix: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        queue_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_s3_bucket_notification", namespace="s3")
class BucketNotification(core.Resource):
    """
    (Required) Name of the bucket for notification configuration.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to enable Amazon EventBridge notifications.
    """
    eventbridge: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Unique identifier for each of the notification configurations.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Multiple) Used to configure notifications to a Lambda Function. See below.
    """
    lambda_function: list[LambdaFunction] | core.ArrayOut[LambdaFunction] | None = core.attr(
        LambdaFunction, default=None, kind=core.Kind.array
    )

    """
    (Optional) Notification configuration to SQS Queue. See below.
    """
    queue: list[Queue] | core.ArrayOut[Queue] | None = core.attr(
        Queue, default=None, kind=core.Kind.array
    )

    """
    (Optional) Notification configuration to SNS Topic. See below.
    """
    topic: list[Topic] | core.ArrayOut[Topic] | None = core.attr(
        Topic, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        eventbridge: bool | core.BoolOut | None = None,
        lambda_function: list[LambdaFunction] | core.ArrayOut[LambdaFunction] | None = None,
        queue: list[Queue] | core.ArrayOut[Queue] | None = None,
        topic: list[Topic] | core.ArrayOut[Topic] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketNotification.Args(
                bucket=bucket,
                eventbridge=eventbridge,
                lambda_function=lambda_function,
                queue=queue,
                topic=topic,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        eventbridge: bool | core.BoolOut | None = core.arg(default=None)

        lambda_function: list[LambdaFunction] | core.ArrayOut[LambdaFunction] | None = core.arg(
            default=None
        )

        queue: list[Queue] | core.ArrayOut[Queue] | None = core.arg(default=None)

        topic: list[Topic] | core.ArrayOut[Topic] | None = core.arg(default=None)
