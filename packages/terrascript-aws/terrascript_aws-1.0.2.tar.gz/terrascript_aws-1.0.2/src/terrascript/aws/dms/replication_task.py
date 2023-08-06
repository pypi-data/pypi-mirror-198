import terrascript.core as core


@core.resource(type="aws_dms_replication_task", namespace="aws_dms")
class ReplicationTask(core.Resource):

    cdc_start_position: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cdc_start_time: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    migration_type: str | core.StringOut = core.attr(str)

    replication_instance_arn: str | core.StringOut = core.attr(str)

    replication_task_arn: str | core.StringOut = core.attr(str, computed=True)

    replication_task_id: str | core.StringOut = core.attr(str)

    replication_task_settings: str | core.StringOut | None = core.attr(str, default=None)

    source_endpoint_arn: str | core.StringOut = core.attr(str)

    start_replication_task: bool | core.BoolOut | None = core.attr(bool, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    table_mappings: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
