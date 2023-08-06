import terrascript.core as core


@core.schema
class OutboundCallerConfig(core.Schema):

    outbound_caller_id_name: str | core.StringOut = core.attr(str, computed=True)

    outbound_caller_id_number_id: str | core.StringOut = core.attr(str, computed=True)

    outbound_flow_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        outbound_caller_id_name: str | core.StringOut,
        outbound_caller_id_number_id: str | core.StringOut,
        outbound_flow_id: str | core.StringOut,
    ):
        super().__init__(
            args=OutboundCallerConfig.Args(
                outbound_caller_id_name=outbound_caller_id_name,
                outbound_caller_id_number_id=outbound_caller_id_number_id,
                outbound_flow_id=outbound_flow_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        outbound_caller_id_name: str | core.StringOut = core.arg()

        outbound_caller_id_number_id: str | core.StringOut = core.arg()

        outbound_flow_id: str | core.StringOut = core.arg()


@core.data(type="aws_connect_queue", namespace="connect")
class DsQueue(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    hours_of_operation_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    max_contacts: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    outbound_caller_config: list[OutboundCallerConfig] | core.ArrayOut[
        OutboundCallerConfig
    ] = core.attr(OutboundCallerConfig, computed=True, kind=core.Kind.array)

    queue_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        name: str | core.StringOut | None = None,
        queue_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsQueue.Args(
                instance_id=instance_id,
                name=name,
                queue_id=queue_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        queue_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
