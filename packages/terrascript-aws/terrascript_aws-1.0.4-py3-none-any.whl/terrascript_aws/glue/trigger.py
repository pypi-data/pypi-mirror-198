import terrascript.core as core


@core.schema
class EventBatchingCondition(core.Schema):

    batch_size: int | core.IntOut = core.attr(int)

    batch_window: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        batch_size: int | core.IntOut,
        batch_window: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EventBatchingCondition.Args(
                batch_size=batch_size,
                batch_window=batch_window,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        batch_size: int | core.IntOut = core.arg()

        batch_window: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Conditions(core.Schema):

    crawl_state: str | core.StringOut | None = core.attr(str, default=None)

    crawler_name: str | core.StringOut | None = core.attr(str, default=None)

    job_name: str | core.StringOut | None = core.attr(str, default=None)

    logical_operator: str | core.StringOut | None = core.attr(str, default=None)

    state: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        crawl_state: str | core.StringOut | None = None,
        crawler_name: str | core.StringOut | None = None,
        job_name: str | core.StringOut | None = None,
        logical_operator: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Conditions.Args(
                crawl_state=crawl_state,
                crawler_name=crawler_name,
                job_name=job_name,
                logical_operator=logical_operator,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crawl_state: str | core.StringOut | None = core.arg(default=None)

        crawler_name: str | core.StringOut | None = core.arg(default=None)

        job_name: str | core.StringOut | None = core.arg(default=None)

        logical_operator: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Predicate(core.Schema):

    conditions: list[Conditions] | core.ArrayOut[Conditions] = core.attr(
        Conditions, kind=core.Kind.array
    )

    logical: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        conditions: list[Conditions] | core.ArrayOut[Conditions],
        logical: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Predicate.Args(
                conditions=conditions,
                logical=logical,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        conditions: list[Conditions] | core.ArrayOut[Conditions] = core.arg()

        logical: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NotificationProperty(core.Schema):

    notify_delay_after: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        notify_delay_after: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NotificationProperty.Args(
                notify_delay_after=notify_delay_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notify_delay_after: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Actions(core.Schema):

    arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    crawler_name: str | core.StringOut | None = core.attr(str, default=None)

    job_name: str | core.StringOut | None = core.attr(str, default=None)

    notification_property: NotificationProperty | None = core.attr(
        NotificationProperty, default=None
    )

    security_configuration: str | core.StringOut | None = core.attr(str, default=None)

    timeout: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        arguments: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        crawler_name: str | core.StringOut | None = None,
        job_name: str | core.StringOut | None = None,
        notification_property: NotificationProperty | None = None,
        security_configuration: str | core.StringOut | None = None,
        timeout: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Actions.Args(
                arguments=arguments,
                crawler_name=crawler_name,
                job_name=job_name,
                notification_property=notification_property,
                security_configuration=security_configuration,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        crawler_name: str | core.StringOut | None = core.arg(default=None)

        job_name: str | core.StringOut | None = core.arg(default=None)

        notification_property: NotificationProperty | None = core.arg(default=None)

        security_configuration: str | core.StringOut | None = core.arg(default=None)

        timeout: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_glue_trigger", namespace="glue")
class Trigger(core.Resource):

    actions: list[Actions] | core.ArrayOut[Actions] = core.attr(Actions, kind=core.Kind.array)

    """
    Amazon Resource Name (ARN) of Glue Trigger
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Batch condition that must be met (specified number of events received or batch time windo
    w expired) before EventBridge event trigger fires. See [Event Batching Condition](#event-batching-co
    ndition).
    """
    event_batching_condition: list[EventBatchingCondition] | core.ArrayOut[
        EventBatchingCondition
    ] | None = core.attr(EventBatchingCondition, default=None, kind=core.Kind.array)

    """
    Trigger name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    predicate: Predicate | None = core.attr(Predicate, default=None)

    schedule: str | core.StringOut | None = core.attr(str, default=None)

    start_on_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The condition job state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIM
    EOUT` and `FAILED`. If this is specified, `job_name` must also be specified. Conflicts with `crawler
    _state`.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    type: str | core.StringOut = core.attr(str)

    """
    (Optional) A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs
    a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITION
    AL` triggers.
    """
    workflow_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        actions: list[Actions] | core.ArrayOut[Actions],
        name: str | core.StringOut,
        type: str | core.StringOut,
        description: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        event_batching_condition: list[EventBatchingCondition]
        | core.ArrayOut[EventBatchingCondition]
        | None = None,
        predicate: Predicate | None = None,
        schedule: str | core.StringOut | None = None,
        start_on_creation: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        workflow_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Trigger.Args(
                actions=actions,
                name=name,
                type=type,
                description=description,
                enabled=enabled,
                event_batching_condition=event_batching_condition,
                predicate=predicate,
                schedule=schedule,
                start_on_creation=start_on_creation,
                tags=tags,
                tags_all=tags_all,
                workflow_name=workflow_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions: list[Actions] | core.ArrayOut[Actions] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        event_batching_condition: list[EventBatchingCondition] | core.ArrayOut[
            EventBatchingCondition
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        predicate: Predicate | None = core.arg(default=None)

        schedule: str | core.StringOut | None = core.arg(default=None)

        start_on_creation: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        workflow_name: str | core.StringOut | None = core.arg(default=None)
