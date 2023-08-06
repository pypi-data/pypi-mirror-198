import terrascript.core as core


@core.schema
class Configurations(core.Schema):

    classification: str | core.StringOut | None = core.attr(str, default=None)

    properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        classification: str | core.StringOut | None = None,
        properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Configurations.Args(
                classification=classification,
                properties=properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: str | core.StringOut | None = core.arg(default=None)

        properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class EbsConfig(core.Schema):

    iops: int | core.IntOut | None = core.attr(int, default=None)

    size: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

    volumes_per_instance: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: int | core.IntOut,
        type: str | core.StringOut,
        iops: int | core.IntOut | None = None,
        volumes_per_instance: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: int | core.IntOut | None = core.arg(default=None)

        size: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()

        volumes_per_instance: int | core.IntOut | None = core.arg(default=None)


@core.schema
class InstanceTypeConfigs(core.Schema):

    bid_price: str | core.StringOut | None = core.attr(str, default=None)

    bid_price_as_percentage_of_on_demand_price: float | core.FloatOut | None = core.attr(
        float, default=None
    )

    configurations: list[Configurations] | core.ArrayOut[Configurations] | None = core.attr(
        Configurations, default=None, kind=core.Kind.array
    )

    ebs_config: list[EbsConfig] | core.ArrayOut[EbsConfig] | None = core.attr(
        EbsConfig, default=None, computed=True, kind=core.Kind.array
    )

    instance_type: str | core.StringOut = core.attr(str)

    weighted_capacity: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        instance_type: str | core.StringOut,
        bid_price: str | core.StringOut | None = None,
        bid_price_as_percentage_of_on_demand_price: float | core.FloatOut | None = None,
        configurations: list[Configurations] | core.ArrayOut[Configurations] | None = None,
        ebs_config: list[EbsConfig] | core.ArrayOut[EbsConfig] | None = None,
        weighted_capacity: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=InstanceTypeConfigs.Args(
                instance_type=instance_type,
                bid_price=bid_price,
                bid_price_as_percentage_of_on_demand_price=bid_price_as_percentage_of_on_demand_price,
                configurations=configurations,
                ebs_config=ebs_config,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bid_price: str | core.StringOut | None = core.arg(default=None)

        bid_price_as_percentage_of_on_demand_price: float | core.FloatOut | None = core.arg(
            default=None
        )

        configurations: list[Configurations] | core.ArrayOut[Configurations] | None = core.arg(
            default=None
        )

        ebs_config: list[EbsConfig] | core.ArrayOut[EbsConfig] | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        weighted_capacity: int | core.IntOut | None = core.arg(default=None)


@core.schema
class SpotSpecification(core.Schema):

    allocation_strategy: str | core.StringOut = core.attr(str)

    block_duration_minutes: int | core.IntOut | None = core.attr(int, default=None)

    timeout_action: str | core.StringOut = core.attr(str)

    timeout_duration_minutes: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        allocation_strategy: str | core.StringOut,
        timeout_action: str | core.StringOut,
        timeout_duration_minutes: int | core.IntOut,
        block_duration_minutes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SpotSpecification.Args(
                allocation_strategy=allocation_strategy,
                timeout_action=timeout_action,
                timeout_duration_minutes=timeout_duration_minutes,
                block_duration_minutes=block_duration_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: str | core.StringOut = core.arg()

        block_duration_minutes: int | core.IntOut | None = core.arg(default=None)

        timeout_action: str | core.StringOut = core.arg()

        timeout_duration_minutes: int | core.IntOut = core.arg()


@core.schema
class OnDemandSpecification(core.Schema):

    allocation_strategy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        allocation_strategy: str | core.StringOut,
    ):
        super().__init__(
            args=OnDemandSpecification.Args(
                allocation_strategy=allocation_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: str | core.StringOut = core.arg()


@core.schema
class LaunchSpecifications(core.Schema):

    on_demand_specification: list[OnDemandSpecification] | core.ArrayOut[
        OnDemandSpecification
    ] | None = core.attr(OnDemandSpecification, default=None, kind=core.Kind.array)

    spot_specification: list[SpotSpecification] | core.ArrayOut[
        SpotSpecification
    ] | None = core.attr(SpotSpecification, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        on_demand_specification: list[OnDemandSpecification]
        | core.ArrayOut[OnDemandSpecification]
        | None = None,
        spot_specification: list[SpotSpecification]
        | core.ArrayOut[SpotSpecification]
        | None = None,
    ):
        super().__init__(
            args=LaunchSpecifications.Args(
                on_demand_specification=on_demand_specification,
                spot_specification=spot_specification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_demand_specification: list[OnDemandSpecification] | core.ArrayOut[
            OnDemandSpecification
        ] | None = core.arg(default=None)

        spot_specification: list[SpotSpecification] | core.ArrayOut[
            SpotSpecification
        ] | None = core.arg(default=None)


@core.resource(type="aws_emr_instance_fleet", namespace="emr")
class InstanceFleet(core.Resource):
    """
    (Required) ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.
    """

    cluster_id: str | core.StringOut = core.attr(str)

    """
    The unique identifier of the instance fleet.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for instance fleet
    """
    instance_type_configs: list[InstanceTypeConfigs] | core.ArrayOut[
        InstanceTypeConfigs
    ] | None = core.attr(InstanceTypeConfigs, default=None, kind=core.Kind.array)

    """
    (Optional) Configuration block for launch specification
    """
    launch_specifications: LaunchSpecifications | None = core.attr(
        LaunchSpecifications, default=None
    )

    """
    (Optional) Friendly name given to the instance fleet.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    provisioned_on_demand_capacity: int | core.IntOut = core.attr(int, computed=True)

    provisioned_spot_capacity: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional)  The target capacity of On-Demand units for the instance fleet, which determines how many
    On-Demand instances to provision.
    """
    target_on_demand_capacity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The target capacity of Spot units for the instance fleet, which determines how many Spot
    instances to provision.
    """
    target_spot_capacity: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: str | core.StringOut,
        instance_type_configs: list[InstanceTypeConfigs]
        | core.ArrayOut[InstanceTypeConfigs]
        | None = None,
        launch_specifications: LaunchSpecifications | None = None,
        name: str | core.StringOut | None = None,
        target_on_demand_capacity: int | core.IntOut | None = None,
        target_spot_capacity: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceFleet.Args(
                cluster_id=cluster_id,
                instance_type_configs=instance_type_configs,
                launch_specifications=launch_specifications,
                name=name,
                target_on_demand_capacity=target_on_demand_capacity,
                target_spot_capacity=target_spot_capacity,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_id: str | core.StringOut = core.arg()

        instance_type_configs: list[InstanceTypeConfigs] | core.ArrayOut[
            InstanceTypeConfigs
        ] | None = core.arg(default=None)

        launch_specifications: LaunchSpecifications | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        target_on_demand_capacity: int | core.IntOut | None = core.arg(default=None)

        target_spot_capacity: int | core.IntOut | None = core.arg(default=None)
