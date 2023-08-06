import terrascript.core as core


@core.data(type="aws_backup_vault", namespace="backup")
class DsVault(core.Data):
    """
    The ARN of the vault.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The server-side encryption key that is used to protect your backups.
    """
    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the backup vault.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The number of recovery points that are stored in a backup vault.
    """
    recovery_points: int | core.IntOut = core.attr(int, computed=True)

    """
    Metadata that you can assign to help organize the resources that you create.
    """
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
            args=DsVault.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
