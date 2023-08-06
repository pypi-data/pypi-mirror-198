import terrascript.core as core


@core.resource(type="aws_ebs_volume", namespace="ebs")
class Volume(core.Resource):
    """
    The volume ARN (e.g., arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The AZ where the EBS volume will exist.
    """
    availability_zone: str | core.StringOut = core.attr(str)

    """
    (Optional) If true, the disk will be encrypted.
    """
    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) If true, snapshot will be created before volume deletion. Any tags on the volume will be
    migrated to the snapshot. By default set to false
    """
    final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The volume ID (e.g., vol-59fcb34e).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The amount of IOPS to provision for the disk. Only valid for `type` of `io1`, `io2` or `g
    p3`.
    """
    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The ARN for the KMS encryption key. When specifying `kms_key_id`, `encrypted` needs to be
    set to true. Note: Terraform must be running with credentials which have the `GenerateDataKeyWithou
    tPlaintext` permission on the specified KMS key as required by the [EBS KMS CMK volume provisioning
    process](https://docs.aws.amazon.com/kms/latest/developerguide/services-ebs.html#ebs-cmk) to prevent
    a volume from being created and almost immediately deleted.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies whether to enable Amazon EBS Multi-Attach. Multi-Attach is supported on `io1` a
    nd `io2` volumes.
    """
    multi_attach_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) of the Outpost.
    """
    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The size of the drive in GiBs.
    """
    size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
    (Optional) The throughput that the volume supports, in MiB/s. Only valid for `type` of `gp3`.
    """
    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The type of EBS volume. Can be `standard`, `gp2`, `gp3`, `io1`, `io2`, `sc1` or `st1` (De
    fault: `gp2`).
    """
    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: str | core.StringOut,
        encrypted: bool | core.BoolOut | None = None,
        final_snapshot: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        multi_attach_enabled: bool | core.BoolOut | None = None,
        outpost_arn: str | core.StringOut | None = None,
        size: int | core.IntOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        throughput: int | core.IntOut | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Volume.Args(
                availability_zone=availability_zone,
                encrypted=encrypted,
                final_snapshot=final_snapshot,
                iops=iops,
                kms_key_id=kms_key_id,
                multi_attach_enabled=multi_attach_enabled,
                outpost_arn=outpost_arn,
                size=size,
                snapshot_id=snapshot_id,
                tags=tags,
                tags_all=tags_all,
                throughput=throughput,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        multi_attach_enabled: bool | core.BoolOut | None = core.arg(default=None)

        outpost_arn: str | core.StringOut | None = core.arg(default=None)

        size: int | core.IntOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
