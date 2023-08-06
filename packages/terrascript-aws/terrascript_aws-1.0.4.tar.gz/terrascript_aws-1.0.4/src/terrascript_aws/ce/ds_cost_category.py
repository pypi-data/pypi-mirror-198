import terrascript.core as core


@core.schema
class Tags(core.Schema):

    key: str | core.StringOut = core.attr(str, computed=True)

    match_options: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        match_options: list[str] | core.ArrayOut[core.StringOut],
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Tags.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        match_options: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class CostCategoryBlk(core.Schema):

    key: str | core.StringOut = core.attr(str, computed=True)

    match_options: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        match_options: list[str] | core.ArrayOut[core.StringOut],
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=CostCategoryBlk.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        match_options: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Dimension(core.Schema):

    key: str | core.StringOut = core.attr(str, computed=True)

    match_options: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        match_options: list[str] | core.ArrayOut[core.StringOut],
        values: list[str] | core.ArrayOut[core.StringOut],
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
        key: str | core.StringOut = core.arg()

        match_options: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class And(core.Schema):

    cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: list[Dimension] | core.ArrayOut[Dimension] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    tags: list[Tags] | core.ArrayOut[Tags] = core.attr(Tags, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk],
        dimension: list[Dimension] | core.ArrayOut[Dimension],
        tags: list[Tags] | core.ArrayOut[Tags],
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
        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.arg()

        dimension: list[Dimension] | core.ArrayOut[Dimension] = core.arg()

        tags: list[Tags] | core.ArrayOut[Tags] = core.arg()


@core.schema
class Not(core.Schema):

    cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: list[Dimension] | core.ArrayOut[Dimension] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    tags: list[Tags] | core.ArrayOut[Tags] = core.attr(Tags, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk],
        dimension: list[Dimension] | core.ArrayOut[Dimension],
        tags: list[Tags] | core.ArrayOut[Tags],
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
        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.arg()

        dimension: list[Dimension] | core.ArrayOut[Dimension] = core.arg()

        tags: list[Tags] | core.ArrayOut[Tags] = core.arg()


@core.schema
class Or(core.Schema):

    cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: list[Dimension] | core.ArrayOut[Dimension] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    tags: list[Tags] | core.ArrayOut[Tags] = core.attr(Tags, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk],
        dimension: list[Dimension] | core.ArrayOut[Dimension],
        tags: list[Tags] | core.ArrayOut[Tags],
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
        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.arg()

        dimension: list[Dimension] | core.ArrayOut[Dimension] = core.arg()

        tags: list[Tags] | core.ArrayOut[Tags] = core.arg()


@core.schema
class RuleRule(core.Schema):

    and_: list[And] | core.ArrayOut[And] = core.attr(
        And, computed=True, kind=core.Kind.array, alias="and"
    )

    cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: list[Dimension] | core.ArrayOut[Dimension] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    not_: list[Not] | core.ArrayOut[Not] = core.attr(
        Not, computed=True, kind=core.Kind.array, alias="not"
    )

    or_: list[Or] | core.ArrayOut[Or] = core.attr(
        Or, computed=True, kind=core.Kind.array, alias="or"
    )

    tags: list[Tags] | core.ArrayOut[Tags] = core.attr(Tags, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        and_: list[And] | core.ArrayOut[And],
        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk],
        dimension: list[Dimension] | core.ArrayOut[Dimension],
        not_: list[Not] | core.ArrayOut[Not],
        or_: list[Or] | core.ArrayOut[Or],
        tags: list[Tags] | core.ArrayOut[Tags],
    ):
        super().__init__(
            args=RuleRule.Args(
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
        and_: list[And] | core.ArrayOut[And] = core.arg()

        cost_category: list[CostCategoryBlk] | core.ArrayOut[CostCategoryBlk] = core.arg()

        dimension: list[Dimension] | core.ArrayOut[Dimension] = core.arg()

        not_: list[Not] | core.ArrayOut[Not] = core.arg()

        or_: list[Or] | core.ArrayOut[Or] = core.arg()

        tags: list[Tags] | core.ArrayOut[Tags] = core.arg()


@core.schema
class InheritedValue(core.Schema):

    dimension_key: str | core.StringOut = core.attr(str, computed=True)

    dimension_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dimension_key: str | core.StringOut,
        dimension_name: str | core.StringOut,
    ):
        super().__init__(
            args=InheritedValue.Args(
                dimension_key=dimension_key,
                dimension_name=dimension_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimension_key: str | core.StringOut = core.arg()

        dimension_name: str | core.StringOut = core.arg()


@core.schema
class Rule(core.Schema):

    inherited_value: list[InheritedValue] | core.ArrayOut[InheritedValue] = core.attr(
        InheritedValue, computed=True, kind=core.Kind.array
    )

    rule: list[RuleRule] | core.ArrayOut[RuleRule] = core.attr(
        RuleRule, computed=True, kind=core.Kind.array
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        inherited_value: list[InheritedValue] | core.ArrayOut[InheritedValue],
        rule: list[RuleRule] | core.ArrayOut[RuleRule],
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Rule.Args(
                inherited_value=inherited_value,
                rule=rule,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        inherited_value: list[InheritedValue] | core.ArrayOut[InheritedValue] = core.arg()

        rule: list[RuleRule] | core.ArrayOut[RuleRule] = core.arg()

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Parameter(core.Schema):

    type: str | core.StringOut = core.attr(str, computed=True)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Parameter.Args(
                type=type,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class SplitChargeRule(core.Schema):

    method: str | core.StringOut = core.attr(str, computed=True)

    parameter: list[Parameter] | core.ArrayOut[Parameter] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    source: str | core.StringOut = core.attr(str, computed=True)

    targets: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        method: str | core.StringOut,
        parameter: list[Parameter] | core.ArrayOut[Parameter],
        source: str | core.StringOut,
        targets: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=SplitChargeRule.Args(
                method=method,
                parameter=parameter,
                source=source,
                targets=targets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        method: str | core.StringOut = core.arg()

        parameter: list[Parameter] | core.ArrayOut[Parameter] = core.arg()

        source: str | core.StringOut = core.arg()

        targets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ce_cost_category", namespace="ce")
class DsCostCategory(core.Data):
    """
    (Required) Unique name for the Cost Category.
    """

    cost_category_arn: str | core.StringOut = core.attr(str)

    """
    Effective end data of your Cost Category.
    """
    effective_end: str | core.StringOut = core.attr(str, computed=True)

    """
    Effective state data of your Cost Category.
    """
    effective_start: str | core.StringOut = core.attr(str, computed=True)

    """
    Unique ID of the cost category.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Configuration block for the Cost Category rules used to categorize costs. See below.
    """
    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, computed=True, kind=core.Kind.array)

    """
    Rule schema version in this particular Cost Category.
    """
    rule_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Configuration block for the split charge rules used to allocate your charges between your Cost Categ
    ory values. See below.
    """
    split_charge_rule: list[SplitChargeRule] | core.ArrayOut[SplitChargeRule] = core.attr(
        SplitChargeRule, computed=True, kind=core.Kind.array
    )

    """
    Resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        cost_category_arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCostCategory.Args(
                cost_category_arn=cost_category_arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
