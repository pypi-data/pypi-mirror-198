import terrascript.core as core


@core.resource(type="aws_msk_configuration", namespace="aws_managed_streaming_for_kafka")
class MskConfiguration(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kafka_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str)

    server_properties: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        server_properties: str | core.StringOut,
        description: str | core.StringOut | None = None,
        kafka_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskConfiguration.Args(
                name=name,
                server_properties=server_properties,
                description=description,
                kafka_versions=kafka_versions,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        kafka_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        server_properties: str | core.StringOut = core.arg()
