import terrascript.core as core


@core.schema
class Principals(core.Schema):

    identifiers: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        identifiers: list[str] | core.ArrayOut[core.StringOut],
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Principals.Args(
                identifiers=identifiers,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifiers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class NotPrincipals(core.Schema):

    identifiers: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        identifiers: list[str] | core.ArrayOut[core.StringOut],
        type: str | core.StringOut,
    ):
        super().__init__(
            args=NotPrincipals.Args(
                identifiers=identifiers,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifiers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class Condition(core.Schema):

    test: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    variable: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        test: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
        variable: str | core.StringOut,
    ):
        super().__init__(
            args=Condition.Args(
                test=test,
                values=values,
                variable=variable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        test: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        variable: str | core.StringOut = core.arg()


@core.schema
class Statement(core.Schema):

    actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    condition: list[Condition] | core.ArrayOut[Condition] | None = core.attr(
        Condition, default=None, kind=core.Kind.array
    )

    effect: str | core.StringOut | None = core.attr(str, default=None)

    not_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    not_principals: list[NotPrincipals] | core.ArrayOut[NotPrincipals] | None = core.attr(
        NotPrincipals, default=None, kind=core.Kind.array
    )

    not_resources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    principals: list[Principals] | core.ArrayOut[Principals] | None = core.attr(
        Principals, default=None, kind=core.Kind.array
    )

    resources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    sid: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        condition: list[Condition] | core.ArrayOut[Condition] | None = None,
        effect: str | core.StringOut | None = None,
        not_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        not_principals: list[NotPrincipals] | core.ArrayOut[NotPrincipals] | None = None,
        not_resources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        principals: list[Principals] | core.ArrayOut[Principals] | None = None,
        resources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        sid: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Statement.Args(
                actions=actions,
                condition=condition,
                effect=effect,
                not_actions=not_actions,
                not_principals=not_principals,
                not_resources=not_resources,
                principals=principals,
                resources=resources,
                sid=sid,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        condition: list[Condition] | core.ArrayOut[Condition] | None = core.arg(default=None)

        effect: str | core.StringOut | None = core.arg(default=None)

        not_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        not_principals: list[NotPrincipals] | core.ArrayOut[NotPrincipals] | None = core.arg(
            default=None
        )

        not_resources: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        principals: list[Principals] | core.ArrayOut[Principals] | None = core.arg(default=None)

        resources: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        sid: str | core.StringOut | None = core.arg(default=None)


@core.data(type="aws_iam_policy_document", namespace="iam")
class DsPolicyDocument(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Standard JSON policy document rendered based on the arguments above.
    """
    json: str | core.StringOut = core.attr(str, computed=True)

    override_json: str | core.StringOut | None = core.attr(str, default=None)

    override_policy_documents: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    policy_id: str | core.StringOut | None = core.attr(str, default=None)

    source_json: str | core.StringOut | None = core.attr(str, default=None)

    source_policy_documents: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    statement: list[Statement] | core.ArrayOut[Statement] | None = core.attr(
        Statement, default=None, kind=core.Kind.array
    )

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        override_json: str | core.StringOut | None = None,
        override_policy_documents: list[str] | core.ArrayOut[core.StringOut] | None = None,
        policy_id: str | core.StringOut | None = None,
        source_json: str | core.StringOut | None = None,
        source_policy_documents: list[str] | core.ArrayOut[core.StringOut] | None = None,
        statement: list[Statement] | core.ArrayOut[Statement] | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPolicyDocument.Args(
                override_json=override_json,
                override_policy_documents=override_policy_documents,
                policy_id=policy_id,
                source_json=source_json,
                source_policy_documents=source_policy_documents,
                statement=statement,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        override_json: str | core.StringOut | None = core.arg(default=None)

        override_policy_documents: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        policy_id: str | core.StringOut | None = core.arg(default=None)

        source_json: str | core.StringOut | None = core.arg(default=None)

        source_policy_documents: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        statement: list[Statement] | core.ArrayOut[Statement] | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)
