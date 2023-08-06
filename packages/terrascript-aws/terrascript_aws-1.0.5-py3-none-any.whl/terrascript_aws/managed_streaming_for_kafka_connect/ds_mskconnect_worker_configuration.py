import terrascript.core as core


@core.data(
    type="aws_mskconnect_worker_configuration", namespace="managed_streaming_for_kafka_connect"
)
class DsMskconnectWorkerConfiguration(core.Data):
    """
    the Amazon Resource Name (ARN) of the worker configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    a summary description of the worker configuration.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    an ID of the latest successfully created revision of the worker configuration.
    """
    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Name of the worker configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    contents of connect-distributed.properties file.
    """
    properties_file_content: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsMskconnectWorkerConfiguration.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
