import terrascript.core as core


@core.data(type="aws_cognito_user_pool_clients", namespace="aws_cognito")
class DsUserPoolClients(core.Data):
    """
    List of Cognito user pool client IDs.
    """

    client_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    List of Cognito user pool client names.
    """
    client_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (required) The Cognito user pool ID.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        user_pool_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsUserPoolClients.Args(
                user_pool_id=user_pool_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        user_pool_id: str | core.StringOut = core.arg()
