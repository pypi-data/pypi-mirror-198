import terrascript.core as core


@core.schema
class EnumerationValue(core.Schema):

    synonyms: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        synonyms: list[str] | core.ArrayOut[core.StringOut],
        value: str | core.StringOut,
    ):
        super().__init__(
            args=EnumerationValue.Args(
                synonyms=synonyms,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        synonyms: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        value: str | core.StringOut = core.arg()


@core.data(type="aws_lex_slot_type", namespace="lex")
class DsSlotType(core.Data):
    """
    Checksum identifying the version of the slot type that was created. The checksum is
    """

    checksum: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the slot type version was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    A description of the slot type.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    A set of EnumerationValue objects that defines the values that
    """
    enumeration_value: list[EnumerationValue] | core.ArrayOut[EnumerationValue] = core.attr(
        EnumerationValue, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the $LATEST version of this slot type was updated.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the slot type. The name is case sensitive.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Determines the slot resolution strategy that Amazon Lex
    """
    value_selection_strategy: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The version of the slot type.
    """
    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSlotType.Args(
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        version: str | core.StringOut | None = core.arg(default=None)
