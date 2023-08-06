import terrascript.core as core


@core.resource(type="aws_location_tracker_association", namespace="location")
class TrackerAssociation(core.Resource):
    """
    (Required) The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker re
    source. Used when you need to specify a resource across all AWS.
    """

    consumer_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the tracker resource to be associated with a geofence collection.
    """
    tracker_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        consumer_arn: str | core.StringOut,
        tracker_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrackerAssociation.Args(
                consumer_arn=consumer_arn,
                tracker_name=tracker_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        consumer_arn: str | core.StringOut = core.arg()

        tracker_name: str | core.StringOut = core.arg()
