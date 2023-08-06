import terrascript.core as core


@core.resource(type="aws_chime_voice_connector_logging", namespace="aws_chime")
class VoiceConnectorLogging(core.Resource):

    enable_media_metric_logs: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_sip_logs: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    voice_connector_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        voice_connector_id: str | core.StringOut,
        enable_media_metric_logs: bool | core.BoolOut | None = None,
        enable_sip_logs: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorLogging.Args(
                voice_connector_id=voice_connector_id,
                enable_media_metric_logs=enable_media_metric_logs,
                enable_sip_logs=enable_sip_logs,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enable_media_metric_logs: bool | core.BoolOut | None = core.arg(default=None)

        enable_sip_logs: bool | core.BoolOut | None = core.arg(default=None)

        voice_connector_id: str | core.StringOut = core.arg()
