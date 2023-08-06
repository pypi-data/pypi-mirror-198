import terrascript.core as core


@core.schema
class InlinePolicy(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    policy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InlinePolicy.Args(
                name=name,
                policy=policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_iam_role", namespace="aws_iam")
class Role(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    assume_role_policy: str | core.StringOut = core.attr(str)

    create_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    force_detach_policies: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    inline_policy: list[InlinePolicy] | core.ArrayOut[InlinePolicy] | None = core.attr(
        InlinePolicy, default=None, computed=True, kind=core.Kind.array
    )

    managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    max_session_duration: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    path: str | core.StringOut | None = core.attr(str, default=None)

    permissions_boundary: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        assume_role_policy: str | core.StringOut,
        description: str | core.StringOut | None = None,
        force_detach_policies: bool | core.BoolOut | None = None,
        inline_policy: list[InlinePolicy] | core.ArrayOut[InlinePolicy] | None = None,
        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        max_session_duration: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
        permissions_boundary: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Role.Args(
                assume_role_policy=assume_role_policy,
                description=description,
                force_detach_policies=force_detach_policies,
                inline_policy=inline_policy,
                managed_policy_arns=managed_policy_arns,
                max_session_duration=max_session_duration,
                name=name,
                name_prefix=name_prefix,
                path=path,
                permissions_boundary=permissions_boundary,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        assume_role_policy: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        force_detach_policies: bool | core.BoolOut | None = core.arg(default=None)

        inline_policy: list[InlinePolicy] | core.ArrayOut[InlinePolicy] | None = core.arg(
            default=None
        )

        managed_policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        max_session_duration: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        permissions_boundary: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
