import terrascript.core as core


@core.data(type="aws_storagegateway_local_disk", namespace="aws_storagegateway")
class DsLocalDisk(core.Data):

    disk_id: str | core.StringOut = core.attr(str, computed=True)

    disk_node: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    disk_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    gateway_arn: str | core.StringOut = core.attr(str)

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
