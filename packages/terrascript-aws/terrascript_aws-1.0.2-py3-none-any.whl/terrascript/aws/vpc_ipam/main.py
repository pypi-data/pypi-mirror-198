import terrascript.core as core


@core.schema
class OperatingRegions(core.Schema):

    region_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        region_name: str | core.StringOut,
    ):
        super().__init__(
            args=OperatingRegions.Args(
                region_name=region_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region_name: str | core.StringOut = core.arg()


@core.resource(type="aws_vpc_ipam", namespace="aws_vpc_ipam")
class Main(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cascade: bool | core.BoolOut | None = core.attr(bool, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    operating_regions: list[OperatingRegions] | core.ArrayOut[OperatingRegions] = core.attr(
        OperatingRegions, kind=core.Kind.array
    )

    private_default_scope_id: str | core.StringOut = core.attr(str, computed=True)

    public_default_scope_id: str | core.StringOut = core.attr(str, computed=True)

    scope_count: int | core.IntOut = core.attr(int, computed=True)

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
        operating_regions: list[OperatingRegions] | core.ArrayOut[OperatingRegions],
        cascade: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                operating_regions=operating_regions,
                cascade=cascade,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cascade: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        operating_regions: list[OperatingRegions] | core.ArrayOut[OperatingRegions] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
