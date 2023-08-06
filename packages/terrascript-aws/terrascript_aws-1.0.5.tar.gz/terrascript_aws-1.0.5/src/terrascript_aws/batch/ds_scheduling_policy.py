import terrascript.core as core


@core.schema
class ShareDistribution(core.Schema):

    share_identifier: str | core.StringOut = core.attr(str, computed=True)

    weight_factor: float | core.FloatOut = core.attr(float, computed=True)

    def __init__(
        self,
        *,
        share_identifier: str | core.StringOut,
        weight_factor: float | core.FloatOut,
    ):
        super().__init__(
            args=ShareDistribution.Args(
                share_identifier=share_identifier,
                weight_factor=weight_factor,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        share_identifier: str | core.StringOut = core.arg()

        weight_factor: float | core.FloatOut = core.arg()


@core.schema
class FairSharePolicy(core.Schema):

    compute_reservation: int | core.IntOut = core.attr(int, computed=True)

    share_decay_seconds: int | core.IntOut = core.attr(int, computed=True)

    share_distribution: list[ShareDistribution] | core.ArrayOut[ShareDistribution] = core.attr(
        ShareDistribution, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        compute_reservation: int | core.IntOut,
        share_decay_seconds: int | core.IntOut,
        share_distribution: list[ShareDistribution] | core.ArrayOut[ShareDistribution],
    ):
        super().__init__(
            args=FairSharePolicy.Args(
                compute_reservation=compute_reservation,
                share_decay_seconds=share_decay_seconds,
                share_distribution=share_distribution,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_reservation: int | core.IntOut = core.arg()

        share_decay_seconds: int | core.IntOut = core.arg()

        share_distribution: list[ShareDistribution] | core.ArrayOut[ShareDistribution] = core.arg()


@core.data(type="aws_batch_scheduling_policy", namespace="batch")
class DsSchedulingPolicy(core.Data):
    """
    (Required) The Amazon Resource Name (ARN) of the scheduling policy.
    """

    arn: str | core.StringOut = core.attr(str)

    fair_share_policy: list[FairSharePolicy] | core.ArrayOut[FairSharePolicy] = core.attr(
        FairSharePolicy, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the name of the scheduling policy.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSchedulingPolicy.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
