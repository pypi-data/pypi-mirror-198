import terrascript.core as core


@core.resource(type="aws_kinesis_video_stream", namespace="kinesis_video")
class Stream(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the Stream (same as `id`)
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A time stamp that indicates when the stream was created.
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    data_retention_in_hours: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The name of the device that is writing to the stream. **In the current implementation, Ki
    nesis Video Streams does not use this name.**
    """
    device_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique Stream id
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video Stream
    s to use to encrypt stream data. If no key ID is specified, the default, Kinesis Video-managed key (
    aws/kinesisvideo`) is used.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The media type of the stream. Consumers of the stream can use this information when proce
    ssing the stream. For more information about media types, see [Media Types][2]. If you choose to spe
    cify the MediaType, see [Naming Requirements][3] for guidelines.
    """
    media_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A name to identify the stream. This is unique to the
    """
    name: str | core.StringOut = core.attr(str)

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

    """
    The version of the stream.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        data_retention_in_hours: int | core.IntOut | None = None,
        device_name: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        media_type: str | core.StringOut | None = None,
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
                data_retention_in_hours=data_retention_in_hours,
                device_name=device_name,
                kms_key_id=kms_key_id,
                media_type=media_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        data_retention_in_hours: int | core.IntOut | None = core.arg(default=None)

        device_name: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        media_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
