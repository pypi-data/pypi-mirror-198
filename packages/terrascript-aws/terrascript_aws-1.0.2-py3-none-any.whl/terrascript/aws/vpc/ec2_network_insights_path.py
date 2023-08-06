import terrascript.core as core


@core.resource(type="aws_ec2_network_insights_path", namespace="aws_vpc")
class Ec2NetworkInsightsPath(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    destination: str | core.StringOut = core.attr(str)

    destination_ip: str | core.StringOut | None = core.attr(str, default=None)

    destination_port: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    protocol: str | core.StringOut = core.attr(str)

    source: str | core.StringOut = core.attr(str)

    source_ip: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        destination: str | core.StringOut,
        protocol: str | core.StringOut,
        source: str | core.StringOut,
        destination_ip: str | core.StringOut | None = None,
        destination_port: int | core.IntOut | None = None,
        source_ip: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2NetworkInsightsPath.Args(
                destination=destination,
                protocol=protocol,
                source=source,
                destination_ip=destination_ip,
                destination_port=destination_port,
                source_ip=source_ip,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination: str | core.StringOut = core.arg()

        destination_ip: str | core.StringOut | None = core.arg(default=None)

        destination_port: int | core.IntOut | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        source: str | core.StringOut = core.arg()

        source_ip: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
