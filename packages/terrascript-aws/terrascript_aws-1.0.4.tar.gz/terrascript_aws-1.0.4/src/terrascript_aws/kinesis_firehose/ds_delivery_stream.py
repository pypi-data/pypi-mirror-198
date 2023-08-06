import terrascript.core as core


@core.data(type="aws_kinesis_firehose_delivery_stream", namespace="kinesis_firehose")
class DsDeliveryStream(core.Data):
    """
    The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Kinesis Stream.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDeliveryStream.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
