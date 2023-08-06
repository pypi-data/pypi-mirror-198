import terrascript.core as core


@core.schema
class Setting(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Setting.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.data(type="aws_ecs_cluster", namespace="ecs")
class DsCluster(core.Data):
    """
    The ARN of the ECS Cluster
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the ECS Cluster
    """
    cluster_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of pending tasks for the ECS Cluster
    """
    pending_tasks_count: int | core.IntOut = core.attr(int, computed=True)

    """
    The number of registered container instances for the ECS Cluster
    """
    registered_container_instances_count: int | core.IntOut = core.attr(int, computed=True)

    """
    The number of running tasks for the ECS Cluster
    """
    running_tasks_count: int | core.IntOut = core.attr(int, computed=True)

    """
    The settings associated with the ECS Cluster.
    """
    setting: list[Setting] | core.ArrayOut[Setting] = core.attr(
        Setting, computed=True, kind=core.Kind.array
    )

    """
    The status of the ECS Cluster
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                cluster_name=cluster_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: str | core.StringOut = core.arg()
