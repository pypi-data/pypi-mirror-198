import terrascript.core as core


@core.schema
class Thumbnails(core.Schema):

    aspect_ratio: str | core.StringOut | None = core.attr(str, default=None)

    format: str | core.StringOut | None = core.attr(str, default=None)

    interval: str | core.StringOut | None = core.attr(str, default=None)

    max_height: str | core.StringOut | None = core.attr(str, default=None)

    max_width: str | core.StringOut | None = core.attr(str, default=None)

    padding_policy: str | core.StringOut | None = core.attr(str, default=None)

    resolution: str | core.StringOut | None = core.attr(str, default=None)

    sizing_policy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aspect_ratio: str | core.StringOut | None = None,
        format: str | core.StringOut | None = None,
        interval: str | core.StringOut | None = None,
        max_height: str | core.StringOut | None = None,
        max_width: str | core.StringOut | None = None,
        padding_policy: str | core.StringOut | None = None,
        resolution: str | core.StringOut | None = None,
        sizing_policy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Thumbnails.Args(
                aspect_ratio=aspect_ratio,
                format=format,
                interval=interval,
                max_height=max_height,
                max_width=max_width,
                padding_policy=padding_policy,
                resolution=resolution,
                sizing_policy=sizing_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aspect_ratio: str | core.StringOut | None = core.arg(default=None)

        format: str | core.StringOut | None = core.arg(default=None)

        interval: str | core.StringOut | None = core.arg(default=None)

        max_height: str | core.StringOut | None = core.arg(default=None)

        max_width: str | core.StringOut | None = core.arg(default=None)

        padding_policy: str | core.StringOut | None = core.arg(default=None)

        resolution: str | core.StringOut | None = core.arg(default=None)

        sizing_policy: str | core.StringOut | None = core.arg(default=None)


@core.schema
class VideoWatermarks(core.Schema):

    horizontal_align: str | core.StringOut | None = core.attr(str, default=None)

    horizontal_offset: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None)

    max_height: str | core.StringOut | None = core.attr(str, default=None)

    max_width: str | core.StringOut | None = core.attr(str, default=None)

    opacity: str | core.StringOut | None = core.attr(str, default=None)

    sizing_policy: str | core.StringOut | None = core.attr(str, default=None)

    target: str | core.StringOut | None = core.attr(str, default=None)

    vertical_align: str | core.StringOut | None = core.attr(str, default=None)

    vertical_offset: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        horizontal_align: str | core.StringOut | None = None,
        horizontal_offset: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
        max_height: str | core.StringOut | None = None,
        max_width: str | core.StringOut | None = None,
        opacity: str | core.StringOut | None = None,
        sizing_policy: str | core.StringOut | None = None,
        target: str | core.StringOut | None = None,
        vertical_align: str | core.StringOut | None = None,
        vertical_offset: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=VideoWatermarks.Args(
                horizontal_align=horizontal_align,
                horizontal_offset=horizontal_offset,
                id=id,
                max_height=max_height,
                max_width=max_width,
                opacity=opacity,
                sizing_policy=sizing_policy,
                target=target,
                vertical_align=vertical_align,
                vertical_offset=vertical_offset,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        horizontal_align: str | core.StringOut | None = core.arg(default=None)

        horizontal_offset: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        max_height: str | core.StringOut | None = core.arg(default=None)

        max_width: str | core.StringOut | None = core.arg(default=None)

        opacity: str | core.StringOut | None = core.arg(default=None)

        sizing_policy: str | core.StringOut | None = core.arg(default=None)

        target: str | core.StringOut | None = core.arg(default=None)

        vertical_align: str | core.StringOut | None = core.arg(default=None)

        vertical_offset: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Video(core.Schema):

    aspect_ratio: str | core.StringOut | None = core.attr(str, default=None)

    bit_rate: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    codec: str | core.StringOut | None = core.attr(str, default=None)

    display_aspect_ratio: str | core.StringOut | None = core.attr(str, default=None)

    fixed_gop: str | core.StringOut | None = core.attr(str, default=None)

    frame_rate: str | core.StringOut | None = core.attr(str, default=None)

    keyframes_max_dist: str | core.StringOut | None = core.attr(str, default=None)

    max_frame_rate: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    max_height: str | core.StringOut | None = core.attr(str, default=None)

    max_width: str | core.StringOut | None = core.attr(str, default=None)

    padding_policy: str | core.StringOut | None = core.attr(str, default=None)

    resolution: str | core.StringOut | None = core.attr(str, default=None)

    sizing_policy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aspect_ratio: str | core.StringOut | None = None,
        bit_rate: str | core.StringOut | None = None,
        codec: str | core.StringOut | None = None,
        display_aspect_ratio: str | core.StringOut | None = None,
        fixed_gop: str | core.StringOut | None = None,
        frame_rate: str | core.StringOut | None = None,
        keyframes_max_dist: str | core.StringOut | None = None,
        max_frame_rate: str | core.StringOut | None = None,
        max_height: str | core.StringOut | None = None,
        max_width: str | core.StringOut | None = None,
        padding_policy: str | core.StringOut | None = None,
        resolution: str | core.StringOut | None = None,
        sizing_policy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Video.Args(
                aspect_ratio=aspect_ratio,
                bit_rate=bit_rate,
                codec=codec,
                display_aspect_ratio=display_aspect_ratio,
                fixed_gop=fixed_gop,
                frame_rate=frame_rate,
                keyframes_max_dist=keyframes_max_dist,
                max_frame_rate=max_frame_rate,
                max_height=max_height,
                max_width=max_width,
                padding_policy=padding_policy,
                resolution=resolution,
                sizing_policy=sizing_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aspect_ratio: str | core.StringOut | None = core.arg(default=None)

        bit_rate: str | core.StringOut | None = core.arg(default=None)

        codec: str | core.StringOut | None = core.arg(default=None)

        display_aspect_ratio: str | core.StringOut | None = core.arg(default=None)

        fixed_gop: str | core.StringOut | None = core.arg(default=None)

        frame_rate: str | core.StringOut | None = core.arg(default=None)

        keyframes_max_dist: str | core.StringOut | None = core.arg(default=None)

        max_frame_rate: str | core.StringOut | None = core.arg(default=None)

        max_height: str | core.StringOut | None = core.arg(default=None)

        max_width: str | core.StringOut | None = core.arg(default=None)

        padding_policy: str | core.StringOut | None = core.arg(default=None)

        resolution: str | core.StringOut | None = core.arg(default=None)

        sizing_policy: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Audio(core.Schema):

    audio_packing_mode: str | core.StringOut | None = core.attr(str, default=None)

    bit_rate: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    channels: str | core.StringOut | None = core.attr(str, default=None)

    codec: str | core.StringOut | None = core.attr(str, default=None)

    sample_rate: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        audio_packing_mode: str | core.StringOut | None = None,
        bit_rate: str | core.StringOut | None = None,
        channels: str | core.StringOut | None = None,
        codec: str | core.StringOut | None = None,
        sample_rate: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Audio.Args(
                audio_packing_mode=audio_packing_mode,
                bit_rate=bit_rate,
                channels=channels,
                codec=codec,
                sample_rate=sample_rate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audio_packing_mode: str | core.StringOut | None = core.arg(default=None)

        bit_rate: str | core.StringOut | None = core.arg(default=None)

        channels: str | core.StringOut | None = core.arg(default=None)

        codec: str | core.StringOut | None = core.arg(default=None)

        sample_rate: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AudioCodecOptions(core.Schema):

    bit_depth: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    bit_order: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    profile: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    signed: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        bit_depth: str | core.StringOut | None = None,
        bit_order: str | core.StringOut | None = None,
        profile: str | core.StringOut | None = None,
        signed: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AudioCodecOptions.Args(
                bit_depth=bit_depth,
                bit_order=bit_order,
                profile=profile,
                signed=signed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bit_depth: str | core.StringOut | None = core.arg(default=None)

        bit_order: str | core.StringOut | None = core.arg(default=None)

        profile: str | core.StringOut | None = core.arg(default=None)

        signed: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_elastictranscoder_preset", namespace="elastictranscoder")
class Preset(core.Resource):
    """
    Amazon Resource Name (ARN) of the Elastic Transcoder Preset.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) Audio parameters object (documented below).
    """
    audio: Audio | None = core.attr(Audio, default=None)

    """
    (Optional, Forces new resource) Codec options for the audio parameters (documented below)
    """
    audio_codec_options: AudioCodecOptions | None = core.attr(
        AudioCodecOptions, default=None, computed=True
    )

    """
    (Required, Forces new resource) The container type for the output file. Valid values are `flac`, `fl
    v`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
    """
    container: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) A description of the preset (maximum 255 characters)
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters l
    ong. You can specify settings for up to four watermarks.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The name of the preset. (maximum 40 characters)
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Thumbnail parameters object (documented below)
    """
    thumbnails: Thumbnails | None = core.attr(Thumbnails, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Video parameters object (documented below)
    """
    video: Video | None = core.attr(Video, default=None)

    video_codec_options: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional, Forces new resource) Watermark parameters for the video parameters (documented below)
    """
    video_watermarks: list[VideoWatermarks] | core.ArrayOut[VideoWatermarks] | None = core.attr(
        VideoWatermarks, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        container: str | core.StringOut,
        audio: Audio | None = None,
        audio_codec_options: AudioCodecOptions | None = None,
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        thumbnails: Thumbnails | None = None,
        type: str | core.StringOut | None = None,
        video: Video | None = None,
        video_codec_options: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        video_watermarks: list[VideoWatermarks] | core.ArrayOut[VideoWatermarks] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Preset.Args(
                container=container,
                audio=audio,
                audio_codec_options=audio_codec_options,
                description=description,
                name=name,
                thumbnails=thumbnails,
                type=type,
                video=video,
                video_codec_options=video_codec_options,
                video_watermarks=video_watermarks,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audio: Audio | None = core.arg(default=None)

        audio_codec_options: AudioCodecOptions | None = core.arg(default=None)

        container: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        thumbnails: Thumbnails | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        video: Video | None = core.arg(default=None)

        video_codec_options: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        video_watermarks: list[VideoWatermarks] | core.ArrayOut[VideoWatermarks] | None = core.arg(
            default=None
        )
