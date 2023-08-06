import terrascript.core as core


@core.data(type="aws_location_tracker", namespace="aws_location")
class DsTracker(core.Data):

    create_time: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    position_filtering: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tracker_arn: str | core.StringOut = core.attr(str, computed=True)

    tracker_name: str | core.StringOut = core.attr(str)

    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        tracker_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTracker.Args(
                tracker_name=tracker_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tracker_name: str | core.StringOut = core.arg()
