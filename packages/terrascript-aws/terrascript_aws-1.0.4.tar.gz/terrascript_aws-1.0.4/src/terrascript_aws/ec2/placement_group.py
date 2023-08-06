import terrascript.core as core


@core.resource(type="aws_placement_group", namespace="ec2")
class PlacementGroup(core.Resource):
    """
    Amazon Resource Name (ARN) of the placement group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the placement group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the placement group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The number of partitions to create in the
    """
    partition_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    The ID of the placement group.
    """
    placement_group_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Determines how placement groups spread instances. Can only be used
    """
    spread_level: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The placement strategy. Can be `"cluster"`, `"partition"` or `"spread"`.
    """
    strategy: str | core.StringOut = core.attr(str)

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
        strategy: str | core.StringOut,
        partition_count: int | core.IntOut | None = None,
        spread_level: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PlacementGroup.Args(
                name=name,
                strategy=strategy,
                partition_count=partition_count,
                spread_level=spread_level,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        partition_count: int | core.IntOut | None = core.arg(default=None)

        spread_level: str | core.StringOut | None = core.arg(default=None)

        strategy: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
