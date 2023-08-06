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


@core.resource(type="aws_vpc_ipam", namespace="vpc_ipam")
class Main(core.Resource):
    """
    Amazon Resource Name (ARN) of IPAM
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any a
    llocations in the pools in private scopes.
    """
    cascade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A description for the IPAM.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the IPAM
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Determines which locales can be chosen when you create pools. Locale is the Region where
    you want to make an IPAM pool available for allocations. You can only create pools with locales that
    match the operating Regions of the IPAM. You can only create VPCs from a pool whose locale matches
    the VPC's Region. You specify a region using the [region_name](#operating_regions) parameter. You **
    must** set your provider block region as an operating_region.
    """
    operating_regions: list[OperatingRegions] | core.ArrayOut[OperatingRegions] = core.attr(
        OperatingRegions, kind=core.Kind.array
    )

    """
    The ID of the IPAM's private scope. A scope is a top-level container in IPAM. Each scope represents
    an IP-independent network. Scopes enable you to represent networks where you have overlapping IP spa
    ce. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private
    scope is intended for private IP space. The public scope is intended for all internet-routable IP sp
    ace.
    """
    private_default_scope_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the IPAM's public scope. A scope is a top-level container in IPAM. Each scope represents a
    n IP-independent network. Scopes enable you to represent networks where you have overlapping IP spac
    e. When you create an IPAM, IPAM automatically creates two scopes: public and private. The private s
    cope is intended for private
    """
    public_default_scope_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of scopes in the IPAM.
    """
    scope_count: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
