import terrascript.core as core


@core.schema
class Schedule(core.Schema):

    schedule_expression: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        schedule_expression: str | core.StringOut,
    ):
        super().__init__(
            args=Schedule.Args(
                schedule_expression=schedule_expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        schedule_expression: str | core.StringOut = core.arg()


@core.schema
class Includes(core.Schema):

    filter_type: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        filter_type: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Includes.Args(
                filter_type=filter_type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter_type: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Excludes(core.Schema):

    filter_type: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        filter_type: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Excludes.Args(
                filter_type=filter_type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter_type: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Options(core.Schema):

    atime: str | core.StringOut | None = core.attr(str, default=None)

    bytes_per_second: int | core.IntOut | None = core.attr(int, default=None)

    gid: str | core.StringOut | None = core.attr(str, default=None)

    log_level: str | core.StringOut | None = core.attr(str, default=None)

    mtime: str | core.StringOut | None = core.attr(str, default=None)

    overwrite_mode: str | core.StringOut | None = core.attr(str, default=None)

    posix_permissions: str | core.StringOut | None = core.attr(str, default=None)

    preserve_deleted_files: str | core.StringOut | None = core.attr(str, default=None)

    preserve_devices: str | core.StringOut | None = core.attr(str, default=None)

    task_queueing: str | core.StringOut | None = core.attr(str, default=None)

    transfer_mode: str | core.StringOut | None = core.attr(str, default=None)

    uid: str | core.StringOut | None = core.attr(str, default=None)

    verify_mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        atime: str | core.StringOut | None = None,
        bytes_per_second: int | core.IntOut | None = None,
        gid: str | core.StringOut | None = None,
        log_level: str | core.StringOut | None = None,
        mtime: str | core.StringOut | None = None,
        overwrite_mode: str | core.StringOut | None = None,
        posix_permissions: str | core.StringOut | None = None,
        preserve_deleted_files: str | core.StringOut | None = None,
        preserve_devices: str | core.StringOut | None = None,
        task_queueing: str | core.StringOut | None = None,
        transfer_mode: str | core.StringOut | None = None,
        uid: str | core.StringOut | None = None,
        verify_mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Options.Args(
                atime=atime,
                bytes_per_second=bytes_per_second,
                gid=gid,
                log_level=log_level,
                mtime=mtime,
                overwrite_mode=overwrite_mode,
                posix_permissions=posix_permissions,
                preserve_deleted_files=preserve_deleted_files,
                preserve_devices=preserve_devices,
                task_queueing=task_queueing,
                transfer_mode=transfer_mode,
                uid=uid,
                verify_mode=verify_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        atime: str | core.StringOut | None = core.arg(default=None)

        bytes_per_second: int | core.IntOut | None = core.arg(default=None)

        gid: str | core.StringOut | None = core.arg(default=None)

        log_level: str | core.StringOut | None = core.arg(default=None)

        mtime: str | core.StringOut | None = core.arg(default=None)

        overwrite_mode: str | core.StringOut | None = core.arg(default=None)

        posix_permissions: str | core.StringOut | None = core.arg(default=None)

        preserve_deleted_files: str | core.StringOut | None = core.arg(default=None)

        preserve_devices: str | core.StringOut | None = core.arg(default=None)

        task_queueing: str | core.StringOut | None = core.arg(default=None)

        transfer_mode: str | core.StringOut | None = core.arg(default=None)

        uid: str | core.StringOut | None = core.arg(default=None)

        verify_mode: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_datasync_task", namespace="aws_datasync")
class Task(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cloudwatch_log_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    destination_location_arn: str | core.StringOut = core.attr(str)

    excludes: Excludes | None = core.attr(Excludes, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    includes: Includes | None = core.attr(Includes, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    options: Options | None = core.attr(Options, default=None)

    schedule: Schedule | None = core.attr(Schedule, default=None)

    source_location_arn: str | core.StringOut = core.attr(str)

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
        destination_location_arn: str | core.StringOut,
        source_location_arn: str | core.StringOut,
        cloudwatch_log_group_arn: str | core.StringOut | None = None,
        excludes: Excludes | None = None,
        includes: Includes | None = None,
        name: str | core.StringOut | None = None,
        options: Options | None = None,
        schedule: Schedule | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Task.Args(
                destination_location_arn=destination_location_arn,
                source_location_arn=source_location_arn,
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                excludes=excludes,
                includes=includes,
                name=name,
                options=options,
                schedule=schedule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_log_group_arn: str | core.StringOut | None = core.arg(default=None)

        destination_location_arn: str | core.StringOut = core.arg()

        excludes: Excludes | None = core.arg(default=None)

        includes: Includes | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        options: Options | None = core.arg(default=None)

        schedule: Schedule | None = core.arg(default=None)

        source_location_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
