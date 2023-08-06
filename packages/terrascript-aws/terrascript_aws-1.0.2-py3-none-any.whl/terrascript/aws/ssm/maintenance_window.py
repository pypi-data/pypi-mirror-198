import terrascript.core as core


@core.resource(type="aws_ssm_maintenance_window", namespace="aws_ssm")
class MaintenanceWindow(core.Resource):

    allow_unassociated_targets: bool | core.BoolOut | None = core.attr(bool, default=None)

    cutoff: int | core.IntOut = core.attr(int)

    description: str | core.StringOut | None = core.attr(str, default=None)

    duration: int | core.IntOut = core.attr(int)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    end_date: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    schedule: str | core.StringOut = core.attr(str)

    schedule_offset: int | core.IntOut | None = core.attr(int, default=None)

    schedule_timezone: str | core.StringOut | None = core.attr(str, default=None)

    start_date: str | core.StringOut | None = core.attr(str, default=None)

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
