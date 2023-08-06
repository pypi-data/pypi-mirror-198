import terrascript.core as core


@core.resource(type="aws_pinpoint_apns_voip_sandbox_channel", namespace="aws_pinpoint")
class ApnsVoipSandboxChannel(core.Resource):
    """
    (Required) The application ID.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID assigned to your iOS app. To find this value, choose Certificates, IDs & Profiles,
    choose App IDs in the Identifiers section, and choose your app.
    """
    bundle_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The pem encoded TLS Certificate from Apple.
    """
    certificate: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The default authentication method used for APNs.
    """
    default_authentication_method: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether the channel is enabled or disabled. Defaults to `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Certificate Private Key file (ie. `.key` file).
    """
    private_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID assigned to your Apple developer account team. This value is provided on the Membe
    rship page.
    """
    team_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The `.p8` file that you download from your Apple developer account when you create an aut
    hentication key.
    """
    token_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID assigned to your signing key. To find this value, choose Certificates, IDs & Profi
    les, and choose your key in the Keys section.
    """
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
            args=ApnsVoipSandboxChannel.Args(
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
