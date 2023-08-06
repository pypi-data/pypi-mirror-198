import terrascript.core as core


@core.data(type="aws_location_tracker", namespace="location")
class DsTracker(core.Data):
    """
    The timestamp for when the tracker resource was created in ISO 8601 format.
    """

    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The optional description for the tracker resource.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A key identifier for an AWS KMS customer managed key assigned to the Amazon Location resource.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The position filtering method of the tracker resource.
    """
    position_filtering: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the tracker.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The Amazon Resource Name (ARN) for the tracker resource. Used when you need to specify a resource ac
    ross all AWS.
    """
    tracker_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the tracker resource.
    """
    tracker_name: str | core.StringOut = core.attr(str)

    """
    The timestamp for when the tracker resource was last updated in ISO 8601 format.
    """
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
