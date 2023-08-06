import terrascript.core as core


@core.data(type="aws_transfer_server", namespace="transfer")
class DsServer(core.Data):
    """
    Amazon Resource Name (ARN) of Transfer Server.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of any certificate.
    """
    certificate: str | core.StringOut = core.attr(str, computed=True)

    """
    The domain of the storage system that is used for file transfers.
    """
    domain: str | core.StringOut = core.attr(str, computed=True)

    """
    The endpoint of the Transfer Server (e.g., `s-12345678.server.transfer.REGION.amazonaws.com`).
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of endpoint that the server is connected to.
    """
    endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which a
    llows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that
    user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an
    identity provider of your choice.
    """
    identity_provider_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_p
    rovider_type` of `API_GATEWAY`.
    """
    invocation_role: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity
    to your Amazon CloudWatch logs for monitoring and auditing purposes.
    """
    logging_role: str | core.StringOut = core.attr(str, computed=True)

    """
    The file transfer protocol or protocols over which your file transfer protocol client can connect to
    your server's endpoint.
    """
    protocols: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The name of the security policy that is attached to the server.
    """
    security_policy_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID for an SFTP server.
    """
    server_id: str | core.StringOut = core.attr(str)

    """
    URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATE
    WAY`.
    """
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
