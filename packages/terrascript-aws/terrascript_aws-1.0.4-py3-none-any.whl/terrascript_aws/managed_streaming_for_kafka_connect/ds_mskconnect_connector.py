import terrascript.core as core


@core.data(type="aws_mskconnect_connector", namespace="managed_streaming_for_kafka_connect")
class DsMskconnectConnector(core.Data):
    """
    The Amazon Resource Name (ARN) of the connector.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A summary description of the connector.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the connector.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The current version of the connector.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsMskconnectConnector.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
