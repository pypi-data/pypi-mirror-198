import terrascript.core as core


@core.data(type="aws_iot_endpoint", namespace="aws_iot")
class DsEndpoint(core.Data):

    endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    endpoint_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        endpoint_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpoint.Args(
                endpoint_type=endpoint_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_type: str | core.StringOut | None = core.arg(default=None)
