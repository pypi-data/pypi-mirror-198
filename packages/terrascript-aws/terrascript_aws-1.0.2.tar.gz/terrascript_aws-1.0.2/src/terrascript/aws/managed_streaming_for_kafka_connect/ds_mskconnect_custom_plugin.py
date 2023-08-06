import terrascript.core as core


@core.data(type="aws_mskconnect_custom_plugin", namespace="aws_managed_streaming_for_kafka_connect")
class DsMskconnectCustomPlugin(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str)

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
