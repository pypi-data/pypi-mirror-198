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


@core.data(type="aws_ecs_cluster", namespace="aws_ecs")
class DsCluster(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    pending_tasks_count: int | core.IntOut = core.attr(int, computed=True)

    registered_container_instances_count: int | core.IntOut = core.attr(int, computed=True)

    running_tasks_count: int | core.IntOut = core.attr(int, computed=True)

    setting: list[Setting] | core.ArrayOut[Setting] = core.attr(
        Setting, computed=True, kind=core.Kind.array
    )

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
