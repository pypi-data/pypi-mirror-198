import terrascript.core as core


@core.resource(type="aws_chime_voice_connector", namespace="chime")
class VoiceConnector(core.Resource):
    """
    (Optional) The AWS Region in which the Amazon Chime Voice Connector is created. Default value: `us-e
    ast-1`
    """

    aws_region: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Amazon Chime Voice Connector.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The outbound host name for the Amazon Chime Voice Connector.
    """
    outbound_host_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) When enabled, requires encryption for the Amazon Chime Voice Connector.
    """
    require_encryption: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        require_encryption: bool | core.BoolOut,
        aws_region: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnector.Args(
                name=name,
                require_encryption=require_encryption,
                aws_region=aws_region,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_region: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        require_encryption: bool | core.BoolOut = core.arg()
