import terrascript.core as core


@core.resource(type="aws_location_geofence_collection", namespace="location")
class GeofenceCollection(core.Resource):
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
    (Optional) The optional description for the geofence collection.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A key identifier for an AWS KMS customer managed key assigned to the Amazon Location reso
    urce.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value tags for the geofence collection. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The timestamp for when the geofence collection resource was last updated in ISO 8601 format.
    """
    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        collection_name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GeofenceCollection.Args(
                collection_name=collection_name,
                description=description,
                kms_key_id=kms_key_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        collection_name: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
