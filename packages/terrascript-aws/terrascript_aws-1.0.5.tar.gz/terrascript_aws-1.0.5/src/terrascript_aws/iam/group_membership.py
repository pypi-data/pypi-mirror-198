import terrascript.core as core


@core.resource(type="aws_iam_group_membership", namespace="iam")
class GroupMembership(core.Resource):

    group: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name to identify the Group Membership
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) A list of IAM User names to associate with the Group
    """
    users: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        group: str | core.StringOut,
        name: str | core.StringOut,
        users: list[str] | core.ArrayOut[core.StringOut],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupMembership.Args(
                group=group,
                name=name,
                users=users,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        users: list[str] | core.ArrayOut[core.StringOut] = core.arg()
