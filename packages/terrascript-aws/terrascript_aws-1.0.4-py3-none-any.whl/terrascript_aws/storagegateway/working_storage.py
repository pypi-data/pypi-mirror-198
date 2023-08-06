import terrascript.core as core


@core.resource(type="aws_storagegateway_working_storage", namespace="storagegateway")
class WorkingStorage(core.Resource):
    """
    (Required) Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
    """

    disk_id: str | core.StringOut = core.attr(str)

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
        disk_id: str | core.StringOut,
        gateway_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=WorkingStorage.Args(
                disk_id=disk_id,
                gateway_arn=gateway_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disk_id: str | core.StringOut = core.arg()

        gateway_arn: str | core.StringOut = core.arg()
