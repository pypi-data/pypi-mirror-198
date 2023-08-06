import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_rule", namespace="eventbridge")
class CloudwatchEventRule(core.Resource):
    """
    The Amazon Resource Name (ARN) of the rule.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the rule.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The event bus to associate with this rule. If you omit this, the `default` event bus is u
    sed.
    """
    event_bus_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The event pattern described a JSON object. At least one of `schedule_expression` or `even
    t_pattern` is required. See full documentation of [Events and Event Patterns in EventBridge](https:/
    /docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) for details.
    """
    event_pattern: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the rule.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether the rule should be enabled (defaults to `true`).
    """
    is_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The name of the rule. If omitted, Terraform will assign a random, unique name. Conflicts
    with `name_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) associated with the role that is used for target invocatio
    n.
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The scheduling expression. For example, `cron(0 20 * * ? *)` or `rate(5 minutes)`. At lea
    st one of `schedule_expression` or `event_pattern` is required. Can only be used on the default even
    t bus. For more information, refer to the AWS documentation [Schedule Expressions for Rules](https:/
    /docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html).
    """
    schedule_expression: str | core.StringOut | None = core.attr(str, default=None)

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
        description: str | core.StringOut | None = None,
        event_bus_name: str | core.StringOut | None = None,
        event_pattern: str | core.StringOut | None = None,
        is_enabled: bool | core.BoolOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
        schedule_expression: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventRule.Args(
                description=description,
                event_bus_name=event_bus_name,
                event_pattern=event_pattern,
                is_enabled=is_enabled,
                name=name,
                name_prefix=name_prefix,
                role_arn=role_arn,
                schedule_expression=schedule_expression,
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

        event_bus_name: str | core.StringOut | None = core.arg(default=None)

        event_pattern: str | core.StringOut | None = core.arg(default=None)

        is_enabled: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        schedule_expression: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
