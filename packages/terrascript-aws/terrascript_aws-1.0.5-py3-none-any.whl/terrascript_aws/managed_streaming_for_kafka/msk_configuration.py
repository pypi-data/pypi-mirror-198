import terrascript.core as core


@core.resource(type="aws_msk_configuration", namespace="managed_streaming_for_kafka")
class MskConfiguration(core.Resource):
    """
    Amazon Resource Name (ARN) of the configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the configuration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) List of Apache Kafka versions which can use this configuration.
    """
    kafka_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Latest revision of the configuration.
    """
    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Name of the configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Contents of the server.properties file. Supported properties are documented in the [MSK D
    eveloper Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.h
    tml).
    """
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
