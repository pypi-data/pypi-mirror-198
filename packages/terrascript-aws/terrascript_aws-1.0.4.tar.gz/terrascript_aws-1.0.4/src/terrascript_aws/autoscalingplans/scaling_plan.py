import terrascript.core as core


@core.schema
class TagFilter(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=TagFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class ApplicationSource(core.Schema):

    cloudformation_stack_arn: str | core.StringOut | None = core.attr(str, default=None)

    tag_filter: list[TagFilter] | core.ArrayOut[TagFilter] | None = core.attr(
        TagFilter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cloudformation_stack_arn: str | core.StringOut | None = None,
        tag_filter: list[TagFilter] | core.ArrayOut[TagFilter] | None = None,
    ):
        super().__init__(
            args=ApplicationSource.Args(
                cloudformation_stack_arn=cloudformation_stack_arn,
                tag_filter=tag_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudformation_stack_arn: str | core.StringOut | None = core.arg(default=None)

        tag_filter: list[TagFilter] | core.ArrayOut[TagFilter] | None = core.arg(default=None)


@core.schema
class PredefinedScalingMetricSpecification(core.Schema):

    predefined_scaling_metric_type: str | core.StringOut = core.attr(str)

    resource_label: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        predefined_scaling_metric_type: str | core.StringOut,
        resource_label: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PredefinedScalingMetricSpecification.Args(
                predefined_scaling_metric_type=predefined_scaling_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_scaling_metric_type: str | core.StringOut = core.arg()

        resource_label: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CustomizedScalingMetricSpecification(core.Schema):

    dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    metric_name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut = core.attr(str)

    statistic: str | core.StringOut = core.attr(str)

    unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_name: str | core.StringOut,
        namespace: str | core.StringOut,
        statistic: str | core.StringOut,
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomizedScalingMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        metric_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()

        statistic: str | core.StringOut = core.arg()

        unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TargetTrackingConfiguration(core.Schema):

    customized_scaling_metric_specification: CustomizedScalingMetricSpecification | None = (
        core.attr(CustomizedScalingMetricSpecification, default=None)
    )

    disable_scale_in: bool | core.BoolOut | None = core.attr(bool, default=None)

    estimated_instance_warmup: int | core.IntOut | None = core.attr(int, default=None)

    predefined_scaling_metric_specification: PredefinedScalingMetricSpecification | None = (
        core.attr(PredefinedScalingMetricSpecification, default=None)
    )

    scale_in_cooldown: int | core.IntOut | None = core.attr(int, default=None)

    scale_out_cooldown: int | core.IntOut | None = core.attr(int, default=None)

    target_value: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        *,
        target_value: float | core.FloatOut,
        customized_scaling_metric_specification: CustomizedScalingMetricSpecification | None = None,
        disable_scale_in: bool | core.BoolOut | None = None,
        estimated_instance_warmup: int | core.IntOut | None = None,
        predefined_scaling_metric_specification: PredefinedScalingMetricSpecification | None = None,
        scale_in_cooldown: int | core.IntOut | None = None,
        scale_out_cooldown: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TargetTrackingConfiguration.Args(
                target_value=target_value,
                customized_scaling_metric_specification=customized_scaling_metric_specification,
                disable_scale_in=disable_scale_in,
                estimated_instance_warmup=estimated_instance_warmup,
                predefined_scaling_metric_specification=predefined_scaling_metric_specification,
                scale_in_cooldown=scale_in_cooldown,
                scale_out_cooldown=scale_out_cooldown,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_scaling_metric_specification: CustomizedScalingMetricSpecification | None = (
            core.arg(default=None)
        )

        disable_scale_in: bool | core.BoolOut | None = core.arg(default=None)

        estimated_instance_warmup: int | core.IntOut | None = core.arg(default=None)

        predefined_scaling_metric_specification: PredefinedScalingMetricSpecification | None = (
            core.arg(default=None)
        )

        scale_in_cooldown: int | core.IntOut | None = core.arg(default=None)

        scale_out_cooldown: int | core.IntOut | None = core.arg(default=None)

        target_value: float | core.FloatOut = core.arg()


@core.schema
class CustomizedLoadMetricSpecification(core.Schema):

    dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    metric_name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut = core.attr(str)

    statistic: str | core.StringOut = core.attr(str)

    unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_name: str | core.StringOut,
        namespace: str | core.StringOut,
        statistic: str | core.StringOut,
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomizedLoadMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        metric_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()

        statistic: str | core.StringOut = core.arg()

        unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class PredefinedLoadMetricSpecification(core.Schema):

    predefined_load_metric_type: str | core.StringOut = core.attr(str)

    resource_label: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        predefined_load_metric_type: str | core.StringOut,
        resource_label: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PredefinedLoadMetricSpecification.Args(
                predefined_load_metric_type=predefined_load_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_load_metric_type: str | core.StringOut = core.arg()

        resource_label: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ScalingInstruction(core.Schema):

    customized_load_metric_specification: CustomizedLoadMetricSpecification | None = core.attr(
        CustomizedLoadMetricSpecification, default=None
    )

    disable_dynamic_scaling: bool | core.BoolOut | None = core.attr(bool, default=None)

    max_capacity: int | core.IntOut = core.attr(int)

    min_capacity: int | core.IntOut = core.attr(int)

    predefined_load_metric_specification: PredefinedLoadMetricSpecification | None = core.attr(
        PredefinedLoadMetricSpecification, default=None
    )

    predictive_scaling_max_capacity_behavior: str | core.StringOut | None = core.attr(
        str, default=None
    )

    predictive_scaling_max_capacity_buffer: int | core.IntOut | None = core.attr(int, default=None)

    predictive_scaling_mode: str | core.StringOut | None = core.attr(str, default=None)

    resource_id: str | core.StringOut = core.attr(str)

    scalable_dimension: str | core.StringOut = core.attr(str)

    scaling_policy_update_behavior: str | core.StringOut | None = core.attr(str, default=None)

    scheduled_action_buffer_time: int | core.IntOut | None = core.attr(int, default=None)

    service_namespace: str | core.StringOut = core.attr(str)

    target_tracking_configuration: list[TargetTrackingConfiguration] | core.ArrayOut[
        TargetTrackingConfiguration
    ] = core.attr(TargetTrackingConfiguration, kind=core.Kind.array)

    def __init__(
        self,
        *,
        max_capacity: int | core.IntOut,
        min_capacity: int | core.IntOut,
        resource_id: str | core.StringOut,
        scalable_dimension: str | core.StringOut,
        service_namespace: str | core.StringOut,
        target_tracking_configuration: list[TargetTrackingConfiguration]
        | core.ArrayOut[TargetTrackingConfiguration],
        customized_load_metric_specification: CustomizedLoadMetricSpecification | None = None,
        disable_dynamic_scaling: bool | core.BoolOut | None = None,
        predefined_load_metric_specification: PredefinedLoadMetricSpecification | None = None,
        predictive_scaling_max_capacity_behavior: str | core.StringOut | None = None,
        predictive_scaling_max_capacity_buffer: int | core.IntOut | None = None,
        predictive_scaling_mode: str | core.StringOut | None = None,
        scaling_policy_update_behavior: str | core.StringOut | None = None,
        scheduled_action_buffer_time: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ScalingInstruction.Args(
                max_capacity=max_capacity,
                min_capacity=min_capacity,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                service_namespace=service_namespace,
                target_tracking_configuration=target_tracking_configuration,
                customized_load_metric_specification=customized_load_metric_specification,
                disable_dynamic_scaling=disable_dynamic_scaling,
                predefined_load_metric_specification=predefined_load_metric_specification,
                predictive_scaling_max_capacity_behavior=predictive_scaling_max_capacity_behavior,
                predictive_scaling_max_capacity_buffer=predictive_scaling_max_capacity_buffer,
                predictive_scaling_mode=predictive_scaling_mode,
                scaling_policy_update_behavior=scaling_policy_update_behavior,
                scheduled_action_buffer_time=scheduled_action_buffer_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_load_metric_specification: CustomizedLoadMetricSpecification | None = core.arg(
            default=None
        )

        disable_dynamic_scaling: bool | core.BoolOut | None = core.arg(default=None)

        max_capacity: int | core.IntOut = core.arg()

        min_capacity: int | core.IntOut = core.arg()

        predefined_load_metric_specification: PredefinedLoadMetricSpecification | None = core.arg(
            default=None
        )

        predictive_scaling_max_capacity_behavior: str | core.StringOut | None = core.arg(
            default=None
        )

        predictive_scaling_max_capacity_buffer: int | core.IntOut | None = core.arg(default=None)

        predictive_scaling_mode: str | core.StringOut | None = core.arg(default=None)

        resource_id: str | core.StringOut = core.arg()

        scalable_dimension: str | core.StringOut = core.arg()

        scaling_policy_update_behavior: str | core.StringOut | None = core.arg(default=None)

        scheduled_action_buffer_time: int | core.IntOut | None = core.arg(default=None)

        service_namespace: str | core.StringOut = core.arg()

        target_tracking_configuration: list[TargetTrackingConfiguration] | core.ArrayOut[
            TargetTrackingConfiguration
        ] = core.arg()


@core.resource(type="aws_autoscalingplans_scaling_plan", namespace="autoscalingplans")
class ScalingPlan(core.Resource):
    """
    (Required) A CloudFormation stack or set of tags. You can create one scaling plan per application so
    urce.
    """

    application_source: ApplicationSource = core.attr(ApplicationSource)

    """
    The scaling plan identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the scaling plan. Names cannot contain vertical bars, colons, or forward slas
    hes.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The scaling instructions. More details can be found in the [AWS Auto Scaling API Referenc
    e](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html).
    """
    scaling_instruction: list[ScalingInstruction] | core.ArrayOut[ScalingInstruction] = core.attr(
        ScalingInstruction, kind=core.Kind.array
    )

    """
    The version number of the scaling plan. This value is always 1.
    """
    scaling_plan_version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_source: ApplicationSource,
        name: str | core.StringOut,
        scaling_instruction: list[ScalingInstruction] | core.ArrayOut[ScalingInstruction],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ScalingPlan.Args(
                application_source=application_source,
                name=name,
                scaling_instruction=scaling_instruction,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_source: ApplicationSource = core.arg()

        name: str | core.StringOut = core.arg()

        scaling_instruction: list[ScalingInstruction] | core.ArrayOut[
            ScalingInstruction
        ] = core.arg()
