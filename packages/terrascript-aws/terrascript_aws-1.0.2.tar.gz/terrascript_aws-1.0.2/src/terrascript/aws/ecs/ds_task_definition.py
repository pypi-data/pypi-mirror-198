import terrascript.core as core


@core.data(type="aws_ecs_task_definition", namespace="aws_ecs")
class DsTaskDefinition(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    family: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    network_mode: str | core.StringOut = core.attr(str, computed=True)

    revision: int | core.IntOut = core.attr(int, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    task_definition: str | core.StringOut = core.attr(str)

    task_role_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        task_definition: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsTaskDefinition.Args(
                task_definition=task_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        task_definition: str | core.StringOut = core.arg()
