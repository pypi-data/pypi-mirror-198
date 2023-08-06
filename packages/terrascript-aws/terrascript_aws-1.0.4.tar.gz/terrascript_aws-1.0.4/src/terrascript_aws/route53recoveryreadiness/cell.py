import terrascript.core as core


@core.resource(type="aws_route53recoveryreadiness_cell", namespace="route53recoveryreadiness")
class Cell(core.Resource):
    """
    ARN of the cell
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique name describing the cell.
    """
    cell_name: str | core.StringOut = core.attr(str)

    """
    (Optional) List of cell arns to add as nested fault domains within this cell.
    """
    cells: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of readiness scopes (recovery groups or cells) that contain this cell.
    """
    parent_readiness_scopes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cell_name: str | core.StringOut,
        cells: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cell.Args(
                cell_name=cell_name,
                cells=cells,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cell_name: str | core.StringOut = core.arg()

        cells: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
