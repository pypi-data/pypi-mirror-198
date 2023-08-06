import terrascript.core as core


@core.data(type="aws_iot_endpoint", namespace="iot")
class DsEndpoint(core.Data):
    """
    The endpoint based on `endpoint_type`:
    """

    endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Endpoint type. Valid values: `iot:CredentialProvider`, `iot:Data`, `iot:Data-ATS`, `iot:J
    obs`.
    """
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
