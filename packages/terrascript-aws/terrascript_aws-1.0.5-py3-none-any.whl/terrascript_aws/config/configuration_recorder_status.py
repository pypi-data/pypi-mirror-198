import terrascript.core as core


@core.resource(type="aws_config_configuration_recorder_status", namespace="config")
class ConfigurationRecorderStatus(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Whether the configuration recorder should be enabled or disabled.
    """
    is_enabled: bool | core.BoolOut = core.attr(bool)

    """
    (Required) The name of the recorder
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        is_enabled: bool | core.BoolOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationRecorderStatus.Args(
                is_enabled=is_enabled,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        is_enabled: bool | core.BoolOut = core.arg()

        name: str | core.StringOut = core.arg()
