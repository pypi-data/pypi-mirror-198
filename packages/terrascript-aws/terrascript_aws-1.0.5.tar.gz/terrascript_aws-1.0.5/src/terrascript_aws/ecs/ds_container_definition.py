import terrascript.core as core


@core.data(type="aws_ecs_container_definition", namespace="ecs")
class DsContainerDefinition(core.Data):
    """
    (Required) The name of the container definition
    """

    container_name: str | core.StringOut = core.attr(str)

    """
    The CPU limit for this container definition
    """
    cpu: int | core.IntOut = core.attr(int, computed=True)

    """
    Indicator if networking is disabled
    """
    disable_networking: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Set docker labels
    """
    docker_labels: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    The environment in use
    """
    environment: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The docker image in use, including the digest
    """
    image: str | core.StringOut = core.attr(str, computed=True)

    """
    The digest of the docker image in use
    """
    image_digest: str | core.StringOut = core.attr(str, computed=True)

    """
    The memory limit for this container definition
    """
    memory: int | core.IntOut = core.attr(int, computed=True)

    """
    The soft limit (in MiB) of memory to reserve for the container. When system memory is under contenti
    on, Docker attempts to keep the container memory to this soft limit
    """
    memory_reservation: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The ARN of the task definition which contains the container
    """
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
