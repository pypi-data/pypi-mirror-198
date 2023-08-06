import terrascript.core as core


@core.data(type="aws_organizations_resource_tags", namespace="organizations")
class DsResourceTags(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the resource with the tags to list. See details below.
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    Map of key=value pairs for each tag set on the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        resource_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsResourceTags.Args(
                resource_id=resource_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
