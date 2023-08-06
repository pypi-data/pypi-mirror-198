import terrascript.core as core


@core.resource(type="aws_cloudwatch_composite_alarm", namespace="cloudwatch")
class CompositeAlarm(core.Resource):
    """
    (Optional, Forces new resource) Indicates whether actions should be executed during any changes to t
    he alarm state of the composite alarm. Defaults to `true`.
    """

    actions_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The set of actions to execute when this alarm transitions to the `ALARM` state from any o
    ther state. Each action is specified as an ARN. Up to 5 actions are allowed.
    """
    alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The description for the composite alarm.
    """
    alarm_description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name for the composite alarm. This name must be unique within the region.
    """
    alarm_name: str | core.StringOut = core.attr(str)

    """
    (Required) An expression that specifies which other alarms are to be evaluated to determine this com
    posite alarm's state. For syntax, see [Creating a Composite Alarm](https://docs.aws.amazon.com/Amazo
    nCloudWatch/latest/monitoring/Create_Composite_Alarm.html). The maximum length is 10240 characters.
    """
    alarm_rule: str | core.StringOut = core.attr(str)

    """
    The ARN of the composite alarm.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the composite alarm resource, which is equivalent to its `alarm_name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The set of actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` stat
    e from any other state. Each action is specified as an ARN. Up to 5 actions are allowed.
    """
    insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The set of actions to execute when this alarm transitions to an `OK` state from any other
    state. Each action is specified as an ARN. Up to 5 actions are allowed.
    """
    ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to associate with the alarm. Up to 50 tags are allowed. If configured with
    a provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aw
    s/latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite thos
    e defined at the provider-level.
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
        alarm_name: str | core.StringOut,
        alarm_rule: str | core.StringOut,
        actions_enabled: bool | core.BoolOut | None = None,
        alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        alarm_description: str | core.StringOut | None = None,
        insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CompositeAlarm.Args(
                alarm_name=alarm_name,
                alarm_rule=alarm_rule,
                actions_enabled=actions_enabled,
                alarm_actions=alarm_actions,
                alarm_description=alarm_description,
                insufficient_data_actions=insufficient_data_actions,
                ok_actions=ok_actions,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions_enabled: bool | core.BoolOut | None = core.arg(default=None)

        alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        alarm_description: str | core.StringOut | None = core.arg(default=None)

        alarm_name: str | core.StringOut = core.arg()

        alarm_rule: str | core.StringOut = core.arg()

        insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
