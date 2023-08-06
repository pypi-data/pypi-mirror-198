import terrascript.core as core


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
class CapacityProviderStrategy(core.Schema):

    base: int | core.IntOut | None = core.attr(int, default=None)

    capacity_provider: str | core.StringOut = core.attr(str)

    weight: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        capacity_provider: str | core.StringOut,
        weight: int | core.IntOut,
        base: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                weight=weight,
                base=base,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: int | core.IntOut | None = core.arg(default=None)

        capacity_provider: str | core.StringOut = core.arg()

        weight: int | core.IntOut = core.arg()


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


@core.schema
class LoadBalancer(core.Schema):

    container_name: str | core.StringOut = core.attr(str)

    container_port: int | core.IntOut | None = core.attr(int, default=None)

    load_balancer_name: str | core.StringOut | None = core.attr(str, default=None)

    target_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        container_name: str | core.StringOut,
        container_port: int | core.IntOut | None = None,
        load_balancer_name: str | core.StringOut | None = None,
        target_group_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LoadBalancer.Args(
                container_name=container_name,
                container_port=container_port,
                load_balancer_name=load_balancer_name,
                target_group_arn=target_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: str | core.StringOut = core.arg()

        container_port: int | core.IntOut | None = core.arg(default=None)

        load_balancer_name: str | core.StringOut | None = core.arg(default=None)

        target_group_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Scale(core.Schema):

    unit: str | core.StringOut | None = core.attr(str, default=None)

    value: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        unit: str | core.StringOut | None = None,
        value: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=Scale.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: str | core.StringOut | None = core.arg(default=None)

        value: float | core.FloatOut | None = core.arg(default=None)


@core.resource(type="aws_ecs_task_set", namespace="ecs")
class TaskSet(core.Resource):
    """
    The Amazon Resource Name (ARN) that identifies the task set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The capacity provider strategy to use for the service. Can be one or more.  [Defined belo
    w](#capacity_provider_strategy).
    """
    capacity_provider_strategy: list[CapacityProviderStrategy] | core.ArrayOut[
        CapacityProviderStrategy
    ] | None = core.attr(CapacityProviderStrategy, default=None, kind=core.Kind.array)

    """
    (Required) The short name or ARN of the cluster that hosts the service to create the task set in.
    """
    cluster: str | core.StringOut = core.attr(str)

    """
    (Optional) The external ID associated with the task set.
    """
    external_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether to allow deleting the task set without waiting for scaling down to 0. You can for
    ce a task set to delete even if it's in the process of scaling a resource. Normally, Terraform drain
    s all the tasks before deleting the task set. This bypasses that behavior and potentially leaves res
    ources dangling.
    """
    force_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The `task_set_id`, `service` and `cluster` separated by commas (`,`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The launch type on which to run your service. The valid values are `EC2`, `FARGATE`, and
    EXTERNAL`. Defaults to `EC2`.
    """
    launch_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Details on load balancers that are used with a task set. [Detailed below](#load_balancer)
    .
    """
    load_balancer: list[LoadBalancer] | core.ArrayOut[LoadBalancer] | None = core.attr(
        LoadBalancer, default=None, kind=core.Kind.array
    )

    """
    (Optional) The network configuration for the service. This parameter is required for task definition
    s that use the `awsvpc` network mode to receive their own Elastic Network Interface, and it is not s
    upported for other network modes. [Detailed below](#network_configuration).
    """
    network_configuration: NetworkConfiguration | None = core.attr(
        NetworkConfiguration, default=None
    )

    """
    (Optional) The platform version on which to run your service. Only applicable for `launch_type` set
    to `FARGATE`. Defaults to `LATEST`. More information about Fargate platform versions can be found in
    the [AWS ECS User Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versi
    ons.html).
    """
    platform_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A floating-point percentage of the desired number of tasks to place and keep running in t
    he task set. [Detailed below](#scale).
    """
    scale: Scale | None = core.attr(Scale, default=None, computed=True)

    """
    (Required) The short name or ARN of the ECS service.
    """
    service: str | core.StringOut = core.attr(str)

    """
    (Optional) The service discovery registries for the service. The maximum number of `service_registri
    es` blocks is `1`. [Detailed below](#service_registries).
    """
    service_registries: ServiceRegistries | None = core.attr(ServiceRegistries, default=None)

    """
    The stability status. This indicates whether the task set has reached a steady state.
    """
    stability_status: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of the task set.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the file system. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level. If you have set `copy_tags_to_backups` to true, and you specify one or more tags, no existing
    file system tags are copied from the file system to the backup.
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
    (Required) The family and revision (`family:revision`) or full ARN of the task definition that you w
    ant to run in your service.
    """
    task_definition: str | core.StringOut = core.attr(str)

    """
    The ID of the task set.
    """
    task_set_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether `terraform` should wait until the task set has reached `STEADY_STATE`.
    """
    wait_until_stable: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Wait timeout for task set to reach `STEADY_STATE`. Valid time units include `ns`, `us` (o
    r `µs`), `ms`, `s`, `m`, and `h`. Default `10m`.
    """
    wait_until_stable_timeout: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster: str | core.StringOut,
        service: str | core.StringOut,
        task_definition: str | core.StringOut,
        capacity_provider_strategy: list[CapacityProviderStrategy]
        | core.ArrayOut[CapacityProviderStrategy]
        | None = None,
        external_id: str | core.StringOut | None = None,
        force_delete: bool | core.BoolOut | None = None,
        launch_type: str | core.StringOut | None = None,
        load_balancer: list[LoadBalancer] | core.ArrayOut[LoadBalancer] | None = None,
        network_configuration: NetworkConfiguration | None = None,
        platform_version: str | core.StringOut | None = None,
        scale: Scale | None = None,
        service_registries: ServiceRegistries | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        wait_until_stable: bool | core.BoolOut | None = None,
        wait_until_stable_timeout: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TaskSet.Args(
                cluster=cluster,
                service=service,
                task_definition=task_definition,
                capacity_provider_strategy=capacity_provider_strategy,
                external_id=external_id,
                force_delete=force_delete,
                launch_type=launch_type,
                load_balancer=load_balancer,
                network_configuration=network_configuration,
                platform_version=platform_version,
                scale=scale,
                service_registries=service_registries,
                tags=tags,
                tags_all=tags_all,
                wait_until_stable=wait_until_stable,
                wait_until_stable_timeout=wait_until_stable_timeout,
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

        cluster: str | core.StringOut = core.arg()

        external_id: str | core.StringOut | None = core.arg(default=None)

        force_delete: bool | core.BoolOut | None = core.arg(default=None)

        launch_type: str | core.StringOut | None = core.arg(default=None)

        load_balancer: list[LoadBalancer] | core.ArrayOut[LoadBalancer] | None = core.arg(
            default=None
        )

        network_configuration: NetworkConfiguration | None = core.arg(default=None)

        platform_version: str | core.StringOut | None = core.arg(default=None)

        scale: Scale | None = core.arg(default=None)

        service: str | core.StringOut = core.arg()

        service_registries: ServiceRegistries | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        task_definition: str | core.StringOut = core.arg()

        wait_until_stable: bool | core.BoolOut | None = core.arg(default=None)

        wait_until_stable_timeout: str | core.StringOut | None = core.arg(default=None)
