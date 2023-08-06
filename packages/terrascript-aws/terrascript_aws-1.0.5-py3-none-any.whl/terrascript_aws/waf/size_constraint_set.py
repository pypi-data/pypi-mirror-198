import terrascript.core as core


@core.schema
class FieldToMatch(core.Schema):

    data: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        data: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FieldToMatch.Args(
                type=type,
                data=data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class SizeConstraints(core.Schema):

    comparison_operator: str | core.StringOut = core.attr(str)

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    size: int | core.IntOut = core.attr(int)

    text_transformation: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison_operator: str | core.StringOut,
        field_to_match: FieldToMatch,
        size: int | core.IntOut,
        text_transformation: str | core.StringOut,
    ):
        super().__init__(
            args=SizeConstraints.Args(
                comparison_operator=comparison_operator,
                field_to_match=field_to_match,
                size=size,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison_operator: str | core.StringOut = core.arg()

        field_to_match: FieldToMatch = core.arg()

        size: int | core.IntOut = core.arg()

        text_transformation: str | core.StringOut = core.arg()


@core.resource(type="aws_waf_size_constraint_set", namespace="waf")
class SizeConstraintSet(core.Resource):
    """
    Amazon Resource Name (ARN)
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the WAF Size Constraint Set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or description of the Size Constraint Set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the parts of web requests that you want to inspect the size of.
    """
    size_constraints: list[SizeConstraints] | core.ArrayOut[SizeConstraints] | None = core.attr(
        SizeConstraints, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        size_constraints: list[SizeConstraints] | core.ArrayOut[SizeConstraints] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SizeConstraintSet.Args(
                name=name,
                size_constraints=size_constraints,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        size_constraints: list[SizeConstraints] | core.ArrayOut[SizeConstraints] | None = core.arg(
            default=None
        )
