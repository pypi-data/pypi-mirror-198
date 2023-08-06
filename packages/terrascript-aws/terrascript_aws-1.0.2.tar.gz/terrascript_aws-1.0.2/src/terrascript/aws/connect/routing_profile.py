import terrascript.core as core


@core.schema
class QueueConfigsAssociated(core.Schema):

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
            args=QueueConfigsAssociated.Args(
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
class QueueConfigs(core.Schema):

    channel: str | core.StringOut = core.attr(str)

    delay: int | core.IntOut = core.attr(int)

    priority: int | core.IntOut = core.attr(int)

    queue_arn: str | core.StringOut = core.attr(str, computed=True)

    queue_id: str | core.StringOut = core.attr(str)

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

    channel: str | core.StringOut = core.attr(str)

    concurrency: int | core.IntOut = core.attr(int)

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


@core.resource(type="aws_connect_routing_profile", namespace="aws_connect")
class RoutingProfile(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_outbound_queue_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    media_concurrencies: list[MediaConcurrencies] | core.ArrayOut[MediaConcurrencies] = core.attr(
        MediaConcurrencies, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    queue_configs: list[QueueConfigs] | core.ArrayOut[QueueConfigs] | None = core.attr(
        QueueConfigs, default=None, kind=core.Kind.array
    )

    queue_configs_associated: list[QueueConfigsAssociated] | core.ArrayOut[
        QueueConfigsAssociated
    ] = core.attr(QueueConfigsAssociated, computed=True, kind=core.Kind.array)

    routing_profile_id: str | core.StringOut = core.attr(str, computed=True)

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
        default_outbound_queue_id: str | core.StringOut,
        description: str | core.StringOut,
        instance_id: str | core.StringOut,
        media_concurrencies: list[MediaConcurrencies] | core.ArrayOut[MediaConcurrencies],
        name: str | core.StringOut,
        queue_configs: list[QueueConfigs] | core.ArrayOut[QueueConfigs] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoutingProfile.Args(
                default_outbound_queue_id=default_outbound_queue_id,
                description=description,
                instance_id=instance_id,
                media_concurrencies=media_concurrencies,
                name=name,
                queue_configs=queue_configs,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_outbound_queue_id: str | core.StringOut = core.arg()

        description: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()

        media_concurrencies: list[MediaConcurrencies] | core.ArrayOut[
            MediaConcurrencies
        ] = core.arg()

        name: str | core.StringOut = core.arg()

        queue_configs: list[QueueConfigs] | core.ArrayOut[QueueConfigs] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
