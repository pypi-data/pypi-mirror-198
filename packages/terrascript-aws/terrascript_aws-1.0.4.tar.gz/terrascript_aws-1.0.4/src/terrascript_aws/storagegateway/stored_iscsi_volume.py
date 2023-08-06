import terrascript.core as core


@core.resource(type="aws_storagegateway_stored_iscsi_volume", namespace="storagegateway")
class StoredIscsiVolume(core.Resource):
    """
    Volume Amazon Resource Name (ARN), e.g., `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-
    12345678/volume/vol-12345678`.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether mutual CHAP is enabled for the iSCSI target.
    """
    chap_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) The unique identifier for the gateway local disk that is configured as a stored volume.
    """
    disk_id: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the gateway.
    """
    gateway_arn: str | core.StringOut = core.attr(str)

    """
    Volume Amazon Resource Name (ARN), e.g., `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-
    12345678/volume/vol-12345678`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to u
    se a key managed by Amazon S3. Optional.
    """
    kms_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side encrypti
    on. This value can only be set when `kms_encrypted` is `true`.
    """
    kms_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    Logical disk number.
    """
    lun_number: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addre
    sses are accepted.
    """
    network_interface_id: str | core.StringOut = core.attr(str)

    """
    The port used to communicate with iSCSI targets.
    """
    network_interface_port: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Specify this field as `true` if you want to preserve the data on the local disk. Otherwis
    e, specifying this field as false creates an empty volume.
    """
    preserve_existing_data: bool | core.BoolOut = core.attr(bool)

    """
    (Optional) The snapshot ID of the snapshot to restore as the new stored volumeE.g., `snap-1122aabb`.
    """
    snapshot_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    Target Amazon Resource Name (ARN), e.g., `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-
    12345678/target/iqn.1997-05.com.amazon:TargetName`.
    """
    target_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the iSCSI target used by initiators to connect to the target and as a suffix
    for the target ARN. The target name must be unique across all volumes of a gateway.
    """
    target_name: str | core.StringOut = core.attr(str)

    """
    A value that indicates whether a storage volume is attached to, detached from, or is in the process
    of detaching from a gateway.
    """
    volume_attachment_status: str | core.StringOut = core.attr(str, computed=True)

    """
    Volume ID, e.g., `vol-12345678`.
    """
    volume_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The size of the data stored on the volume in bytes.
    """
    volume_size_in_bytes: int | core.IntOut = core.attr(int, computed=True)

    """
    indicates the state of the storage volume.
    """
    volume_status: str | core.StringOut = core.attr(str, computed=True)

    """
    indicates the type of the volume.
    """
    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        disk_id: str | core.StringOut,
        gateway_arn: str | core.StringOut,
        network_interface_id: str | core.StringOut,
        preserve_existing_data: bool | core.BoolOut,
        target_name: str | core.StringOut,
        kms_encrypted: bool | core.BoolOut | None = None,
        kms_key: str | core.StringOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StoredIscsiVolume.Args(
                disk_id=disk_id,
                gateway_arn=gateway_arn,
                network_interface_id=network_interface_id,
                preserve_existing_data=preserve_existing_data,
                target_name=target_name,
                kms_encrypted=kms_encrypted,
                kms_key=kms_key,
                snapshot_id=snapshot_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disk_id: str | core.StringOut = core.arg()

        gateway_arn: str | core.StringOut = core.arg()

        kms_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key: str | core.StringOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut = core.arg()

        preserve_existing_data: bool | core.BoolOut = core.arg()

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_name: str | core.StringOut = core.arg()
