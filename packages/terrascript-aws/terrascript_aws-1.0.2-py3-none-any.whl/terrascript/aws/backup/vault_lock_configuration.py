import terrascript.core as core


@core.resource(type="aws_backup_vault_lock_configuration", namespace="aws_backup")
class VaultLockConfiguration(core.Resource):

    backup_vault_arn: str | core.StringOut = core.attr(str, computed=True)

    backup_vault_name: str | core.StringOut = core.attr(str)

    changeable_for_days: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    max_retention_days: int | core.IntOut | None = core.attr(int, default=None)

    min_retention_days: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        backup_vault_name: str | core.StringOut,
        changeable_for_days: int | core.IntOut | None = None,
        max_retention_days: int | core.IntOut | None = None,
        min_retention_days: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VaultLockConfiguration.Args(
                backup_vault_name=backup_vault_name,
                changeable_for_days=changeable_for_days,
                max_retention_days=max_retention_days,
                min_retention_days=min_retention_days,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        backup_vault_name: str | core.StringOut = core.arg()

        changeable_for_days: int | core.IntOut | None = core.arg(default=None)

        max_retention_days: int | core.IntOut | None = core.arg(default=None)

        min_retention_days: int | core.IntOut | None = core.arg(default=None)
