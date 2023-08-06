import terrascript.core as core


@core.data(type="aws_ecs_task_definition", namespace="ecs")
class DsTaskDefinition(core.Data):
    """
    The ARN of the task definition
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The family of this task definition
    """
    family: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the task definition
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Docker networking mode to use for the containers in this task.
    """
    network_mode: str | core.StringOut = core.attr(str, computed=True)

    """
    The revision of this task definition
    """
    revision: int | core.IntOut = core.attr(int, computed=True)

    """
    The status of this task definition
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The family for the latest ACTIVE revision, family and revision (family:revision) for a sp
    ecific revision in the family, the ARN of the task definition to access to.
    """
    task_definition: str | core.StringOut = core.attr(str)

    """
    The ARN of the IAM role that containers in this task can assume
    """
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
