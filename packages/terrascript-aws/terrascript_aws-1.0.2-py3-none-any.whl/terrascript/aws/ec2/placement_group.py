import terrascript.core as core


@core.resource(type="aws_placement_group", namespace="aws_ec2")
class PlacementGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    partition_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    placement_group_id: str | core.StringOut = core.attr(str, computed=True)

    spread_level: str | core.StringOut | None = core.attr(str, default=None)

    strategy: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
