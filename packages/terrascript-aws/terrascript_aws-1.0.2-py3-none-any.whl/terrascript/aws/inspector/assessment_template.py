import terrascript.core as core


@core.schema
class EventSubscription(core.Schema):

    event: str | core.StringOut = core.attr(str)

    topic_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        event: str | core.StringOut,
        topic_arn: str | core.StringOut,
    ):
        super().__init__(
            args=EventSubscription.Args(
                event=event,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event: str | core.StringOut = core.arg()

        topic_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_inspector_assessment_template", namespace="aws_inspector")
class AssessmentTemplate(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    duration: int | core.IntOut = core.attr(int)

    event_subscription: list[EventSubscription] | core.ArrayOut[
        EventSubscription
    ] | None = core.attr(EventSubscription, default=None, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    rules_package_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        duration: int | core.IntOut,
        name: str | core.StringOut,
        rules_package_arns: list[str] | core.ArrayOut[core.StringOut],
        target_arn: str | core.StringOut,
        event_subscription: list[EventSubscription]
        | core.ArrayOut[EventSubscription]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AssessmentTemplate.Args(
                duration=duration,
                name=name,
                rules_package_arns=rules_package_arns,
                target_arn=target_arn,
                event_subscription=event_subscription,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        duration: int | core.IntOut = core.arg()

        event_subscription: list[EventSubscription] | core.ArrayOut[
            EventSubscription
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rules_package_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_arn: str | core.StringOut = core.arg()
