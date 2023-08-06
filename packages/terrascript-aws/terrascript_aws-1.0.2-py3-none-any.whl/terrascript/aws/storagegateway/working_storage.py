import terrascript.core as core


@core.resource(type="aws_storagegateway_working_storage", namespace="aws_storagegateway")
class WorkingStorage(core.Resource):

    disk_id: str | core.StringOut = core.attr(str)

    gateway_arn: str | core.StringOut = core.attr(str)

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
