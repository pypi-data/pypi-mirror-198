import terrascript.core as core


@core.schema
class OnPremisesInstanceTagFilter(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OnPremisesInstanceTagFilter.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DeploymentStyle(core.Schema):

    deployment_option: str | core.StringOut | None = core.attr(str, default=None)

    deployment_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        deployment_option: str | core.StringOut | None = None,
        deployment_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DeploymentStyle.Args(
                deployment_option=deployment_option,
                deployment_type=deployment_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        deployment_option: str | core.StringOut | None = core.arg(default=None)

        deployment_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DeploymentReadyOption(core.Schema):

    action_on_timeout: str | core.StringOut | None = core.attr(str, default=None)

    wait_time_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        action_on_timeout: str | core.StringOut | None = None,
        wait_time_in_minutes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DeploymentReadyOption.Args(
                action_on_timeout=action_on_timeout,
                wait_time_in_minutes=wait_time_in_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_on_timeout: str | core.StringOut | None = core.arg(default=None)

        wait_time_in_minutes: int | core.IntOut | None = core.arg(default=None)


@core.schema
class GreenFleetProvisioningOption(core.Schema):

    action: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        action: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=GreenFleetProvisioningOption.Args(
                action=action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TerminateBlueInstancesOnDeploymentSuccess(core.Schema):

    action: str | core.StringOut | None = core.attr(str, default=None)

    termination_wait_time_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        action: str | core.StringOut | None = None,
        termination_wait_time_in_minutes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TerminateBlueInstancesOnDeploymentSuccess.Args(
                action=action,
                termination_wait_time_in_minutes=termination_wait_time_in_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut | None = core.arg(default=None)

        termination_wait_time_in_minutes: int | core.IntOut | None = core.arg(default=None)


@core.schema
class BlueGreenDeploymentConfig(core.Schema):

    deployment_ready_option: DeploymentReadyOption | None = core.attr(
        DeploymentReadyOption, default=None
    )

    green_fleet_provisioning_option: GreenFleetProvisioningOption | None = core.attr(
        GreenFleetProvisioningOption, default=None, computed=True
    )

    terminate_blue_instances_on_deployment_success: TerminateBlueInstancesOnDeploymentSuccess | None = core.attr(
        TerminateBlueInstancesOnDeploymentSuccess, default=None
    )

    def __init__(
        self,
        *,
        deployment_ready_option: DeploymentReadyOption | None = None,
        green_fleet_provisioning_option: GreenFleetProvisioningOption | None = None,
        terminate_blue_instances_on_deployment_success: TerminateBlueInstancesOnDeploymentSuccess
        | None = None,
    ):
        super().__init__(
            args=BlueGreenDeploymentConfig.Args(
                deployment_ready_option=deployment_ready_option,
                green_fleet_provisioning_option=green_fleet_provisioning_option,
                terminate_blue_instances_on_deployment_success=terminate_blue_instances_on_deployment_success,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        deployment_ready_option: DeploymentReadyOption | None = core.arg(default=None)

        green_fleet_provisioning_option: GreenFleetProvisioningOption | None = core.arg(
            default=None
        )

        terminate_blue_instances_on_deployment_success: TerminateBlueInstancesOnDeploymentSuccess | None = core.arg(
            default=None
        )


@core.schema
class TargetGroupInfo(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TargetGroupInfo.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ProdTrafficRoute(core.Schema):

    listener_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        listener_arns: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=ProdTrafficRoute.Args(
                listener_arns=listener_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        listener_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class TargetGroup(core.Schema):

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=TargetGroup.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class TestTrafficRoute(core.Schema):

    listener_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        listener_arns: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=TestTrafficRoute.Args(
                listener_arns=listener_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        listener_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class TargetGroupPairInfo(core.Schema):

    prod_traffic_route: ProdTrafficRoute = core.attr(ProdTrafficRoute)

    target_group: list[TargetGroup] | core.ArrayOut[TargetGroup] = core.attr(
        TargetGroup, kind=core.Kind.array
    )

    test_traffic_route: TestTrafficRoute | None = core.attr(TestTrafficRoute, default=None)

    def __init__(
        self,
        *,
        prod_traffic_route: ProdTrafficRoute,
        target_group: list[TargetGroup] | core.ArrayOut[TargetGroup],
        test_traffic_route: TestTrafficRoute | None = None,
    ):
        super().__init__(
            args=TargetGroupPairInfo.Args(
                prod_traffic_route=prod_traffic_route,
                target_group=target_group,
                test_traffic_route=test_traffic_route,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prod_traffic_route: ProdTrafficRoute = core.arg()

        target_group: list[TargetGroup] | core.ArrayOut[TargetGroup] = core.arg()

        test_traffic_route: TestTrafficRoute | None = core.arg(default=None)


@core.schema
class ElbInfo(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ElbInfo.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LoadBalancerInfo(core.Schema):

    elb_info: list[ElbInfo] | core.ArrayOut[ElbInfo] | None = core.attr(
        ElbInfo, default=None, kind=core.Kind.array
    )

    target_group_info: list[TargetGroupInfo] | core.ArrayOut[TargetGroupInfo] | None = core.attr(
        TargetGroupInfo, default=None, kind=core.Kind.array
    )

    target_group_pair_info: TargetGroupPairInfo | None = core.attr(
        TargetGroupPairInfo, default=None
    )

    def __init__(
        self,
        *,
        elb_info: list[ElbInfo] | core.ArrayOut[ElbInfo] | None = None,
        target_group_info: list[TargetGroupInfo] | core.ArrayOut[TargetGroupInfo] | None = None,
        target_group_pair_info: TargetGroupPairInfo | None = None,
    ):
        super().__init__(
            args=LoadBalancerInfo.Args(
                elb_info=elb_info,
                target_group_info=target_group_info,
                target_group_pair_info=target_group_pair_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        elb_info: list[ElbInfo] | core.ArrayOut[ElbInfo] | None = core.arg(default=None)

        target_group_info: list[TargetGroupInfo] | core.ArrayOut[TargetGroupInfo] | None = core.arg(
            default=None
        )

        target_group_pair_info: TargetGroupPairInfo | None = core.arg(default=None)


@core.schema
class Ec2TagFilter(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Ec2TagFilter.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Ec2TagSet(core.Schema):

    ec2_tag_filter: list[Ec2TagFilter] | core.ArrayOut[Ec2TagFilter] | None = core.attr(
        Ec2TagFilter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ec2_tag_filter: list[Ec2TagFilter] | core.ArrayOut[Ec2TagFilter] | None = None,
    ):
        super().__init__(
            args=Ec2TagSet.Args(
                ec2_tag_filter=ec2_tag_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ec2_tag_filter: list[Ec2TagFilter] | core.ArrayOut[Ec2TagFilter] | None = core.arg(
            default=None
        )


@core.schema
class AlarmConfiguration(core.Schema):

    alarms: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    ignore_poll_alarm_failure: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        alarms: list[str] | core.ArrayOut[core.StringOut] | None = None,
        enabled: bool | core.BoolOut | None = None,
        ignore_poll_alarm_failure: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=AlarmConfiguration.Args(
                alarms=alarms,
                enabled=enabled,
                ignore_poll_alarm_failure=ignore_poll_alarm_failure,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarms: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        ignore_poll_alarm_failure: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class TriggerConfiguration(core.Schema):

    trigger_events: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    trigger_name: str | core.StringOut = core.attr(str)

    trigger_target_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        trigger_events: list[str] | core.ArrayOut[core.StringOut],
        trigger_name: str | core.StringOut,
        trigger_target_arn: str | core.StringOut,
    ):
        super().__init__(
            args=TriggerConfiguration.Args(
                trigger_events=trigger_events,
                trigger_name=trigger_name,
                trigger_target_arn=trigger_target_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        trigger_events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        trigger_name: str | core.StringOut = core.arg()

        trigger_target_arn: str | core.StringOut = core.arg()


@core.schema
class AutoRollbackConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        events: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AutoRollbackConfiguration.Args(
                enabled=enabled,
                events=events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class EcsService(core.Schema):

    cluster_name: str | core.StringOut = core.attr(str)

    service_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cluster_name: str | core.StringOut,
        service_name: str | core.StringOut,
    ):
        super().__init__(
            args=EcsService.Args(
                cluster_name=cluster_name,
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: str | core.StringOut = core.arg()

        service_name: str | core.StringOut = core.arg()


@core.resource(type="aws_codedeploy_deployment_group", namespace="codedeploy")
class DeploymentGroup(core.Resource):
    """
    (Optional) Configuration block of alarms associated with the deployment group (documented below).
    """

    alarm_configuration: AlarmConfiguration | None = core.attr(AlarmConfiguration, default=None)

    """
    (Required) The name of the application.
    """
    app_name: str | core.StringOut = core.attr(str)

    """
    The ARN of the CodeDeploy deployment group.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block of the automatic rollback configuration associated with the deploymen
    t group (documented below).
    """
    auto_rollback_configuration: AutoRollbackConfiguration | None = core.attr(
        AutoRollbackConfiguration, default=None
    )

    """
    (Optional) Autoscaling groups associated with the deployment group.
    """
    autoscaling_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block of the blue/green deployment options for a deployment group (document
    ed below).
    """
    blue_green_deployment_config: BlueGreenDeploymentConfig | None = core.attr(
        BlueGreenDeploymentConfig, default=None, computed=True
    )

    """
    The destination platform type for the deployment.
    """
    compute_platform: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".
    """
    deployment_config_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the CodeDeploy deployment group.
    """
    deployment_group_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the deployment group.
    """
    deployment_group_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block of the type of deployment, either in-place or blue/green, you want to
    run and whether to route deployment traffic behind a load balancer (documented below).
    """
    deployment_style: DeploymentStyle | None = core.attr(DeploymentStyle, default=None)

    """
    (Optional) Tag filters associated with the deployment group. See the AWS docs for details.
    """
    ec2_tag_filter: list[Ec2TagFilter] | core.ArrayOut[Ec2TagFilter] | None = core.attr(
        Ec2TagFilter, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) of Tag filters associated with the deployment group, which are als
    o referred to as tag groups (documented below). See the AWS docs for details.
    """
    ec2_tag_set: list[Ec2TagSet] | core.ArrayOut[Ec2TagSet] | None = core.attr(
        Ec2TagSet, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) of the ECS services for a deployment group (documented below).
    """
    ecs_service: EcsService | None = core.attr(EcsService, default=None)

    """
    Application name and deployment group name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Single configuration block of the load balancer to use in a blue/green deployment (docume
    nted below).
    """
    load_balancer_info: LoadBalancerInfo | None = core.attr(LoadBalancerInfo, default=None)

    """
    (Optional) On premise tag filters associated with the group. See the AWS docs for details.
    """
    on_premises_instance_tag_filter: list[OnPremisesInstanceTagFilter] | core.ArrayOut[
        OnPremisesInstanceTagFilter
    ] | None = core.attr(OnPremisesInstanceTagFilter, default=None, kind=core.Kind.array)

    """
    (Required) The service role ARN that allows deployments.
    """
    service_role_arn: str | core.StringOut = core.attr(str)

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
    (Optional) Configuration block(s) of the triggers for the deployment group (documented below).
    """
    trigger_configuration: list[TriggerConfiguration] | core.ArrayOut[
        TriggerConfiguration
    ] | None = core.attr(TriggerConfiguration, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        app_name: str | core.StringOut,
        deployment_group_name: str | core.StringOut,
        service_role_arn: str | core.StringOut,
        alarm_configuration: AlarmConfiguration | None = None,
        auto_rollback_configuration: AutoRollbackConfiguration | None = None,
        autoscaling_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        blue_green_deployment_config: BlueGreenDeploymentConfig | None = None,
        deployment_config_name: str | core.StringOut | None = None,
        deployment_style: DeploymentStyle | None = None,
        ec2_tag_filter: list[Ec2TagFilter] | core.ArrayOut[Ec2TagFilter] | None = None,
        ec2_tag_set: list[Ec2TagSet] | core.ArrayOut[Ec2TagSet] | None = None,
        ecs_service: EcsService | None = None,
        load_balancer_info: LoadBalancerInfo | None = None,
        on_premises_instance_tag_filter: list[OnPremisesInstanceTagFilter]
        | core.ArrayOut[OnPremisesInstanceTagFilter]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        trigger_configuration: list[TriggerConfiguration]
        | core.ArrayOut[TriggerConfiguration]
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeploymentGroup.Args(
                app_name=app_name,
                deployment_group_name=deployment_group_name,
                service_role_arn=service_role_arn,
                alarm_configuration=alarm_configuration,
                auto_rollback_configuration=auto_rollback_configuration,
                autoscaling_groups=autoscaling_groups,
                blue_green_deployment_config=blue_green_deployment_config,
                deployment_config_name=deployment_config_name,
                deployment_style=deployment_style,
                ec2_tag_filter=ec2_tag_filter,
                ec2_tag_set=ec2_tag_set,
                ecs_service=ecs_service,
                load_balancer_info=load_balancer_info,
                on_premises_instance_tag_filter=on_premises_instance_tag_filter,
                tags=tags,
                tags_all=tags_all,
                trigger_configuration=trigger_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alarm_configuration: AlarmConfiguration | None = core.arg(default=None)

        app_name: str | core.StringOut = core.arg()

        auto_rollback_configuration: AutoRollbackConfiguration | None = core.arg(default=None)

        autoscaling_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        blue_green_deployment_config: BlueGreenDeploymentConfig | None = core.arg(default=None)

        deployment_config_name: str | core.StringOut | None = core.arg(default=None)

        deployment_group_name: str | core.StringOut = core.arg()

        deployment_style: DeploymentStyle | None = core.arg(default=None)

        ec2_tag_filter: list[Ec2TagFilter] | core.ArrayOut[Ec2TagFilter] | None = core.arg(
            default=None
        )

        ec2_tag_set: list[Ec2TagSet] | core.ArrayOut[Ec2TagSet] | None = core.arg(default=None)

        ecs_service: EcsService | None = core.arg(default=None)

        load_balancer_info: LoadBalancerInfo | None = core.arg(default=None)

        on_premises_instance_tag_filter: list[OnPremisesInstanceTagFilter] | core.ArrayOut[
            OnPremisesInstanceTagFilter
        ] | None = core.arg(default=None)

        service_role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        trigger_configuration: list[TriggerConfiguration] | core.ArrayOut[
            TriggerConfiguration
        ] | None = core.arg(default=None)
