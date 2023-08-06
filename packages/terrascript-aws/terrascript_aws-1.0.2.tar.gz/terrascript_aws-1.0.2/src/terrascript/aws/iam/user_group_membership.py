import terrascript.core as core


@core.resource(type="aws_iam_user_group_membership", namespace="aws_iam")
class UserGroupMembership(core.Resource):

    groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    user: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        groups: list[str] | core.ArrayOut[core.StringOut],
        user: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroupMembership.Args(
                groups=groups,
                user=user,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        user: str | core.StringOut = core.arg()
