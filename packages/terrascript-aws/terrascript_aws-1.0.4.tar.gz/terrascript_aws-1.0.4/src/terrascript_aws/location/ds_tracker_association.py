import terrascript.core as core


@core.data(type="aws_location_tracker_association", namespace="location")
class DsTrackerAssociation(core.Data):
    """
    (Required) The Amazon Resource Name (ARN) of the geofence collection associated to tracker resource.
    """

    consumer_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the tracker resource associated with a geofence collection.
    """
    tracker_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        consumer_arn: str | core.StringOut,
        tracker_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsTrackerAssociation.Args(
                consumer_arn=consumer_arn,
                tracker_name=tracker_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        consumer_arn: str | core.StringOut = core.arg()

        tracker_name: str | core.StringOut = core.arg()
