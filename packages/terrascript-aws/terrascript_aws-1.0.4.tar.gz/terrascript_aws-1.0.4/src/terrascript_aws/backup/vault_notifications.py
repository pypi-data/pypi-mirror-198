import terrascript.core as core


@core.resource(type="aws_backup_vault_notifications", namespace="backup")
class VaultNotifications(core.Resource):
    """
    The ARN of the vault.
    """

    backup_vault_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) An array of events that indicate the status of jobs to back up resources to the backup va
    ult.
    """
    backup_vault_events: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) Name of the backup vault to add notifications for.
    """
    backup_vault_name: str | core.StringOut = core.attr(str)

    """
    The name of the vault.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events
    """
    sns_topic_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        backup_vault_events: list[str] | core.ArrayOut[core.StringOut],
        backup_vault_name: str | core.StringOut,
        sns_topic_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VaultNotifications.Args(
                backup_vault_events=backup_vault_events,
                backup_vault_name=backup_vault_name,
                sns_topic_arn=sns_topic_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        backup_vault_events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        backup_vault_name: str | core.StringOut = core.arg()

        sns_topic_arn: str | core.StringOut = core.arg()
