import terrascript.core as core


@core.schema
class OutboundCallerConfig(core.Schema):

    outbound_caller_id_name: str | core.StringOut | None = core.attr(str, default=None)

    outbound_caller_id_number_id: str | core.StringOut | None = core.attr(str, default=None)

    outbound_flow_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        outbound_caller_id_name: str | core.StringOut | None = None,
        outbound_caller_id_number_id: str | core.StringOut | None = None,
        outbound_flow_id: str | core.StringOut | None = None,
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
        outbound_caller_id_name: str | core.StringOut | None = core.arg(default=None)

        outbound_caller_id_number_id: str | core.StringOut | None = core.arg(default=None)

        outbound_flow_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_connect_queue", namespace="aws_connect")
class Queue(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    hours_of_operation_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    max_contacts: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut = core.attr(str)

    outbound_caller_config: OutboundCallerConfig | None = core.attr(
        OutboundCallerConfig, default=None
    )

    queue_id: str | core.StringOut = core.attr(str, computed=True)

    quick_connect_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    quick_connect_ids_associated: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        hours_of_operation_id: str | core.StringOut,
        instance_id: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        max_contacts: int | core.IntOut | None = None,
        outbound_caller_config: OutboundCallerConfig | None = None,
        quick_connect_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        status: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Queue.Args(
                hours_of_operation_id=hours_of_operation_id,
                instance_id=instance_id,
                name=name,
                description=description,
                max_contacts=max_contacts,
                outbound_caller_config=outbound_caller_config,
                quick_connect_ids=quick_connect_ids,
                status=status,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        hours_of_operation_id: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()

        max_contacts: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        outbound_caller_config: OutboundCallerConfig | None = core.arg(default=None)

        quick_connect_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
