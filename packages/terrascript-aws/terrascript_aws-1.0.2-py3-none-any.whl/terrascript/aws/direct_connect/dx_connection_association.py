import terrascript.core as core


@core.resource(type="aws_dx_connection_association", namespace="aws_direct_connect")
class DxConnectionAssociation(core.Resource):

    connection_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
