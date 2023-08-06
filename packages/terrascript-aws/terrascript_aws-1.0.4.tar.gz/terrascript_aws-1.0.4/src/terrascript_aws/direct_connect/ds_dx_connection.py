import terrascript.core as core


@core.data(type="aws_dx_connection", namespace="direct_connect")
class DsDxConnection(core.Data):
    """
    The ARN of the connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Direct Connect endpoint on which the physical connection terminates.
    """
    aws_device: str | core.StringOut = core.attr(str, computed=True)

    """
    The bandwidth of the connection.
    """
    bandwidth: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the connection.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS Direct Connect location where the connection is located.
    """
    location: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the connection to retrieve.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The ID of the AWS account that owns the connection.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the service provider associated with the connection.
    """
    provider_name: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDxConnection.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
