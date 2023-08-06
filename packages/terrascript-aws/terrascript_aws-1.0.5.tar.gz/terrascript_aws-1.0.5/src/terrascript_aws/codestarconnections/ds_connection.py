import terrascript.core as core


@core.data(type="aws_codestarconnections_connection", namespace="codestarconnections")
class DsConnection(core.Data):
    """
    (Optional) The CodeStar Connection ARN.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The CodeStar Connection status. Possible values are `PENDING`, `AVAILABLE` and `ERROR`.
    """
    connection_status: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the host associated with the connection.
    """
    host_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The CodeStar Connection ARN.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The CodeStar Connection name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The name of the external provider where your third-party code repository is configured. Possible val
    ues are `Bitbucket` and `GitHub`. For connections to a GitHub Enterprise Server instance, you must c
    reate an [aws_codestarconnections_host](https://registry.terraform.io/providers/hashicorp/aws/latest
    /docs/resources/codestarconnections_host) resource and use `host_arn` instead.
    """
    provider_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Map of key-value resource tags to associate with the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConnection.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
