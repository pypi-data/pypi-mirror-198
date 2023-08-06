import terrascript.core as core


@core.data(type="aws_ecs_container_definition", namespace="aws_ecs")
class DsContainerDefinition(core.Data):

    container_name: str | core.StringOut = core.attr(str)

    cpu: int | core.IntOut = core.attr(int, computed=True)

    disable_networking: bool | core.BoolOut = core.attr(bool, computed=True)

    docker_labels: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    environment: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    image: str | core.StringOut = core.attr(str, computed=True)

    image_digest: str | core.StringOut = core.attr(str, computed=True)

    memory: int | core.IntOut = core.attr(int, computed=True)

    memory_reservation: int | core.IntOut = core.attr(int, computed=True)

    task_definition: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        container_name: str | core.StringOut,
        task_definition: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsContainerDefinition.Args(
                container_name=container_name,
                task_definition=task_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: str | core.StringOut = core.arg()

        task_definition: str | core.StringOut = core.arg()
