import terrascript.core as core


@core.resource(type="aws_fsx_backup", namespace="fsx")
class Backup(core.Resource):
    """
    Amazon Resource Name of the backup.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the file system to back up. Required if backing up Lustre or Windows file syste
    ms.
    """
    file_system_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    Identifier of the backup, e.g., `fs-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the backup of the Amazon FSx
    file system's data at rest.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    AWS account identifier that created the file system.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

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
    The type of the file system backup.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the volume to back up. Required if backing up a ONTAP Volume.
    """
    volume_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        volume_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Backup.Args(
                file_system_id=file_system_id,
                tags=tags,
                tags_all=tags_all,
                volume_id=volume_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        file_system_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        volume_id: str | core.StringOut | None = core.arg(default=None)
