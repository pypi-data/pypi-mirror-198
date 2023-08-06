import terrascript.core as core


@core.schema
class EnumerationValue(core.Schema):

    synonyms: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        value: str | core.StringOut,
        synonyms: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=EnumerationValue.Args(
                value=value,
                synonyms=synonyms,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        synonyms: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_lex_slot_type", namespace="lex")
class SlotType(core.Resource):
    """
    Checksum identifying the version of the slot type that was created. The checksum is
    """

    checksum: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional)
    """
    create_version: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The date when the slot type version was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of the slot type. Must be less than or equal to 200 characters in length.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A list of EnumerationValue objects that defines the values that
    """
    enumeration_value: list[EnumerationValue] | core.ArrayOut[EnumerationValue] = core.attr(
        EnumerationValue, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the `$LATEST` version of this slot type was updated.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the slot type. The name is not case sensitive. Must be less than or equal to
    100 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Determines the slot resolution strategy that Amazon Lex
    """
    value_selection_strategy: str | core.StringOut | None = core.attr(str, default=None)

    """
    The version of the slot type.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        enumeration_value: list[EnumerationValue] | core.ArrayOut[EnumerationValue],
        name: str | core.StringOut,
        create_version: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        value_selection_strategy: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SlotType.Args(
                enumeration_value=enumeration_value,
                name=name,
                create_version=create_version,
                description=description,
                value_selection_strategy=value_selection_strategy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        create_version: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        enumeration_value: list[EnumerationValue] | core.ArrayOut[EnumerationValue] = core.arg()

        name: str | core.StringOut = core.arg()

        value_selection_strategy: str | core.StringOut | None = core.arg(default=None)
