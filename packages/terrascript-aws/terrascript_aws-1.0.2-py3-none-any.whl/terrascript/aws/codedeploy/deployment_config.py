import terrascript.core as core


@core.schema
class TimeBasedCanary(core.Schema):

    interval: int | core.IntOut | None = core.attr(int, default=None)

    percentage: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        interval: int | core.IntOut | None = None,
        percentage: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TimeBasedCanary.Args(
                interval=interval,
                percentage=percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: int | core.IntOut | None = core.arg(default=None)

        percentage: int | core.IntOut | None = core.arg(default=None)


@core.schema
class TimeBasedLinear(core.Schema):

    interval: int | core.IntOut | None = core.attr(int, default=None)

    percentage: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        interval: int | core.IntOut | None = None,
        percentage: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TimeBasedLinear.Args(
                interval=interval,
                percentage=percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: int | core.IntOut | None = core.arg(default=None)

        percentage: int | core.IntOut | None = core.arg(default=None)


@core.schema
class TrafficRoutingConfig(core.Schema):

    time_based_canary: TimeBasedCanary | None = core.attr(TimeBasedCanary, default=None)

    time_based_linear: TimeBasedLinear | None = core.attr(TimeBasedLinear, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        time_based_canary: TimeBasedCanary | None = None,
        time_based_linear: TimeBasedLinear | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TrafficRoutingConfig.Args(
                time_based_canary=time_based_canary,
                time_based_linear=time_based_linear,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        time_based_canary: TimeBasedCanary | None = core.arg(default=None)

        time_based_linear: TimeBasedLinear | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MinimumHealthyHosts(core.Schema):

    type: str | core.StringOut | None = core.attr(str, default=None)

    value: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        type: str | core.StringOut | None = None,
        value: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=MinimumHealthyHosts.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut | None = core.arg(default=None)

        value: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_codedeploy_deployment_config", namespace="aws_codedeploy")
class DeploymentConfig(core.Resource):

    compute_platform: str | core.StringOut | None = core.attr(str, default=None)

    deployment_config_id: str | core.StringOut = core.attr(str, computed=True)

    deployment_config_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    minimum_healthy_hosts: MinimumHealthyHosts | None = core.attr(MinimumHealthyHosts, default=None)

    traffic_routing_config: TrafficRoutingConfig | None = core.attr(
        TrafficRoutingConfig, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_config_name: str | core.StringOut,
        compute_platform: str | core.StringOut | None = None,
        minimum_healthy_hosts: MinimumHealthyHosts | None = None,
        traffic_routing_config: TrafficRoutingConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeploymentConfig.Args(
                deployment_config_name=deployment_config_name,
                compute_platform=compute_platform,
                minimum_healthy_hosts=minimum_healthy_hosts,
                traffic_routing_config=traffic_routing_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_platform: str | core.StringOut | None = core.arg(default=None)

        deployment_config_name: str | core.StringOut = core.arg()

        minimum_healthy_hosts: MinimumHealthyHosts | None = core.arg(default=None)

        traffic_routing_config: TrafficRoutingConfig | None = core.arg(default=None)
