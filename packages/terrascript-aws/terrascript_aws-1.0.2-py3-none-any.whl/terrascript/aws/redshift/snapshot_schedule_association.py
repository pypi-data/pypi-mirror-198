import terrascript.core as core


@core.resource(type="aws_redshift_snapshot_schedule_association", namespace="aws_redshift")
class SnapshotScheduleAssociation(core.Resource):

    cluster_identifier: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    schedule_identifier: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        schedule_identifier: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SnapshotScheduleAssociation.Args(
                cluster_identifier=cluster_identifier,
                schedule_identifier=schedule_identifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: str | core.StringOut = core.arg()

        schedule_identifier: str | core.StringOut = core.arg()
