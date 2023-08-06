import terrascript.core as core


@core.resource(type="aws_snapshot_create_volume_permission", namespace="aws_ebs")
class SnapshotCreateVolumePermission(core.Resource):

    account_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    snapshot_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut,
        snapshot_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SnapshotCreateVolumePermission.Args(
                account_id=account_id,
                snapshot_id=snapshot_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut = core.arg()

        snapshot_id: str | core.StringOut = core.arg()
