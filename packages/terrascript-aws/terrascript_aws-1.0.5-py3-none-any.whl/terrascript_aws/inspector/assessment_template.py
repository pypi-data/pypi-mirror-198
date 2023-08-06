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


@core.resource(type="aws_inspector_assessment_template", namespace="inspector")
class AssessmentTemplate(core.Resource):
    """
    The template assessment ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The duration of the inspector run.
    """
    duration: int | core.IntOut = core.attr(int)

    """
    (Optional) A block that enables sending notifications about a specified assessment template event to
    a designated SNS topic. See [Event Subscriptions](#event-subscriptions) for details.
    """
    event_subscription: list[EventSubscription] | core.ArrayOut[
        EventSubscription
    ] | None = core.attr(EventSubscription, default=None, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the assessment template.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The rules to be used during the run.
    """
    rules_package_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) Key-value map of tags for the Inspector assessment template. If configured with a provide
    r [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/
    docs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
    at the provider-level.
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

    """
    (Required) The assessment target ARN to attach the template to.
    """
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
