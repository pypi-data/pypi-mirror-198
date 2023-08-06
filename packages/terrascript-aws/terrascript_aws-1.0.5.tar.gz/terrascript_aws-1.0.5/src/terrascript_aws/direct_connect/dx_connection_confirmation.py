import terrascript.core as core


@core.resource(type="aws_dx_connection_confirmation", namespace="direct_connect")
class DxConnectionConfirmation(core.Resource):
    """
    (Required) The ID of the hosted connection.
    """

    connection_id: str | core.StringOut = core.attr(str)

    """
    The ID of the connection.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxConnectionConfirmation.Args(
                connection_id=connection_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_id: str | core.StringOut = core.arg()
