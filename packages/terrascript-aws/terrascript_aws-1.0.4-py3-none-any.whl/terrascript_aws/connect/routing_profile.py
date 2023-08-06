import terrascript.core as core


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


@core.resource(type="aws_connect_routing_profile", namespace="connect")
class RoutingProfile(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Routing Profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the default outbound queue for the Routing Profile.
    """
    default_outbound_queue_id: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the description of the Routing Profile.
    """
    description: str | core.StringOut = core.attr(str)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Routing Profile separate
    d by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) One or more `media_concurrencies` blocks that specify the channels that agents can handle
    in the Contact Control Panel (CCP) for this Routing Profile. The `media_concurrencies` block is doc
    umented below.
    """
    media_concurrencies: list[MediaConcurrencies] | core.ArrayOut[MediaConcurrencies] = core.attr(
        MediaConcurrencies, kind=core.Kind.array
    )

    """
    (Required) Specifies the name of the Routing Profile.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) One or more `queue_configs` blocks that specify the inbound queues associated with the ro
    uting profile. If no queue is added, the agent only can make outbound calls. The `queue_configs` blo
    ck is documented below.
    """
    queue_configs: list[QueueConfigs] | core.ArrayOut[QueueConfigs] | None = core.attr(
        QueueConfigs, default=None, kind=core.Kind.array
    )

    queue_configs_associated: list[QueueConfigsAssociated] | core.ArrayOut[
        QueueConfigsAssociated
    ] = core.attr(QueueConfigsAssociated, computed=True, kind=core.Kind.array)

    """
    The identifier for the Routing Profile.
    """
    routing_profile_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Tags to apply to the Routing Profile. If configured with a provider
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
