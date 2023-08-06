import terrascript.core as core


@core.schema
class ComputeLimits(core.Schema):

    maximum_capacity_units: int | core.IntOut = core.attr(int)

    maximum_core_capacity_units: int | core.IntOut | None = core.attr(int, default=None)

    maximum_ondemand_capacity_units: int | core.IntOut | None = core.attr(int, default=None)

    minimum_capacity_units: int | core.IntOut = core.attr(int)

    unit_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        maximum_capacity_units: int | core.IntOut,
        minimum_capacity_units: int | core.IntOut,
        unit_type: str | core.StringOut,
        maximum_core_capacity_units: int | core.IntOut | None = None,
        maximum_ondemand_capacity_units: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ComputeLimits.Args(
                maximum_capacity_units=maximum_capacity_units,
                minimum_capacity_units=minimum_capacity_units,
                unit_type=unit_type,
                maximum_core_capacity_units=maximum_core_capacity_units,
                maximum_ondemand_capacity_units=maximum_ondemand_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_capacity_units: int | core.IntOut = core.arg()

        maximum_core_capacity_units: int | core.IntOut | None = core.arg(default=None)

        maximum_ondemand_capacity_units: int | core.IntOut | None = core.arg(default=None)

        minimum_capacity_units: int | core.IntOut = core.arg()

        unit_type: str | core.StringOut = core.arg()


@core.resource(type="aws_emr_managed_scaling_policy", namespace="emr")
class ManagedScalingPolicy(core.Resource):
    """
    (Required) The id of the EMR cluster
    """

    cluster_id: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block with compute limit settings. Described below.
    """
    compute_limits: list[ComputeLimits] | core.ArrayOut[ComputeLimits] = core.attr(
        ComputeLimits, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: str | core.StringOut,
        compute_limits: list[ComputeLimits] | core.ArrayOut[ComputeLimits],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ManagedScalingPolicy.Args(
                cluster_id=cluster_id,
                compute_limits=compute_limits,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_id: str | core.StringOut = core.arg()

        compute_limits: list[ComputeLimits] | core.ArrayOut[ComputeLimits] = core.arg()
