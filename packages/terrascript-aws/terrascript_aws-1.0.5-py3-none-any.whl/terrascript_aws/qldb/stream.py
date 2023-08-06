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


@core.resource(type="aws_qldb_stream", namespace="qldb")
class Stream(core.Resource):
    """
    The ARN of the QLDB Stream.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The exclusive date and time that specifies when the stream ends. If you don't define this
    parameter, the stream runs indefinitely until you cancel it. It must be in ISO 8601 date and time f
    ormat and in Universal Coordinated Time (UTC). For example: `"2019-06-13T21:36:34Z"`.
    """
    exclusive_end_time: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the QLDB Stream.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The inclusive start date and time from which to start streaming journal data. This parame
    ter must be in ISO 8601 date and time format and in Universal Coordinated Time (UTC). For example: `
    "2019-06-13T21:36:34Z"`.  This cannot be in the future and must be before `exclusive_end_time`.  If
    you provide a value that is before the ledger's `CreationDateTime`, QLDB effectively defaults it to
    the ledger's `CreationDateTime`.
    """
    inclusive_start_time: str | core.StringOut = core.attr(str)

    """
    (Required) The configuration settings of the Kinesis Data Streams destination for your stream reques
    t. Documented below.
    """
    kinesis_configuration: KinesisConfiguration = core.attr(KinesisConfiguration)

    """
    (Required) The name of the QLDB ledger.
    """
    ledger_name: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal
    stream to write data records to a Kinesis Data Streams resource.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The name that you want to assign to the QLDB journal stream. User-defined names can help
    identify and indicate the purpose of a stream.  Your stream name must be unique among other active s
    treams for a given ledger. Stream names have the same naming constraints as ledger names, as defined
    in the [Amazon QLDB Developer Guide](https://docs.aws.amazon.com/qldb/latest/developerguide/limits.
    html#limits.naming).
    """
    stream_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
