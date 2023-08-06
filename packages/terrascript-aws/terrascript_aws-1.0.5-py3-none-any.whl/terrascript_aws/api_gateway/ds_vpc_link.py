import terrascript.core as core


@core.data(type="aws_api_gateway_vpc_link", namespace="api_gateway")
class DsVpcLink(core.Data):
    """
    The description of the VPC link.
    """

    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the ID of the found API Gateway VPC Link.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the API Gateway VPC Link to look up. If no API Gateway VPC Link is found with
    this name, an error will be returned.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The status of the VPC link.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The status message of the VPC link.
    """
    status_message: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only suppo
    rts 1 target.
    """
    target_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
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
            args=DsVpcLink.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
