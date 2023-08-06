import terrascript.core as core


@core.data(type="aws_connect_instance", namespace="aws_connect")
class DsInstance(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_resolve_best_voices_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    contact_flow_logs_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    contact_lens_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    created_time: str | core.StringOut = core.attr(str, computed=True)

    early_media_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_management_type: str | core.StringOut = core.attr(str, computed=True)

    inbound_calls_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    instance_alias: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    instance_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    outbound_calls_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    service_role: str | core.StringOut = core.attr(str, computed=True)

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
