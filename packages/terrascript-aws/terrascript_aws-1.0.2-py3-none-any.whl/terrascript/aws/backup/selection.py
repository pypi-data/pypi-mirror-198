import terrascript.core as core


@core.schema
class StringEquals(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=StringEquals.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class StringLike(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=StringLike.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class StringNotEquals(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=StringNotEquals.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class StringNotLike(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=StringNotLike.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Condition(core.Schema):

    string_equals: list[StringEquals] | core.ArrayOut[StringEquals] | None = core.attr(
        StringEquals, default=None, kind=core.Kind.array
    )

    string_like: list[StringLike] | core.ArrayOut[StringLike] | None = core.attr(
        StringLike, default=None, kind=core.Kind.array
    )

    string_not_equals: list[StringNotEquals] | core.ArrayOut[StringNotEquals] | None = core.attr(
        StringNotEquals, default=None, kind=core.Kind.array
    )

    string_not_like: list[StringNotLike] | core.ArrayOut[StringNotLike] | None = core.attr(
        StringNotLike, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        string_equals: list[StringEquals] | core.ArrayOut[StringEquals] | None = None,
        string_like: list[StringLike] | core.ArrayOut[StringLike] | None = None,
        string_not_equals: list[StringNotEquals] | core.ArrayOut[StringNotEquals] | None = None,
        string_not_like: list[StringNotLike] | core.ArrayOut[StringNotLike] | None = None,
    ):
        super().__init__(
            args=Condition.Args(
                string_equals=string_equals,
                string_like=string_like,
                string_not_equals=string_not_equals,
                string_not_like=string_not_like,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        string_equals: list[StringEquals] | core.ArrayOut[StringEquals] | None = core.arg(
            default=None
        )

        string_like: list[StringLike] | core.ArrayOut[StringLike] | None = core.arg(default=None)

        string_not_equals: list[StringNotEquals] | core.ArrayOut[StringNotEquals] | None = core.arg(
            default=None
        )

        string_not_like: list[StringNotLike] | core.ArrayOut[StringNotLike] | None = core.arg(
            default=None
        )


@core.schema
class SelectionTag(core.Schema):

    key: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=SelectionTag.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_backup_selection", namespace="aws_backup")
class Selection(core.Resource):

    condition: list[Condition] | core.ArrayOut[Condition] | None = core.attr(
        Condition, default=None, computed=True, kind=core.Kind.array
    )

    iam_role_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    not_resources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    plan_id: str | core.StringOut = core.attr(str)

    resources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    selection_tag: list[SelectionTag] | core.ArrayOut[SelectionTag] | None = core.attr(
        SelectionTag, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        iam_role_arn: str | core.StringOut,
        name: str | core.StringOut,
        plan_id: str | core.StringOut,
        condition: list[Condition] | core.ArrayOut[Condition] | None = None,
        not_resources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        resources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        selection_tag: list[SelectionTag] | core.ArrayOut[SelectionTag] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Selection.Args(
                iam_role_arn=iam_role_arn,
                name=name,
                plan_id=plan_id,
                condition=condition,
                not_resources=not_resources,
                resources=resources,
                selection_tag=selection_tag,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        condition: list[Condition] | core.ArrayOut[Condition] | None = core.arg(default=None)

        iam_role_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        not_resources: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        plan_id: str | core.StringOut = core.arg()

        resources: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        selection_tag: list[SelectionTag] | core.ArrayOut[SelectionTag] | None = core.arg(
            default=None
        )
