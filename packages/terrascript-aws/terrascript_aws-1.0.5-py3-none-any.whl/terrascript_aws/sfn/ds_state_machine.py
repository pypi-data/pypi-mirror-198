import terrascript.core as core


@core.data(type="aws_sfn_state_machine", namespace="sfn")
class DsStateMachine(core.Data):
    """
    Set to the arn of the state function.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date the state machine was created.
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the state machine definition.
    """
    definition: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the ARN of the found state machine, suitable for referencing in other resources that support
    State Machines.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly name of the state machine to match.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Set to the role_arn used by the state function.
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the current status of the state machine.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsStateMachine.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
