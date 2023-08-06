import terrascript.core as core


@core.data(type="aws_mskconnect_custom_plugin", namespace="managed_streaming_for_kafka_connect")
class DsMskconnectCustomPlugin(core.Data):
    """
    the Amazon Resource Name (ARN) of the custom plugin.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    a summary description of the custom plugin.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    an ID of the latest successfully created revision of the custom plugin.
    """
    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Name of the custom plugin.
    """
    name: str | core.StringOut = core.attr(str)

    """
    the state of the custom plugin.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsMskconnectCustomPlugin.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
