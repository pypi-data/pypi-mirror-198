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


@core.data(type="aws_ebs_volume", namespace="ebs")
class DsVolume(core.Data):
    """
    The volume ARN (e.g., arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The AZ where the EBS volume exists.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the disk is encrypted.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) One or more name/value pairs to filter off of. There are
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    The volume ID (e.g., vol-59fcb34e).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The amount of IOPS for the disk.
    """
    iops: int | core.IntOut = core.attr(int, computed=True)

    """
    The ARN for the KMS encryption key.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If more than one result is returned, use the most
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether Amazon EBS Multi-Attach is enabled.
    """
    multi_attach_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The Amazon Resource Name (ARN) of the Outpost.
    """
    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The size of the drive in GiBs.
    """
    size: int | core.IntOut = core.attr(int, computed=True)

    """
    The snapshot_id the EBS volume is based off.
    """
    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The throughput that the volume supports, in MiB/s.
    """
    throughput: int | core.IntOut = core.attr(int, computed=True)

    """
    The volume ID (e.g., vol-59fcb34e).
    """
    volume_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of EBS volume.
    """
    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        most_recent: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsVolume.Args(
                filter=filter,
                most_recent=most_recent,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
