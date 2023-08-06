import terrascript.core as core


@core.schema
class Connector(core.Schema):

    priority: int | core.IntOut = core.attr(int)

    voice_connector_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        priority: int | core.IntOut,
        voice_connector_id: str | core.StringOut,
    ):
        super().__init__(
            args=Connector.Args(
                priority=priority,
                voice_connector_id=voice_connector_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: int | core.IntOut = core.arg()

        voice_connector_id: str | core.StringOut = core.arg()


@core.resource(type="aws_chime_voice_connector_group", namespace="chime")
class VoiceConnectorGroup(core.Resource):
    """
    (Optional) The Amazon Chime Voice Connectors to route inbound calls to.
    """

    connector: list[Connector] | core.ArrayOut[Connector] | None = core.attr(
        Connector, default=None, kind=core.Kind.array
    )

    """
    Amazon Chime Voice Connector group ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Amazon Chime Voice Connector group.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        connector: list[Connector] | core.ArrayOut[Connector] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorGroup.Args(
                name=name,
                connector=connector,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connector: list[Connector] | core.ArrayOut[Connector] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
