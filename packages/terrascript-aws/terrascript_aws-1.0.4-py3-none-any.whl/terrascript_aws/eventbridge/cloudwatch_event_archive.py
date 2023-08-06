import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_archive", namespace="eventbridge")
class CloudwatchEventArchive(core.Resource):
    """
    The Amazon Resource Name (ARN) of the event archive.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the new event archive.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Instructs the new event archive to only capture events matched by this pattern. By defaul
    t, it attempts to archive every event received in the `event_source_arn`.
    """
    event_pattern: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Event bus source ARN from where these events should be archived.
    """
    event_source_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the new event archive. The archive name cannot exceed 48 characters.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The maximum number of days to retain events in the new event archive. By default, it arch
    ives indefinitely.
    """
    retention_days: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        event_source_arn: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        event_pattern: str | core.StringOut | None = None,
        retention_days: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventArchive.Args(
                event_source_arn=event_source_arn,
                name=name,
                description=description,
                event_pattern=event_pattern,
                retention_days=retention_days,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        event_pattern: str | core.StringOut | None = core.arg(default=None)

        event_source_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        retention_days: int | core.IntOut | None = core.arg(default=None)
