import terrascript.core as core


@core.schema
class Ec2Configuration(core.Schema):

    image_id_override: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    image_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        image_id_override: str | core.StringOut | None = None,
        image_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Ec2Configuration.Args(
                image_id_override=image_id_override,
                image_type=image_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_id_override: str | core.StringOut | None = core.arg(default=None)

        image_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LaunchTemplate(core.Schema):

    launch_template_id: str | core.StringOut | None = core.attr(str, default=None)

    launch_template_name: str | core.StringOut | None = core.attr(str, default=None)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        launch_template_id: str | core.StringOut | None = None,
        launch_template_name: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: str | core.StringOut | None = core.arg(default=None)

        launch_template_name: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ComputeResources(core.Schema):

    allocation_strategy: str | core.StringOut | None = core.attr(str, default=None)

    bid_percentage: int | core.IntOut | None = core.attr(int, default=None)

    desired_vcpus: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    ec2_configuration: Ec2Configuration | None = core.attr(
        Ec2Configuration, default=None, computed=True
    )

    ec2_key_pair: str | core.StringOut | None = core.attr(str, default=None)

    image_id: str | core.StringOut | None = core.attr(str, default=None)

    instance_role: str | core.StringOut | None = core.attr(str, default=None)

    instance_type: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    launch_template: LaunchTemplate | None = core.attr(LaunchTemplate, default=None)

    max_vcpus: int | core.IntOut = core.attr(int)

    min_vcpus: int | core.IntOut | None = core.attr(int, default=None)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    spot_iam_fleet_role: str | core.StringOut | None = core.attr(str, default=None)

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        max_vcpus: int | core.IntOut,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnets: list[str] | core.ArrayOut[core.StringOut],
        type: str | core.StringOut,
        allocation_strategy: str | core.StringOut | None = None,
        bid_percentage: int | core.IntOut | None = None,
        desired_vcpus: int | core.IntOut | None = None,
        ec2_configuration: Ec2Configuration | None = None,
        ec2_key_pair: str | core.StringOut | None = None,
        image_id: str | core.StringOut | None = None,
        instance_role: str | core.StringOut | None = None,
        instance_type: list[str] | core.ArrayOut[core.StringOut] | None = None,
        launch_template: LaunchTemplate | None = None,
        min_vcpus: int | core.IntOut | None = None,
        spot_iam_fleet_role: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=ComputeResources.Args(
                max_vcpus=max_vcpus,
                security_group_ids=security_group_ids,
                subnets=subnets,
                type=type,
                allocation_strategy=allocation_strategy,
                bid_percentage=bid_percentage,
                desired_vcpus=desired_vcpus,
                ec2_configuration=ec2_configuration,
                ec2_key_pair=ec2_key_pair,
                image_id=image_id,
                instance_role=instance_role,
                instance_type=instance_type,
                launch_template=launch_template,
                min_vcpus=min_vcpus,
                spot_iam_fleet_role=spot_iam_fleet_role,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: str | core.StringOut | None = core.arg(default=None)

        bid_percentage: int | core.IntOut | None = core.arg(default=None)

        desired_vcpus: int | core.IntOut | None = core.arg(default=None)

        ec2_configuration: Ec2Configuration | None = core.arg(default=None)

        ec2_key_pair: str | core.StringOut | None = core.arg(default=None)

        image_id: str | core.StringOut | None = core.arg(default=None)

        instance_role: str | core.StringOut | None = core.arg(default=None)

        instance_type: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        launch_template: LaunchTemplate | None = core.arg(default=None)

        max_vcpus: int | core.IntOut = core.arg()

        min_vcpus: int | core.IntOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        spot_iam_fleet_role: str | core.StringOut | None = core.arg(default=None)

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_batch_compute_environment", namespace="batch")
class ComputeEnvironment(core.Resource):
    """
    The Amazon Resource Name (ARN) of the compute environment.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The name for your compute environment. Up to 128 letters (uppercase
    and lowercase), numbers, and underscores are allowed. If omitted, Terraform will assign a random, un
    ique name.
    """
    compute_environment_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Forces new resource) Creates a unique compute environment name beginning with the specifi
    ed prefix. Conflicts with `compute_environment_name`.
    """
    compute_environment_name_prefix: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Details of the compute resources managed by the compute environment. This parameter is re
    quired for managed compute environments. See details below.
    """
    compute_resources: ComputeResources | None = core.attr(ComputeResources, default=None)

    """
    The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.
    """
    ecs_cluster_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls t
    o other AWS services on your behalf.
    """
    service_role: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The state of the compute environment. If the state is `ENABLED`, then the compute environ
    ment accepts jobs from a queue and can scale out automatically based on queues. Valid items are `ENA
    BLED` or `DISABLED`. Defaults to `ENABLED`.
    """
    state: str | core.StringOut | None = core.attr(str, default=None)

    """
    The current status of the compute environment (for example, CREATING or VALID).
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    A short, human-readable string to provide additional details about the current status of the compute
    environment.
    """
    status_reason: str | core.StringOut = core.attr(str, computed=True)

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
    (Required) The type of the compute environment. Valid items are `MANAGED` or `UNMANAGED`.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        type: str | core.StringOut,
        compute_environment_name: str | core.StringOut | None = None,
        compute_environment_name_prefix: str | core.StringOut | None = None,
        compute_resources: ComputeResources | None = None,
        service_role: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ComputeEnvironment.Args(
                type=type,
                compute_environment_name=compute_environment_name,
                compute_environment_name_prefix=compute_environment_name_prefix,
                compute_resources=compute_resources,
                service_role=service_role,
                state=state,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_environment_name: str | core.StringOut | None = core.arg(default=None)

        compute_environment_name_prefix: str | core.StringOut | None = core.arg(default=None)

        compute_resources: ComputeResources | None = core.arg(default=None)

        service_role: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
