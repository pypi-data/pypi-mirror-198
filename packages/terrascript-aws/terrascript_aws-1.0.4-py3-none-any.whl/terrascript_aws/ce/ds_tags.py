import terrascript.core as core


@core.schema
class SortBy(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    sort_order: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: str | core.StringOut | None = None,
        sort_order: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SortBy.Args(
                key=key,
                sort_order=sort_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        sort_order: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TimePeriod(core.Schema):

    end: str | core.StringOut = core.attr(str)

    start: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        end: str | core.StringOut,
        start: str | core.StringOut,
    ):
        super().__init__(
            args=TimePeriod.Args(
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        end: str | core.StringOut = core.arg()

        start: str | core.StringOut = core.arg()


@core.schema
class TagsBlk(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    match_options: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut | None = None,
        match_options: list[str] | core.ArrayOut[core.StringOut] | None = None,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=TagsBlk.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        match_options: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class CostCategory(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    match_options: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut | None = None,
        match_options: list[str] | core.ArrayOut[core.StringOut] | None = None,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=CostCategory.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        match_options: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Dimension(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    match_options: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut | None = None,
        match_options: list[str] | core.ArrayOut[core.StringOut] | None = None,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Dimension.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        match_options: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class And(core.Schema):

    cost_category: CostCategory | None = core.attr(CostCategory, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    tags: TagsBlk | None = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        cost_category: CostCategory | None = None,
        dimension: Dimension | None = None,
        tags: TagsBlk | None = None,
    ):
        super().__init__(
            args=And.Args(
                cost_category=cost_category,
                dimension=dimension,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category: CostCategory | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        tags: TagsBlk | None = core.arg(default=None)


@core.schema
class Not(core.Schema):

    cost_category: CostCategory | None = core.attr(CostCategory, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    tags: TagsBlk | None = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        cost_category: CostCategory | None = None,
        dimension: Dimension | None = None,
        tags: TagsBlk | None = None,
    ):
        super().__init__(
            args=Not.Args(
                cost_category=cost_category,
                dimension=dimension,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category: CostCategory | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        tags: TagsBlk | None = core.arg(default=None)


@core.schema
class Or(core.Schema):

    cost_category: CostCategory | None = core.attr(CostCategory, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    tags: TagsBlk | None = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        cost_category: CostCategory | None = None,
        dimension: Dimension | None = None,
        tags: TagsBlk | None = None,
    ):
        super().__init__(
            args=Or.Args(
                cost_category=cost_category,
                dimension=dimension,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category: CostCategory | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        tags: TagsBlk | None = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    and_: list[And] | core.ArrayOut[And] | None = core.attr(
        And, default=None, kind=core.Kind.array, alias="and"
    )

    cost_category: CostCategory | None = core.attr(CostCategory, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    not_: Not | None = core.attr(Not, default=None, alias="not")

    or_: list[Or] | core.ArrayOut[Or] | None = core.attr(
        Or, default=None, kind=core.Kind.array, alias="or"
    )

    tags: TagsBlk | None = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        and_: list[And] | core.ArrayOut[And] | None = None,
        cost_category: CostCategory | None = None,
        dimension: Dimension | None = None,
        not_: Not | None = None,
        or_: list[Or] | core.ArrayOut[Or] | None = None,
        tags: TagsBlk | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                and_=and_,
                cost_category=cost_category,
                dimension=dimension,
                not_=not_,
                or_=or_,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: list[And] | core.ArrayOut[And] | None = core.arg(default=None)

        cost_category: CostCategory | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        not_: Not | None = core.arg(default=None)

        or_: list[Or] | core.ArrayOut[Or] | None = core.arg(default=None)

        tags: TagsBlk | None = core.arg(default=None)


@core.data(type="aws_ce_tags", namespace="ce")
class DsTags(core.Data):
    """
    (Optional) Configuration block for the `Expression` object used to categorize costs. See below.
    """

    filter: Filter | None = core.attr(Filter, default=None)

    """
    Unique ID of the tag.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Value that you want to search for.
    """
    search_string: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block for the value by which you want to sort the data. See below.
    """
    sort_by: list[SortBy] | core.ArrayOut[SortBy] | None = core.attr(
        SortBy, default=None, kind=core.Kind.array
    )

    """
    (Optional) Key of the tag that you want to return values for.
    """
    tag_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    Tags that match your request.
    """
    tags: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) Configuration block for the start and end dates for retrieving the dimension values.
    """
    time_period: TimePeriod = core.attr(TimePeriod)

    def __init__(
        self,
        data_name: str,
        *,
        time_period: TimePeriod,
        filter: Filter | None = None,
        search_string: str | core.StringOut | None = None,
        sort_by: list[SortBy] | core.ArrayOut[SortBy] | None = None,
        tag_key: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTags.Args(
                time_period=time_period,
                filter=filter,
                search_string=search_string,
                sort_by=sort_by,
                tag_key=tag_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Filter | None = core.arg(default=None)

        search_string: str | core.StringOut | None = core.arg(default=None)

        sort_by: list[SortBy] | core.ArrayOut[SortBy] | None = core.arg(default=None)

        tag_key: str | core.StringOut | None = core.arg(default=None)

        time_period: TimePeriod = core.arg()
