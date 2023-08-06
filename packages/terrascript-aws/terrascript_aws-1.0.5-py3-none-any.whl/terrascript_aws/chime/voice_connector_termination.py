import terrascript.core as core


@core.resource(type="aws_chime_voice_connector_termination", namespace="chime")
class VoiceConnectorTermination(core.Resource):
    """
    (Required) The countries to which calls are allowed, in ISO 3166-1 alpha-2 format.
    """

    calling_regions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) The IP addresses allowed to make calls, in CIDR format.
    """
    cidr_allow_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) The limit on calls per second. Max value based on account service quota. Default value of
    1`.
    """
    cps_limit: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The default caller ID phone number.
    """
    default_phone_number: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) When termination settings are disabled, outbound calls can not be made.
    """
    disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Amazon Chime Voice Connector ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Chime Voice Connector ID.
    """
    voice_connector_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        calling_regions: list[str] | core.ArrayOut[core.StringOut],
        cidr_allow_list: list[str] | core.ArrayOut[core.StringOut],
        voice_connector_id: str | core.StringOut,
        cps_limit: int | core.IntOut | None = None,
        default_phone_number: str | core.StringOut | None = None,
        disabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorTermination.Args(
                calling_regions=calling_regions,
                cidr_allow_list=cidr_allow_list,
                voice_connector_id=voice_connector_id,
                cps_limit=cps_limit,
                default_phone_number=default_phone_number,
                disabled=disabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        calling_regions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        cidr_allow_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        cps_limit: int | core.IntOut | None = core.arg(default=None)

        default_phone_number: str | core.StringOut | None = core.arg(default=None)

        disabled: bool | core.BoolOut | None = core.arg(default=None)

        voice_connector_id: str | core.StringOut = core.arg()
