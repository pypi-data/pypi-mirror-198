import terrascript.core as core


@core.data(type="aws_ecs_service", namespace="ecs")
class DsService(core.Data):
    """
    The ARN of the ECS Service
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The arn of the ECS Cluster
    """
    cluster_arn: str | core.StringOut = core.attr(str)

    """
    The number of tasks for the ECS Service
    """
    desired_count: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The launch type for the ECS Service
    """
    launch_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The scheduling strategy for the ECS Service
    """
    scheduling_strategy: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the ECS Service
    """
    service_name: str | core.StringOut = core.attr(str)

    """
    Resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The family for the latest ACTIVE revision
    """
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
