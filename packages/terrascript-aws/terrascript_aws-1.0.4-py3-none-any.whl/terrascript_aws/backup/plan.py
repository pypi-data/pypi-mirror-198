import terrascript.core as core


@core.schema
class Lifecycle(core.Schema):

    cold_storage_after: int | core.IntOut | None = core.attr(int, default=None)

    delete_after: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cold_storage_after: int | core.IntOut | None = None,
        delete_after: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Lifecycle.Args(
                cold_storage_after=cold_storage_after,
                delete_after=delete_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cold_storage_after: int | core.IntOut | None = core.arg(default=None)

        delete_after: int | core.IntOut | None = core.arg(default=None)


@core.schema
class CopyAction(core.Schema):

    destination_vault_arn: str | core.StringOut = core.attr(str)

    lifecycle: Lifecycle | None = core.attr(Lifecycle, default=None)

    def __init__(
        self,
        *,
        destination_vault_arn: str | core.StringOut,
        lifecycle: Lifecycle | None = None,
    ):
        super().__init__(
            args=CopyAction.Args(
                destination_vault_arn=destination_vault_arn,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_vault_arn: str | core.StringOut = core.arg()

        lifecycle: Lifecycle | None = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    completion_window: int | core.IntOut | None = core.attr(int, default=None)

    copy_action: list[CopyAction] | core.ArrayOut[CopyAction] | None = core.attr(
        CopyAction, default=None, kind=core.Kind.array
    )

    enable_continuous_backup: bool | core.BoolOut | None = core.attr(bool, default=None)

    lifecycle: Lifecycle | None = core.attr(Lifecycle, default=None)

    recovery_point_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rule_name: str | core.StringOut = core.attr(str)

    schedule: str | core.StringOut | None = core.attr(str, default=None)

    start_window: int | core.IntOut | None = core.attr(int, default=None)

    target_vault_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        rule_name: str | core.StringOut,
        target_vault_name: str | core.StringOut,
        completion_window: int | core.IntOut | None = None,
        copy_action: list[CopyAction] | core.ArrayOut[CopyAction] | None = None,
        enable_continuous_backup: bool | core.BoolOut | None = None,
        lifecycle: Lifecycle | None = None,
        recovery_point_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        schedule: str | core.StringOut | None = None,
        start_window: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                rule_name=rule_name,
                target_vault_name=target_vault_name,
                completion_window=completion_window,
                copy_action=copy_action,
                enable_continuous_backup=enable_continuous_backup,
                lifecycle=lifecycle,
                recovery_point_tags=recovery_point_tags,
                schedule=schedule,
                start_window=start_window,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        completion_window: int | core.IntOut | None = core.arg(default=None)

        copy_action: list[CopyAction] | core.ArrayOut[CopyAction] | None = core.arg(default=None)

        enable_continuous_backup: bool | core.BoolOut | None = core.arg(default=None)

        lifecycle: Lifecycle | None = core.arg(default=None)

        recovery_point_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        rule_name: str | core.StringOut = core.arg()

        schedule: str | core.StringOut | None = core.arg(default=None)

        start_window: int | core.IntOut | None = core.arg(default=None)

        target_vault_name: str | core.StringOut = core.arg()


@core.schema
class AdvancedBackupSetting(core.Schema):

    backup_options: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, kind=core.Kind.map
    )

    resource_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        backup_options: dict[str, str] | core.MapOut[core.StringOut],
        resource_type: str | core.StringOut,
    ):
        super().__init__(
            args=AdvancedBackupSetting.Args(
                backup_options=backup_options,
                resource_type=resource_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        backup_options: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        resource_type: str | core.StringOut = core.arg()


@core.resource(type="aws_backup_plan", namespace="backup")
class Plan(core.Resource):
    """
    (Optional) An object that specifies backup options for each resource type.
    """

    advanced_backup_setting: list[AdvancedBackupSetting] | core.ArrayOut[
        AdvancedBackupSetting
    ] | None = core.attr(AdvancedBackupSetting, default=None, kind=core.Kind.array)

    """
    The ARN of the backup plan.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The id of the backup plan.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The display name of a backup plan.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) A rule object that specifies a scheduled task that is used to back up a selection of reso
    urces.
    """
    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, kind=core.Kind.array)

    """
    (Optional) Metadata that you can assign to help organize the plans you create. If configured with a
    provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/
    latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those
    defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Unique, randomly generated, Unicode, UTF-8 encoded string that serves as the version ID of the backu
    p plan.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        rule: list[Rule] | core.ArrayOut[Rule],
        advanced_backup_setting: list[AdvancedBackupSetting]
        | core.ArrayOut[AdvancedBackupSetting]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Plan.Args(
                name=name,
                rule=rule,
                advanced_backup_setting=advanced_backup_setting,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        advanced_backup_setting: list[AdvancedBackupSetting] | core.ArrayOut[
            AdvancedBackupSetting
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rule: list[Rule] | core.ArrayOut[Rule] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
