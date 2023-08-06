import terrascript.core as core


@core.schema
class BackupPolicyBlk(core.Schema):

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=BackupPolicyBlk.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()


@core.resource(type="aws_efs_backup_policy", namespace="efs")
class BackupPolicy(core.Resource):
    """
    (Required) A backup_policy object (documented below).
    """

    backup_policy: BackupPolicyBlk = core.attr(BackupPolicyBlk)

    """
    (Required) The ID of the EFS file system.
    """
    file_system_id: str | core.StringOut = core.attr(str)

    """
    The ID that identifies the file system (e.g., fs-ccfc0d65).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        backup_policy: BackupPolicyBlk,
        file_system_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BackupPolicy.Args(
                backup_policy=backup_policy,
                file_system_id=file_system_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        backup_policy: BackupPolicyBlk = core.arg()

        file_system_id: str | core.StringOut = core.arg()
