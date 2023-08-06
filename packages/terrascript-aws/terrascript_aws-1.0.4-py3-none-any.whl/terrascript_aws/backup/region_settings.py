import terrascript.core as core


@core.resource(type="aws_backup_region_settings", namespace="backup")
class RegionSettings(core.Resource):
    """
    The AWS region.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of services along with the management preferences for the Region.
    """
    resource_type_management_preference: dict[str, bool] | core.MapOut[
        core.BoolOut
    ] | None = core.attr(bool, default=None, computed=True, kind=core.Kind.map)

    """
    (Required) A map of services along with the opt-in preferences for the Region.
    """
    resource_type_opt_in_preference: dict[str, bool] | core.MapOut[core.BoolOut] = core.attr(
        bool, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        resource_type_opt_in_preference: dict[str, bool] | core.MapOut[core.BoolOut],
        resource_type_management_preference: dict[str, bool]
        | core.MapOut[core.BoolOut]
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegionSettings.Args(
                resource_type_opt_in_preference=resource_type_opt_in_preference,
                resource_type_management_preference=resource_type_management_preference,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_type_management_preference: dict[str, bool] | core.MapOut[
            core.BoolOut
        ] | None = core.arg(default=None)

        resource_type_opt_in_preference: dict[str, bool] | core.MapOut[core.BoolOut] = core.arg()
