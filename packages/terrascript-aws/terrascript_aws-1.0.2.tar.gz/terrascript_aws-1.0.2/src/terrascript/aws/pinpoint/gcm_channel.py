import terrascript.core as core


@core.resource(type="aws_pinpoint_gcm_channel", namespace="aws_pinpoint")
class GcmChannel(core.Resource):
    """
    (Required) Platform credential API key from Google.
    """

    api_key: str | core.StringOut = core.attr(str)

    """
    (Required) The application ID.
    """
    application_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether the channel is enabled or disabled. Defaults to `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        api_key: str | core.StringOut,
        application_id: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GcmChannel.Args(
                api_key=api_key,
                application_id=application_id,
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key: str | core.StringOut = core.arg()

        application_id: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)
