import terrascript.core as core


@core.resource(type="aws_pinpoint_apns_channel", namespace="pinpoint")
class ApnsChannel(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    bundle_id: str | core.StringOut | None = core.attr(str, default=None)

    certificate: str | core.StringOut | None = core.attr(str, default=None)

    default_authentication_method: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    private_key: str | core.StringOut | None = core.attr(str, default=None)

    team_id: str | core.StringOut | None = core.attr(str, default=None)

    token_key: str | core.StringOut | None = core.attr(str, default=None)

    token_key_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        bundle_id: str | core.StringOut | None = None,
        certificate: str | core.StringOut | None = None,
        default_authentication_method: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        private_key: str | core.StringOut | None = None,
        team_id: str | core.StringOut | None = None,
        token_key: str | core.StringOut | None = None,
        token_key_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApnsChannel.Args(
                application_id=application_id,
                bundle_id=bundle_id,
                certificate=certificate,
                default_authentication_method=default_authentication_method,
                enabled=enabled,
                private_key=private_key,
                team_id=team_id,
                token_key=token_key,
                token_key_id=token_key_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        bundle_id: str | core.StringOut | None = core.arg(default=None)

        certificate: str | core.StringOut | None = core.arg(default=None)

        default_authentication_method: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        private_key: str | core.StringOut | None = core.arg(default=None)

        team_id: str | core.StringOut | None = core.arg(default=None)

        token_key: str | core.StringOut | None = core.arg(default=None)

        token_key_id: str | core.StringOut | None = core.arg(default=None)
