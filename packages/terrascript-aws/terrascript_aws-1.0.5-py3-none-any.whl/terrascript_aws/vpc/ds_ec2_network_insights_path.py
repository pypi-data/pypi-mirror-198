import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ec2_network_insights_path", namespace="vpc")
class DsEc2NetworkInsightsPath(core.Data):
    """
    The ARN of the selected Network Insights Path.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS resource that is the destination of the path.
    """
    destination: str | core.StringOut = core.attr(str, computed=True)

    """
    The IP address of the AWS resource that is the destination of the path.
    """
    destination_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    The destination port.
    """
    destination_port: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the Network Insights Path to select.
    """
    network_insights_path_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The protocol.
    """
    protocol: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS resource that is the source of the path.
    """
    source: str | core.StringOut = core.attr(str, computed=True)

    """
    The IP address of the AWS resource that is the source of the path.
    """
    source_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        network_insights_path_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2NetworkInsightsPath.Args(
                filter=filter,
                network_insights_path_id=network_insights_path_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        network_insights_path_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
