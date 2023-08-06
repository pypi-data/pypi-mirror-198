import terrascript.core as core


@core.schema
class EndTime(core.Schema):

    hours: int | core.IntOut = core.attr(int, computed=True)

    minutes: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        hours: int | core.IntOut,
        minutes: int | core.IntOut,
    ):
        super().__init__(
            args=EndTime.Args(
                hours=hours,
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hours: int | core.IntOut = core.arg()

        minutes: int | core.IntOut = core.arg()


@core.schema
class StartTime(core.Schema):

    hours: int | core.IntOut = core.attr(int, computed=True)

    minutes: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        hours: int | core.IntOut,
        minutes: int | core.IntOut,
    ):
        super().__init__(
            args=StartTime.Args(
                hours=hours,
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hours: int | core.IntOut = core.arg()

        minutes: int | core.IntOut = core.arg()


@core.schema
class Config(core.Schema):

    day: str | core.StringOut = core.attr(str, computed=True)

    end_time: list[EndTime] | core.ArrayOut[EndTime] = core.attr(
        EndTime, computed=True, kind=core.Kind.array
    )

    start_time: list[StartTime] | core.ArrayOut[StartTime] = core.attr(
        StartTime, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        day: str | core.StringOut,
        end_time: list[EndTime] | core.ArrayOut[EndTime],
        start_time: list[StartTime] | core.ArrayOut[StartTime],
    ):
        super().__init__(
            args=Config.Args(
                day=day,
                end_time=end_time,
                start_time=start_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        day: str | core.StringOut = core.arg()

        end_time: list[EndTime] | core.ArrayOut[EndTime] = core.arg()

        start_time: list[StartTime] | core.ArrayOut[StartTime] = core.arg()


@core.data(type="aws_connect_hours_of_operation", namespace="connect")
class DsHoursOfOperation(core.Data):
    """
    The Amazon Resource Name (ARN) of the Hours of Operation.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies configuration information for the hours of operation: day, start time, and end time . Conf
    ig blocks are documented below. Config blocks are documented below.
    """
    config: list[Config] | core.ArrayOut[Config] = core.attr(
        Config, computed=True, kind=core.Kind.array
    )

    """
    Specifies the description of the Hours of Operation.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (**Deprecated**) The Amazon Resource Name (ARN) of the Hours of Operation.
    """
    hours_of_operation_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific Hours of Operation by hours of operation id
    """
    hours_of_operation_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Returns information on a specific Hours of Operation by name
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A map of tags to assign to the Hours of Operation.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Specifies the time zone of the Hours of Operation.
    """
    time_zone: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        hours_of_operation_id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsHoursOfOperation.Args(
                instance_id=instance_id,
                hours_of_operation_id=hours_of_operation_id,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hours_of_operation_id: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
