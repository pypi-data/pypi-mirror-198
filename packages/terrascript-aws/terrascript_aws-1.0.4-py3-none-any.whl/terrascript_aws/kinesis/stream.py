import terrascript.core as core


@core.schema
class StreamModeDetails(core.Schema):

    stream_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        stream_mode: str | core.StringOut,
    ):
        super().__init__(
            args=StreamModeDetails.Args(
                stream_mode=stream_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stream_mode: str | core.StringOut = core.arg()


@core.resource(type="aws_kinesis_stream", namespace="kinesis")
class Stream(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the Stream (same as `id`)
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default v
    alue is `NONE`.
    """
    encryption_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A boolean that indicates all registered consumers should be deregistered from the stream
    so that the stream can be destroyed without error. The default value is `false`.
    """
    enforce_consumer_deletion: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The unique Stream id
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The GUID for the customer-managed KMS key to use for encryption. You can also use a Kines
    is-owned master key by specifying the alias `alias/aws/kinesis`.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A name to identify the stream. This is unique to the AWS account and region the Stream is
    created in.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Length of time data records are accessible after they are added to the stream. The maximu
    m value of a stream's retention period is 8760 hours. Minimum value is 24. Default is 24.
    """
    retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    The count of Shards for this Stream
    """
    shard_count: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monito
    ring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should pr
    ovide an explicit list of metrics you wish to enable.
    """
    shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Indicates the [capacity mode](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-siz
    e-a-stream.html) of the data stream. Detailed below.
    """
    stream_mode_details: StreamModeDetails | None = core.attr(
        StreamModeDetails, default=None, computed=True
    )

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
        name: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        encryption_type: str | core.StringOut | None = None,
        enforce_consumer_deletion: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        retention_period: int | core.IntOut | None = None,
        shard_count: int | core.IntOut | None = None,
        shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] | None = None,
        stream_mode_details: StreamModeDetails | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stream.Args(
                name=name,
                arn=arn,
                encryption_type=encryption_type,
                enforce_consumer_deletion=enforce_consumer_deletion,
                kms_key_id=kms_key_id,
                retention_period=retention_period,
                shard_count=shard_count,
                shard_level_metrics=shard_level_metrics,
                stream_mode_details=stream_mode_details,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: str | core.StringOut | None = core.arg(default=None)

        encryption_type: str | core.StringOut | None = core.arg(default=None)

        enforce_consumer_deletion: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        retention_period: int | core.IntOut | None = core.arg(default=None)

        shard_count: int | core.IntOut | None = core.arg(default=None)

        shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        stream_mode_details: StreamModeDetails | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
