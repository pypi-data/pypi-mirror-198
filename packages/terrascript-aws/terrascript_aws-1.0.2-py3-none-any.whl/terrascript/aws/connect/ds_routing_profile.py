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


@core.data(type="aws_connect_routing_profile", namespace="aws_connect")
class DsRoutingProfile(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_outbound_queue_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    media_concurrencies: list[MediaConcurrencies] | core.ArrayOut[MediaConcurrencies] = core.attr(
        MediaConcurrencies, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    queue_configs: list[QueueConfigs] | core.ArrayOut[QueueConfigs] = core.attr(
        QueueConfigs, computed=True, kind=core.Kind.array
    )

    routing_profile_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
