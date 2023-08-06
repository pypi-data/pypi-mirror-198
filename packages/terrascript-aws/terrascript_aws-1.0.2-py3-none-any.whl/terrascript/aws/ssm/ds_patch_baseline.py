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


@core.data(type="aws_ssm_patch_baseline", namespace="aws_ssm")
class DsPatchBaseline(core.Data):

    approval_rule: list[ApprovalRule] | core.ArrayOut[ApprovalRule] = core.attr(
        ApprovalRule, computed=True, kind=core.Kind.array
    )

    approved_patches: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    approved_patches_compliance_level: str | core.StringOut = core.attr(str, computed=True)

    approved_patches_enable_non_security: bool | core.BoolOut = core.attr(bool, computed=True)

    default_baseline: bool | core.BoolOut | None = core.attr(bool, default=None)

    description: str | core.StringOut = core.attr(str, computed=True)

    global_filter: list[GlobalFilter] | core.ArrayOut[GlobalFilter] = core.attr(
        GlobalFilter, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    operating_system: str | core.StringOut | None = core.attr(str, default=None)

    owner: str | core.StringOut = core.attr(str)

    rejected_patches: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    rejected_patches_action: str | core.StringOut = core.attr(str, computed=True)

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
