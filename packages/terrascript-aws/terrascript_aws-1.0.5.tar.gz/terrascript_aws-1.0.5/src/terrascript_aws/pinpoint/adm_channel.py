import terrascript.core as core


@core.resource(type="aws_pinpoint_adm_channel", namespace="pinpoint")
class AdmChannel(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AdmChannel.Args(
                application_id=application_id,
                client_id=client_id,
                client_secret=client_secret,
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut | None = core.arg(default=None)
