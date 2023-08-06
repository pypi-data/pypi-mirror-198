import terrascript.core as core


@core.data(type="aws_storagegateway_local_disk", namespace="storagegateway")
class DsLocalDisk(core.Data):
    """
    The disk identifierE.g., `pci-0000:03:00.0-scsi-0:0:0:0`
    """

    disk_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The device node of the local disk to retrieve. For example, `/dev/sdb`.
    """
    disk_node: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The device path of the local disk to retrieve. For example, `/dev/xvdb` or `/dev/nvme1n1`
    .
    """
    disk_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of the gateway.
    """
    gateway_arn: str | core.StringOut = core.attr(str)

    """
    The disk identifierE.g., `pci-0000:03:00.0-scsi-0:0:0:0`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        gateway_arn: str | core.StringOut,
        disk_node: str | core.StringOut | None = None,
        disk_path: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLocalDisk.Args(
                gateway_arn=gateway_arn,
                disk_node=disk_node,
                disk_path=disk_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        disk_node: str | core.StringOut | None = core.arg(default=None)

        disk_path: str | core.StringOut | None = core.arg(default=None)

        gateway_arn: str | core.StringOut = core.arg()
