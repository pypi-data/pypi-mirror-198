import terrascript.core as core


@core.data(type="aws_connect_instance", namespace="connect")
class DsInstance(core.Data):
    """
    The Amazon Resource Name (ARN) of the instance.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_resolve_best_voices_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies Whether contact flow logs are enabled.
    """
    contact_flow_logs_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies Whether contact lens is enabled.
    """
    contact_lens_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies When the instance was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies Whether early media for outbound calls is enabled .
    """
    early_media_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies The identity management type attached to the instance.
    """
    identity_management_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies Whether inbound calls are enabled.
    """
    inbound_calls_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Returns information on a specific connect instance by alias
    """
    instance_alias: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Returns information on a specific connect instance by id
    """
    instance_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Specifies Whether outbound calls are enabled.
    """
    outbound_calls_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The service role of the instance.
    """
    service_role: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies The state of the instance.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        instance_alias: str | core.StringOut | None = None,
        instance_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInstance.Args(
                instance_alias=instance_alias,
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_alias: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)
