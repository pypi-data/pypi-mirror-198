import terrascript.core as core


@core.resource(type="aws_fsx_openzfs_snapshot", namespace="fsx")
class OpenzfsSnapshot(core.Resource):
    """
    Amazon Resource Name of the snapshot.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the snapshot, e.g., `fsvolsnap-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Snapshot. You can use a maximum of 203 alphanumeric characters plus eithe
    r _ or -  or : or . for the name.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the file system. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level. If you have set `copy_tags_to_backups` to true, and you specify one or more tags, no existing
    file system tags are copied from the file system to the backup.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) The ID of the volume to snapshot. This can be the root volume or a child volume.
    """
    volume_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        volume_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OpenzfsSnapshot.Args(
                name=name,
                volume_id=volume_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        volume_id: str | core.StringOut = core.arg()
