import terrascript.core as core


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


@core.resource(type="aws_ecs_service", namespace="ecs")
class Service(core.Resource):
    """
    (Optional) Capacity provider strategies to use for the service. Can be one or more. These can be upd
    ated without destroying and recreating the service only if `force_new_deployment = true` and not cha
    nging from 0 `capacity_provider_strategy` blocks to greater than 0, or vice versa. See below.
    """

    capacity_provider_strategy: list[CapacityProviderStrategy] | core.ArrayOut[
        CapacityProviderStrategy
    ] | None = core.attr(CapacityProviderStrategy, default=None, kind=core.Kind.array)

    """
    (Optional) ARN of an ECS cluster.
    """
    cluster: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for deployment circuit breaker. See below.
    """
    deployment_circuit_breaker: DeploymentCircuitBreaker | None = core.attr(
        DeploymentCircuitBreaker, default=None
    )

    """
    (Optional) Configuration block for deployment controller configuration. See below.
    """
    deployment_controller: DeploymentController | None = core.attr(
        DeploymentController, default=None
    )

    """
    (Optional) Upper limit (as a percentage of the service's desiredCount) of the number of running task
    s that can be running in a service during a deployment. Not valid when using the `DAEMON` scheduling
    strategy.
    """
    deployment_maximum_percent: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Lower limit (as a percentage of the service's desiredCount) of the number of running task
    s that must remain running and healthy in a service during a deployment.
    """
    deployment_minimum_healthy_percent: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Number of instances of the task definition to place and keep running. Defaults to 0. Do n
    ot specify if using the `DAEMON` scheduling strategy.
    """
    desired_count: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Specifies whether to enable Amazon ECS managed tags for the tasks within the service.
    """
    enable_ecs_managed_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether to enable Amazon ECS Exec for the tasks within the service.
    """
    enable_execute_command: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enable to force a new task deployment of the service. This can be used to update tasks to
    use a newer Docker image with same image/tag combination (e.g., `myimage:latest`), roll Fargate tas
    ks onto a newer platform version, or immediately deploy `ordered_placement_strategy` and `placement_
    constraints` updates.
    """
    force_new_deployment: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Seconds to ignore failing load balancer health checks on newly instantiated tasks to prev
    ent premature shutdown, up to 2147483647. Only valid for services configured to use load balancers.
    """
    health_check_grace_period_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your be
    half. This parameter is required if you are using a load balancer with your service, but only if you
    r task definition does not use the `awsvpc` network mode. If using `awsvpc` network mode, do not spe
    cify this role. If your account has already created the Amazon ECS service-linked role, that role is
    used by default for your service unless you specify a role here.
    """
    iam_role: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    ARN that identifies the service.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Launch type on which to run your service. The valid values are `EC2`, `FARGATE`, and `EXT
    ERNAL`. Defaults to `EC2`.
    """
    launch_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for load balancers. See below.
    """
    load_balancer: list[LoadBalancer] | core.ArrayOut[LoadBalancer] | None = core.attr(
        LoadBalancer, default=None, kind=core.Kind.array
    )

    """
    (Required) Name of the service (up to 255 letters, numbers, hyphens, and underscores)
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Network configuration for the service. This parameter is required for task definitions th
    at use the `awsvpc` network mode to receive their own Elastic Network Interface, and it is not suppo
    rted for other network modes. See below.
    """
    network_configuration: NetworkConfiguration | None = core.attr(
        NetworkConfiguration, default=None
    )

    """
    (Optional) Service level strategy rules that are taken into consideration during task placement. Lis
    t from top to bottom in order of precedence. Updates to this configuration will take effect next tas
    k deployment unless `force_new_deployment` is enabled. The maximum number of `ordered_placement_stra
    tegy` blocks is `5`. See below.
    """
    ordered_placement_strategy: list[OrderedPlacementStrategy] | core.ArrayOut[
        OrderedPlacementStrategy
    ] | None = core.attr(OrderedPlacementStrategy, default=None, kind=core.Kind.array)

    """
    (Optional) Rules that are taken into consideration during task placement. Updates to this configurat
    ion will take effect next task deployment unless `force_new_deployment` is enabled. Maximum number o
    f `placement_constraints` is `10`. See below.
    """
    placement_constraints: list[PlacementConstraints] | core.ArrayOut[
        PlacementConstraints
    ] | None = core.attr(PlacementConstraints, default=None, kind=core.Kind.array)

    """
    (Optional) Platform version on which to run your service. Only applicable for `launch_type` set to `
    FARGATE`. Defaults to `LATEST`. More information about Fargate platform versions can be found in the
    [AWS ECS User Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.
    html).
    """
    platform_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies whether to propagate the tags from the task definition or the service to the ta
    sks. The valid values are `SERVICE` and `TASK_DEFINITION`.
    """
    propagate_tags: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Scheduling strategy to use for the service. The valid values are `REPLICA` and `DAEMON`.
    Defaults to `REPLICA`. Note that [*Tasks using the Fargate launch type or the `CODE_DEPLOY` or `EXTE
    RNAL` deployment controller types don't support the `DAEMON` scheduling strategy*](https://docs.aws.
    amazon.com/AmazonECS/latest/APIReference/API_CreateService.html).
    """
    scheduling_strategy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Service discovery registries for the service. The maximum number of `service_registries`
    blocks is `1`. See below.
    """
    service_registries: ServiceRegistries | None = core.attr(ServiceRegistries, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) Family and revision (`family:revision`) or full ARN of the task definition that you want
    to run in your service. Required unless using the `EXTERNAL` deployment controller. If a revision is
    not specified, the latest `ACTIVE` revision is used.
    """
    task_definition: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) If `true`, Terraform will wait for the service to reach a steady state (like [`aws ecs wa
    it services-stable`](https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html)
    ) before continuing. Default `false`.
    """
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
