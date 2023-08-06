import terrascript.core as core


@core.resource(type="aws_connect_instance", namespace="connect")
class Instance(core.Resource):
    """
    Amazon Resource Name (ARN) of the instance.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether auto resolve best voices is enabled. Defaults to `true`.
    """
    auto_resolve_best_voices_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether contact flow logs are enabled. Defaults to `false`.
    """
    contact_flow_logs_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether contact lens is enabled. Defaults to `true`.
    """
    contact_lens_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Specifies when the instance was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The identifier for the directory if identity_management_type is `EXISTING_DIRECTORY`.
    """
    directory_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether early media for outbound calls is enabled . Defaults to `true` if outbo
    und calls is enabled.
    """
    early_media_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The identifier of the instance.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identity management type attached to the instance. Allowed Values are: `SAM
    L`, `CONNECT_MANAGED`, `EXISTING_DIRECTORY`.
    """
    identity_management_type: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies whether inbound calls are enabled.
    """
    inbound_calls_enabled: bool | core.BoolOut = core.attr(bool)

    """
    (Optional) Specifies the name of the instance. Required if `directory_id` not specified.
    """
    instance_alias: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Specifies whether outbound calls are enabled.
    """
    outbound_calls_enabled: bool | core.BoolOut = core.attr(bool)

    """
    The service role of the instance.
    """
    service_role: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the instance.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_management_type: str | core.StringOut,
        inbound_calls_enabled: bool | core.BoolOut,
        outbound_calls_enabled: bool | core.BoolOut,
        auto_resolve_best_voices_enabled: bool | core.BoolOut | None = None,
        contact_flow_logs_enabled: bool | core.BoolOut | None = None,
        contact_lens_enabled: bool | core.BoolOut | None = None,
        directory_id: str | core.StringOut | None = None,
        early_media_enabled: bool | core.BoolOut | None = None,
        instance_alias: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                identity_management_type=identity_management_type,
                inbound_calls_enabled=inbound_calls_enabled,
                outbound_calls_enabled=outbound_calls_enabled,
                auto_resolve_best_voices_enabled=auto_resolve_best_voices_enabled,
                contact_flow_logs_enabled=contact_flow_logs_enabled,
                contact_lens_enabled=contact_lens_enabled,
                directory_id=directory_id,
                early_media_enabled=early_media_enabled,
                instance_alias=instance_alias,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_resolve_best_voices_enabled: bool | core.BoolOut | None = core.arg(default=None)

        contact_flow_logs_enabled: bool | core.BoolOut | None = core.arg(default=None)

        contact_lens_enabled: bool | core.BoolOut | None = core.arg(default=None)

        directory_id: str | core.StringOut | None = core.arg(default=None)

        early_media_enabled: bool | core.BoolOut | None = core.arg(default=None)

        identity_management_type: str | core.StringOut = core.arg()

        inbound_calls_enabled: bool | core.BoolOut = core.arg()

        instance_alias: str | core.StringOut | None = core.arg(default=None)

        outbound_calls_enabled: bool | core.BoolOut = core.arg()
