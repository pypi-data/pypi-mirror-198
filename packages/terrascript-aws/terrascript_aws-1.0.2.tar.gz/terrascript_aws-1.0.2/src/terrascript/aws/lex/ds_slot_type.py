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


@core.data(type="aws_lex_slot_type", namespace="aws_lex")
class DsSlotType(core.Data):

    checksum: str | core.StringOut = core.attr(str, computed=True)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    enumeration_value: list[EnumerationValue] | core.ArrayOut[EnumerationValue] = core.attr(
        EnumerationValue, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    value_selection_strategy: str | core.StringOut = core.attr(str, computed=True)

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
