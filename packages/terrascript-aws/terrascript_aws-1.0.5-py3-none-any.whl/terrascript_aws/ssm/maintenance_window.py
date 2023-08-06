import terrascript.core as core


@core.resource(type="aws_ssm_maintenance_window", namespace="ssm")
class MaintenanceWindow(core.Resource):
    """
    (Optional) Whether targets must be registered with the Maintenance Window before tasks can be define
    d for those targets.
    """

    allow_unassociated_targets: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The number of hours before the end of the Maintenance Window that Systems Manager stops s
    cheduling new tasks for execution.
    """
    cutoff: int | core.IntOut = core.attr(int)

    """
    (Optional) A description for the maintenance window.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The duration of the Maintenance Window in hours.
    """
    duration: int | core.IntOut = core.attr(int)

    """
    (Optional) Whether the maintenance window is enabled. Default: `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format
    .html) when to no longer run the maintenance window.
    """
    end_date: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the maintenance window.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the maintenance window.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.co
    m/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.
    """
    schedule: str | core.StringOut = core.attr(str)

    """
    (Optional) The number of days to wait after the date and time specified by a CRON expression before
    running the maintenance window.
    """
    schedule_offset: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Timezone for schedule in [Internet Assigned Numbers Authority (IANA) Time Zone Database f
    ormat](https://www.iana.org/time-zones). For example: `America/Los_Angeles`, `etc/UTC`, or `Asia/Seo
    ul`.
    """
    schedule_timezone: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format
    .html) when to begin the maintenance window.
    """
    start_date: str | core.StringOut | None = core.attr(str, default=None)

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
        cutoff: int | core.IntOut,
        duration: int | core.IntOut,
        name: str | core.StringOut,
        schedule: str | core.StringOut,
        allow_unassociated_targets: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        end_date: str | core.StringOut | None = None,
        schedule_offset: int | core.IntOut | None = None,
        schedule_timezone: str | core.StringOut | None = None,
        start_date: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MaintenanceWindow.Args(
                cutoff=cutoff,
                duration=duration,
                name=name,
                schedule=schedule,
                allow_unassociated_targets=allow_unassociated_targets,
                description=description,
                enabled=enabled,
                end_date=end_date,
                schedule_offset=schedule_offset,
                schedule_timezone=schedule_timezone,
                start_date=start_date,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_unassociated_targets: bool | core.BoolOut | None = core.arg(default=None)

        cutoff: int | core.IntOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        duration: int | core.IntOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        end_date: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        schedule: str | core.StringOut = core.arg()

        schedule_offset: int | core.IntOut | None = core.arg(default=None)

        schedule_timezone: str | core.StringOut | None = core.arg(default=None)

        start_date: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
