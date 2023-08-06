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
class ByteMatchTuples(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    positional_constraint: str | core.StringOut = core.attr(str)

    target_string: str | core.StringOut | None = core.attr(str, default=None)

    text_transformation: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        positional_constraint: str | core.StringOut,
        text_transformation: str | core.StringOut,
        target_string: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ByteMatchTuples.Args(
                field_to_match=field_to_match,
                positional_constraint=positional_constraint,
                text_transformation=text_transformation,
                target_string=target_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        positional_constraint: str | core.StringOut = core.arg()

        target_string: str | core.StringOut | None = core.arg(default=None)

        text_transformation: str | core.StringOut = core.arg()


@core.resource(type="aws_waf_byte_match_set", namespace="waf")
class ByteMatchSet(core.Resource):
    """
    Specifies the bytes (typically a string that corresponds
    """

    byte_match_tuples: list[ByteMatchTuples] | core.ArrayOut[ByteMatchTuples] | None = core.attr(
        ByteMatchTuples, default=None, kind=core.Kind.array
    )

    """
    The ID of the WAF Byte Match Set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or description of the Byte Match Set.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        byte_match_tuples: list[ByteMatchTuples] | core.ArrayOut[ByteMatchTuples] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ByteMatchSet.Args(
                name=name,
                byte_match_tuples=byte_match_tuples,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        byte_match_tuples: list[ByteMatchTuples] | core.ArrayOut[ByteMatchTuples] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()
