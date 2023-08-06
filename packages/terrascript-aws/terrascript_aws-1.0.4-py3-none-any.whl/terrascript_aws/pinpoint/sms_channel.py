import terrascript.core as core


@core.resource(type="aws_pinpoint_sms_channel", namespace="pinpoint")
class SmsChannel(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    promotional_messages_per_second: int | core.IntOut = core.attr(int, computed=True)

    sender_id: str | core.StringOut | None = core.attr(str, default=None)

    short_code: str | core.StringOut | None = core.attr(str, default=None)

    transactional_messages_per_second: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        sender_id: str | core.StringOut | None = None,
        short_code: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SmsChannel.Args(
                application_id=application_id,
                enabled=enabled,
                sender_id=sender_id,
                short_code=short_code,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        sender_id: str | core.StringOut | None = core.arg(default=None)

        short_code: str | core.StringOut | None = core.arg(default=None)
