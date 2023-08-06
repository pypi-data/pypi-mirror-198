import terrascript.core as core


@core.schema
class ShareDistribution(core.Schema):

    share_identifier: str | core.StringOut = core.attr(str)

    weight_factor: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        share_identifier: str | core.StringOut,
        weight_factor: float | core.FloatOut | None = None,
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

        weight_factor: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class FairSharePolicy(core.Schema):

    compute_reservation: int | core.IntOut | None = core.attr(int, default=None)

    share_decay_seconds: int | core.IntOut | None = core.attr(int, default=None)

    share_distribution: list[ShareDistribution] | core.ArrayOut[
        ShareDistribution
    ] | None = core.attr(ShareDistribution, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        compute_reservation: int | core.IntOut | None = None,
        share_decay_seconds: int | core.IntOut | None = None,
        share_distribution: list[ShareDistribution]
        | core.ArrayOut[ShareDistribution]
        | None = None,
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
        compute_reservation: int | core.IntOut | None = core.arg(default=None)

        share_decay_seconds: int | core.IntOut | None = core.arg(default=None)

        share_distribution: list[ShareDistribution] | core.ArrayOut[
            ShareDistribution
        ] | None = core.arg(default=None)


@core.resource(type="aws_batch_scheduling_policy", namespace="batch")
class SchedulingPolicy(core.Resource):
    """
    The Amazon Resource Name of the scheduling policy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    fair_share_policy: FairSharePolicy | None = core.attr(FairSharePolicy, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the name of the scheduling policy.
    """
    name: str | core.StringOut = core.attr(str)

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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        fair_share_policy: FairSharePolicy | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SchedulingPolicy.Args(
                name=name,
                fair_share_policy=fair_share_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        fair_share_policy: FairSharePolicy | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
