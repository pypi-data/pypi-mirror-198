import terrascript.core as core


@core.schema
class Source(core.Schema):

    configuration: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    products: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

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
class GlobalFilter(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

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

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

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

    approve_after_days: int | core.IntOut | None = core.attr(int, default=None)

    approve_until_date: str | core.StringOut | None = core.attr(str, default=None)

    compliance_level: str | core.StringOut | None = core.attr(str, default=None)

    enable_non_security: bool | core.BoolOut | None = core.attr(bool, default=None)

    patch_filter: list[PatchFilter] | core.ArrayOut[PatchFilter] = core.attr(
        PatchFilter, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        patch_filter: list[PatchFilter] | core.ArrayOut[PatchFilter],
        approve_after_days: int | core.IntOut | None = None,
        approve_until_date: str | core.StringOut | None = None,
        compliance_level: str | core.StringOut | None = None,
        enable_non_security: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ApprovalRule.Args(
                patch_filter=patch_filter,
                approve_after_days=approve_after_days,
                approve_until_date=approve_until_date,
                compliance_level=compliance_level,
                enable_non_security=enable_non_security,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        approve_after_days: int | core.IntOut | None = core.arg(default=None)

        approve_until_date: str | core.StringOut | None = core.arg(default=None)

        compliance_level: str | core.StringOut | None = core.arg(default=None)

        enable_non_security: bool | core.BoolOut | None = core.arg(default=None)

        patch_filter: list[PatchFilter] | core.ArrayOut[PatchFilter] = core.arg()


@core.resource(type="aws_ssm_patch_baseline", namespace="ssm")
class PatchBaseline(core.Resource):
    """
    (Optional) A set of rules used to include patches in the baseline. up to 10 approval rules can be sp
    ecified. Each approval_rule block requires the fields documented below.
    """

    approval_rule: list[ApprovalRule] | core.ArrayOut[ApprovalRule] | None = core.attr(
        ApprovalRule, default=None, kind=core.Kind.array
    )

    """
    (Optional) A list of explicitly approved patches for the baseline.
    """
    approved_patches: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Defines the compliance level for approved patches. This means that if an approved patch i
    s reported as missing, this is the severity of the compliance violation. Valid compliance levels inc
    lude the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default
    value is `UNSPECIFIED`.
    """
    approved_patches_compliance_level: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether the list of approved patches includes non-security updates that should
    be applied to the instances. Applies to Linux instances only.
    """
    approved_patches_enable_non_security: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The ARN of the patch baseline.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the patch baseline.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A set of global filters used to exclude patches from the baseline. Up to 4 global filters
    can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY |
    PATCH_ID`.
    """
    global_filter: list[GlobalFilter] | core.ArrayOut[GlobalFilter] | None = core.attr(
        GlobalFilter, default=None, kind=core.Kind.array
    )

    """
    The ID of the patch baseline.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the patch baseline.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Defines the operating system the patch baseline applies to. Supported operating systems i
    nclude `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRI
    SE_LINUX`. The Default value is `WINDOWS`.
    """
    operating_system: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of rejected patches.
    """
    rejected_patches: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The action for Patch Manager to take on patches included in the `rejected_patches` list.
    Allow values are `ALLOW_AS_DEPENDENCY` and `BLOCK`.
    """
    rejected_patches_action: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Configuration block(s) with alternate sources for patches. Applies to Linux instances onl
    y. Documented below.
    """
    source: list[Source] | core.ArrayOut[Source] | None = core.attr(
        Source, default=None, kind=core.Kind.array
    )

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
        name: str | core.StringOut,
        approval_rule: list[ApprovalRule] | core.ArrayOut[ApprovalRule] | None = None,
        approved_patches: list[str] | core.ArrayOut[core.StringOut] | None = None,
        approved_patches_compliance_level: str | core.StringOut | None = None,
        approved_patches_enable_non_security: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        global_filter: list[GlobalFilter] | core.ArrayOut[GlobalFilter] | None = None,
        operating_system: str | core.StringOut | None = None,
        rejected_patches: list[str] | core.ArrayOut[core.StringOut] | None = None,
        rejected_patches_action: str | core.StringOut | None = None,
        source: list[Source] | core.ArrayOut[Source] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PatchBaseline.Args(
                name=name,
                approval_rule=approval_rule,
                approved_patches=approved_patches,
                approved_patches_compliance_level=approved_patches_compliance_level,
                approved_patches_enable_non_security=approved_patches_enable_non_security,
                description=description,
                global_filter=global_filter,
                operating_system=operating_system,
                rejected_patches=rejected_patches,
                rejected_patches_action=rejected_patches_action,
                source=source,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        approval_rule: list[ApprovalRule] | core.ArrayOut[ApprovalRule] | None = core.arg(
            default=None
        )

        approved_patches: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        approved_patches_compliance_level: str | core.StringOut | None = core.arg(default=None)

        approved_patches_enable_non_security: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        global_filter: list[GlobalFilter] | core.ArrayOut[GlobalFilter] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        operating_system: str | core.StringOut | None = core.arg(default=None)

        rejected_patches: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        rejected_patches_action: str | core.StringOut | None = core.arg(default=None)

        source: list[Source] | core.ArrayOut[Source] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
