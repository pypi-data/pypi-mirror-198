import terrascript.core as core


@core.resource(type="aws_dx_connection_association", namespace="direct_connect")
class DxConnectionAssociation(core.Resource):
    """
    (Required) The ID of the connection.
    """

    connection_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the LAG with which to associate the connection.
    """
    lag_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_id: str | core.StringOut,
        lag_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxConnectionAssociation.Args(
                connection_id=connection_id,
                lag_id=lag_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_id: str | core.StringOut = core.arg()

        lag_id: str | core.StringOut = core.arg()
