import terrascript.core as core


@core.resource(type="aws_dms_replication_task", namespace="dms")
class ReplicationTask(core.Resource):
    """
    (Optional, Conflicts with `cdc_start_time`) Indicates when you want a change data capture (CDC) oper
    ation to start. The value can be in date, checkpoint, or LSN/SCN format depending on the source engi
    ne. For more information, see [Determining a CDC native start point](https://docs.aws.amazon.com/dms
    /latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native).
    """

    cdc_start_position: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Conflicts with `cdc_start_position`) The Unix timestamp integer for the start of the Chan
    ge Data Capture (CDC) operation.
    """
    cdc_start_time: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The migration type. Can be one of `full-load | cdc | full-load-and-cdc`.
    """
    migration_type: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the replication instance.
    """
    replication_instance_arn: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the replication task.
    """
    replication_task_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The replication task identifier.
    """
    replication_task_id: str | core.StringOut = core.attr(str)

    """
    (Optional) An escaped JSON string that contains the task settings. For a complete list of task setti
    ngs, see [Task Settings for AWS Database Migration Service Tasks](http://docs.aws.amazon.com/dms/lat
    est/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html).
    """
    replication_task_settings: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.
    """
    source_endpoint_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to run or stop the replication task.
    """
    start_replication_task: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Replication Task status.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) An escaped JSON string that contains the table mappings. For information on table mapping
    see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](htt
    p://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html)
    """
    table_mappings: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
    (Required) The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.
    """
    target_endpoint_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        migration_type: str | core.StringOut,
        replication_instance_arn: str | core.StringOut,
        replication_task_id: str | core.StringOut,
        source_endpoint_arn: str | core.StringOut,
        table_mappings: str | core.StringOut,
        target_endpoint_arn: str | core.StringOut,
        cdc_start_position: str | core.StringOut | None = None,
        cdc_start_time: str | core.StringOut | None = None,
        replication_task_settings: str | core.StringOut | None = None,
        start_replication_task: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationTask.Args(
                migration_type=migration_type,
                replication_instance_arn=replication_instance_arn,
                replication_task_id=replication_task_id,
                source_endpoint_arn=source_endpoint_arn,
                table_mappings=table_mappings,
                target_endpoint_arn=target_endpoint_arn,
                cdc_start_position=cdc_start_position,
                cdc_start_time=cdc_start_time,
                replication_task_settings=replication_task_settings,
                start_replication_task=start_replication_task,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cdc_start_position: str | core.StringOut | None = core.arg(default=None)

        cdc_start_time: str | core.StringOut | None = core.arg(default=None)

        migration_type: str | core.StringOut = core.arg()

        replication_instance_arn: str | core.StringOut = core.arg()

        replication_task_id: str | core.StringOut = core.arg()

        replication_task_settings: str | core.StringOut | None = core.arg(default=None)

        source_endpoint_arn: str | core.StringOut = core.arg()

        start_replication_task: bool | core.BoolOut | None = core.arg(default=None)

        table_mappings: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_endpoint_arn: str | core.StringOut = core.arg()
