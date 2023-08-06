import terrascript.core as core


@core.resource(type="aws_elasticache_user_group_association", namespace="elasticache")
class UserGroupAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID of the user group.
    """
    user_group_id: str | core.StringOut = core.attr(str)

    """
    (Required) ID of the user to associated with the user group.
    """
    user_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_group_id: str | core.StringOut,
        user_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroupAssociation.Args(
                user_group_id=user_group_id,
                user_id=user_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        user_group_id: str | core.StringOut = core.arg()

        user_id: str | core.StringOut = core.arg()
