import terrascript.core as core


@core.data(type="aws_connect_contact_flow_module", namespace="connect")
class DsContactFlowModule(core.Data):
    """
    The Amazon Resource Name (ARN) of the Contact Flow Module.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific Contact Flow Module by contact flow module id
    """
    contact_flow_module_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    Specifies the logic of the Contact Flow Module.
    """
    content: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the description of the Contact Flow Module.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Returns information on a specific Contact Flow Module by name
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Specifies the type of Contact Flow Module Module. Values are either `ACTIVE` or `ARCHIVED`.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of the Contact Flow Module Module. Values are either `PUBLISHED` or `SAVED`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags to assign to the Contact Flow Module.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        contact_flow_module_id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsContactFlowModule.Args(
                instance_id=instance_id,
                contact_flow_module_id=contact_flow_module_id,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contact_flow_module_id: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
