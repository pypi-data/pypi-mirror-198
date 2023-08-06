import terrascript.core as core


@core.schema
class Constraints(core.Schema):

    encryption_context_equals: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    encryption_context_subset: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        encryption_context_equals: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        encryption_context_subset: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Constraints.Args(
                encryption_context_equals=encryption_context_equals,
                encryption_context_subset=encryption_context_subset,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_context_equals: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        encryption_context_subset: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.resource(type="aws_kms_grant", namespace="aws_kms")
class Grant(core.Resource):

    constraints: list[Constraints] | core.ArrayOut[Constraints] | None = core.attr(
        Constraints, default=None, kind=core.Kind.array
    )

    grant_creation_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    grant_id: str | core.StringOut = core.attr(str, computed=True)

    grant_token: str | core.StringOut = core.attr(str, computed=True)

    grantee_principal: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    key_id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None)

    operations: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    retire_on_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    retiring_principal: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        grantee_principal: str | core.StringOut,
        key_id: str | core.StringOut,
        operations: list[str] | core.ArrayOut[core.StringOut],
        constraints: list[Constraints] | core.ArrayOut[Constraints] | None = None,
        grant_creation_tokens: list[str] | core.ArrayOut[core.StringOut] | None = None,
        name: str | core.StringOut | None = None,
        retire_on_delete: bool | core.BoolOut | None = None,
        retiring_principal: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Grant.Args(
                grantee_principal=grantee_principal,
                key_id=key_id,
                operations=operations,
                constraints=constraints,
                grant_creation_tokens=grant_creation_tokens,
                name=name,
                retire_on_delete=retire_on_delete,
                retiring_principal=retiring_principal,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        constraints: list[Constraints] | core.ArrayOut[Constraints] | None = core.arg(default=None)

        grant_creation_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        grantee_principal: str | core.StringOut = core.arg()

        key_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        operations: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        retire_on_delete: bool | core.BoolOut | None = core.arg(default=None)

        retiring_principal: str | core.StringOut | None = core.arg(default=None)
