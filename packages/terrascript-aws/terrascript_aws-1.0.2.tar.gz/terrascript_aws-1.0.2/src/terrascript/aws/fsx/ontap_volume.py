import terrascript.core as core


@core.schema
class TieringPolicy(core.Schema):

    cooling_period: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cooling_period: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TieringPolicy.Args(
                cooling_period=cooling_period,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cooling_period: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_fsx_ontap_volume", namespace="aws_fsx")
class OntapVolume(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    file_system_id: str | core.StringOut = core.attr(str, computed=True)

    flexcache_endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    junction_path: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    ontap_volume_type: str | core.StringOut = core.attr(str, computed=True)

    security_style: str | core.StringOut | None = core.attr(str, default=None)

    size_in_megabytes: int | core.IntOut = core.attr(int)

    storage_efficiency_enabled: bool | core.BoolOut = core.attr(bool)

    storage_virtual_machine_id: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tiering_policy: TieringPolicy | None = core.attr(TieringPolicy, default=None)

    uuid: str | core.StringOut = core.attr(str, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        junction_path: str | core.StringOut,
        name: str | core.StringOut,
        size_in_megabytes: int | core.IntOut,
        storage_efficiency_enabled: bool | core.BoolOut,
        storage_virtual_machine_id: str | core.StringOut,
        security_style: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tiering_policy: TieringPolicy | None = None,
        volume_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OntapVolume.Args(
                junction_path=junction_path,
                name=name,
                size_in_megabytes=size_in_megabytes,
                storage_efficiency_enabled=storage_efficiency_enabled,
                storage_virtual_machine_id=storage_virtual_machine_id,
                security_style=security_style,
                tags=tags,
                tags_all=tags_all,
                tiering_policy=tiering_policy,
                volume_type=volume_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        junction_path: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        security_style: str | core.StringOut | None = core.arg(default=None)

        size_in_megabytes: int | core.IntOut = core.arg()

        storage_efficiency_enabled: bool | core.BoolOut = core.arg()

        storage_virtual_machine_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tiering_policy: TieringPolicy | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)
