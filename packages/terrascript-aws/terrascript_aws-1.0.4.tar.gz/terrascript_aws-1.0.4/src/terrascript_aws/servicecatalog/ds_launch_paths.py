import terrascript.core as core


@core.schema
class ConstraintSummaries(core.Schema):

    description: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        description: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=ConstraintSummaries.Args(
                description=description,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class Summaries(core.Schema):

    constraint_summaries: list[ConstraintSummaries] | core.ArrayOut[
        ConstraintSummaries
    ] = core.attr(ConstraintSummaries, computed=True, kind=core.Kind.array)

    name: str | core.StringOut = core.attr(str, computed=True)

    path_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        constraint_summaries: list[ConstraintSummaries] | core.ArrayOut[ConstraintSummaries],
        name: str | core.StringOut,
        path_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Summaries.Args(
                constraint_summaries=constraint_summaries,
                name=name,
                path_id=path_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        constraint_summaries: list[ConstraintSummaries] | core.ArrayOut[
            ConstraintSummaries
        ] = core.arg()

        name: str | core.StringOut = core.arg()

        path_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.data(type="aws_servicecatalog_launch_paths", namespace="servicecatalog")
class DsLaunchPaths(core.Data):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Product identifier.
    """
    product_id: str | core.StringOut = core.attr(str)

    """
    Block with information about the launch path. See details below.
    """
    summaries: list[Summaries] | core.ArrayOut[Summaries] = core.attr(
        Summaries, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        product_id: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLaunchPaths.Args(
                product_id=product_id,
                accept_language=accept_language,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        product_id: str | core.StringOut = core.arg()
