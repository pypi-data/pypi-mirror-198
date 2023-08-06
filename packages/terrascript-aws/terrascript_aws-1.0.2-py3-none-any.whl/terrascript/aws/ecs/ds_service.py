import terrascript.core as core


@core.data(type="aws_ecs_service", namespace="aws_ecs")
class DsService(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_arn: str | core.StringOut = core.attr(str)

    desired_count: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    launch_type: str | core.StringOut = core.attr(str, computed=True)

    scheduling_strategy: str | core.StringOut = core.attr(str, computed=True)

    service_name: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    task_definition: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_arn: str | core.StringOut,
        service_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsService.Args(
                cluster_arn=cluster_arn,
                service_name=service_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_arn: str | core.StringOut = core.arg()

        service_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
