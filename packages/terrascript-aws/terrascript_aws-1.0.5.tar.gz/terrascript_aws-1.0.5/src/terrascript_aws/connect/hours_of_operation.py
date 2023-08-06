import terrascript.core as core


@core.schema
class EndTime(core.Schema):

    hours: int | core.IntOut = core.attr(int)

    minutes: int | core.IntOut = core.attr(int)

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

    hours: int | core.IntOut = core.attr(int)

    minutes: int | core.IntOut = core.attr(int)

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

    day: str | core.StringOut = core.attr(str)

    end_time: EndTime = core.attr(EndTime)

    start_time: StartTime = core.attr(StartTime)

    def __init__(
        self,
        *,
        day: str | core.StringOut,
        end_time: EndTime,
        start_time: StartTime,
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

        end_time: EndTime = core.arg()

        start_time: StartTime = core.arg()


@core.resource(type="aws_connect_hours_of_operation", namespace="connect")
class HoursOfOperation(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Hours of Operation.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) One or more config blocks which define the configuration information for the hours of ope
    ration: day, start time, and end time . Config blocks are documented below.
    """
    config: list[Config] | core.ArrayOut[Config] = core.attr(Config, kind=core.Kind.array)

    """
    (Optional) Specifies the description of the Hours of Operation.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (**Deprecated**) The Amazon Resource Name (ARN) of the Hours of Operation.
    """
    hours_of_operation_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier for the hours of operation.
    """
    hours_of_operation_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Hours of Operation separ
    ated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the name of the Hours of Operation.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Tags to apply to the Hours of Operation. If configured with a provider [`default_tags` co
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

    """
    (Required) Specifies the time zone of the Hours of Operation.
    """
    time_zone: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        config: list[Config] | core.ArrayOut[Config],
        instance_id: str | core.StringOut,
        name: str | core.StringOut,
        time_zone: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=HoursOfOperation.Args(
                config=config,
                instance_id=instance_id,
                name=name,
                time_zone=time_zone,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        config: list[Config] | core.ArrayOut[Config] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        time_zone: str | core.StringOut = core.arg()
