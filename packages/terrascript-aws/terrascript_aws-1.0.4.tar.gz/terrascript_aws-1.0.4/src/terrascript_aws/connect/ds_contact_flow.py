import terrascript.core as core


@core.data(type="aws_connect_contact_flow", namespace="connect")
class DsContactFlow(core.Data):
    """
    The Amazon Resource Name (ARN) of the Contact Flow.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific Contact Flow by contact flow id
    """
    contact_flow_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Specifies the logic of the Contact Flow.
    """
    content: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the description of the Contact Flow.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Returns information on a specific Contact Flow by name
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A the map of tags to assign to the Contact Flow.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Specifies the type of Contact Flow.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        contact_flow_id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsContactFlow.Args(
                instance_id=instance_id,
                contact_flow_id=contact_flow_id,
                name=name,
                tags=tags,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contact_flow_id: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
