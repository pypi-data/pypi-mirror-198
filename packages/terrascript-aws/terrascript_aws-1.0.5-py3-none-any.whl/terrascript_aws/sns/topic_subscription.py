import terrascript.core as core


@core.resource(type="aws_sns_topic_subscription", namespace="sns")
class TopicSubscription(core.Resource):
    """
    ARN of the subscription.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Integer indicating number of minutes to wait in retrying mode for fetching subscription a
    rn before marking it as failure. Only applicable for http and https protocols. Default is `1`.
    """
    confirmation_timeout_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    """
    Whether the subscription confirmation request was authenticated.
    """
    confirmation_was_authenticated: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) JSON String with the delivery policy (retries, backoff, etc.) that will be used in the su
    bscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.ama
    zon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
    """
    delivery_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Endpoint to send data to. The contents vary with the protocol. See details below.
    """
    endpoint: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether the endpoint is capable of [auto confirming subscription](http://docs.aws.amazon.
    com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) (e.g., PagerDuty). Default is `f
    alse`.
    """
    endpoint_auto_confirms: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) JSON String with the filter policy that will be used in the subscription to filter messag
    es seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/me
    ssage-filtering.html) for more details.
    """
    filter_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN of the subscription.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    AWS account ID of the subscription's owner.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the subscription has not been confirmed.
    """
    pending_confirmation: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) Protocol to use. Valid values are: `sqs`, `sms`, `lambda`, `firehose`, and `application`.
    Protocols `email`, `email-json`, `http` and `https` are also valid but partially supported. See det
    ails below.
    """
    protocol: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to enable raw message delivery (the original message is directly passed, not wrap
    ped in JSON with the original message in the message property). Default is `false`.
    """
    raw_message_delivery: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) JSON String with the redrive policy that will be used in the subscription. Refer to the [
    SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html#how-messages-moved-i
    nto-dead-letter-queue) for more details.
    """
    redrive_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required if `protocol` is `firehose`) ARN of the IAM role to publish to Kinesis Data Firehose deliv
    ery stream. Refer to [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber
    .html).
    """
    subscription_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) ARN of the SNS topic to subscribe to.
    """
    topic_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        endpoint: str | core.StringOut,
        protocol: str | core.StringOut,
        topic_arn: str | core.StringOut,
        confirmation_timeout_in_minutes: int | core.IntOut | None = None,
        delivery_policy: str | core.StringOut | None = None,
        endpoint_auto_confirms: bool | core.BoolOut | None = None,
        filter_policy: str | core.StringOut | None = None,
        raw_message_delivery: bool | core.BoolOut | None = None,
        redrive_policy: str | core.StringOut | None = None,
        subscription_role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TopicSubscription.Args(
                endpoint=endpoint,
                protocol=protocol,
                topic_arn=topic_arn,
                confirmation_timeout_in_minutes=confirmation_timeout_in_minutes,
                delivery_policy=delivery_policy,
                endpoint_auto_confirms=endpoint_auto_confirms,
                filter_policy=filter_policy,
                raw_message_delivery=raw_message_delivery,
                redrive_policy=redrive_policy,
                subscription_role_arn=subscription_role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        confirmation_timeout_in_minutes: int | core.IntOut | None = core.arg(default=None)

        delivery_policy: str | core.StringOut | None = core.arg(default=None)

        endpoint: str | core.StringOut = core.arg()

        endpoint_auto_confirms: bool | core.BoolOut | None = core.arg(default=None)

        filter_policy: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        raw_message_delivery: bool | core.BoolOut | None = core.arg(default=None)

        redrive_policy: str | core.StringOut | None = core.arg(default=None)

        subscription_role_arn: str | core.StringOut | None = core.arg(default=None)

        topic_arn: str | core.StringOut = core.arg()
