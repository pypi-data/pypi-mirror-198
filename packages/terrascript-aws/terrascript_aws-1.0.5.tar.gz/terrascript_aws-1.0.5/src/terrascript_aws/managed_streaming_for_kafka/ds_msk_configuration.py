import terrascript.core as core


@core.data(type="aws_msk_configuration", namespace="managed_streaming_for_kafka")
class DsMskConfiguration(core.Data):
    """
    Amazon Resource Name (ARN) of the configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the configuration.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of Apache Kafka versions which can use this configuration.
    """
    kafka_versions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
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
    Contents of the server.properties file.
    """
    server_properties: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsMskConfiguration.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
