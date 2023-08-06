import terrascript.core as core


@core.schema
class LaunchTemplate(core.Schema):

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                id=id,
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InstanceDefinition(core.Schema):

    instance_type: str | core.StringOut = core.attr(str)

    weighted_capacity: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_type: str | core.StringOut,
        weighted_capacity: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InstanceDefinition.Args(
                instance_type=instance_type,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_type: str | core.StringOut = core.arg()

        weighted_capacity: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TargetTrackingConfiguration(core.Schema):

    target_value: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        *,
        target_value: float | core.FloatOut,
    ):
        super().__init__(
            args=TargetTrackingConfiguration.Args(
                target_value=target_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_value: float | core.FloatOut = core.arg()


@core.schema
class AutoScalingPolicy(core.Schema):

    estimated_instance_warmup: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    target_tracking_configuration: TargetTrackingConfiguration = core.attr(
        TargetTrackingConfiguration
    )

    def __init__(
        self,
        *,
        target_tracking_configuration: TargetTrackingConfiguration,
        estimated_instance_warmup: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AutoScalingPolicy.Args(
                target_tracking_configuration=target_tracking_configuration,
                estimated_instance_warmup=estimated_instance_warmup,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        estimated_instance_warmup: int | core.IntOut | None = core.arg(default=None)

        target_tracking_configuration: TargetTrackingConfiguration = core.arg()


@core.resource(type="aws_gamelift_game_server_group", namespace="gamelift")
class GameServerGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_scaling_group_arn: str | core.StringOut = core.attr(str, computed=True)

    auto_scaling_policy: AutoScalingPolicy | None = core.attr(AutoScalingPolicy, default=None)

    balancing_strategy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    game_server_group_name: str | core.StringOut = core.attr(str)

    game_server_protection_policy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_definition: list[InstanceDefinition] | core.ArrayOut[InstanceDefinition] = core.attr(
        InstanceDefinition, kind=core.Kind.array
    )

    launch_template: LaunchTemplate = core.attr(LaunchTemplate)

    max_size: int | core.IntOut = core.attr(int)

    min_size: int | core.IntOut = core.attr(int)

    role_arn: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        game_server_group_name: str | core.StringOut,
        instance_definition: list[InstanceDefinition] | core.ArrayOut[InstanceDefinition],
        launch_template: LaunchTemplate,
        max_size: int | core.IntOut,
        min_size: int | core.IntOut,
        role_arn: str | core.StringOut,
        auto_scaling_policy: AutoScalingPolicy | None = None,
        balancing_strategy: str | core.StringOut | None = None,
        game_server_protection_policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_subnets: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GameServerGroup.Args(
                game_server_group_name=game_server_group_name,
                instance_definition=instance_definition,
                launch_template=launch_template,
                max_size=max_size,
                min_size=min_size,
                role_arn=role_arn,
                auto_scaling_policy=auto_scaling_policy,
                balancing_strategy=balancing_strategy,
                game_server_protection_policy=game_server_protection_policy,
                tags=tags,
                tags_all=tags_all,
                vpc_subnets=vpc_subnets,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_scaling_policy: AutoScalingPolicy | None = core.arg(default=None)

        balancing_strategy: str | core.StringOut | None = core.arg(default=None)

        game_server_group_name: str | core.StringOut = core.arg()

        game_server_protection_policy: str | core.StringOut | None = core.arg(default=None)

        instance_definition: list[InstanceDefinition] | core.ArrayOut[
            InstanceDefinition
        ] = core.arg()

        launch_template: LaunchTemplate = core.arg()

        max_size: int | core.IntOut = core.arg()

        min_size: int | core.IntOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_subnets: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
