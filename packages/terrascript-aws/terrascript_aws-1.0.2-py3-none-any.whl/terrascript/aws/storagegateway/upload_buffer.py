import terrascript.core as core


@core.resource(type="aws_storagegateway_upload_buffer", namespace="aws_storagegateway")
class UploadBuffer(core.Resource):

    disk_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    disk_path: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    gateway_arn: str | core.StringOut = core.attr(str)

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
