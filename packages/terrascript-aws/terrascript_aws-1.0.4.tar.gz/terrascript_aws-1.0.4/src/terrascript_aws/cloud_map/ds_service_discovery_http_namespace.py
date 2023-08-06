import terrascript.core as core


@core.data(type="aws_service_discovery_http_namespace", namespace="cloud_map")
class DsServiceDiscoveryHttpNamespace(core.Data):
    """
    The ARN that Amazon Route 53 assigns to the namespace when you create it.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The description that you specify for the namespace when you create it.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of an HTTP namespace.
    """
    http_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of a namespace.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the http namespace.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServiceDiscoveryHttpNamespace.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
