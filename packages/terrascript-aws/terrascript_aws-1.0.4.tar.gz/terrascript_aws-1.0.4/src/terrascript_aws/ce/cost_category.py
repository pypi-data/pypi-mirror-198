import terrascript.core as core


@core.schema
class InheritedValue(core.Schema):

    dimension_key: str | core.StringOut | None = core.attr(str, default=None)

    dimension_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        dimension_key: str | core.StringOut | None = None,
        dimension_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InheritedValue.Args(
                dimension_key=dimension_key,
                dimension_name=dimension_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimension_key: str | core.StringOut | None = core.arg(default=None)

        dimension_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CostCategoryBlk(core.Schema):

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
            args=CostCategoryBlk.Args(
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
class Tags(core.Schema):

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
            args=Tags.Args(
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
class Not(core.Schema):

    cost_category: CostCategoryBlk | None = core.attr(CostCategoryBlk, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    tags: Tags | None = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        cost_category: CostCategoryBlk | None = None,
        dimension: Dimension | None = None,
        tags: Tags | None = None,
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
        cost_category: CostCategoryBlk | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        tags: Tags | None = core.arg(default=None)


@core.schema
class Or(core.Schema):

    cost_category: CostCategoryBlk | None = core.attr(CostCategoryBlk, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    tags: Tags | None = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        cost_category: CostCategoryBlk | None = None,
        dimension: Dimension | None = None,
        tags: Tags | None = None,
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
        cost_category: CostCategoryBlk | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        tags: Tags | None = core.arg(default=None)


@core.schema
class And(core.Schema):

    cost_category: CostCategoryBlk | None = core.attr(CostCategoryBlk, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    tags: Tags | None = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        cost_category: CostCategoryBlk | None = None,
        dimension: Dimension | None = None,
        tags: Tags | None = None,
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
        cost_category: CostCategoryBlk | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        tags: Tags | None = core.arg(default=None)


@core.schema
class RuleRule(core.Schema):

    and_: list[And] | core.ArrayOut[And] | None = core.attr(
        And, default=None, kind=core.Kind.array, alias="and"
    )

    cost_category: CostCategoryBlk | None = core.attr(CostCategoryBlk, default=None)

    dimension: Dimension | None = core.attr(Dimension, default=None)

    not_: Not | None = core.attr(Not, default=None, alias="not")

    or_: list[Or] | core.ArrayOut[Or] | None = core.attr(
        Or, default=None, kind=core.Kind.array, alias="or"
    )

    tags: Tags | None = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        and_: list[And] | core.ArrayOut[And] | None = None,
        cost_category: CostCategoryBlk | None = None,
        dimension: Dimension | None = None,
        not_: Not | None = None,
        or_: list[Or] | core.ArrayOut[Or] | None = None,
        tags: Tags | None = None,
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
        and_: list[And] | core.ArrayOut[And] | None = core.arg(default=None)

        cost_category: CostCategoryBlk | None = core.arg(default=None)

        dimension: Dimension | None = core.arg(default=None)

        not_: Not | None = core.arg(default=None)

        or_: list[Or] | core.ArrayOut[Or] | None = core.arg(default=None)

        tags: Tags | None = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    inherited_value: InheritedValue | None = core.attr(InheritedValue, default=None)

    rule: RuleRule | None = core.attr(RuleRule, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        inherited_value: InheritedValue | None = None,
        rule: RuleRule | None = None,
        type: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
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
        inherited_value: InheritedValue | None = core.arg(default=None)

        rule: RuleRule | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Parameter(core.Schema):

    type: str | core.StringOut | None = core.attr(str, default=None)

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        type: str | core.StringOut | None = None,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Parameter.Args(
                type=type,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class SplitChargeRule(core.Schema):

    method: str | core.StringOut = core.attr(str)

    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    source: str | core.StringOut = core.attr(str)

    targets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        method: str | core.StringOut,
        source: str | core.StringOut,
        targets: list[str] | core.ArrayOut[core.StringOut],
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
    ):
        super().__init__(
            args=SplitChargeRule.Args(
                method=method,
                source=source,
                targets=targets,
                parameter=parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        method: str | core.StringOut = core.arg()

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)

        source: str | core.StringOut = core.arg()

        targets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_ce_cost_category", namespace="ce")
class CostCategory(core.Resource):
    """
    ARN of the cost category.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Default value for the cost category.
    """
    default_value: str | core.StringOut | None = core.attr(str, default=None)

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

    """
    (Required) Unique name for the Cost Category.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block for the Cost Category rules used to categorize costs. See below.
    """
    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, kind=core.Kind.array)

    """
    (Required) Rule schema version in this particular Cost Category.
    """
    rule_version: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for the split charge rules used to allocate your charges between your
    Cost Category values. See below.
    """
    split_charge_rule: list[SplitChargeRule] | core.ArrayOut[SplitChargeRule] | None = core.attr(
        SplitChargeRule, default=None, kind=core.Kind.array
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
        rule: list[Rule] | core.ArrayOut[Rule],
        rule_version: str | core.StringOut,
        default_value: str | core.StringOut | None = None,
        split_charge_rule: list[SplitChargeRule] | core.ArrayOut[SplitChargeRule] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CostCategory.Args(
                name=name,
                rule=rule,
                rule_version=rule_version,
                default_value=default_value,
                split_charge_rule=split_charge_rule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_value: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rule: list[Rule] | core.ArrayOut[Rule] = core.arg()

        rule_version: str | core.StringOut = core.arg()

        split_charge_rule: list[SplitChargeRule] | core.ArrayOut[SplitChargeRule] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
