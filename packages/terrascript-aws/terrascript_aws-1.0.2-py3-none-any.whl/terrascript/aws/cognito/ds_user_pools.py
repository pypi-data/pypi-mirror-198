import terrascript.core as core


@core.data(type="aws_cognito_user_pools", namespace="aws_cognito")
class DsUserPools(core.Data):
    """
    The set of cognito user pool Amazon Resource Names (ARNs).
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The set of cognito user pool ids.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (required) Name of the cognito user pools. Name is not a unique attribute for cognito user pool, so
    multiple pools might be returned with given name. If the pool name is expected to be unique, you can
    reference the pool id via ```tolist(data.aws_cognito_user_pools.selected.ids)[0]```
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsUserPools.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
