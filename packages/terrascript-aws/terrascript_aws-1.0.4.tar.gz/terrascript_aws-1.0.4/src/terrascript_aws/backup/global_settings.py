import terrascript.core as core


@core.resource(type="aws_backup_global_settings", namespace="backup")
class GlobalSettings(core.Resource):
    """
    (Required) A list of resources along with the opt-in preferences for the account.
    """

    global_settings: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, kind=core.Kind.map
    )

    """
    The AWS Account ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        global_settings: dict[str, str] | core.MapOut[core.StringOut],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalSettings.Args(
                global_settings=global_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        global_settings: dict[str, str] | core.MapOut[core.StringOut] = core.arg()
