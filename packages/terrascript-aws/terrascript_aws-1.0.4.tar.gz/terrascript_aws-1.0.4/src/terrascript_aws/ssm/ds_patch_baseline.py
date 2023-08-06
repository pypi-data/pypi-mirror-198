import terrascript.core as core


@core.schema
class GlobalFilter(core.Schema):

    key: str | core.StringOut = core.attr(str, computed=True)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=GlobalFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Source(core.Schema):

    configuration: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    products: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        configuration: str | core.StringOut,
        name: str | core.StringOut,
        products: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Source.Args(
                configuration=configuration,
                name=name,
                products=products,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configuration: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        products: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class PatchFilter(core.Schema):

    key: str | core.StringOut = core.attr(str, computed=True)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=PatchFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class ApprovalRule(core.Schema):

    approve_after_days: int | core.IntOut = core.attr(int, computed=True)

    approve_until_date: str | core.StringOut = core.attr(str, computed=True)

    compliance_level: str | core.StringOut = core.attr(str, computed=True)

    enable_non_security: bool | core.BoolOut = core.attr(bool, computed=True)

    patch_filter: list[PatchFilter] | core.ArrayOut[PatchFilter] = core.attr(
        PatchFilter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        approve_after_days: int | core.IntOut,
        approve_until_date: str | core.StringOut,
        compliance_level: str | core.StringOut,
        enable_non_security: bool | core.BoolOut,
        patch_filter: list[PatchFilter] | core.ArrayOut[PatchFilter],
    ):
        super().__init__(
            args=ApprovalRule.Args(
                approve_after_days=approve_after_days,
                approve_until_date=approve_until_date,
                compliance_level=compliance_level,
                enable_non_security=enable_non_security,
                patch_filter=patch_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        approve_after_days: int | core.IntOut = core.arg()

        approve_until_date: str | core.StringOut = core.arg()

        compliance_level: str | core.StringOut = core.arg()

        enable_non_security: bool | core.BoolOut = core.arg()

        patch_filter: list[PatchFilter] | core.ArrayOut[PatchFilter] = core.arg()


@core.data(type="aws_ssm_patch_baseline", namespace="ssm")
class DsPatchBaseline(core.Data):
    """
    A list of rules used to include patches in the baseline.
    """

    approval_rule: list[ApprovalRule] | core.ArrayOut[ApprovalRule] = core.attr(
        ApprovalRule, computed=True, kind=core.Kind.array
    )

    """
    A list of explicitly approved patches for the baseline.
    """
    approved_patches: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The compliance level for approved patches.
    """
    approved_patches_compliance_level: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether the list of approved patches includes non-security updates that should be applied
    to the instances.
    """
    approved_patches_enable_non_security: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Filters the results against the baselines default_baseline field.
    """
    default_baseline: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The description of the baseline.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    A set of global filters used to exclude patches from the baseline.
    """
    global_filter: list[GlobalFilter] | core.ArrayOut[GlobalFilter] = core.attr(
        GlobalFilter, computed=True, kind=core.Kind.array
    )

    """
    The id of the baseline.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the baseline.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Filter results by the baseline name prefix.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The specified OS for the baseline.
    """
    operating_system: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The owner of the baseline. Valid values: `All`, `AWS`, `Self` (the current account).
    """
    owner: str | core.StringOut = core.attr(str)

    """
    A list of rejected patches.
    """
    rejected_patches: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The action specified to take on patches included in the `rejected_patches` list.
    """
    rejected_patches_action: str | core.StringOut = core.attr(str, computed=True)

    """
    Information about the patches to use to update the managed nodes, including target operating systems
    and source repositories.
    """
    source: list[Source] | core.ArrayOut[Source] = core.attr(
        Source, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        owner: str | core.StringOut,
        default_baseline: bool | core.BoolOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        operating_system: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPatchBaseline.Args(
                owner=owner,
                default_baseline=default_baseline,
                name_prefix=name_prefix,
                operating_system=operating_system,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_baseline: bool | core.BoolOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        operating_system: str | core.StringOut | None = core.arg(default=None)

        owner: str | core.StringOut = core.arg()
