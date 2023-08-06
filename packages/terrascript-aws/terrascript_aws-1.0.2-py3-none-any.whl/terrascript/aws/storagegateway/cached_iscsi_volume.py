import terrascript.core as core


@core.resource(type="aws_storagegateway_cached_iscsi_volume", namespace="aws_storagegateway")
class CachedIscsiVolume(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    chap_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    gateway_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    kms_key: str | core.StringOut | None = core.attr(str, default=None)

    lun_number: int | core.IntOut = core.attr(int, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str)

    network_interface_port: int | core.IntOut = core.attr(int, computed=True)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None)

    source_volume_arn: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_arn: str | core.StringOut = core.attr(str, computed=True)

    target_name: str | core.StringOut = core.attr(str)

    volume_arn: str | core.StringOut = core.attr(str, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

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
