import terrascript.core as core


@core.schema
class QueueConfigs(core.Schema):

    channel: str | core.StringOut = core.attr(str, computed=True)

    delay: int | core.IntOut = core.attr(int, computed=True)

    priority: int | core.IntOut = core.attr(int, computed=True)

    queue_arn: str | core.StringOut = core.attr(str, computed=True)

    queue_id: str | core.StringOut = core.attr(str, computed=True)

    queue_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        channel: str | core.StringOut,
        delay: int | core.IntOut,
        priority: int | core.IntOut,
        queue_arn: str | core.StringOut,
        queue_id: str | core.StringOut,
        queue_name: str | core.StringOut,
    ):
        super().__init__(
            args=QueueConfigs.Args(
                channel=channel,
                delay=delay,
                priority=priority,
                queue_arn=queue_arn,
                queue_id=queue_id,
                queue_name=queue_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        channel: str | core.StringOut = core.arg()

        delay: int | core.IntOut = core.arg()

        priority: int | core.IntOut = core.arg()

        queue_arn: str | core.StringOut = core.arg()

        queue_id: str | core.StringOut = core.arg()

        queue_name: str | core.StringOut = core.arg()


@core.schema
class MediaConcurrencies(core.Schema):

    channel: str | core.StringOut = core.attr(str, computed=True)

    concurrency: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        channel: str | core.StringOut,
        concurrency: int | core.IntOut,
    ):
        super().__init__(
            args=MediaConcurrencies.Args(
                channel=channel,
                concurrency=concurrency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        channel: str | core.StringOut = core.arg()

        concurrency: int | core.IntOut = core.arg()


@core.data(type="aws_connect_routing_profile", namespace="connect")
class DsRoutingProfile(core.Data):
    """
    The Amazon Resource Name (ARN) of the Routing Profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the default outbound queue for the Routing Profile.
    """
    default_outbound_queue_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the description of the Routing Profile.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Routing Profile separate
    d by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    One or more `media_concurrencies` blocks that specify the channels that agents can handle in the Con
    tact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is documented bel
    ow.
    """
    media_concurrencies: list[MediaConcurrencies] | core.ArrayOut[MediaConcurrencies] = core.attr(
        MediaConcurrencies, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Returns information on a specific Routing Profile by name
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    One or more `queue_configs` blocks that specify the inbound queues associated with the routing profi
    le. If no queue is added, the agent only can make outbound calls. The `queue_configs` block is docum
    ented below.
    """
    queue_configs: list[QueueConfigs] | core.ArrayOut[QueueConfigs] = core.attr(
        QueueConfigs, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Returns information on a specific Routing Profile by Routing Profile id
    """
    routing_profile_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A map of tags to assign to the Routing Profile.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        name: str | core.StringOut | None = None,
        routing_profile_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRoutingProfile.Args(
                instance_id=instance_id,
                name=name,
                routing_profile_id=routing_profile_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        routing_profile_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
