import terrascript.core as core


@core.resource(type="aws_chime_voice_connector_streaming", namespace="chime")
class VoiceConnectorStreaming(core.Resource):

    data_retention: int | core.IntOut = core.attr(int)

    """
    (Optional) When true, media streaming to Amazon Kinesis is turned off. Default: `false`
    """
    disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Amazon Chime Voice Connector ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The streaming notification targets. Valid Values: `EventBridge | SNS | SQS`
    """
    streaming_notification_targets: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The Amazon Chime Voice Connector ID.
    """
    voice_connector_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        data_retention: int | core.IntOut,
        voice_connector_id: str | core.StringOut,
        disabled: bool | core.BoolOut | None = None,
        streaming_notification_targets: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorStreaming.Args(
                data_retention=data_retention,
                voice_connector_id=voice_connector_id,
                disabled=disabled,
                streaming_notification_targets=streaming_notification_targets,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        data_retention: int | core.IntOut = core.arg()

        disabled: bool | core.BoolOut | None = core.arg(default=None)

        streaming_notification_targets: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        voice_connector_id: str | core.StringOut = core.arg()
