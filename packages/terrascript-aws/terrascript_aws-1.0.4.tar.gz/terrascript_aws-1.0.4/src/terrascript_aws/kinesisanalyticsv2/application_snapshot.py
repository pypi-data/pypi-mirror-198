import terrascript.core as core


@core.resource(type="aws_kinesisanalyticsv2_application_snapshot", namespace="kinesisanalyticsv2")
class ApplicationSnapshot(core.Resource):
    """
    (Required) The name of an existing  [Kinesis Analytics v2 Application](/docs/providers/aws/r/kinesis
    analyticsv2_application.html). Note that the application must be running for a snapshot to be create
    d.
    """

    application_name: str | core.StringOut = core.attr(str)

    """
    The current application version ID when the snapshot was created.
    """
    application_version_id: int | core.IntOut = core.attr(int, computed=True)

    """
    The application snapshot identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The timestamp of the application snapshot.
    """
    snapshot_creation_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the application snapshot.
    """
    snapshot_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        application_name: str | core.StringOut,
        snapshot_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApplicationSnapshot.Args(
                application_name=application_name,
                snapshot_name=snapshot_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_name: str | core.StringOut = core.arg()

        snapshot_name: str | core.StringOut = core.arg()
