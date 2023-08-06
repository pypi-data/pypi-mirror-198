import terrascript.core as core


@core.schema
class LaunchTemplate(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        name: str | core.StringOut,
        version: str | core.StringOut,
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
        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        version: str | core.StringOut = core.arg()


@core.data(type="aws_autoscaling_group", namespace="autoscaling")
class DsGroup(core.Data):
    """
    The Amazon Resource Name (ARN) of the Auto Scaling group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    One or more Availability Zones for the group.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    default_cooldown: int | core.IntOut = core.attr(int, computed=True)

    """
    The desired size of the group.
    """
    desired_capacity: int | core.IntOut = core.attr(int, computed=True)

    """
    The list of metrics enabled for collection.
    """
    enabled_metrics: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status
    of an EC2 instance that has come into service.
    """
    health_check_grace_period: int | core.IntOut = core.attr(int, computed=True)

    """
    The service to use for the health checks. The valid values are EC2 and ELB.
    """
    health_check_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the Auto Scaling Group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the associated launch configuration.
    """
    launch_configuration: str | core.StringOut = core.attr(str, computed=True)

    launch_template: list[LaunchTemplate] | core.ArrayOut[LaunchTemplate] = core.attr(
        LaunchTemplate, computed=True, kind=core.Kind.array
    )

    """
    One or more load balancers associated with the group.
    """
    load_balancers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The maximum size of the group.
    """
    max_size: int | core.IntOut = core.attr(int, computed=True)

    """
    The minimum size of the group.
    """
    min_size: int | core.IntOut = core.attr(int, computed=True)

    """
    Specify the exact name of the desired autoscaling group.
    """
    name: str | core.StringOut = core.attr(str)

    new_instances_protected_from_scale_in: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The name of the placement group into which to launch your instances, if any. For more information, s
    ee Placement Groups (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in th
    e Amazon Elastic Compute Cloud User Guide.
    """
    placement_group: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call o
    ther AWS services on your behalf.
    """
    service_linked_role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The current state of the group when DeleteAutoScalingGroup is in progress.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Names (ARN) of the target groups for your load balancer.
    """
    target_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The termination policies for the group.
    """
    termination_policies: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    VPC ID for the group.
    """
    vpc_zone_identifier: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsGroup.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
