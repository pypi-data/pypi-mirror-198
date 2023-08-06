import terrascript.core as core


@core.resource(type="aws_storagegateway_cached_iscsi_volume", namespace="storagegateway")
class CachedIscsiVolume(core.Resource):
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
    (Required) The Amazon Resource Name (ARN) of the gateway.
    """
    gateway_arn: str | core.StringOut = core.attr(str)

    """
    Volume Amazon Resource Name (ARN), e.g., `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-
    12345678/volume/vol-12345678`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set to `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `fals
    e` to use a key managed by Amazon S3.
    """
    kms_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side encrypti
    on. Is required when `kms_encrypted` is set.
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
    (Optional) The snapshot ID of the snapshot to restore as the new cached volumeE.g., `snap-1122aabb`.
    """
    snapshot_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN for an existing volume. Specifying this ARN makes the new volume into an exact co
    py of the specified existing volume's latest recovery point. The `volume_size_in_bytes` value for th
    is new volume must be equal to or larger than the size of the existing volume, in bytes.
    """
    source_volume_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    Volume Amazon Resource Name (ARN), e.g., `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-
    12345678/volume/vol-12345678`.
    """
    volume_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Volume ID, e.g., `vol-12345678`.
    """
    volume_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The size of the volume in bytes.
    """
    volume_size_in_bytes: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: str | core.StringOut,
        network_interface_id: str | core.StringOut,
        target_name: str | core.StringOut,
        volume_size_in_bytes: int | core.IntOut,
        kms_encrypted: bool | core.BoolOut | None = None,
        kms_key: str | core.StringOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        source_volume_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CachedIscsiVolume.Args(
                gateway_arn=gateway_arn,
                network_interface_id=network_interface_id,
                target_name=target_name,
                volume_size_in_bytes=volume_size_in_bytes,
                kms_encrypted=kms_encrypted,
                kms_key=kms_key,
                snapshot_id=snapshot_id,
                source_volume_arn=source_volume_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        gateway_arn: str | core.StringOut = core.arg()

        kms_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key: str | core.StringOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut = core.arg()

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        source_volume_arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_name: str | core.StringOut = core.arg()

        volume_size_in_bytes: int | core.IntOut = core.arg()
