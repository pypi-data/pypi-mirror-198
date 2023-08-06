import terrascript.core as core


@core.data(type="aws_location_geofence_collection", namespace="location")
class DsGeofenceCollection(core.Data):
    """
    The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a
    resource across all AWS.
    """

    collection_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the geofence collection.
    """
    collection_name: str | core.StringOut = core.attr(str)

    """
    The timestamp for when the geofence collection resource was created in ISO 8601 format.
    """
    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The optional description of the geofence collection resource.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A key identifier for an AWS KMS customer managed key assigned to the Amazon Location resource.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Key-value map of resource tags for the geofence collection.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The timestamp for when the geofence collection resource was last updated in ISO 8601 format.
    """
    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        collection_name: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsGeofenceCollection.Args(
                collection_name=collection_name,
                kms_key_id=kms_key_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        collection_name: str | core.StringOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
