import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_imagebuilder_container_recipes", namespace="imagebuilder")
class DsContainerRecipes(core.Data):
    """
    Set of ARNs of the matched Image Builder Container Recipes.
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of names of the matched Image Builder Container Recipes.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The owner of the container recipes. Valid values are `Self`, `Shared` and `Amazon`. Defau
    lts to `Self`.
    """
    owner: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        owner: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsContainerRecipes.Args(
                filter=filter,
                owner=owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        owner: str | core.StringOut | None = core.arg(default=None)
