import terrascript.core as core


@core.schema
class Route(core.Schema):

    host: str | core.StringOut = core.attr(str)

    port: int | core.IntOut | None = core.attr(int, default=None)

    priority: int | core.IntOut = core.attr(int)

    protocol: str | core.StringOut = core.attr(str)

    weight: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        host: str | core.StringOut,
        priority: int | core.IntOut,
        protocol: str | core.StringOut,
        weight: int | core.IntOut,
        port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Route.Args(
                host=host,
                priority=priority,
                protocol=protocol,
                weight=weight,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: str | core.StringOut = core.arg()

        port: int | core.IntOut | None = core.arg(default=None)

        priority: int | core.IntOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        weight: int | core.IntOut = core.arg()


@core.resource(type="aws_chime_voice_connector_origination", namespace="chime")
class VoiceConnectorOrigination(core.Resource):
    """
    (Optional) When origination settings are disabled, inbound calls are not enabled for your Amazon Chi
    me Voice Connector.
    """

    disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Amazon Chime Voice Connector ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Set of call distribution properties defined for your SIP hosts. See [route](#route) below
    for more details. Minimum of 1. Maximum of 20.
    """
    route: list[Route] | core.ArrayOut[Route] = core.attr(Route, kind=core.Kind.array)

    """
    (Required) The Amazon Chime Voice Connector ID.
    """
    voice_connector_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        route: list[Route] | core.ArrayOut[Route],
        voice_connector_id: str | core.StringOut,
        disabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorOrigination.Args(
                route=route,
                voice_connector_id=voice_connector_id,
                disabled=disabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disabled: bool | core.BoolOut | None = core.arg(default=None)

        route: list[Route] | core.ArrayOut[Route] = core.arg()

        voice_connector_id: str | core.StringOut = core.arg()
