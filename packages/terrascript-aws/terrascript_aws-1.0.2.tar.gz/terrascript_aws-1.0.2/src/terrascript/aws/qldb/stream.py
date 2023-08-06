import terrascript.core as core


@core.schema
class KinesisConfiguration(core.Schema):

    aggregation_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    stream_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        stream_arn: str | core.StringOut,
        aggregation_enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=KinesisConfiguration.Args(
                stream_arn=stream_arn,
                aggregation_enabled=aggregation_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_enabled: bool | core.BoolOut | None = core.arg(default=None)

        stream_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_qldb_stream", namespace="aws_qldb")
class Stream(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    exclusive_end_time: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    inclusive_start_time: str | core.StringOut = core.attr(str)

    kinesis_configuration: KinesisConfiguration = core.attr(KinesisConfiguration)

    ledger_name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    stream_name: str | core.StringOut = core.attr(str)

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
        inclusive_start_time: str | core.StringOut,
        kinesis_configuration: KinesisConfiguration,
        ledger_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        stream_name: str | core.StringOut,
        exclusive_end_time: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stream.Args(
                inclusive_start_time=inclusive_start_time,
                kinesis_configuration=kinesis_configuration,
                ledger_name=ledger_name,
                role_arn=role_arn,
                stream_name=stream_name,
                exclusive_end_time=exclusive_end_time,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        exclusive_end_time: str | core.StringOut | None = core.arg(default=None)

        inclusive_start_time: str | core.StringOut = core.arg()

        kinesis_configuration: KinesisConfiguration = core.arg()

        ledger_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        stream_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
