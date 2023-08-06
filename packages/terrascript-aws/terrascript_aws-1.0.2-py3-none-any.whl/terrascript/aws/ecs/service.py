import terrascript.core as core


@core.schema
class LoadBalancer(core.Schema):

    container_name: str | core.StringOut = core.attr(str)

    container_port: int | core.IntOut = core.attr(int)

    elb_name: str | core.StringOut | None = core.attr(str, default=None)

    target_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        container_name: str | core.StringOut,
        container_port: int | core.IntOut,
        elb_name: str | core.StringOut | None = None,
        target_group_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LoadBalancer.Args(
                container_name=container_name,
                container_port=container_port,
                elb_name=elb_name,
                target_group_arn=target_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: str | core.StringOut = core.arg()

        container_port: int | core.IntOut = core.arg()

        elb_name: str | core.StringOut | None = core.arg(default=None)

        target_group_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class OrderedPlacementStrategy(core.Schema):

    field: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        field: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OrderedPlacementStrategy.Args(
                type=type,
                field=field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class DeploymentController(core.Schema):

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DeploymentController.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DeploymentCircuitBreaker(core.Schema):

    enable: bool | core.BoolOut = core.attr(bool)

    rollback: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enable: bool | core.BoolOut,
        rollback: bool | core.BoolOut,
    ):
        super().__init__(
            args=DeploymentCircuitBreaker.Args(
                enable=enable,
                rollback=rollback,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: bool | core.BoolOut = core.arg()

        rollback: bool | core.BoolOut = core.arg()


@core.schema
class PlacementConstraints(core.Schema):

    expression: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        expression: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PlacementConstraints.Args(
                type=type,
                expression=expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        expression: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class CapacityProviderStrategy(core.Schema):

    base: int | core.IntOut | None = core.attr(int, default=None)

    capacity_provider: str | core.StringOut = core.attr(str)

    weight: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        capacity_provider: str | core.StringOut,
        base: int | core.IntOut | None = None,
        weight: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                base=base,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: int | core.IntOut | None = core.arg(default=None)

        capacity_provider: str | core.StringOut = core.arg()

        weight: int | core.IntOut | None = core.arg(default=None)


@core.schema
class NetworkConfiguration(core.Schema):

    assign_public_ip: bool | core.BoolOut | None = core.attr(bool, default=None)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        subnets: list[str] | core.ArrayOut[core.StringOut],
        assign_public_ip: bool | core.BoolOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                subnets=subnets,
                assign_public_ip=assign_public_ip,
                security_groups=security_groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        assign_public_ip: bool | core.BoolOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class ServiceRegistries(core.Schema):

    container_name: str | core.StringOut | None = core.attr(str, default=None)

    container_port: int | core.IntOut | None = core.attr(int, default=None)

    port: int | core.IntOut | None = core.attr(int, default=None)

    registry_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        registry_arn: str | core.StringOut,
        container_name: str | core.StringOut | None = None,
        container_port: int | core.IntOut | None = None,
        port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ServiceRegistries.Args(
                registry_arn=registry_arn,
                container_name=container_name,
                container_port=container_port,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: str | core.StringOut | None = core.arg(default=None)

        container_port: int | core.IntOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        registry_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_ecs_service", namespace="aws_ecs")
class Service(core.Resource):

    capacity_provider_strategy: list[CapacityProviderStrategy] | core.ArrayOut[
        CapacityProviderStrategy
    ] | None = core.attr(CapacityProviderStrategy, default=None, kind=core.Kind.array)

    cluster: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    deployment_circuit_breaker: DeploymentCircuitBreaker | None = core.attr(
        DeploymentCircuitBreaker, default=None
    )

    deployment_controller: DeploymentController | None = core.attr(
        DeploymentController, default=None
    )

    deployment_maximum_percent: int | core.IntOut | None = core.attr(int, default=None)

    deployment_minimum_healthy_percent: int | core.IntOut | None = core.attr(int, default=None)

    desired_count: int | core.IntOut | None = core.attr(int, default=None)

    enable_ecs_managed_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_execute_command: bool | core.BoolOut | None = core.attr(bool, default=None)

    force_new_deployment: bool | core.BoolOut | None = core.attr(bool, default=None)

    health_check_grace_period_seconds: int | core.IntOut | None = core.attr(int, default=None)

    iam_role: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    launch_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    load_balancer: list[LoadBalancer] | core.ArrayOut[LoadBalancer] | None = core.attr(
        LoadBalancer, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    network_configuration: NetworkConfiguration | None = core.attr(
        NetworkConfiguration, default=None
    )

    ordered_placement_strategy: list[OrderedPlacementStrategy] | core.ArrayOut[
        OrderedPlacementStrategy
    ] | None = core.attr(OrderedPlacementStrategy, default=None, kind=core.Kind.array)

    placement_constraints: list[PlacementConstraints] | core.ArrayOut[
        PlacementConstraints
    ] | None = core.attr(PlacementConstraints, default=None, kind=core.Kind.array)

    platform_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    propagate_tags: str | core.StringOut | None = core.attr(str, default=None)

    scheduling_strategy: str | core.StringOut | None = core.attr(str, default=None)

    service_registries: ServiceRegistries | None = core.attr(ServiceRegistries, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    task_definition: str | core.StringOut | None = core.attr(str, default=None)

    wait_for_steady_state: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        capacity_provider_strategy: list[CapacityProviderStrategy]
        | core.ArrayOut[CapacityProviderStrategy]
        | None = None,
        cluster: str | core.StringOut | None = None,
        deployment_circuit_breaker: DeploymentCircuitBreaker | None = None,
        deployment_controller: DeploymentController | None = None,
        deployment_maximum_percent: int | core.IntOut | None = None,
        deployment_minimum_healthy_percent: int | core.IntOut | None = None,
        desired_count: int | core.IntOut | None = None,
        enable_ecs_managed_tags: bool | core.BoolOut | None = None,
        enable_execute_command: bool | core.BoolOut | None = None,
        force_new_deployment: bool | core.BoolOut | None = None,
        health_check_grace_period_seconds: int | core.IntOut | None = None,
        iam_role: str | core.StringOut | None = None,
        launch_type: str | core.StringOut | None = None,
        load_balancer: list[LoadBalancer] | core.ArrayOut[LoadBalancer] | None = None,
        network_configuration: NetworkConfiguration | None = None,
        ordered_placement_strategy: list[OrderedPlacementStrategy]
        | core.ArrayOut[OrderedPlacementStrategy]
        | None = None,
        placement_constraints: list[PlacementConstraints]
        | core.ArrayOut[PlacementConstraints]
        | None = None,
        platform_version: str | core.StringOut | None = None,
        propagate_tags: str | core.StringOut | None = None,
        scheduling_strategy: str | core.StringOut | None = None,
        service_registries: ServiceRegistries | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        task_definition: str | core.StringOut | None = None,
        wait_for_steady_state: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Service.Args(
                name=name,
                capacity_provider_strategy=capacity_provider_strategy,
                cluster=cluster,
                deployment_circuit_breaker=deployment_circuit_breaker,
                deployment_controller=deployment_controller,
                deployment_maximum_percent=deployment_maximum_percent,
                deployment_minimum_healthy_percent=deployment_minimum_healthy_percent,
                desired_count=desired_count,
                enable_ecs_managed_tags=enable_ecs_managed_tags,
                enable_execute_command=enable_execute_command,
                force_new_deployment=force_new_deployment,
                health_check_grace_period_seconds=health_check_grace_period_seconds,
                iam_role=iam_role,
                launch_type=launch_type,
                load_balancer=load_balancer,
                network_configuration=network_configuration,
                ordered_placement_strategy=ordered_placement_strategy,
                placement_constraints=placement_constraints,
                platform_version=platform_version,
                propagate_tags=propagate_tags,
                scheduling_strategy=scheduling_strategy,
                service_registries=service_registries,
                tags=tags,
                tags_all=tags_all,
                task_definition=task_definition,
                wait_for_steady_state=wait_for_steady_state,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_provider_strategy: list[CapacityProviderStrategy] | core.ArrayOut[
            CapacityProviderStrategy
        ] | None = core.arg(default=None)

        cluster: str | core.StringOut | None = core.arg(default=None)

        deployment_circuit_breaker: DeploymentCircuitBreaker | None = core.arg(default=None)

        deployment_controller: DeploymentController | None = core.arg(default=None)

        deployment_maximum_percent: int | core.IntOut | None = core.arg(default=None)

        deployment_minimum_healthy_percent: int | core.IntOut | None = core.arg(default=None)

        desired_count: int | core.IntOut | None = core.arg(default=None)

        enable_ecs_managed_tags: bool | core.BoolOut | None = core.arg(default=None)

        enable_execute_command: bool | core.BoolOut | None = core.arg(default=None)

        force_new_deployment: bool | core.BoolOut | None = core.arg(default=None)

        health_check_grace_period_seconds: int | core.IntOut | None = core.arg(default=None)

        iam_role: str | core.StringOut | None = core.arg(default=None)

        launch_type: str | core.StringOut | None = core.arg(default=None)

        load_balancer: list[LoadBalancer] | core.ArrayOut[LoadBalancer] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        network_configuration: NetworkConfiguration | None = core.arg(default=None)

        ordered_placement_strategy: list[OrderedPlacementStrategy] | core.ArrayOut[
            OrderedPlacementStrategy
        ] | None = core.arg(default=None)

        placement_constraints: list[PlacementConstraints] | core.ArrayOut[
            PlacementConstraints
        ] | None = core.arg(default=None)

        platform_version: str | core.StringOut | None = core.arg(default=None)

        propagate_tags: str | core.StringOut | None = core.arg(default=None)

        scheduling_strategy: str | core.StringOut | None = core.arg(default=None)

        service_registries: ServiceRegistries | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        task_definition: str | core.StringOut | None = core.arg(default=None)

        wait_for_steady_state: bool | core.BoolOut | None = core.arg(default=None)
