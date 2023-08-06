import terrascript.core as core


@core.resource(type="aws_sns_topic_subscription", namespace="aws_sns")
class TopicSubscription(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    confirmation_timeout_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    confirmation_was_authenticated: bool | core.BoolOut = core.attr(bool, computed=True)

    delivery_policy: str | core.StringOut | None = core.attr(str, default=None)

    endpoint: str | core.StringOut = core.attr(str)

    endpoint_auto_confirms: bool | core.BoolOut | None = core.attr(bool, default=None)

    filter_policy: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    pending_confirmation: bool | core.BoolOut = core.attr(bool, computed=True)

    protocol: str | core.StringOut = core.attr(str)

    raw_message_delivery: bool | core.BoolOut | None = core.attr(bool, default=None)

    redrive_policy: str | core.StringOut | None = core.attr(str, default=None)

    subscription_role_arn: str | core.StringOut | None = core.attr(str, default=None)

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
