import terrascript.core as core


@core.schema
class RealtimeMetricsSubscriptionConfig(core.Schema):

    realtime_metrics_subscription_status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        realtime_metrics_subscription_status: str | core.StringOut,
    ):
        super().__init__(
            args=RealtimeMetricsSubscriptionConfig.Args(
                realtime_metrics_subscription_status=realtime_metrics_subscription_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        realtime_metrics_subscription_status: str | core.StringOut = core.arg()


@core.schema
class MonitoringSubscriptionBlk(core.Schema):

    realtime_metrics_subscription_config: RealtimeMetricsSubscriptionConfig = core.attr(
        RealtimeMetricsSubscriptionConfig
    )

    def __init__(
        self,
        *,
        realtime_metrics_subscription_config: RealtimeMetricsSubscriptionConfig,
    ):
        super().__init__(
            args=MonitoringSubscriptionBlk.Args(
                realtime_metrics_subscription_config=realtime_metrics_subscription_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        realtime_metrics_subscription_config: RealtimeMetricsSubscriptionConfig = core.arg()


@core.resource(type="aws_cloudfront_monitoring_subscription", namespace="cloudfront")
class MonitoringSubscription(core.Resource):
    """
    (Required) The ID of the distribution that you are enabling metrics for.
    """

    distribution_id: str | core.StringOut = core.attr(str)

    """
    The ID of the CloudFront monitoring subscription, which corresponds to the `distribution_id`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A monitoring subscription. This structure contains information about whether additional C
    loudWatch metrics are enabled for a given CloudFront distribution.
    """
    monitoring_subscription: MonitoringSubscriptionBlk = core.attr(MonitoringSubscriptionBlk)

    def __init__(
        self,
        resource_name: str,
        *,
        distribution_id: str | core.StringOut,
        monitoring_subscription: MonitoringSubscriptionBlk,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MonitoringSubscription.Args(
                distribution_id=distribution_id,
                monitoring_subscription=monitoring_subscription,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        distribution_id: str | core.StringOut = core.arg()

        monitoring_subscription: MonitoringSubscriptionBlk = core.arg()
