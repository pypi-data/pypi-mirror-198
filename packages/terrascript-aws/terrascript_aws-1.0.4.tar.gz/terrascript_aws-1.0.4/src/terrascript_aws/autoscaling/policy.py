import terrascript.core as core


@core.schema
class PredefinedMetricPairSpecification(core.Schema):

    predefined_metric_type: str | core.StringOut = core.attr(str)

    resource_label: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        predefined_metric_type: str | core.StringOut,
        resource_label: str | core.StringOut,
    ):
        super().__init__(
            args=PredefinedMetricPairSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: str | core.StringOut = core.arg()

        resource_label: str | core.StringOut = core.arg()


@core.schema
class PredefinedScalingMetricSpecification(core.Schema):

    predefined_metric_type: str | core.StringOut = core.attr(str)

    resource_label: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        predefined_metric_type: str | core.StringOut,
        resource_label: str | core.StringOut,
    ):
        super().__init__(
            args=PredefinedScalingMetricSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: str | core.StringOut = core.arg()

        resource_label: str | core.StringOut = core.arg()


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
class Metric(core.Schema):

    dimensions: list[Dimensions] | core.ArrayOut[Dimensions] | None = core.attr(
        Dimensions, default=None, kind=core.Kind.array
    )

    metric_name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        metric_name: str | core.StringOut,
        namespace: str | core.StringOut,
        dimensions: list[Dimensions] | core.ArrayOut[Dimensions] | None = None,
    ):
        super().__init__(
            args=Metric.Args(
                metric_name=metric_name,
                namespace=namespace,
                dimensions=dimensions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: list[Dimensions] | core.ArrayOut[Dimensions] | None = core.arg(default=None)

        metric_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()


@core.schema
class MetricStat(core.Schema):

    metric: Metric = core.attr(Metric)

    stat: str | core.StringOut = core.attr(str)

    unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric: Metric,
        stat: str | core.StringOut,
        unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MetricStat.Args(
                metric=metric,
                stat=stat,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric: Metric = core.arg()

        stat: str | core.StringOut = core.arg()

        unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MetricDataQueries(core.Schema):

    expression: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str)

    label: str | core.StringOut | None = core.attr(str, default=None)

    metric_stat: MetricStat | None = core.attr(MetricStat, default=None)

    return_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        expression: str | core.StringOut | None = None,
        label: str | core.StringOut | None = None,
        metric_stat: MetricStat | None = None,
        return_data: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=MetricDataQueries.Args(
                id=id,
                expression=expression,
                label=label,
                metric_stat=metric_stat,
                return_data=return_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        expression: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        label: str | core.StringOut | None = core.arg(default=None)

        metric_stat: MetricStat | None = core.arg(default=None)

        return_data: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class CustomizedCapacityMetricSpecification(core.Schema):

    metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries] = core.attr(
        MetricDataQueries, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries],
    ):
        super().__init__(
            args=CustomizedCapacityMetricSpecification.Args(
                metric_data_queries=metric_data_queries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries] = core.arg()


@core.schema
class CustomizedLoadMetricSpecification(core.Schema):

    metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries] = core.attr(
        MetricDataQueries, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries],
    ):
        super().__init__(
            args=CustomizedLoadMetricSpecification.Args(
                metric_data_queries=metric_data_queries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries] = core.arg()


@core.schema
class CustomizedScalingMetricSpecification(core.Schema):

    metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries] = core.attr(
        MetricDataQueries, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries],
    ):
        super().__init__(
            args=CustomizedScalingMetricSpecification.Args(
                metric_data_queries=metric_data_queries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_data_queries: list[MetricDataQueries] | core.ArrayOut[MetricDataQueries] = core.arg()


@core.schema
class PredefinedLoadMetricSpecification(core.Schema):

    predefined_metric_type: str | core.StringOut = core.attr(str)

    resource_label: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        predefined_metric_type: str | core.StringOut,
        resource_label: str | core.StringOut,
    ):
        super().__init__(
            args=PredefinedLoadMetricSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: str | core.StringOut = core.arg()

        resource_label: str | core.StringOut = core.arg()


@core.schema
class MetricSpecification(core.Schema):

    customized_capacity_metric_specification: CustomizedCapacityMetricSpecification | None = (
        core.attr(CustomizedCapacityMetricSpecification, default=None)
    )

    customized_load_metric_specification: CustomizedLoadMetricSpecification | None = core.attr(
        CustomizedLoadMetricSpecification, default=None
    )

    customized_scaling_metric_specification: CustomizedScalingMetricSpecification | None = (
        core.attr(CustomizedScalingMetricSpecification, default=None)
    )

    predefined_load_metric_specification: PredefinedLoadMetricSpecification | None = core.attr(
        PredefinedLoadMetricSpecification, default=None
    )

    predefined_metric_pair_specification: PredefinedMetricPairSpecification | None = core.attr(
        PredefinedMetricPairSpecification, default=None
    )

    predefined_scaling_metric_specification: PredefinedScalingMetricSpecification | None = (
        core.attr(PredefinedScalingMetricSpecification, default=None)
    )

    target_value: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        target_value: int | core.IntOut,
        customized_capacity_metric_specification: CustomizedCapacityMetricSpecification
        | None = None,
        customized_load_metric_specification: CustomizedLoadMetricSpecification | None = None,
        customized_scaling_metric_specification: CustomizedScalingMetricSpecification | None = None,
        predefined_load_metric_specification: PredefinedLoadMetricSpecification | None = None,
        predefined_metric_pair_specification: PredefinedMetricPairSpecification | None = None,
        predefined_scaling_metric_specification: PredefinedScalingMetricSpecification | None = None,
    ):
        super().__init__(
            args=MetricSpecification.Args(
                target_value=target_value,
                customized_capacity_metric_specification=customized_capacity_metric_specification,
                customized_load_metric_specification=customized_load_metric_specification,
                customized_scaling_metric_specification=customized_scaling_metric_specification,
                predefined_load_metric_specification=predefined_load_metric_specification,
                predefined_metric_pair_specification=predefined_metric_pair_specification,
                predefined_scaling_metric_specification=predefined_scaling_metric_specification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_capacity_metric_specification: CustomizedCapacityMetricSpecification | None = (
            core.arg(default=None)
        )

        customized_load_metric_specification: CustomizedLoadMetricSpecification | None = core.arg(
            default=None
        )

        customized_scaling_metric_specification: CustomizedScalingMetricSpecification | None = (
            core.arg(default=None)
        )

        predefined_load_metric_specification: PredefinedLoadMetricSpecification | None = core.arg(
            default=None
        )

        predefined_metric_pair_specification: PredefinedMetricPairSpecification | None = core.arg(
            default=None
        )

        predefined_scaling_metric_specification: PredefinedScalingMetricSpecification | None = (
            core.arg(default=None)
        )

        target_value: int | core.IntOut = core.arg()


@core.schema
class PredictiveScalingConfiguration(core.Schema):

    max_capacity_breach_behavior: str | core.StringOut | None = core.attr(str, default=None)

    max_capacity_buffer: str | core.StringOut | None = core.attr(str, default=None)

    metric_specification: MetricSpecification = core.attr(MetricSpecification)

    mode: str | core.StringOut | None = core.attr(str, default=None)

    scheduling_buffer_time: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_specification: MetricSpecification,
        max_capacity_breach_behavior: str | core.StringOut | None = None,
        max_capacity_buffer: str | core.StringOut | None = None,
        mode: str | core.StringOut | None = None,
        scheduling_buffer_time: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PredictiveScalingConfiguration.Args(
                metric_specification=metric_specification,
                max_capacity_breach_behavior=max_capacity_breach_behavior,
                max_capacity_buffer=max_capacity_buffer,
                mode=mode,
                scheduling_buffer_time=scheduling_buffer_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_capacity_breach_behavior: str | core.StringOut | None = core.arg(default=None)

        max_capacity_buffer: str | core.StringOut | None = core.arg(default=None)

        metric_specification: MetricSpecification = core.arg()

        mode: str | core.StringOut | None = core.arg(default=None)

        scheduling_buffer_time: str | core.StringOut | None = core.arg(default=None)


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
class MetricDimension(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=MetricDimension.Args(
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

    metric_dimension: list[MetricDimension] | core.ArrayOut[MetricDimension] | None = core.attr(
        MetricDimension, default=None, kind=core.Kind.array
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
        metric_dimension: list[MetricDimension] | core.ArrayOut[MetricDimension] | None = None,
        unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomizedMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                metric_dimension=metric_dimension,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_dimension: list[MetricDimension] | core.ArrayOut[MetricDimension] | None = core.arg(
            default=None
        )

        metric_name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut = core.arg()

        statistic: str | core.StringOut = core.arg()

        unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TargetTrackingConfiguration(core.Schema):

    customized_metric_specification: CustomizedMetricSpecification | None = core.attr(
        CustomizedMetricSpecification, default=None
    )

    disable_scale_in: bool | core.BoolOut | None = core.attr(bool, default=None)

    predefined_metric_specification: PredefinedMetricSpecification | None = core.attr(
        PredefinedMetricSpecification, default=None
    )

    target_value: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        *,
        target_value: float | core.FloatOut,
        customized_metric_specification: CustomizedMetricSpecification | None = None,
        disable_scale_in: bool | core.BoolOut | None = None,
        predefined_metric_specification: PredefinedMetricSpecification | None = None,
    ):
        super().__init__(
            args=TargetTrackingConfiguration.Args(
                target_value=target_value,
                customized_metric_specification=customized_metric_specification,
                disable_scale_in=disable_scale_in,
                predefined_metric_specification=predefined_metric_specification,
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

        target_value: float | core.FloatOut = core.arg()


@core.resource(type="aws_autoscaling_policy", namespace="autoscaling")
class Policy(core.Resource):
    """
    (Optional) Specifies whether the adjustment is an absolute number or a percentage of the current cap
    acity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
    """

    adjustment_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN assigned by AWS to the scaling policy.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the autoscaling group.
    """
    autoscaling_group_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The amount of time, in seconds, after a scaling activity completes and before the next sc
    aling activity can start.
    """
    cooldown: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Indicates whether the scaling policy is enabled or disabled. Default: `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The estimated time, in seconds, until a newly launched instance will contribute CloudWatc
    h metrics. Without a value, AWS will default to the group's specified cooldown period.
    """
    estimated_instance_warmup: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) A short name for the metric used in predictive scaling policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and
    "Average". Without a value, AWS will treat the aggregation type as "Average".
    """
    metric_aggregation_type: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
    """
    min_adjustment_magnitude: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The name of the policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The policy type, either "SimpleScaling", "StepScaling", "TargetTrackingScaling", or "Pred
    ictiveScaling". If this value isn't provided, AWS will default to "SimpleScaling."
    """
    policy_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The predictive scaling policy configuration to use with Amazon EC2 Auto Scaling.
    """
    predictive_scaling_configuration: PredictiveScalingConfiguration | None = core.attr(
        PredictiveScalingConfiguration, default=None
    )

    """
    (Optional) The number of instances by which to scale. `adjustment_type` determines the interpretatio
    n of this number (e.g., as an absolute number or as a percentage of the existing Auto Scaling group
    size). A positive increment adds to the current capacity and a negative value removes from the curre
    nt capacity.
    """
    scaling_adjustment: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) A set of adjustments that manage
    """
    step_adjustment: list[StepAdjustment] | core.ArrayOut[StepAdjustment] | None = core.attr(
        StepAdjustment, default=None, kind=core.Kind.array
    )

    """
    (Optional) A target tracking policy. These have the following structure:
    """
    target_tracking_configuration: TargetTrackingConfiguration | None = core.attr(
        TargetTrackingConfiguration, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: str | core.StringOut,
        name: str | core.StringOut,
        adjustment_type: str | core.StringOut | None = None,
        cooldown: int | core.IntOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        estimated_instance_warmup: int | core.IntOut | None = None,
        metric_aggregation_type: str | core.StringOut | None = None,
        min_adjustment_magnitude: int | core.IntOut | None = None,
        policy_type: str | core.StringOut | None = None,
        predictive_scaling_configuration: PredictiveScalingConfiguration | None = None,
        scaling_adjustment: int | core.IntOut | None = None,
        step_adjustment: list[StepAdjustment] | core.ArrayOut[StepAdjustment] | None = None,
        target_tracking_configuration: TargetTrackingConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                autoscaling_group_name=autoscaling_group_name,
                name=name,
                adjustment_type=adjustment_type,
                cooldown=cooldown,
                enabled=enabled,
                estimated_instance_warmup=estimated_instance_warmup,
                metric_aggregation_type=metric_aggregation_type,
                min_adjustment_magnitude=min_adjustment_magnitude,
                policy_type=policy_type,
                predictive_scaling_configuration=predictive_scaling_configuration,
                scaling_adjustment=scaling_adjustment,
                step_adjustment=step_adjustment,
                target_tracking_configuration=target_tracking_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        adjustment_type: str | core.StringOut | None = core.arg(default=None)

        autoscaling_group_name: str | core.StringOut = core.arg()

        cooldown: int | core.IntOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        estimated_instance_warmup: int | core.IntOut | None = core.arg(default=None)

        metric_aggregation_type: str | core.StringOut | None = core.arg(default=None)

        min_adjustment_magnitude: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        policy_type: str | core.StringOut | None = core.arg(default=None)

        predictive_scaling_configuration: PredictiveScalingConfiguration | None = core.arg(
            default=None
        )

        scaling_adjustment: int | core.IntOut | None = core.arg(default=None)

        step_adjustment: list[StepAdjustment] | core.ArrayOut[StepAdjustment] | None = core.arg(
            default=None
        )

        target_tracking_configuration: TargetTrackingConfiguration | None = core.arg(default=None)
