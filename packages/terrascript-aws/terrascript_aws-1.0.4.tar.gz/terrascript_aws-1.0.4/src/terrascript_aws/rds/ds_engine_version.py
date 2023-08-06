import terrascript.core as core


@core.data(type="aws_rds_engine_version", namespace="rds")
class DsEngineVersion(core.Data):

    default_character_set: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut = core.attr(str)

    engine_description: str | core.StringOut = core.attr(str, computed=True)

    exportable_log_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    parameter_group_family: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    preferred_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    supported_character_sets: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_feature_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_modes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_timezones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supports_global_databases: bool | core.BoolOut = core.attr(bool, computed=True)

    supports_log_exports_to_cloudwatch: bool | core.BoolOut = core.attr(bool, computed=True)

    supports_parallel_query: bool | core.BoolOut = core.attr(bool, computed=True)

    supports_read_replica: bool | core.BoolOut = core.attr(bool, computed=True)

    valid_upgrade_targets: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version_description: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        engine: str | core.StringOut,
        parameter_group_family: str | core.StringOut | None = None,
        preferred_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEngineVersion.Args(
                engine=engine,
                parameter_group_family=parameter_group_family,
                preferred_versions=preferred_versions,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        engine: str | core.StringOut = core.arg()

        parameter_group_family: str | core.StringOut | None = core.arg(default=None)

        preferred_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        version: str | core.StringOut | None = core.arg(default=None)
