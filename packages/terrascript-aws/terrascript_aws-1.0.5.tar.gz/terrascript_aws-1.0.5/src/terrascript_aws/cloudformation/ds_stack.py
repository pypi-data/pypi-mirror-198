import terrascript.core as core


@core.data(type="aws_cloudformation_stack", namespace="cloudformation")
class DsStack(core.Data):
    """
    A list of capabilities
    """

    capabilities: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Description of the stack
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the rollback of the stack is disabled when stack creation fails
    """
    disable_rollback: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The ARN of the IAM role used to create the stack.
    """
    iam_role_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the stack
    """
    name: str | core.StringOut = core.attr(str)

    """
    A list of SNS topic ARNs to publish stack related events
    """
    notification_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A map of outputs from the stack.
    """
    outputs: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    A map of parameters that specify input parameters for the stack.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    A map of tags associated with this stack.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Structure containing the template body.
    """
    template_body: str | core.StringOut = core.attr(str, computed=True)

    """
    The amount of time that can pass before the stack status becomes `CREATE_FAILED`
    """
    timeout_in_minutes: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsStack.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
