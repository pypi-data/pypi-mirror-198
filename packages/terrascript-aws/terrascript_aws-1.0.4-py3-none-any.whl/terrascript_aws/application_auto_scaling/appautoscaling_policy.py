import terrascript.core as core


@core.schema
class StepAdjustment(core.Schema):

    metric_interval_lower_bound: str | core.StringOut | None = core.attr(str, default=None)

    metric_interval_upper_bound: str | core.StringOut | None = core.attr(str, default=None)

    scaling_adjustment: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        scaling_adjustment: int | core.IntOut,
        metric_interval_lower_bound: str | core.StringOut | None = None,
        metric_interval_upper_bound: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StepAdjustment.Args(
                scaling_adjustment=scaling_adjustment,
                metric_interval_lower_bound=metric_interval_lower_bound,
                metric_interval_upper_bound=metric_interval_upper_bound,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_interval_lower_bound: str | core.StringOut | None = core.arg(default=None)

        metric_interval_upper_bound: str | core.StringOut | None = core.arg(default=None)

        scaling_adjustment: int | core.IntOut = core.arg()


@core.schema
class StepScalingPolicyConfiguration(core.Schema):

    adjustment_type: str | core.StringOut | None = core.attr(str, default=None)

    cooldown: int | core.IntOut | None = core.attr(int, default=None)

    metric_aggregation_type: str | core.StringOut | None = core.attr(str, default=None)

    min_adjustment_magnitude: int | core.IntOut | None = core.attr(int, default=None)

    step_adjustment: list[StepAdjustment] | core.ArrayOut[StepAdjustment] | None = core.attr(
        StepAdjustment, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        adjustment_type: str | core.StringOut | None = None,
        cooldown: int | core.IntOut | None = None,
        metric_aggregation_type: str | core.StringOut | None = None,
        min_adjustment_magnitude: int | core.IntOut | None = None,
        step_adjustment: list[StepAdjustment] | core.ArrayOut[StepAdjustment] | None = None,
    ):
        super().__init__(
            args=StepScalingPolicyConfiguration.Args(
                adjustment_type=adjustment_type,
                cooldown=cooldown,
                metric_aggregation_type=metric_aggregation_type,
                min_adjustment_magnitude=min_adjustment_magnitude,
                step_adjustment=step_adjustment,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        adjustment_type: str | core.StringOut | None = core.arg(default=None)

        cooldown: int | core.IntOut | None = core.arg(default=None)

        metric_aggregation_type: str | core.StringOut | None = core.arg(default=None)

        min_adjustment_magnitude: int | core.IntOut | None = core.arg(default=None)

        step_adjustment: list[StepAdjustment] | core.ArrayOut[StepAdjustment] | None = core.arg(
            default=None
        )


@core.schema
class Dimensions(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Dimensions.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class CustomizedMetricSpecification(core.Schema):

    dimensions: list[Dimensions] | core.ArrayOut[Dimensions] | None = core.attr(
        Dimensions, default=None, kind=core.Kind.array
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
        dimensions: list[Dimensions] | core.ArrayOut[Dimensions] | None = None,
        unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomizedMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: list[Dimensions] | core.ArrayOut[Dimensions] | None = core.arg(default=None)

        metric_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()

        statistic: str | core.StringOut = core.arg()

        unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class PredefinedMetricSpecification(core.Schema):

    predefined_metric_type: str | core.StringOut = core.attr(str)

    resource_label: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        predefined_metric_type: str | core.StringOut,
        resource_label: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PredefinedMetricSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: str | core.StringOut = core.arg()

        resource_label: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TargetTrackingScalingPolicyConfiguration(core.Schema):

    customized_metric_specification: CustomizedMetricSpecification | None = core.attr(
        CustomizedMetricSpecification, default=None
    )

    disable_scale_in: bool | core.BoolOut | None = core.attr(bool, default=None)

    predefined_metric_specification: PredefinedMetricSpecification | None = core.attr(
        PredefinedMetricSpecification, default=None
    )

    scale_in_cooldown: int | core.IntOut | None = core.attr(int, default=None)

    scale_out_cooldown: int | core.IntOut | None = core.attr(int, default=None)

    target_value: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        *,
        target_value: float | core.FloatOut,
        customized_metric_specification: CustomizedMetricSpecification | None = None,
        disable_scale_in: bool | core.BoolOut | None = None,
        predefined_metric_specification: PredefinedMetricSpecification | None = None,
        scale_in_cooldown: int | core.IntOut | None = None,
        scale_out_cooldown: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TargetTrackingScalingPolicyConfiguration.Args(
                target_value=target_value,
                customized_metric_specification=customized_metric_specification,
                disable_scale_in=disable_scale_in,
                predefined_metric_specification=predefined_metric_specification,
                scale_in_cooldown=scale_in_cooldown,
                scale_out_cooldown=scale_out_cooldown,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_metric_specification: CustomizedMetricSpecification | None = core.arg(
            default=None
        )

        disable_scale_in: bool | core.BoolOut | None = core.arg(default=None)

        predefined_metric_specification: PredefinedMetricSpecification | None = core.arg(
            default=None
        )

        scale_in_cooldown: int | core.IntOut | None = core.arg(default=None)

        scale_out_cooldown: int | core.IntOut | None = core.arg(default=None)

        target_value: float | core.FloatOut = core.arg()


@core.resource(type="aws_appautoscaling_policy", namespace="application_auto_scaling")
class AppautoscalingPolicy(core.Resource):
    """
    The ARN assigned by AWS to the scaling policy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the policy. Must be between 1 and 255 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The policy type. Valid values are `StepScaling` and `TargetTrackingScaling`. Defaults to
    StepScaling`. Certain services only support only one policy type. For more information see the [Tar
    get Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/application/userguide/applica
    tion-auto-scaling-target-tracking.html) and [Step Scaling Policies](https://docs.aws.amazon.com/auto
    scaling/application/userguide/application-auto-scaling-step-scaling-policies.html) documentation.
    """
    policy_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The resource type and unique identifier string for the resource associated with the scali
    ng policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scalin
    g API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterS
    calableTarget.html#API_RegisterScalableTarget_RequestParameters)
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    (Required) The scalable dimension of the scalable target. Documentation can be found in the `Scalabl
    eDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/Ap
    plicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_
    RequestParameters)
    """
    scalable_dimension: str | core.StringOut = core.attr(str)

    """
    (Required) The AWS service namespace of the scalable target. Documentation can be found in the `Serv
    iceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/
    ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarge
    t_RequestParameters)
    """
    service_namespace: str | core.StringOut = core.attr(str)

    """
    (Optional) Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See
    supported fields below.
    """
    step_scaling_policy_configuration: StepScalingPolicyConfiguration | None = core.attr(
        StepScalingPolicyConfiguration, default=None
    )

    """
    (Optional) A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported
    fields below.
    """
    target_tracking_scaling_policy_configuration: TargetTrackingScalingPolicyConfiguration | None = core.attr(
        TargetTrackingScalingPolicyConfiguration, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        resource_id: str | core.StringOut,
        scalable_dimension: str | core.StringOut,
        service_namespace: str | core.StringOut,
        policy_type: str | core.StringOut | None = None,
        step_scaling_policy_configuration: StepScalingPolicyConfiguration | None = None,
        target_tracking_scaling_policy_configuration: TargetTrackingScalingPolicyConfiguration
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppautoscalingPolicy.Args(
                name=name,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                service_namespace=service_namespace,
                policy_type=policy_type,
                step_scaling_policy_configuration=step_scaling_policy_configuration,
                target_tracking_scaling_policy_configuration=target_tracking_scaling_policy_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        policy_type: str | core.StringOut | None = core.arg(default=None)

        resource_id: str | core.StringOut = core.arg()

        scalable_dimension: str | core.StringOut = core.arg()

        service_namespace: str | core.StringOut = core.arg()

        step_scaling_policy_configuration: StepScalingPolicyConfiguration | None = core.arg(
            default=None
        )

        target_tracking_scaling_policy_configuration: TargetTrackingScalingPolicyConfiguration | None = core.arg(
            default=None
        )
