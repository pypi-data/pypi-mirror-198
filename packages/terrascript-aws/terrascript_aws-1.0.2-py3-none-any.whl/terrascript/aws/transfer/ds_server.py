import terrascript.core as core


@core.data(type="aws_transfer_server", namespace="aws_transfer")
class DsServer(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut = core.attr(str, computed=True)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_provider_type: str | core.StringOut = core.attr(str, computed=True)

    invocation_role: str | core.StringOut = core.attr(str, computed=True)

    logging_role: str | core.StringOut = core.attr(str, computed=True)

    protocols: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_policy_name: str | core.StringOut = core.attr(str, computed=True)

    server_id: str | core.StringOut = core.attr(str)

    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        server_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsServer.Args(
                server_id=server_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        server_id: str | core.StringOut = core.arg()
