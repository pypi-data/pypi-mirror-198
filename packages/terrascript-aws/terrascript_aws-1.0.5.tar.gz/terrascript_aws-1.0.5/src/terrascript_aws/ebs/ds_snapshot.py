import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ebs_snapshot", namespace="ebs")
class DsSnapshot(core.Data):
    """
    Amazon Resource Name (ARN) of the EBS Snapshot.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The data encryption key identifier for the snapshot.
    """
    data_encryption_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A description for the snapshot
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the snapshot is encrypted.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) One or more name/value pairs to filter off of. There are
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    The snapshot ID (e.g., snap-59fcb34e).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN for the KMS encryption key.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If more than one result is returned, use the most recent snapshot.
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The ARN of the Outpost on which the snapshot is stored.
    """
    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
    """
    owner_alias: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account ID of the EBS snapshot owner.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns the snapshots owned by the specified owner id. Multiple owners can be specified.
    """
    owners: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) One or more AWS accounts IDs that can create volumes from the snapshot.
    """
    restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The snapshot ID (e.g., snap-59fcb34e).
    """
    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific snapshot_id.
    """
    snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The snapshot state.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    The storage tier in which the snapshot is stored.
    """
    storage_tier: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The volume ID (e.g., vol-59fcb34e).
    """
    volume_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The size of the drive in GiBs.
    """
    volume_size: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        most_recent: bool | core.BoolOut | None = None,
        owners: list[str] | core.ArrayOut[core.StringOut] | None = None,
        restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSnapshot.Args(
                filter=filter,
                most_recent=most_recent,
                owners=owners,
                restorable_by_user_ids=restorable_by_user_ids,
                snapshot_ids=snapshot_ids,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        owners: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        restorable_by_user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        snapshot_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
