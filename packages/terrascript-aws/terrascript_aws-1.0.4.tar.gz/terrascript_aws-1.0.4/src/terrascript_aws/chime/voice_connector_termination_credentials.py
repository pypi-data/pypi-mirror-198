import terrascript.core as core


@core.schema
class Credentials(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=Credentials.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.resource(type="aws_chime_voice_connector_termination_credentials", namespace="chime")
class VoiceConnectorTerminationCredentials(core.Resource):
    """
    (Required) List of termination SIP credentials.
    """

    credentials: list[Credentials] | core.ArrayOut[Credentials] = core.attr(
        Credentials, kind=core.Kind.array
    )

    """
    Amazon Chime Voice Connector ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon Chime Voice Connector ID.
    """
    voice_connector_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        credentials: list[Credentials] | core.ArrayOut[Credentials],
        voice_connector_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorTerminationCredentials.Args(
                credentials=credentials,
                voice_connector_id=voice_connector_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        credentials: list[Credentials] | core.ArrayOut[Credentials] = core.arg()

        voice_connector_id: str | core.StringOut = core.arg()
