import terrascript.core as core


@core.resource(type="aws_ebs_snapshot_copy", namespace="ebs")
class SnapshotCopy(core.Resource):
    """
    Amazon Resource Name (ARN) of the EBS Snapshot.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The data encryption key identifier for the snapshot.
    """
    data_encryption_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of what the snapshot is.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Whether the snapshot is encrypted.
    """
    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The snapshot ID (e.g., snap-59fcb34e).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN for the KMS encryption key.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
    """
    owner_alias: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account ID of the snapshot owner.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether to permanently restore an archived snapshot.
    """
    permanent_restore: bool | core.BoolOut | None = core.attr(bool, default=None)

    source_region: str | core.StringOut = core.attr(str)

    source_snapshot_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the storage tier. Valid values are `archive` and `standard`. Default value is
    standard`.
    """
    storage_tier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A map of tags for the snapshot. If configured with a provider [`default_tags` configuration block](h
    ttps://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-block) p
    resent, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) Specifies the number of days for which to temporarily restore an archived snapshot. Requi
    red for temporary restores only. The snapshot will be automatically re-archived after this period.
    """
    temporary_restore_days: int | core.IntOut | None = core.attr(int, default=None)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The size of the drive in GiBs.
    """
    volume_size: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        source_region: str | core.StringOut,
        source_snapshot_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        permanent_restore: bool | core.BoolOut | None = None,
        storage_tier: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        temporary_restore_days: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SnapshotCopy.Args(
                source_region=source_region,
                source_snapshot_id=source_snapshot_id,
                description=description,
                encrypted=encrypted,
                kms_key_id=kms_key_id,
                permanent_restore=permanent_restore,
                storage_tier=storage_tier,
                tags=tags,
                tags_all=tags_all,
                temporary_restore_days=temporary_restore_days,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        permanent_restore: bool | core.BoolOut | None = core.arg(default=None)

        source_region: str | core.StringOut = core.arg()

        source_snapshot_id: str | core.StringOut = core.arg()

        storage_tier: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        temporary_restore_days: int | core.IntOut | None = core.arg(default=None)
