import terrascript.core as core


@core.resource(type="aws_storagegateway_upload_buffer", namespace="storagegateway")
class UploadBuffer(core.Resource):
    """
    (Optional) Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
    """

    disk_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Local disk path. For example, `/dev/nvme1n1`.
    """
    disk_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of the gateway.
    """
    gateway_arn: str | core.StringOut = core.attr(str)

    """
    Combined gateway Amazon Resource Name (ARN) and local disk identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: str | core.StringOut,
        disk_id: str | core.StringOut | None = None,
        disk_path: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UploadBuffer.Args(
                gateway_arn=gateway_arn,
                disk_id=disk_id,
                disk_path=disk_path,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disk_id: str | core.StringOut | None = core.arg(default=None)

        disk_path: str | core.StringOut | None = core.arg(default=None)

        gateway_arn: str | core.StringOut = core.arg()
