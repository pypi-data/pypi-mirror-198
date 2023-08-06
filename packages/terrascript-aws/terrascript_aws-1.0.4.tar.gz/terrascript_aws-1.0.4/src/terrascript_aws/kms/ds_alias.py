import terrascript.core as core


@core.data(type="aws_kms_alias", namespace="kms")
class DsAlias(core.Data):
    """
    The Amazon Resource Name(ARN) of the key alias.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name(ARN) of the key alias.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The display name of the alias. The name must start with the word "alias" followed by a fo
    rward slash (alias/)
    """
    name: str | core.StringOut = core.attr(str)

    """
    ARN pointed to by the alias.
    """
    target_key_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Key identifier pointed to by the alias.
    """
    target_key_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsAlias.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
