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


@core.resource(type="aws_cloudfront_monitoring_subscription", namespace="aws_cloudfront")
class MonitoringSubscription(core.Resource):

    distribution_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
