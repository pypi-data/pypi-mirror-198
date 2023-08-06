import terrascript.core as core


@core.schema
class Alarms(core.Schema):

    alarm_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        alarm_name: str | core.StringOut,
    ):
        super().__init__(
            args=Alarms.Args(
                alarm_name=alarm_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarm_name: str | core.StringOut = core.arg()


@core.schema
class AutoRollbackConfiguration(core.Schema):

    alarms: list[Alarms] | core.ArrayOut[Alarms] | None = core.attr(
        Alarms, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        alarms: list[Alarms] | core.ArrayOut[Alarms] | None = None,
    ):
        super().__init__(
            args=AutoRollbackConfiguration.Args(
                alarms=alarms,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarms: list[Alarms] | core.ArrayOut[Alarms] | None = core.arg(default=None)


@core.schema
class LinearStepSize(core.Schema):

    type: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=LinearStepSize.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class CanarySize(core.Schema):

    type: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=CanarySize.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class TrafficRoutingConfiguration(core.Schema):

    canary_size: CanarySize | None = core.attr(CanarySize, default=None)

    linear_step_size: LinearStepSize | None = core.attr(LinearStepSize, default=None)

    type: str | core.StringOut = core.attr(str)

    wait_interval_in_seconds: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        wait_interval_in_seconds: int | core.IntOut,
        canary_size: CanarySize | None = None,
        linear_step_size: LinearStepSize | None = None,
    ):
        super().__init__(
            args=TrafficRoutingConfiguration.Args(
                type=type,
                wait_interval_in_seconds=wait_interval_in_seconds,
                canary_size=canary_size,
                linear_step_size=linear_step_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        canary_size: CanarySize | None = core.arg(default=None)

        linear_step_size: LinearStepSize | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        wait_interval_in_seconds: int | core.IntOut = core.arg()


@core.schema
class BlueGreenUpdatePolicy(core.Schema):

    maximum_execution_timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    termination_wait_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    traffic_routing_configuration: TrafficRoutingConfiguration = core.attr(
        TrafficRoutingConfiguration
    )

    def __init__(
        self,
        *,
        traffic_routing_configuration: TrafficRoutingConfiguration,
        maximum_execution_timeout_in_seconds: int | core.IntOut | None = None,
        termination_wait_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=BlueGreenUpdatePolicy.Args(
                traffic_routing_configuration=traffic_routing_configuration,
                maximum_execution_timeout_in_seconds=maximum_execution_timeout_in_seconds,
                termination_wait_in_seconds=termination_wait_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_execution_timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)

        termination_wait_in_seconds: int | core.IntOut | None = core.arg(default=None)

        traffic_routing_configuration: TrafficRoutingConfiguration = core.arg()


@core.schema
class DeploymentConfig(core.Schema):

    auto_rollback_configuration: AutoRollbackConfiguration | None = core.attr(
        AutoRollbackConfiguration, default=None
    )

    blue_green_update_policy: BlueGreenUpdatePolicy = core.attr(BlueGreenUpdatePolicy)

    def __init__(
        self,
        *,
        blue_green_update_policy: BlueGreenUpdatePolicy,
        auto_rollback_configuration: AutoRollbackConfiguration | None = None,
    ):
        super().__init__(
            args=DeploymentConfig.Args(
                blue_green_update_policy=blue_green_update_policy,
                auto_rollback_configuration=auto_rollback_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_rollback_configuration: AutoRollbackConfiguration | None = core.arg(default=None)

        blue_green_update_policy: BlueGreenUpdatePolicy = core.arg()


@core.resource(type="aws_sagemaker_endpoint", namespace="sagemaker")
class Endpoint(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The deployment configuration for an endpoint, which contains the desired deployment strat
    egy and rollback configurations. See [Deployment Config](#deployment-config).
    """
    deployment_config: DeploymentConfig | None = core.attr(DeploymentConfig, default=None)

    """
    (Required) The name of the endpoint configuration to use.
    """
    endpoint_config_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the endpoint. If omitted, Terraform will assign a random, unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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

    def __init__(
        self,
        resource_name: str,
        *,
        endpoint_config_name: str | core.StringOut,
        deployment_config: DeploymentConfig | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                endpoint_config_name=endpoint_config_name,
                deployment_config=deployment_config,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        deployment_config: DeploymentConfig | None = core.arg(default=None)

        endpoint_config_name: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
