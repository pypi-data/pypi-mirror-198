import terrascript.core as core


@core.schema
class EventFilter(core.Schema):

    source: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source: str | core.StringOut,
    ):
        super().__init__(
            args=EventFilter.Args(
                source=source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source: str | core.StringOut = core.arg()


@core.resource(type="aws_appintegrations_event_integration", namespace="appintegrations")
class EventIntegration(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Event Integration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the description of the Event Integration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A block that defines the configuration information for the event filter. The Event Filter
    block is documented below.
    """
    event_filter: EventFilter = core.attr(EventFilter)

    """
    (Required) Specifies the EventBridge bus.
    """
    eventbridge_bus: str | core.StringOut = core.attr(str)

    """
    The identifier of the Event Integration which is the name of the Event Integration.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the name of the Event Integration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Tags to apply to the Event Integration. If configured with a provider [`default_tags` con
    figuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-con
    figuration-block) present, tags with matching keys will overwrite those defined at the provider-leve
    l.
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
        event_filter: EventFilter,
        eventbridge_bus: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventIntegration.Args(
                event_filter=event_filter,
                eventbridge_bus=eventbridge_bus,
                name=name,
                description=description,
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

        event_filter: EventFilter = core.arg()

        eventbridge_bus: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
