import terrascript.core as core


@core.resource(type="aws_redshift_event_subscription", namespace="redshift")
class EventSubscription(core.Resource):
    """
    Amazon Resource Name (ARN) of the Redshift event notification subscription
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS customer account associated with the Redshift event notification subscription
    """
    customer_aws_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A boolean flag to enable/disable the subscription. Defaults to `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A list of event categories for a SourceType that you want to subscribe to. See https://do
    cs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html or run `aws redshift de
    scribe-event-categories`.
    """
    event_categories: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The name of the Redshift event notification subscription
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Redshift event subscription.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The event severity to be published by the notification subscription. Valid options are `I
    NFO` or `ERROR`. Default value of `INFO`.
    """
    severity: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ARN of the SNS topic to send events to.
    """
    sns_topic_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of identifiers of the event sources for which events will be returned. If not spec
    ified, then all sources are included in the response. If specified, a `source_type` must also be spe
    cified.
    """
    source_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The type of source that will be generating the events. Valid options are `cluster`, `clus
    ter-parameter-group`, `cluster-security-group`, `cluster-snapshot`, or `scheduled-action`. If not se
    t, all sources will be subscribed to.
    """
    source_type: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
        name: str | core.StringOut,
        sns_topic_arn: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        event_categories: list[str] | core.ArrayOut[core.StringOut] | None = None,
        severity: str | core.StringOut | None = None,
        source_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        source_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventSubscription.Args(
                name=name,
                sns_topic_arn=sns_topic_arn,
                enabled=enabled,
                event_categories=event_categories,
                severity=severity,
                source_ids=source_ids,
                source_type=source_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        event_categories: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        severity: str | core.StringOut | None = core.arg(default=None)

        sns_topic_arn: str | core.StringOut = core.arg()

        source_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        source_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
