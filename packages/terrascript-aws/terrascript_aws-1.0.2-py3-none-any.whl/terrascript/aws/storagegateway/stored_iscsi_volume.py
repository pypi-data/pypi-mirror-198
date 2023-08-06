import terrascript.core as core


@core.resource(type="aws_storagegateway_stored_iscsi_volume", namespace="aws_storagegateway")
class StoredIscsiVolume(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    chap_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    disk_id: str | core.StringOut = core.attr(str)

    gateway_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    kms_key: str | core.StringOut | None = core.attr(str, default=None)

    lun_number: int | core.IntOut = core.attr(int, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str)

    network_interface_port: int | core.IntOut = core.attr(int, computed=True)

    preserve_existing_data: bool | core.BoolOut = core.attr(bool)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_arn: str | core.StringOut = core.attr(str, computed=True)

    target_name: str | core.StringOut = core.attr(str)

    volume_attachment_status: str | core.StringOut = core.attr(str, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size_in_bytes: int | core.IntOut = core.attr(int, computed=True)

    volume_status: str | core.StringOut = core.attr(str, computed=True)

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
