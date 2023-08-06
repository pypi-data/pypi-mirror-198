import terrascript.core as core


@core.data(type="aws_qldb_ledger", namespace="qldb")
class DsLedger(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    deletion_protection: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly name of the ledger to match.
    """
    name: str | core.StringOut = core.attr(str)

    permissions_mode: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLedger.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
