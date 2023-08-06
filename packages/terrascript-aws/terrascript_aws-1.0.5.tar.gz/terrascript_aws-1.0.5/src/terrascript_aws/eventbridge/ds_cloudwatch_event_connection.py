import terrascript.core as core


@core.data(type="aws_cloudwatch_event_connection", namespace="eventbridge")
class DsCloudwatchEventConnection(core.Data):
    """
    The ARN (Amazon Resource Name) for the connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of authorization to use to connect. One of `API_KEY`,`BASIC`,`OAUTH_CLIENT_CREDENTIALS`.
    """
    authorization_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the connection.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The ARN (Amazon Resource Name) for the secret created from the authorization parameters specified fo
    r the connection.
    """
    secret_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsCloudwatchEventConnection.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
