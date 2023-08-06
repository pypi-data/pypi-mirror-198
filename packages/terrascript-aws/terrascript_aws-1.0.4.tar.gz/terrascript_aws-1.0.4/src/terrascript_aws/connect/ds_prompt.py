import terrascript.core as core


@core.data(type="aws_connect_prompt", namespace="connect")
class DsPrompt(core.Data):
    """
    The Amazon Resource Name (ARN) of the Prompt.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) Returns information on a specific Prompt by name
    """
    name: str | core.StringOut = core.attr(str)

    """
    The identifier for the prompt.
    """
    prompt_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsPrompt.Args(
                instance_id=instance_id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
