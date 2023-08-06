import terrascript.core as core


@core.data(type="aws_lex_intent", namespace="lex")
class DsIntent(core.Data):
    """
    The ARN of the Lex intent.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Checksum identifying the version of the intent that was created. The checksum is not
    """
    checksum: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the intent version was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    A description of the intent.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the $LATEST version of this intent was updated.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the intent. The name is case sensitive.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A unique identifier for the built-in intent to base this
    """
    parent_intent_signature: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The version of the intent.
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
            args=DsIntent.Args(
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        version: str | core.StringOut | None = core.arg(default=None)
