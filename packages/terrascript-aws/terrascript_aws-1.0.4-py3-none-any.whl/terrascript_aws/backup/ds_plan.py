import terrascript.core as core


@core.data(type="aws_backup_plan", namespace="backup")
class DsPlan(core.Data):
    """
    The ARN of the backup plan.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The display name of a backup plan.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The backup plan ID.
    """
    plan_id: str | core.StringOut = core.attr(str)

    """
    Metadata that you can assign to help organize the plans you create.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Unique, randomly generated, Unicode, UTF-8 encoded string that serves as the version ID of the backu
    p plan.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        plan_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPlan.Args(
                plan_id=plan_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        plan_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
