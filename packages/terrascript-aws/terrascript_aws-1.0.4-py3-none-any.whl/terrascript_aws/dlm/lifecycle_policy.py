import terrascript.core as core


@core.schema
class PolicyDetailsParameters(core.Schema):

    exclude_boot_volume: bool | core.BoolOut | None = core.attr(bool, default=None)

    no_reboot: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        exclude_boot_volume: bool | core.BoolOut | None = None,
        no_reboot: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=PolicyDetailsParameters.Args(
                exclude_boot_volume=exclude_boot_volume,
                no_reboot=no_reboot,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_boot_volume: bool | core.BoolOut | None = core.arg(default=None)

        no_reboot: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class FastRestoreRule(core.Schema):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    count: int | core.IntOut | None = core.attr(int, default=None)

    interval: int | core.IntOut | None = core.attr(int, default=None)

    interval_unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        availability_zones: list[str] | core.ArrayOut[core.StringOut],
        count: int | core.IntOut | None = None,
        interval: int | core.IntOut | None = None,
        interval_unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FastRestoreRule.Args(
                availability_zones=availability_zones,
                count=count,
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        count: int | core.IntOut | None = core.arg(default=None)

        interval: int | core.IntOut | None = core.arg(default=None)

        interval_unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CrossRegionCopyRuleRetainRule(core.Schema):

    interval: int | core.IntOut = core.attr(int)

    interval_unit: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        interval: int | core.IntOut,
        interval_unit: str | core.StringOut,
    ):
        super().__init__(
            args=CrossRegionCopyRuleRetainRule.Args(
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: int | core.IntOut = core.arg()

        interval_unit: str | core.StringOut = core.arg()


@core.schema
class CrossRegionCopyRuleDeprecateRule(core.Schema):

    interval: int | core.IntOut = core.attr(int)

    interval_unit: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        interval: int | core.IntOut,
        interval_unit: str | core.StringOut,
    ):
        super().__init__(
            args=CrossRegionCopyRuleDeprecateRule.Args(
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: int | core.IntOut = core.arg()

        interval_unit: str | core.StringOut = core.arg()


@core.schema
class CrossRegionCopyRule(core.Schema):

    cmk_arn: str | core.StringOut | None = core.attr(str, default=None)

    copy_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    deprecate_rule: CrossRegionCopyRuleDeprecateRule | None = core.attr(
        CrossRegionCopyRuleDeprecateRule, default=None
    )

    encrypted: bool | core.BoolOut = core.attr(bool)

    retain_rule: CrossRegionCopyRuleRetainRule | None = core.attr(
        CrossRegionCopyRuleRetainRule, default=None
    )

    target: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        encrypted: bool | core.BoolOut,
        target: str | core.StringOut,
        cmk_arn: str | core.StringOut | None = None,
        copy_tags: bool | core.BoolOut | None = None,
        deprecate_rule: CrossRegionCopyRuleDeprecateRule | None = None,
        retain_rule: CrossRegionCopyRuleRetainRule | None = None,
    ):
        super().__init__(
            args=CrossRegionCopyRule.Args(
                encrypted=encrypted,
                target=target,
                cmk_arn=cmk_arn,
                copy_tags=copy_tags,
                deprecate_rule=deprecate_rule,
                retain_rule=retain_rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cmk_arn: str | core.StringOut | None = core.arg(default=None)

        copy_tags: bool | core.BoolOut | None = core.arg(default=None)

        deprecate_rule: CrossRegionCopyRuleDeprecateRule | None = core.arg(default=None)

        encrypted: bool | core.BoolOut = core.arg()

        retain_rule: CrossRegionCopyRuleRetainRule | None = core.arg(default=None)

        target: str | core.StringOut = core.arg()


@core.schema
class ScheduleDeprecateRule(core.Schema):

    count: int | core.IntOut | None = core.attr(int, default=None)

    interval: int | core.IntOut | None = core.attr(int, default=None)

    interval_unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        count: int | core.IntOut | None = None,
        interval: int | core.IntOut | None = None,
        interval_unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ScheduleDeprecateRule.Args(
                count=count,
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut | None = core.arg(default=None)

        interval: int | core.IntOut | None = core.arg(default=None)

        interval_unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ShareRule(core.Schema):

    target_accounts: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    unshare_interval: int | core.IntOut | None = core.attr(int, default=None)

    unshare_interval_unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        target_accounts: list[str] | core.ArrayOut[core.StringOut],
        unshare_interval: int | core.IntOut | None = None,
        unshare_interval_unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ShareRule.Args(
                target_accounts=target_accounts,
                unshare_interval=unshare_interval,
                unshare_interval_unit=unshare_interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_accounts: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        unshare_interval: int | core.IntOut | None = core.arg(default=None)

        unshare_interval_unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ScheduleRetainRule(core.Schema):

    count: int | core.IntOut | None = core.attr(int, default=None)

    interval: int | core.IntOut | None = core.attr(int, default=None)

    interval_unit: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        count: int | core.IntOut | None = None,
        interval: int | core.IntOut | None = None,
        interval_unit: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ScheduleRetainRule.Args(
                count=count,
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut | None = core.arg(default=None)

        interval: int | core.IntOut | None = core.arg(default=None)

        interval_unit: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CreateRule(core.Schema):

    cron_expression: str | core.StringOut | None = core.attr(str, default=None)

    interval: int | core.IntOut | None = core.attr(int, default=None)

    interval_unit: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    location: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    times: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cron_expression: str | core.StringOut | None = None,
        interval: int | core.IntOut | None = None,
        interval_unit: str | core.StringOut | None = None,
        location: str | core.StringOut | None = None,
        times: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=CreateRule.Args(
                cron_expression=cron_expression,
                interval=interval,
                interval_unit=interval_unit,
                location=location,
                times=times,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cron_expression: str | core.StringOut | None = core.arg(default=None)

        interval: int | core.IntOut | None = core.arg(default=None)

        interval_unit: str | core.StringOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        times: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Schedule(core.Schema):

    copy_tags: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    create_rule: CreateRule = core.attr(CreateRule)

    cross_region_copy_rule: list[CrossRegionCopyRule] | core.ArrayOut[
        CrossRegionCopyRule
    ] | None = core.attr(CrossRegionCopyRule, default=None, kind=core.Kind.array)

    deprecate_rule: ScheduleDeprecateRule | None = core.attr(ScheduleDeprecateRule, default=None)

    fast_restore_rule: FastRestoreRule | None = core.attr(FastRestoreRule, default=None)

    name: str | core.StringOut = core.attr(str)

    retain_rule: ScheduleRetainRule = core.attr(ScheduleRetainRule)

    share_rule: ShareRule | None = core.attr(ShareRule, default=None)

    tags_to_add: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    variable_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        create_rule: CreateRule,
        name: str | core.StringOut,
        retain_rule: ScheduleRetainRule,
        copy_tags: bool | core.BoolOut | None = None,
        cross_region_copy_rule: list[CrossRegionCopyRule]
        | core.ArrayOut[CrossRegionCopyRule]
        | None = None,
        deprecate_rule: ScheduleDeprecateRule | None = None,
        fast_restore_rule: FastRestoreRule | None = None,
        share_rule: ShareRule | None = None,
        tags_to_add: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        variable_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Schedule.Args(
                create_rule=create_rule,
                name=name,
                retain_rule=retain_rule,
                copy_tags=copy_tags,
                cross_region_copy_rule=cross_region_copy_rule,
                deprecate_rule=deprecate_rule,
                fast_restore_rule=fast_restore_rule,
                share_rule=share_rule,
                tags_to_add=tags_to_add,
                variable_tags=variable_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_tags: bool | core.BoolOut | None = core.arg(default=None)

        create_rule: CreateRule = core.arg()

        cross_region_copy_rule: list[CrossRegionCopyRule] | core.ArrayOut[
            CrossRegionCopyRule
        ] | None = core.arg(default=None)

        deprecate_rule: ScheduleDeprecateRule | None = core.arg(default=None)

        fast_restore_rule: FastRestoreRule | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        retain_rule: ScheduleRetainRule = core.arg()

        share_rule: ShareRule | None = core.arg(default=None)

        tags_to_add: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        variable_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class EncryptionConfiguration(core.Schema):

    cmk_arn: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        cmk_arn: str | core.StringOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                cmk_arn=cmk_arn,
                encrypted=encrypted,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cmk_arn: str | core.StringOut | None = core.arg(default=None)

        encrypted: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class CrossRegionCopy(core.Schema):

    encryption_configuration: EncryptionConfiguration = core.attr(EncryptionConfiguration)

    retain_rule: CrossRegionCopyRuleRetainRule | None = core.attr(
        CrossRegionCopyRuleRetainRule, default=None
    )

    target: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        encryption_configuration: EncryptionConfiguration,
        target: str | core.StringOut,
        retain_rule: CrossRegionCopyRuleRetainRule | None = None,
    ):
        super().__init__(
            args=CrossRegionCopy.Args(
                encryption_configuration=encryption_configuration,
                target=target,
                retain_rule=retain_rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_configuration: EncryptionConfiguration = core.arg()

        retain_rule: CrossRegionCopyRuleRetainRule | None = core.arg(default=None)

        target: str | core.StringOut = core.arg()


@core.schema
class Action(core.Schema):

    cross_region_copy: list[CrossRegionCopy] | core.ArrayOut[CrossRegionCopy] = core.attr(
        CrossRegionCopy, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cross_region_copy: list[CrossRegionCopy] | core.ArrayOut[CrossRegionCopy],
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Action.Args(
                cross_region_copy=cross_region_copy,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cross_region_copy: list[CrossRegionCopy] | core.ArrayOut[CrossRegionCopy] = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class EventSourceParameters(core.Schema):

    description_regex: str | core.StringOut = core.attr(str)

    event_type: str | core.StringOut = core.attr(str)

    snapshot_owner: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        description_regex: str | core.StringOut,
        event_type: str | core.StringOut,
        snapshot_owner: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=EventSourceParameters.Args(
                description_regex=description_regex,
                event_type=event_type,
                snapshot_owner=snapshot_owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description_regex: str | core.StringOut = core.arg()

        event_type: str | core.StringOut = core.arg()

        snapshot_owner: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class EventSource(core.Schema):

    parameters: EventSourceParameters = core.attr(EventSourceParameters)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        parameters: EventSourceParameters,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=EventSource.Args(
                parameters=parameters,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameters: EventSourceParameters = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class PolicyDetails(core.Schema):

    action: Action | None = core.attr(Action, default=None)

    event_source: EventSource | None = core.attr(EventSource, default=None)

    parameters: PolicyDetailsParameters | None = core.attr(PolicyDetailsParameters, default=None)

    policy_type: str | core.StringOut | None = core.attr(str, default=None)

    resource_locations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    schedule: list[Schedule] | core.ArrayOut[Schedule] | None = core.attr(
        Schedule, default=None, kind=core.Kind.array
    )

    target_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        action: Action | None = None,
        event_source: EventSource | None = None,
        parameters: PolicyDetailsParameters | None = None,
        policy_type: str | core.StringOut | None = None,
        resource_locations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        resource_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        schedule: list[Schedule] | core.ArrayOut[Schedule] | None = None,
        target_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=PolicyDetails.Args(
                action=action,
                event_source=event_source,
                parameters=parameters,
                policy_type=policy_type,
                resource_locations=resource_locations,
                resource_types=resource_types,
                schedule=schedule,
                target_tags=target_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action | None = core.arg(default=None)

        event_source: EventSource | None = core.arg(default=None)

        parameters: PolicyDetailsParameters | None = core.arg(default=None)

        policy_type: str | core.StringOut | None = core.arg(default=None)

        resource_locations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        schedule: list[Schedule] | core.ArrayOut[Schedule] | None = core.arg(default=None)

        target_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_dlm_lifecycle_policy", namespace="dlm")
class LifecyclePolicy(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str)

    execution_role_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy_details: PolicyDetails = core.attr(PolicyDetails)

    state: str | core.StringOut | None = core.attr(str, default=None)

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
        description: str | core.StringOut,
        execution_role_arn: str | core.StringOut,
        policy_details: PolicyDetails,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LifecyclePolicy.Args(
                description=description,
                execution_role_arn=execution_role_arn,
                policy_details=policy_details,
                state=state,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut = core.arg()

        execution_role_arn: str | core.StringOut = core.arg()

        policy_details: PolicyDetails = core.arg()

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
