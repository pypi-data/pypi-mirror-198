import terrascript.core as core


@core.data(type="aws_service_discovery_dns_namespace", namespace="cloud_map")
class DsServiceDiscoveryDnsNamespace(core.Data):
    """
    The Amazon Resource Name (ARN) of the namespace.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A description of the namespace.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.
    """
    hosted_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    The namespace ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the namespace.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The type of the namespace. Allowed values are `DNS_PUBLIC` or `DNS_PRIVATE`.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServiceDiscoveryDnsNamespace.Args(
                name=name,
                type=type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
