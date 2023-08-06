import terrascript.core as core


@core.data(type="aws_connect_contact_flow_module", namespace="aws_connect")
class DsContactFlowModule(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    contact_flow_module_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    content: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

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
