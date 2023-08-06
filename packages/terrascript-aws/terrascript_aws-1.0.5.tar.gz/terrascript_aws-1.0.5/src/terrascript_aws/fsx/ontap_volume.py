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


@core.resource(type="aws_fsx_ontap_volume", namespace="fsx")
class OntapVolume(core.Resource):
    """
    Amazon Resource Name of the volune.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Describes the file system for the volume, e.g. `fs-12345679`
    """
    file_system_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the FlexCache endpoint type of the volume, Valid values are `NONE`, `ORIGIN`, `CACHE`. Def
    ault value is `NONE`. These can be set by the ONTAP CLI or API and are use with FlexCache feature.
    """
    flexcache_endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the volume, e.g., `fsvol-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the location in the storage virtual machine's namespace where the volume is mou
    nted. The junction_path must have a leading forward slash, such as `/vol3`
    """
    junction_path: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the Volume. You can use a maximum of 203 alphanumeric characters, plus the un
    derscore (_) special character.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Specifies the type of volume, Valid values are `RW`, `DP`,  and `LS`. Default value is `RW`. These c
    an be set by the ONTAP CLI or API. This setting is used as part of migration and replication [Migrat
    ing to Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/migrating-fsx-
    ontap.html)
    """
    ontap_volume_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the volume security style, Valid values are `UNIX`, `NTFS`, and `MIXED`. Defaul
    t value is `UNIX`.
    """
    security_style: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Specifies the size of the volume, in megabytes (MB), that you are creating.
    """
    size_in_megabytes: int | core.IntOut = core.attr(int)

    """
    (Required) Set to true to enable deduplication, compression, and compaction storage efficiency featu
    res on the volume.
    """
    storage_efficiency_enabled: bool | core.BoolOut = core.attr(bool)

    """
    (Required) Specifies the storage virtual machine in which to create the volume.
    """
    storage_virtual_machine_id: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the volume. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tiering_policy: TieringPolicy | None = core.attr(TieringPolicy, default=None)

    """
    The Volume's UUID (universally unique identifier).
    """
    uuid: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of volume, currently the only valid value is `ONTAP`.
    """
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
